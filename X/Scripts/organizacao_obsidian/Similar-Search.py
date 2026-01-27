#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OBSIDIAN SMART NOTE LINKER
--------------------------------
- Encontra notas semanticamente semelhantes usando vetorização simples + similaridade de cosseno.
- Suporta caminhos absolutos e relativos (incluindo prefixos '+/').
- Salva resultados em um único arquivo Markdown (SimilarLinks.md).
"""

import os
import re
import sys
import unicodedata
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple

# Garante UTF-8 no terminal
sys.stdout.reconfigure(encoding="utf-8")

# ==========================
# 🔧 CONFIGURAÇÕES
# ==========================
VAULT_PATH = Path(r"/home/nonaka/Documentos/Vaults/Notes/")
OUTPUT_FILE = "/home/nonaka/Documentos/Vaults/Notes/+/SimilarLinks.md"
OUTPUT_DIR = VAULT_PATH  # salvar no root do vault

# Caminho relativo EXEMPLO:
TARGET_NOTE = "Code/+/doc-tmux-basic-comands.md"
# ==========================


# ==========================
# 📂 PROCESSAMENTO DE TEXTO
# ==========================
def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    return "".join(c for c in text if not unicodedata.combining(c)).lower()


def tokenize(text: str) -> List[str]:
    return re.findall(r"\b\w+\b", normalize_text(text))


def vectorize(tokens: List[str]) -> Dict[str, int]:
    vec = defaultdict(int)
    for t in tokens:
        vec[t] += 1
    return dict(vec)


def cosine_similarity(vec1: Dict[str, int], vec2: Dict[str, int]) -> float:
    common = set(vec1.keys()) & set(vec2.keys())
    dot = sum(vec1[w] * vec2[w] for w in common)

    norm1 = sum(v * v for v in vec1.values()) ** 0.5
    norm2 = sum(v * v for v in vec2.values()) ** 0.5

    return dot / (norm1 * norm2) if norm1 and norm2 else 0.0


# ==========================
# 🔍 CAMINHOS
# ==========================
def resolve_path(user_path: str) -> Path:
    """
    Interpreta:
      - Caminhos absolutos
      - Caminhos relativos ao vault (começando com '/')
      - Prefixo '+/' usado para caminhos relativos dentro do vault
    """
    user_path = user_path.strip()

    # caso relativo estilo '/folder/note.md'
    if user_path.startswith("/"):
        return (VAULT_PATH / user_path[1:]).resolve()

    # caso '+/folder/...'
    if user_path.startswith("+/"):
        return (VAULT_PATH / user_path[2:]).resolve()

    # caso absoluto
    up = Path(user_path)
    if up.is_absolute():
        return up

    # fallback: considerar relativo ao vault
    return (VAULT_PATH / user_path).resolve()


# ==========================
# 🔍 ANÁLISE DO VAULT
# ==========================
def build_note_vectors(vault_path: Path) -> Dict[str, Dict[str, int]]:
    vectors = {}
    for path in vault_path.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
            vectors[str(path)] = vectorize(tokenize(text))
        except Exception as e:
            print(f"⚠️ Erro ao ler {path}: {e}")
    return vectors


def find_similar_notes(target_note: Path,
                       vectors: Dict[str, Dict[str, int]],
                       top_n=10) -> List[Tuple[str, float]]:

    target_text = target_note.read_text(encoding="utf-8")
    target_vec = vectorize(tokenize(target_text))

    sims = [
        (note, cosine_similarity(target_vec, vec))
        for note, vec in vectors.items()
        if Path(note) != target_note
    ]

    return sorted(sims, key=lambda x: x[1], reverse=True)[:top_n]


# ==========================
# 📝 SAÍDA
# ==========================
def save_markdown(target_note: Path, results: List[Tuple[str, float]]):
    filepath = OUTPUT_DIR / OUTPUT_FILE
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    base_name = target_note.stem

    try:
        with filepath.open("w", encoding="utf-8") as f:
            f.write(f"### 🔗 Notas semelhantes a: [[{base_name}]]\n\n")

            for note, score in results:
                filename = Path(note).stem.replace("_", " ")
                f.write(f"- [[{filename}]] — **{score:.1%}**\n")

        print(f"✅ : {filepath}")
    except Exception as e:
        print(f"❌ Erro ao salvar Markdown: {e}")


# ==========================
# 🚀 EXECUÇÃO
# ==========================
def main():
    target_note = resolve_path(TARGET_NOTE)

    if not target_note.exists():
        print(f"❌ Arquivo não encontrado: {target_note}")
        return

    print("📂 Indexando notas...")
    vectors = build_note_vectors(VAULT_PATH)
    results = find_similar_notes(target_note, vectors)

    save_markdown(target_note, results)


if __name__ == "__main__":
    main()
