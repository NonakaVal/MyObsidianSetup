#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
obsidian_tools/vault_tools.py
Ferramentas para gestão de vaults Obsidian:
 - Busca por termo (índice invertido)
 - Busca por nota similar (TF-IDF cosine)
 - Substituição global em notas
 - Reset de frontmatter por pasta
 - Gerador Zettelkasten (split por ## em notas atômicas)
 - Tradutor de vault (EN→PT via OpenAI)
 - Gerenciador de template folder (Templater plugin)
"""

import json
import math
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

# ── Ambiente PyBox ────────────────────────────────────────────────────────
CALL_DIR = Path(os.environ.get("PYBOX_CALL_DIR", Path.cwd()))


# ══════════════════════════════════════════════════════════════════════════
#  1 — BUSCA POR TERMO
# ══════════════════════════════════════════════════════════════════════════

class BuscadorNotas:
    def __init__(self, pasta: Path):
        self.indice: dict[str, list[tuple]] = defaultdict(list)
        self._construir(pasta)

    def _construir(self, pasta: Path):
        print("🔍 Construindo índice...")
        for root, _, files in os.walk(pasta):
            for f in files:
                if f.endswith(".md"):
                    caminho = Path(root) / f
                    try:
                        conteudo = caminho.read_text(encoding="utf-8", errors="ignore").lower()
                        for palavra in set(re.findall(r"\b\w+\b", conteudo)):
                            self.indice[palavra].append((f, str(caminho)))
                    except Exception:
                        pass
        print(f"✅ Índice com {len(self.indice)} termos.\n")

    def buscar(self, termo: str):
        res = self.indice.get(termo.lower(), [])
        print(f"\n🔎 '{termo}': {len(res)} nota(s) encontrada(s)")
        for arq, caminho in res:
            print(f"  - {arq}\n    {caminho}")
        return res


def modo_busca_termo(vault: Path):
    b = BuscadorNotas(vault)
    while True:
        t = input("\nTermo (ou 'sair'): ").strip()
        if t.lower() in ("sair", "q", ""):
            break
        b.buscar(t)


# ══════════════════════════════════════════════════════════════════════════
#  2 — BUSCA POR SIMILARIDADE (TF-IDF)
# ══════════════════════════════════════════════════════════════════════════

STOPWORDS = {
    "o", "a", "os", "as", "um", "uma", "de", "do", "da", "em", "no", "na",
    "que", "com", "para", "por", "sem", "ao", "the", "and", "of", "to", "in",
    "is", "it", "that", "for", "with", "on",
}

MIN_WORD = 3
SIM_THRESHOLD = 0.15
MAX_RESULTS = 10


def _normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text.lower())
    return "".join(c for c in text if not unicodedata.combining(c))


def _tokenize(text: str) -> list[str]:
    words = re.findall(r"\b[\w-]+\b", _normalize(text))
    return [w for w in words if w not in STOPWORDS and len(w) >= MIN_WORD and not w.isdigit()]


def _load_notes(vault: Path) -> dict[str, str]:
    notes = {}
    for p in vault.glob("**/*.md"):
        if ".obsidian" in p.parts:
            continue
        content = re.sub(r"^---\n.*?\n---\n", "", p.read_text(encoding="utf-8", errors="ignore"), flags=re.DOTALL)
        content = re.sub(r"\[\[(.*?)\]\]", r"\1", content)
        notes[str(p.relative_to(vault))] = content
    return notes


def _build_tfidf(notes: dict) -> dict[str, dict[str, float]]:
    doc_freq: Counter = Counter()
    for content in notes.values():
        for w in set(_tokenize(content)):
            doc_freq[w] += 1
    total = len(notes)
    vecs = {}
    for path, content in notes.items():
        tokens = _tokenize(content)
        tf = Counter(tokens)
        vec = {}
        for w, c in tf.items():
            vec[w] = (c / len(tokens)) * math.log(total / (1 + doc_freq[w]))
        vecs[path] = vec
    return vecs


def _cosine(a: dict, b: dict) -> float:
    common = set(a) & set(b)
    dot = sum(a[w] * b[w] for w in common)
    na = math.sqrt(sum(v ** 2 for v in a.values()))
    nb = math.sqrt(sum(v ** 2 for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0


def modo_busca_similar(vault: Path):
    print("⏳ Carregando notas e construindo vetores TF-IDF...")
    notes = _load_notes(vault)
    vecs = _build_tfidf(notes)
    print(f"✅ {len(notes)} notas carregadas.\n")

    while True:
        alvo = input("Caminho da nota (ex: ATLAS/nota.md) ou 'sair': ").strip()
        if alvo.lower() in ("sair", "q", ""):
            break
        if alvo not in vecs:
            print(f"❌ Nota não encontrada: {alvo}")
            continue
        resultados = sorted(
            [(p, _cosine(vecs[alvo], v)) for p, v in vecs.items() if p != alvo and _cosine(vecs[alvo], v) >= SIM_THRESHOLD],
            key=lambda x: x[1], reverse=True,
        )[:MAX_RESULTS]

        if not resultados:
            print("Nenhuma nota similar encontrada.")
            continue

        print(f"\n🔗 Similares a '{alvo}':")
        for i, (nota, score) in enumerate(resultados, 1):
            print(f"  {i}. {nota} ({score:.1%})")

        salvar = input("\n💾 Salvar resultado? (s/N): ").strip().lower()
        if salvar == "s":
            nome_saida = f"similar_{Path(alvo).stem}.md"
            saida = CALL_DIR / nome_saida
            with open(saida, "w", encoding="utf-8") as f:
                f.write(f"# 🔗 Notas semelhantes a `{alvo}`\n\n")
                for nota, score in resultados:
                    f.write(f"- [[{Path(nota).with_suffix('')}]] ({score:.1%})\n")
            print(f"✅ Salvo em: {saida}")


# ══════════════════════════════════════════════════════════════════════════
#  3 — SUBSTITUIÇÃO GLOBAL
# ══════════════════════════════════════════════════════════════════════════

def modo_substituicao_global(vault: Path):
    alvo = input("🔎 Texto a buscar: ")
    if not alvo:
        return

    encontrados = []
    total_occ = 0
    for root, _, files in os.walk(vault):
        for f in files:
            if f.endswith(".md"):
                p = Path(root) / f
                content = p.read_text(encoding="utf-8", errors="ignore")
                n = content.count(alvo)
                if n > 0:
                    encontrados.append((p, n))
                    total_occ += n
                    print(f"  {p} → {n} ocorrência(s)")

    print(f"\n📊 {len(encontrados)} arquivo(s), {total_occ} ocorrência(s)")
    if not encontrados:
        return

    substituto = input("✏️  Substituir por: ")
    confirm = input("Confirmar? (sim/N): ").strip().lower()
    if confirm != "sim":
        print("Cancelado.")
        return

    for p, _ in encontrados:
        content = p.read_text(encoding="utf-8")
        p.write_text(content.replace(alvo, substituto), encoding="utf-8")
        print(f"  ✔ {p.name}")
    print(f"\n✅ {len(encontrados)} arquivo(s) atualizados.")


# ══════════════════════════════════════════════════════════════════════════
#  4 — RESET DE FRONTMATTER POR PASTA
# ══════════════════════════════════════════════════════════════════════════

def modo_reset_frontmatter():
    pasta_str = input("📂 Pasta alvo: ").strip()
    pasta = Path(pasta_str).expanduser().resolve()
    if not pasta.exists():
        print("❌ Pasta não encontrada.")
        return

    confirm_path = input("✔ Redigite o caminho para confirmar: ").strip()
    if confirm_path not in str(pasta):
        print("❌ Confirmação falhou.")
        return

    print("Escreva o novo frontmatter (termine com uma linha vazia):")
    linhas_fm = []
    while True:
        linha = input()
        if linha == "":
            break
        linhas_fm.append(linha)
    novo_fm = "\n".join(linhas_fm)

    confirm = input("\n⚠️  Sobrescrever frontmatter em todos os .md da pasta? (confirmar/N): ").strip().lower()
    if confirm != "confirmar":
        print("Cancelado.")
        return

    count = 0
    for root, _, files in os.walk(pasta):
        for f in files:
            if f.endswith(".md"):
                p = Path(root) / f
                content = p.read_text(encoding="utf-8", errors="ignore")
                if content.startswith("---"):
                    end = content.find("---", 3)
                    if end != -1:
                        content = content[end + 3:].lstrip()
                p.write_text(novo_fm + "\n" + content, encoding="utf-8")
                print(f"  ✔ {p.name}")
                count += 1

    print(f"\n✅ {count} arquivo(s) atualizados.")


# ══════════════════════════════════════════════════════════════════════════
#  5 — GERADOR ZETTELKASTEN
# ══════════════════════════════════════════════════════════════════════════

def _sanitizar_nome(nome: str) -> str:
    nome = re.sub(r'[\\/#%&{}<>*?$\'":@\[\]]', "", nome)
    nome = nome.strip().lower().replace(" ", "-")
    return re.sub(r"-+", "-", nome) or "untitled"


def _extrair_secoes(conteudo: str) -> list[str]:
    return re.findall(r"(## .+?)(?=\n## |\Z)", conteudo, flags=re.DOTALL)


def modo_zettelkasten():
    arq_str = input("📄 Arquivo .md para dividir: ").strip()
    arq = Path(arq_str).expanduser().resolve()
    if not arq.is_file() or arq.suffix != ".md":
        print("❌ Arquivo inválido.")
        return

    prefixo = input("🔖 Prefixo para novos arquivos: ").strip()
    print("Escreva o frontmatter template para as novas notas (linha vazia para terminar):")
    linhas_fm = []
    while True:
        linha = input()
        if linha == "":
            break
        linhas_fm.append(linha)
    template_fm = "\n".join(linhas_fm)

    conteudo = arq.read_text(encoding="utf-8")
    nome_base = arq.stem
    destino = arq.parent
    secoes = _extrair_secoes(conteudo)

    if not secoes:
        print("❌ Nenhuma seção ## encontrada.")
        return

    novo_conteudo = conteudo
    count = 0
    for secao in secoes:
        titulo = secao.splitlines()[0].replace("##", "").strip()
        nome_fmt = _sanitizar_nome(titulo)
        nome_arq = f"{prefixo}{nome_fmt}.md"
        novo_arq = destino / nome_arq
        novo_arq.write_text(
            f"{template_fm}\n\n{secao.strip()}\n\n← Parte de [[{nome_base}]]",
            encoding="utf-8",
        )
        print(f"  ✅ {nome_arq}")
        novo_conteudo = novo_conteudo.replace(secao.strip(), f"## [[{prefixo}{nome_fmt}]]")
        count += 1

    arq.write_text(novo_conteudo, encoding="utf-8")
    print(f"\n✅ {count} nota(s) criada(s). Original atualizado.")


# ══════════════════════════════════════════════════════════════════════════
#  6 — TRADUTOR DE VAULT (OpenAI)
# ══════════════════════════════════════════════════════════════════════════

def modo_tradutor():
    try:
        from openai import OpenAI
        from dotenv import load_dotenv
        load_dotenv()
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    except ImportError:
        print("❌ openai/dotenv não instalados.")
        return

    source_lang = input("🌐 Idioma de origem [en]: ").strip() or "en"
    target_lang = input("🌐 Idioma de destino [pt]: ").strip() or "pt"
    base_str = input("📂 Pasta base a traduzir: ").strip()
    base = Path(base_str).expanduser().resolve()
    if not base.exists():
        print("❌ Pasta não encontrada.")
        return

    saida_str = input(f"📂 Pasta de saída [{CALL_DIR / 'translated'}]: ").strip()
    saida = Path(saida_str).expanduser().resolve() if saida_str else CALL_DIR / "translated"
    saida.mkdir(parents=True, exist_ok=True)

    modelo = input("🤖 Modelo OpenAI [gpt-4o-mini]: ").strip() or "gpt-4o-mini"
    chunk_size = 8000

    def traduzir(texto: str) -> str:
        prompt = f"Traduza de {source_lang} para {target_lang}, mantendo Markdown:\n\n{texto}"
        resp = client.responses.create(model=modelo, input=prompt)
        return resp.output_text.strip()

    for arq in base.rglob("*.md"):
        rel = arq.relative_to(base)
        destino = saida / rel
        destino.parent.mkdir(parents=True, exist_ok=True)
        content = arq.read_text(encoding="utf-8")
        print(f"🔄 {rel}")
        chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]
        traduzido = "\n".join(traduzir(c) for c in chunks)
        destino.write_text(traduzido, encoding="utf-8")
        print(f"  ✅ {destino.name}")

    print(f"\n✅ Tradução concluída em: {saida}")


# ══════════════════════════════════════════════════════════════════════════
#  7 — GERENCIADOR DE TEMPLATE FOLDER (Templater)
# ══════════════════════════════════════════════════════════════════════════

def modo_template_folder():
    json_str = input("📄 Caminho do data.json do Templater: ").strip()
    json_path = Path(json_str).expanduser().resolve()
    if not json_path.exists():
        print("❌ Arquivo não encontrado.")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"\n  Valor atual: '{data.get('templates_folder', '')}'")
    print("Informe os valores possíveis (linha vazia para terminar):")
    valores = []
    while True:
        v = input("  Valor: ").strip()
        if not v:
            break
        valores.append(v)

    if not valores:
        print("❌ Nenhum valor informado.")
        return

    atual = data.get("templates_folder", "")
    if atual in valores:
        prox = valores[(valores.index(atual) + 1) % len(valores)]
    else:
        prox = valores[0]

    data["templates_folder"] = prox
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"✅ Template folder → '{prox}'")


# ══════════════════════════════════════════════════════════════════════════
#  MENU PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════

def main():
    print("\n╭──────────────────────────────────────╮")
    print("│  Obsidian Vault Tools                │")
    print("╰──────────────────────────────────────╯")
    print("\n1. Buscar por termo")
    print("2. Buscar notas similares (TF-IDF)")
    print("3. Substituição global")
    print("4. Reset de frontmatter por pasta")
    print("5. Gerador Zettelkasten")
    print("6. Tradutor de vault (OpenAI)")
    print("7. Gerenciar template folder (Templater)")

    modo = input("\nFerramenta: ").strip()

    if modo in ("1", "2", "3"):
        vault_str = input("🏛  Vault: ").strip()
        vault = Path(vault_str).expanduser().resolve()
        if not vault.exists():
            print("❌ Vault não encontrado.")
            return
        if modo == "1":
            modo_busca_termo(vault)
        elif modo == "2":
            modo_busca_similar(vault)
        elif modo == "3":
            modo_substituicao_global(vault)
    elif modo == "4":
        modo_reset_frontmatter()
    elif modo == "5":
        modo_zettelkasten()
    elif modo == "6":
        modo_tradutor()
    elif modo == "7":
        modo_template_folder()
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()
