import time, wave, tempfile, subprocess
import numpy as np
import whisper
from pathlib import Path

INPUT_PATH = Path("/home/val/Músicas/")
OUT_TXT    = Path("/home/val/Documentos/Notes/+/_output/quick_transcribe.txt")
MODEL_NAME = "medium"


def to_wav(f: Path) -> Path:
    out = Path(tempfile.gettempdir()) / f"{f.stem}.wav"

    subprocess.run(
        ["ffmpeg", "-y", "-i", str(f), "-ac", "1", "-ar", "16000", "-vn", str(out)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return out


def valid(w: Path) -> bool:
    try:
        with wave.open(str(w)) as f:
            frames = f.readframes(n := f.getnframes())
            return n / f.getframerate() >= 0.2 and not np.all(
                np.frombuffer(frames, np.int16) == 0
            )
    except:
        return False


def transcribe(f: Path, model) -> str | None:
    w = to_wav(f)

    if not valid(w):
        return None

    try:
        return model.transcribe(str(w), fp16=False)["text"].strip()
    except Exception as e:
        print(f"❌ {f.name}: {e}")
        return None


exts = {'.mp3', '.wav', '.ogg', '.opus', '.m4a', '.mp4', '.flac', '.mov','.mkv'}

files = sorted(
    [f for f in INPUT_PATH.rglob("*") if f.suffix.lower() in exts],
    key=lambda f: (str(f.parent), f.name.lower())
)

OUT_TXT.parent.mkdir(parents=True, exist_ok=True)

print(f"Loading Whisper model '{MODEL_NAME}'...")
model = whisper.load_model(MODEL_NAME)
print("Model loaded successfully.")

with open(OUT_TXT, "a", encoding="utf-8") as out:
    for f in files:
        t = time.time()
        text = transcribe(f, model)

        if text:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            elapsed = time.time() - t

            block = f"""[{timestamp}] - [{f.name}]
{text}
⏱ Tempo: {elapsed:.1f}s

"""

            print(block)
            out.write(block)

print(f"✅ Transcrições adicionadas em: {OUT_TXT}")