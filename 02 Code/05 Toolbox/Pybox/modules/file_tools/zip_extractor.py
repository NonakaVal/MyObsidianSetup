#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
file_tools/zip_extractor.py
Extrai arquivos ZIP preservando estrutura e ignorando duplicatas (SHA-256).
Saída no diretório onde o comando foi chamado ou caminho especificado.
"""

import hashlib
import os
import shutil
import zipfile
from pathlib import Path

# ── Ambiente PyBox ────────────────────────────────────────────────────────
CALL_DIR = Path(os.environ.get("PYBOX_CALL_DIR", Path.cwd()))


# ── Hash ──────────────────────────────────────────────────────────────────

def sha256sum(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


# ── Extração segura ───────────────────────────────────────────────────────

def safe_extract(zf: zipfile.ZipFile, member: str, temp_root: Path) -> Path | None:
    member = member.replace("\\", "/")
    dest = temp_root / member
    if member.endswith("/"):
        dest.mkdir(parents=True, exist_ok=True)
        return None
    dest.parent.mkdir(parents=True, exist_ok=True)
    with zf.open(member) as src, open(dest, "wb") as dst:
        shutil.copyfileobj(src, dst)
    return dest


def ensure_unique(dest: Path) -> Path:
    if not dest.exists():
        return dest
    stem, suffix, parent = dest.stem, dest.suffix, dest.parent
    i = 1
    while True:
        cand = parent / f"{stem}_{i}{suffix}"
        if not cand.exists():
            return cand
        i += 1


# ── Processamento ─────────────────────────────────────────────────────────

def extrair_zip(zip_path: Path, dest: Path, hash_db: dict):
    print(f"\n📦 {zip_path.name}")
    temp_root = dest / "_pybox_temp_extract"
    temp_root.mkdir(parents=True, exist_ok=True)

    try:
        with zipfile.ZipFile(zip_path, "r") as z:
            for member in z.namelist():
                try:
                    tmp = safe_extract(z, member, temp_root)
                    if tmp is None or not tmp.exists() or tmp.is_dir():
                        continue

                    fhash = sha256sum(tmp)
                    if fhash in hash_db:
                        print(f"  ⚠ Duplicata: {member}")
                        tmp.unlink()
                        continue

                    hash_db[fhash] = member
                    final = ensure_unique(dest / member)
                    final.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(tmp), str(final))
                    print(f"  ✔ {final.relative_to(dest)}")
                except Exception as e:
                    print(f"  ❌ {member}: {e}")
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)


# ── Entrypoint ────────────────────────────────────────────────────────────

def main():
    print("\n╭──────────────────────────────────────╮")
    print("│  Smart ZIP Extractor                 │")
    print("╰──────────────────────────────────────╯\n")

    zip_dir_str = input("📁 Pasta com os arquivos .zip: ").strip()
    zip_dir = Path(zip_dir_str).expanduser().resolve()
    if not zip_dir.exists():
        print("❌ Pasta não encontrada.")
        return

    dest_str = input(f"📂 Destino da extração [{CALL_DIR}]: ").strip()
    dest = Path(dest_str).expanduser().resolve() if dest_str else CALL_DIR
    dest.mkdir(parents=True, exist_ok=True)

    zips = list(zip_dir.rglob("*.zip"))
    if not zips:
        print("❌ Nenhum arquivo .zip encontrado.")
        return

    print(f"\n🔍 {len(zips)} ZIP(s) encontrado(s).")
    hash_db = {}
    for z in zips:
        extrair_zip(z, dest, hash_db)

    print(f"\n✅ Extração concluída. Arquivos em: {dest}")


if __name__ == "__main__":
    main()