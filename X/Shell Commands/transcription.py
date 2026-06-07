import time
import wave
import numpy as np
import whisper
from pathlib import Path
import subprocess
import tempfile



CAMINHO_AUDIOS = Path("/home/val/Músicas/d/")
PESSOA = "jhee"  # Nome da pessoa associada aos áudios (ex: 'Henrique'): ").strip() or "Pessoa"

MODEL = "medium"    # 🤖 Modelo Whisper (ex: tiny, base, small, medium): ").strip() or "medium"


def listar_audios_recursivo(pasta: Path):
    exts = {'.mp3', '.wav', '.ogg', '.opus', '.m4a', '.mp4', '.flac'}
    return [p for p in pasta.rglob("*") if p.suffix.lower() in exts]


def has_audio_stream(path: Path) -> bool:
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "a",
             "-show_entries", "stream=codec_type", "-of", "default=nw=1",
             str(path)],
            capture_output=True, text=True
        )
        return "codec_type=audio" in result.stdout
    except:
        return False


def converter_para_wav(arquivo: Path) -> Path:
    temp_file = Path(tempfile.gettempdir()) / f"{arquivo.stem}.wav"
    cmd = [
        "ffmpeg", "-y", "-i", str(arquivo),
        "-ac", "1", "-ar", "16000",
        "-vn",
        str(temp_file)
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return temp_file


def wav_valido(wav_path: Path) -> bool:
    try:
        with wave.open(str(wav_path), "rb") as wav:
            nframes = wav.getnframes()
            rate = wav.getframerate()
            dur = nframes / float(rate)

            if dur < 0.2:
                return False

            audio = np.frombuffer(wav.readframes(nframes), dtype=np.int16)
            if np.all(audio == 0):
                return False

        return True

    except:
        return False


def transcrever_audio(caminho_audio, modelo):
    wav_temp = converter_para_wav(caminho_audio)

    if not wav_valido(wav_temp):
        # print("❌ Áudio inválido/silencioso → ignorado.")
        return None

    try:
        inicio = time.time()
        resultado = modelo.transcribe(str(wav_temp), fp16=False)
        #print(f"✔️ Finalizado em {time.time() - inicio:.2f}s")
        return resultado["text"].strip()
    except Exception as e:
        #print(f"❌ Erro: {e}")
        return None


def processar_todos_audios():
    caminho_audios = CAMINHO_AUDIOS
    modelo_nome = MODEL

    audios = listar_audios_recursivo(caminho_audios)
    total = len(audios)
    # print(f"\n📥 {total} arquivos encontrados (recursivo).")

    modelo = whisper.load_model(modelo_nome)
    # print("Modelo carregado.")

    grupos = {}
    for audio in audios:
        rel = audio.parent.relative_to(caminho_audios)
        grupos.setdefault(str(rel), []).append(audio)

    contador = 0

    for pasta, arquivos in sorted(grupos.items()):
        arquivos_ordenados = sorted(arquivos, key=lambda a: a.name.lower())

        print(f"- 🔊 {PESSOA} \n")

        for audio in arquivos_ordenados:
            contador += 1
            # print(f"\n({contador}/{total}) ▶️ Transcrevendo: {audio.name}")

            texto = transcrever_audio(audio, modelo)

            if texto:
                print(f"- audio {audio.name}")
                print(f"   - {texto}")


if __name__ == "__main__":
    processar_todos_audios()
