#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OBSIDIAN SMART NOTE LINKER
- Finds semantically similar notes using TF-IDF + cosine similarity
- Pure content-based analysis
- Supports note names with spaces
- Automatically updates Similar Links.md
"""

import os
import re
import math
import shlex
import unicodedata

from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Tuple, Set


# =========================
# CONFIG
# =========================

MIN_WORD_LENGTH = 3
SIMILARITY_THRESHOLD = 0.15
MAX_RESULTS = 10

MAIN_PATH = "/home/val/Documentos/Notes"
OUTPUT_FILE = "/home/val/Documentos/Notes/+/Similar Links.md"


# =========================
# NOTE LINKER
# =========================

class NoteLinker:

    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path).resolve()
        self._validate_vault()
        self.stopwords = self._load_stopwords()
        self.notes = {}
        self.vocabulary = set()
        self.tfidf_vectors = {}

    # =========================
    # VALIDATION
    # =========================
    def _validate_vault(self):

        if not self.vault_path.exists():
            raise FileNotFoundError(
                f"Vault not found at {self.vault_path}"
            )

        if not list(self.vault_path.glob("**/*.md")):
            print(f"⚠️ Warning: No markdown files found in {self.vault_path}")
   
    # =========================
    # STOPWORDS
    # =========================
    def _load_stopwords(self) -> Set[str]:

        return {
            'o', 'a', 'os', 'as',
            'um', 'uma',
            'de', 'do', 'da',
            'em', 'no', 'na',
            'que', 'com',
            'para', 'por',
            'sem', 'ao', 'à',
            'das', 'dos',

            'the', 'and', 'of',
            'to', 'in', 'is',
            'it', 'that', 'for',
            'with', 'on'
        }

    # =========================
    # TEXT NORMALIZATION
    # =========================
    def _normalize_text(self, text: str) -> str:

        text = unicodedata.normalize(
            'NFKD',
            text.lower()
        )
        return ''.join(
            c for c in text
            if not unicodedata.combining(c)
        )

    # =========================
    # TOKENIZATION
    # =========================
    def _tokenize(self, text: str) -> List[str]:

        text = self._normalize_text(text)
        words = re.findall(r'\b[\w-]+\b', text)
        return [
            w for w in words
            if (
                w not in self.stopwords
                and len(w) >= MIN_WORD_LENGTH
                and not w.isdigit()
            )
        ]

    # =========================
    # LOAD NOTES
    # =========================
    def load_notes(self):

        for note_path in self.vault_path.glob("**/*.md"):

            if ".obsidian" in note_path.parts:
                continue

            try:

                with open(note_path, "r", encoding="utf-8") as f:

                    content = f.read()

                    # Remove YAML frontmatter
                    content = re.sub(
                        r'^---\n.*?\n---\n',
                        '',
                        content,
                        flags=re.DOTALL
                    )

                    # Remove Obsidian links
                    content = re.sub(
                        r'\[\[(.*?)\]\]',
                        r'\1',
                        content
                    )

                    relative = str(
                        note_path.relative_to(self.vault_path)
                    )

                    self.notes[relative] = content

                    self.vocabulary.update(
                        self._tokenize(content)
                    )

            except Exception as e:

                print(f"⚠️ Error processing {note_path.name}: {e}")

        self._build_tfidf_vectors()

    # =========================
    # TF-IDF
    # =========================
    def _build_tfidf_vectors(self):

        doc_freq = defaultdict(int)

        for content in self.notes.values():

            unique_words = set(
                self._tokenize(content)
            )

            for word in unique_words:
                doc_freq[word] += 1

        total_docs = len(self.notes)

        for note_path, content in self.notes.items():

            tokens = self._tokenize(content)

            if not tokens:
                continue

            term_freq = Counter(tokens)

            vector = {}

            for word, count in term_freq.items():

                tf = count / len(tokens)

                idf = math.log(
                    total_docs / (1 + doc_freq[word])
                )

                vector[word] = tf * idf

            self.tfidf_vectors[note_path] = vector

    # =========================
    # COSINE SIMILARITY
    # =========================
    def _cosine_similarity(
        self,
        vec_a: Dict[str, float],
        vec_b: Dict[str, float]
    ) -> float:

        common_words = (
            set(vec_a.keys()) &
            set(vec_b.keys())
        )

        dot_product = sum(
            vec_a[word] * vec_b[word]
            for word in common_words
        )

        norm_a = math.sqrt(
            sum(v ** 2 for v in vec_a.values())
        )

        norm_b = math.sqrt(
            sum(v ** 2 for v in vec_b.values())
        )

        if norm_a == 0 or norm_b == 0:
            return 0.0

        return dot_product / (norm_a * norm_b)

    # =========================
    # FIND SIMILAR
    # =========================

    def find_similar(
        self,
        target_note: str,
        threshold: float = SIMILARITY_THRESHOLD
    ) -> List[Tuple[str, float]]:

        if target_note not in self.tfidf_vectors:

            raise ValueError(
                f"Note not found: {target_note}"
            )

        target_vector = self.tfidf_vectors[target_note]

        results = []

        for note_path, vector in self.tfidf_vectors.items():

            if note_path == target_note:
                continue

            similarity = self._cosine_similarity(
                target_vector,
                vector
            )

            if similarity >= threshold:

                results.append(
                    (note_path, similarity)
                )

        return sorted(
            results,
            key=lambda x: x[1],
            reverse=True
        )[:MAX_RESULTS]


# =========================
# DISPLAY RESULTS
# =========================

def display_results(
    target: str,
    results: List[Tuple[str, float]]
):

    if not results:

        print(f"\nNo similar notes found for '{target}'")
        return

    print(f"\n🔗 Similar notes for '{target}':")
    print("=" * 60)

    for i, (note, score) in enumerate(results, 1):

        print(f"{i}. {note} ({score:.1%})")
        print(f"   {os.path.dirname(note)}")
        print()


# =========================
# SAVE MARKDOWN
# =========================

def save_markdown(
    target_note: str,
    results: List[Tuple[str, float]]
):

    output_path = Path(OUTPUT_FILE)

    try:

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(output_path, "w", encoding="utf-8") as f:        
            f.write("Note Search\n")
            f.write(
                f"[[{Path(target_note).with_suffix('')}]]\n\n"
            )

            if not results:
                f.write(
                    "> No similar notes found.\n"
                )
            else:
                f.write("Related Notes\n\n")
                for note, score in results:
                    relative_path = Path(note).with_suffix('')
                    f.write(
                        f"- [[{relative_path}]] — {score:.1%}\n"
                    )

        print(f"✅ Arquivo atualizado: {output_path}")

    except Exception as e:

        print(f"❌ Error saving markdown: {e}")


# =========================
# MAIN
# =========================

if __name__ == "__main__":

    print("OBSIDIAN NOTE LINKER")
    print("=" * 40)

    try:

        linker = NoteLinker(MAIN_PATH)

        linker.load_notes()

        print(f"\nLoaded {len(linker.notes)} notes from vault")

        print("\nEnter note path")
        print("Examples:")
        print("  Projetos/ideias")
        print('  "+/draft Snippet Intelligence System"')
        print('  "+/draft Snippet Intelligence System" 0.25')

        print(f"\nThreshold default: {SIMILARITY_THRESHOLD}")
        print("Type 'exit' to quit\n")

        while True:

            try:

                user_input = input(">> ").strip()

                if user_input.lower() in (
                    'exit',
                    'quit',
                    'q'
                ):
                    break

                if not user_input:
                    continue

                # Parse shell-like input
                parts = shlex.split(user_input)

                threshold = SIMILARITY_THRESHOLD

                # Check if last argument is float
                if len(parts) > 1:

                    try:

                        threshold = float(parts[-1])

                        note_path = " ".join(parts[:-1])

                    except ValueError:

                        note_path = " ".join(parts)

                else:

                    note_path = parts[0]

                # Normalize path
                note_path = note_path.strip()

                note_path = note_path.replace("\\", "/")

                # Auto-add .md
                if not note_path.endswith(".md"):
                    note_path += ".md"

                results = linker.find_similar(
                    note_path,
                    threshold
                )

                display_results(
                    note_path,
                    results
                )

                save_markdown(
                    note_path,
                    results
                )

            except Exception as e:

                print(f"Error: {e}")

    except Exception as e:

        print(f"Fatal error: {e}")