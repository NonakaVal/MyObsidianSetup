#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audio/transcriber.py
Transcreve áudios usando Whisper.
Modos: simples (texto) ou com timestamps (segmentado).
Saída gerada no diretório onde o comando foi chamado.
"""

import os
import sys
import time
import wave
import tempfile
import subprocess
from pathlib import Path
from datetime import datetime

import numpy as np

# ── Ambiente PyBox ────────────────────────────────────────────────────────
CALL_DIR = Path(os.environ.get("PYBOX_CALL_DIR", Path.cwd()))


# ── Helpers de áudio ─────────────────────────────────────────────────────

def listar_audios(pasta: Path) -> list[Path]:
    exts = {".mp3", ".wav", ".ogg", ".opus", ".m4a", ".mp4", ".flac", ".mov", ".mkv"}
    return sorted([p for p in pasta.rglob("*") if p.suffix.lower() in exts])


def converter_para_wav(arquivo: Path) -> Path:
    tmp = Path(tempfile.gettempdir()) / f"pybox_{arquivo.stem}.wav"
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(arquivo), "-ac", "1", "-ar", "16000", "-vn", str(tmp)],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    return tmp


def wav_valido(p: Path) -> bool:
    try:
        with wave.open(str(p), "rb") as w:
            n = w.getnframes()
            dur = n / float(w.getframerate())
            if dur < 0.2:
                return False
            audio = np.frombuffer(w.readframes(n), dtype=np.int16)
            return not np.all(audio == 0)
    except Exception:
        return False


def duracao_wav(p: Path) -> float:
    try:
        with wave.open(str(p), "rb") as w:
            return w.getnframes() / float(w.getframerate())
    except Exception:
        return 0.0


def fmt_tempo(s: float) -> str:
    t = int(s)
    h, m, seg = t // 3600, (t % 3600) // 60, t % 60
    return f"{h}:{m:02d}:{seg:02d}" if h else f"{m:02d}:{seg:02d}"


# ── Transcrição simples ───────────────────────────────────────────────────

def transcrever_simples(caminho: Path, modelo) -> str | None:
    wav = converter_para_wav(caminho)
    if not wav_valido(wav):
        return None
    try:
        t0 = time.time()
        resultado = modelo.transcribe(str(wav), fp16=False)
        print(f"  ✔ {time.time() - t0:.1f}s")
        return resultado["text"].strip()
    except Exception as e:
        print(f"  ❌ {e}")
        return None


# ── Transcrição com timestamps ────────────────────────────────────────────

def transcrever_timestamps(caminho: Path, modelo, silencio_min: float):
    wav = converter_para_wav(caminho)
    if not wav_valido(wav):
        return None, 0.0
    try:
        duracao = duracao_wav(wav)
        t0 = time.time()
        resultado = modelo.transcribe(str(wav), fp16=False)
        print(f"  ✔ {time.time() - t0:.1f}s")

        itens = []
        prev_end = None
        for seg in resultado.get("segments", []):
            texto = seg["text"].strip()
            if not texto:
                continue
            if prev_end is not None:
                gap = seg["start"] - prev_end
                if gap >= silencio_min:
                    itens.append(("silencio", gap))
            itens.append(("linha", seg["start"], seg["end"], texto))
            prev_end = seg["end"]

        return itens, duracao
    except Exception as e:
        print(f"  ❌ {e}")
        return None, 0.0


# ── Frontmatter ───────────────────────────────────────────────────────────

def frontmatter(extra: dict | None = None) -> str:
    hoje = datetime.now().strftime("%Y-%m-%d")
    linhas = ["---", f'created: "[[{hoje}]]"', "tags:", "  - transcriptions"]
    if extra:
        for k, v in extra.items():
            linhas.append(f'{k}: "{v}"')
    linhas.append("---\n")
    return "\n".join(linhas)


# ── Modo simples ──────────────────────────────────────────────────────────

def modo_simples():
    print("\n── Transcrição Simples ──────────────────────────────")
    pasta_str = input("📂 Pasta com áudios: ").strip()
    pasta = Path(pasta_str).expanduser().resolve()
    if not pasta.exists():
        print("❌ Pasta não encontrada.")
        return

    modelo_nome = input("🤖 Modelo Whisper [medium]: ").strip() or "medium"
    saida_nome = input(f"💾 Nome do arquivo de saída [transcricoes.md]: ").strip() or "transcricoes.md"

    audios = listar_audios(pasta)
    if not audios:
        print("❌ Nenhum áudio encontrado.")
        return

    print(f"\n📥 {len(audios)} arquivo(s) encontrado(s).")

    import whisper
    modelo = whisper.load_model(modelo_nome)

    grupos: dict[str, list[Path]] = {}
    for a in audios:
        rel = str(a.parent.relative_to(pasta))
        grupos.setdefault(rel, []).append(a)

    saida = CALL_DIR / saida_nome
    with open(saida, "w", encoding="utf-8") as f:
        f.write(frontmatter())
        for pasta_rel, arquivos in sorted(grupos.items()):
            f.write(f"## 📁 {pasta_rel}\n\n")
            for i, audio in enumerate(sorted(arquivos, key=lambda x: x.name.lower()), 1):
                print(f"({i}/{len(audios)}) ▶ {audio.name}")
                texto = transcrever_simples(audio, modelo)
                if texto:
                    f.write(f"- audio {audio.name}\n")
                    f.write(f"   - {texto}\n")
        f.write("\n")

    print(f"\n✅ Salvo em: {saida}")


# ── Modo com timestamps ───────────────────────────────────────────────────

def modo_timestamps():
    print("\n── Transcrição com Timestamps ───────────────────────")
    pasta_str = input("📂 Pasta com áudios: ").strip()
    pasta = Path(pasta_str).expanduser().resolve()
    if not pasta.exists():
        print("❌ Pasta não encontrada.")
        return

    modelo_nome = input("🤖 Modelo Whisper [medium]: ").strip() or "medium"

    while True:
        try:
            silencio_min = float(input("🔇 Silêncio mínimo p/ separação (s) [2.0]: ").strip() or "2.0")
            if silencio_min > 0:
                break
        except ValueError:
            pass

    saida_nome = input(f"💾 Nome do arquivo de saída [transcricoes_ts.md]: ").strip() or "transcricoes_ts.md"

    audios = listar_audios(pasta)
    if not audios:
        print("❌ Nenhum áudio encontrado.")
        return

    print(f"\n📥 {len(audios)} arquivo(s) encontrado(s).")

    import whisper
    modelo = whisper.load_model(modelo_nome)

    grupos: dict[str, list[Path]] = {}
    for a in audios:
        rel = str(a.parent.relative_to(pasta))
        grupos.setdefault(rel, []).append(a)

    dados: dict[str, list] = {}
    total = len(audios)
    contador = 0
    for rel, arquivos in grupos.items():
        dados[rel] = []
        for audio in sorted(arquivos):
            contador += 1
            print(f"({contador}/{total}) ▶ {audio.name}")
            itens, dur = transcrever_timestamps(audio, modelo, silencio_min)
            if itens is not None:
                dados[rel].append((audio, itens, dur))

    hoje = datetime.now().strftime("%Y-%m-%d")
    saida = CALL_DIR / saida_nome

    with open(saida, "w", encoding="utf-8") as f:
        f.write(frontmatter({
            "source": str(pasta),
            "model": modelo_nome,
            "silence_gap": f"{silencio_min}s",
        }))
        f.write(f"# 🎙️ Transcrições — {hoje}\n\n")

        for rel, registros in dados.items():
            if not registros:
                continue
            f.write(f"## 📁 {rel}\n\n")
            for audio, itens, dur in registros:
                n_segs = sum(1 for i in itens if i[0] == "linha")
                f.write(f"### 🎞️ {audio.name}\n\n")
                f.write(f"> ⏱ Duração: `{fmt_tempo(dur)}` · 📝 {n_segs} segmento(s)\n\n")

                for item in itens:
                    if item[0] == "linha":
                        _, t_ini, t_fim, texto = item
                        f.write(f"- `{fmt_tempo(t_ini)} → {fmt_tempo(t_fim)}` {texto}\n")
                    else:
                        _, dur_sil = item
                        f.write(f"\n> 🔇 *silêncio de {dur_sil:.1f}s*\n\n")

                f.write("\n---\n\n")

    print(f"\n✅ Salvo em: {saida}")


# ── Entrypoint ────────────────────────────────────────────────────────────

def main():
    print("\n╭──────────────────────────────────────╮")
    print("│  Audio Transcriber                   │")
    print("╰──────────────────────────────────────╯")
    print("\n1. Transcrição simples")
    print("2. Com timestamps e silêncios")

    modo = input("\nModo [1]: ").strip() or "1"
    if modo == "1":
        modo_simples()
    elif modo == "2":
        modo_timestamps()
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()