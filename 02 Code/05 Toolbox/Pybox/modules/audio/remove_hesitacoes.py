#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audio/remove_hesitacoes.py
Remove hesitações (né, ãh, hm, pausas longas) de áudio usando Whisper + ffmpeg.
Saída gerada no diretório onde o comando foi chamado.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

# ── Ambiente PyBox ────────────────────────────────────────────────────────
CALL_DIR = Path(os.environ.get("PYBOX_CALL_DIR", Path.cwd()))

# ── Padrões de hesitações ─────────────────────────────────────────────────
HESITACOES_RAW = [
    r"^ne$", r"^neh$",
    r"^a+h+$", r"^e+h+$", r"^o+h+$", r"^u+h+$",
    r"^hm+$", r"^m+$", r"^a+h+n+$", r"^e+h+n+$",
    r"^u+h+-?h+u+h?$", r"^ta+$",
]
HESITACAO_RE = re.compile("|".join(HESITACOES_RAW), re.IGNORECASE | re.UNICODE)
MAX_DUR_HES = 2.5

INITIAL_PROMPT = (
    "Transcrição literal e fiel de fala coloquial brasileira. "
    "Inclua todas as hesitações, pausas preenchidas e marcadores discursivos "
    "como: né, né?, nê, ãh, ah, éh, eh, hm, hmm, ahn, mm, tipo, tá."
)


# ── Helpers ───────────────────────────────────────────────────────────────

def remover_acentos(t: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")


def normalizar(p: str) -> str:
    s = p.strip().strip(".,!?;:\"'()[]{}—–-·…¿¡")
    return remover_acentos(s).lower().strip()


def e_hesitacao(p: str) -> bool:
    return bool(HESITACAO_RE.match(normalizar(p)))


def segmento_so_hesitacoes(texto: str) -> bool:
    tokens = texto.strip().split()
    return bool(tokens) and all(e_hesitacao(t) for t in tokens)


def converter_para_wav(audio_path: str, wav_path: str):
    subprocess.run(
        ["ffmpeg", "-y", "-i", audio_path, "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", wav_path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def extrair_trecho_wav(audio_path: str, start: float, end: float, wav_path: str):
    subprocess.run(
        ["ffmpeg", "-y", "-ss", f"{start:.4f}", "-to", f"{end:.4f}",
         "-i", audio_path, "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", wav_path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def duracao_audio(path: str) -> float:
    out = subprocess.check_output(
        ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", path]
    )
    return float(json.loads(out)["format"]["duration"])


# ── Transcrição ───────────────────────────────────────────────────────────

def transcrever(audio_path: str, modelo_nome: str):
    try:
        import torch
        device = "cuda" if torch.cuda.is_available() else "cpu"
    except ImportError:
        device = "cpu"

    import whisper
    print(f"[Whisper] Carregando modelo '{modelo_nome}' em '{device}'...")
    model = whisper.load_model(modelo_nome, device=device)

    tmp_wav = audio_path + "_tmp_whisper.wav"
    try:
        print("[ffmpeg] Convertendo para WAV...")
        converter_para_wav(audio_path, tmp_wav)
        print("[Whisper] Transcrevendo...")
        result = model.transcribe(
            tmp_wav, language="pt", word_timestamps=True, verbose=False, fp16=False,
            initial_prompt=INITIAL_PROMPT, condition_on_previous_text=False,
            no_speech_threshold=0.3, logprob_threshold=-1.2, compression_ratio_threshold=2.8,
        )
    finally:
        if os.path.exists(tmp_wav):
            os.unlink(tmp_wav)

    return result, model


def retranscrever_suspeitos(audio_path: str, model, result: dict) -> dict:
    LIMITE = 3
    JANELA = 0.05
    for i, seg in enumerate(result["segments"]):
        palavras = seg.get("words", [])
        if len(palavras) == 0 or len(palavras) > LIMITE:
            continue
        if segmento_so_hesitacoes(seg["text"]):
            continue
        start = max(0.0, seg["start"] - JANELA)
        end = seg["end"] + JANELA
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tf:
            tmp = tf.name
        try:
            extrair_trecho_wav(audio_path, start, end, tmp)
            novo = model.transcribe(
                tmp, language="pt", word_timestamps=True, verbose=False, fp16=False,
                initial_prompt=INITIAL_PROMPT, condition_on_previous_text=False,
                no_speech_threshold=0.3, logprob_threshold=-1.2,
            )
        finally:
            if os.path.exists(tmp):
                os.unlink(tmp)

        offset = start
        for ns in novo["segments"]:
            ns["start"] += offset
            ns["end"] += offset
            for w in ns.get("words", []):
                w["start"] += offset
                w["end"] += offset

        if not novo["segments"]:
            continue

        novo_texto = " ".join(s["text"].strip() for s in novo["segments"]).strip()
        if segmento_so_hesitacoes(novo_texto) or len(novo_texto) <= len(seg["text"].strip()):
            seg["text"] = novo_texto
            novos_words = []
            for ns in novo["segments"]:
                novos_words.extend(ns.get("words", []))
            seg["words"] = novos_words

    return result


# ── Detecção e montagem ───────────────────────────────────────────────────

def detectar_cortes(result: dict, silencio_min: float, padding: float) -> list:
    remover = []
    for seg in result["segments"]:
        texto = seg["text"].strip()
        dur = seg["end"] - seg["start"]
        if segmento_so_hesitacoes(texto) and dur <= MAX_DUR_HES:
            remover.append((seg["start"], seg["end"]))
            continue
        for w in seg.get("words", []):
            if e_hesitacao(w.get("word", "")) and (w["end"] - w["start"]) <= MAX_DUR_HES:
                remover.append((w["start"], w["end"]))

    segs = result["segments"]
    for i in range(1, len(segs)):
        gap_s, gap_e = segs[i - 1]["end"], segs[i]["start"]
        gap = gap_e - gap_s
        if gap >= silencio_min:
            rs, re_ = gap_s + padding, gap_e - padding
            if re_ > rs + 0.04:
                remover.append((rs, re_))

    remover.sort(key=lambda x: x[0])
    merged = []
    for s, e in remover:
        if merged and s <= merged[-1][1] + 0.20:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e))
        else:
            merged.append([s, e])
    return merged


def manter_segmentos(cortes: list, duracao_total: float) -> list:
    manter = []
    cursor = 0.0
    for s, e in cortes:
        if s > cursor + 0.01:
            manter.append((cursor, s))
        cursor = e
    if cursor < duracao_total - 0.01:
        manter.append((cursor, duracao_total))
    return manter


def montar_audio(input_path: str, output_path: str, manter: list):
    print(f"\n🔧 Montando áudio com {len(manter)} segmento(s)...")
    parts, labels = [], []
    for i, (s, e) in enumerate(manter):
        parts.append(f"[0:a]atrim=start={s:.4f}:end={e:.4f},asetpts=PTS-STARTPTS[a{i}]")
        labels.append(f"[a{i}]")
    parts.append("".join(labels) + f"concat=n={len(manter)}:v=0:a=1[out]")
    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-filter_complex", ";".join(parts),
        "-map", "[out]", "-c:a", "libmp3lame", "-q:a", "2", output_path,
    ]
    subprocess.run(cmd, check=True)


# ── Entrypoint ────────────────────────────────────────────────────────────

def main():
    print("\n╭──────────────────────────────────────╮")
    print("│  Remove Hesitações                   │")
    print("╰──────────────────────────────────────╯\n")

    input_path = input("🎙 Arquivo de entrada (mp3/mp4/wav...): ").strip()
    if not input_path or not os.path.isfile(input_path):
        print("❌ Arquivo não encontrado.")
        return

    p = Path(input_path)
    default_out = CALL_DIR / f"{p.stem}_limpo.mp3"
    saida_str = input(f"💾 Arquivo de saída [{default_out.name}]: ").strip()
    output_path = str(CALL_DIR / saida_str) if saida_str else str(default_out)

    modelo = input("🤖 Modelo Whisper [large]: ").strip() or "large"

    try:
        silencio_min = float(input("🔇 Silêncio mínimo (s) [0.45]: ").strip() or "0.45")
    except ValueError:
        silencio_min = 0.45

    try:
        padding = float(input("🔇 Padding nas bordas (s) [0.07]: ").strip() or "0.07")
    except ValueError:
        padding = 0.07

    print(f"\n🎙  Entrada : {input_path}")
    print(f"💾  Saída   : {output_path}")

    result, model = transcrever(input_path, modelo)
    print("[Whisper] Re-transcrevendo segmentos curtos...")
    result = retranscrever_suspeitos(input_path, model, result)

    cortes = detectar_cortes(result, silencio_min, padding)
    print(f"\n✂️  {len(cortes)} trecho(s) marcado(s):")
    for s, e in cortes:
        print(f"    {s:.2f}s → {e:.2f}s  ({e - s:.2f}s)")

    if not cortes:
        print("Nenhuma hesitação detectada.")
        return

    duracao = duracao_audio(input_path)
    manter = manter_segmentos(cortes, duracao)
    if not manter:
        print("⚠️  Nenhum segmento a manter.")
        return

    montar_audio(input_path, output_path, manter)

    removido = sum(e - s for s, e in cortes)
    print(f"\n✅ Salvo em: {output_path}")
    print(f"⏱  Removido: {removido:.1f}s | Original: {duracao:.1f}s | Novo: ~{duracao - removido:.1f}s")


if __name__ == "__main__":
    main()