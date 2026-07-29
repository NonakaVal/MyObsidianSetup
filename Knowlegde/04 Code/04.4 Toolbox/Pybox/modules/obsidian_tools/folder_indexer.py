#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
index_notes/folder_indexer.py
Gera arquivos de índice Markdown (_folder_index_<pasta>.md) para qualquer pasta
de um vault Obsidian. Substitui todos os *_index.py individuais do projeto.
Suporta geração de sumário geral do vault com análise de frontmatter e hubs.
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

# ── Ambiente PyBox ────────────────────────────────────────────────────────
CALL_DIR = Path(os.environ.get("PYBOX_CALL_DIR", Path.cwd()))

EXTENSOES_NOTAS = {".md", ".base", ".canvas"}
TEMPLATE_KEYWORDS = {"Templates", "Template", "Ideaverse-Templates"}
ICONES_PASTA = {1: "📁", 2: "📂", 3: "📘", 4: "📙", 5: "📗", 6: "📄"}
ICONES_NOTA = {".base": "🔷", ".canvas": "🎨"}

FRONTMATTER_RE = re.compile(r"\{\{.*?\}\}")


# ── Helpers ───────────────────────────────────────────────────────────────

def is_template(path: str) -> bool:
    return any(kw in path for kw in TEMPLATE_KEYWORDS)


def sanitize_frontmatter(yaml_text: str) -> str:
    return FRONTMATTER_RE.sub("PLACEHOLDER", yaml_text)


def parse_frontmatter(content: str) -> dict:
    if not HAS_YAML or not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    try:
        return yaml.safe_load(sanitize_frontmatter(content[3:end].strip())) or {}
    except Exception:
        return {}


def formatar_numero(n) -> str:
    if isinstance(n, int):
        return f"{n:,}".replace(",", ".")
    return f"{n:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".")


# ── Listagem de notas ─────────────────────────────────────────────────────

def listar_notas(pasta_raiz: Path) -> dict[str, list[str]]:
    resultado: dict[str, list[str]] = {}
    for raiz, _, arquivos in os.walk(pasta_raiz):
        if is_template(raiz):
            continue
        rel = os.path.relpath(raiz, pasta_raiz)
        if rel == ".":
            rel = "Raiz"
        notas = []
        for arq in arquivos:
            nome, ext = os.path.splitext(arq)
            if ext.lower() in EXTENSOES_NOTAS and not arq.startswith("_"):
                notas.append(nome if ext.lower() == ".md" else f"{nome}{ext}")
        if notas:
            resultado[rel] = sorted(notas)
    return resultado


# ── Escrita do índice ─────────────────────────────────────────────────────

def escrever_indice(notas: dict[str, list[str]], saida: Path):
    with open(saida, "w", encoding="utf-8") as f:
        f.write("---\ncssclasses:\n  - dash\n  - dashboard\ntags:\n  - index\n---\n\n")
        f.write(f"*Atualizado em {datetime.now().strftime('%Y/%m/%d %H:%M')}*\n\n")

        pastas_escritas: set = set()

        for caminho_completo, lista_notas in sorted(notas.items()):
            partes = [""] if caminho_completo == "Raiz" else caminho_completo.split(os.sep)
            acumulado: list = []

            for i, parte in enumerate(partes):
                if parte:
                    acumulado.append(parte)
                    chave = os.sep.join(acumulado)
                    if chave not in pastas_escritas:
                        nivel = min(i + 1, 6)
                        icone = ICONES_PASTA.get(nivel, "📦")
                        f.write(f"{'#' * nivel} {icone} {parte}\n\n")
                        pastas_escritas.add(chave)

            for nota in lista_notas:
                ext = Path(nota).suffix.lower()
                icone = ICONES_NOTA.get(ext, "📄")
                f.write(f"- {icone} [[{nota}]]\n")
            f.write("\n")


# ── Sumário completo do vault ─────────────────────────────────────────────

def analisar_frontmatter(vault: Path) -> dict:
    prop_presence: Counter = Counter()
    total = 0
    for raiz, _, arqs in os.walk(vault):
        if is_template(raiz):
            continue
        for arq in arqs:
            if not arq.endswith(".md") or arq.startswith("_"):
                continue
            total += 1
            content = (Path(raiz) / arq).read_text(encoding="utf-8", errors="ignore")
            data = parse_frontmatter(content)
            for prop in data:
                prop_presence[prop] += 1
    return {"presence": prop_presence, "total": total}


def contar_hubs(vault: Path, campo: str = "HUB") -> Counter:
    contador: Counter = Counter()
    for raiz, _, arqs in os.walk(vault):
        if is_template(raiz):
            continue
        for arq in arqs:
            if not arq.endswith(".md") or arq.startswith("_"):
                continue
            content = (Path(raiz) / arq).read_text(encoding="utf-8", errors="ignore")
            data = parse_frontmatter(content)
            hub = data.get(campo, [])
            if isinstance(hub, list):
                contador.update(hub)
            elif isinstance(hub, str):
                contador[hub] += 1
    return contador


def gerar_sumario_vault(vault: Path, saida: Path, campo_hub: str = "HUB"):
    notas = listar_notas(vault)
    fm_data = analisar_frontmatter(vault)
    hubs = contar_hubs(vault, campo_hub)

    with open(saida, "w", encoding="utf-8") as f:
        f.write(f"*Atualizado em {datetime.now().strftime('%Y/%m/%d %H:%M')}*\n\n")

        total_notas = sum(len(n) for n in notas.values())
        f.write("## 🗒️ Informações Gerais\n\n")
        f.write(f"- **Total de Notas:** {formatar_numero(total_notas)}\n")
        f.write(f"- **Pastas:** {formatar_numero(len(notas))}\n")
        if notas:
            maior = max(notas.items(), key=lambda x: len(x[1]))
            f.write(f"- **Pasta com mais notas:** `{maior[0]}` ({formatar_numero(len(maior[1]))} notas)\n")

        f.write("\n---\n\n## 🏷️ Hubs Mais Utilizados\n\n")
        if hubs:
            f.write("| Hub | Contagem |\n|------|----------|\n")
            for hub, qtd in hubs.most_common(100):
                f.write(f"| `{hub}` | {qtd} |\n")
        else:
            f.write("Nenhum hub encontrado.\n")

        f.write("\n---\n\n## 🔍 Propriedades no Frontmatter\n\n")
        if fm_data["presence"]:
            f.write("| Propriedade | Arquivos | Cobertura |\n|--------------|----------|-----------|\n")
            for prop, count in fm_data["presence"].most_common(10):
                cov = (count / fm_data["total"]) * 100 if fm_data["total"] else 0
                f.write(f"| `{prop}` | {count} | {cov:.1f}% |\n")
        else:
            f.write("Nenhuma propriedade encontrada.\n")

        f.write("\n---\n\n# 🗂️ Pastas e Notas\n\n")
        pastas_escritas: set = set()
        for caminho, lista in sorted(notas.items()):
            partes = caminho.split(os.sep)
            acumulado: list = []
            for i, parte in enumerate(partes):
                acumulado.append(parte)
                chave = os.sep.join(acumulado)
                if chave not in pastas_escritas:
                    nivel = min(i + 1, 6)
                    icone = ICONES_PASTA.get(nivel, "📦")
                    f.write(f"{'#' * nivel} {icone} {parte}\n\n")
                    pastas_escritas.add(chave)
            for nota in lista:
                f.write(f"- 📄 [{nota}]\n")
        f.write("\n---\n")

    print(f"✅ Sumário do vault gerado: {saida}")


# ── Entrypoint ────────────────────────────────────────────────────────────

def main():
    print("\n╭──────────────────────────────────────╮")
    print("│  Folder Indexer (Obsidian)           │")
    print("╰──────────────────────────────────────╯")
    print("\n1. Gerar índice de uma pasta")
    print("2. Gerar sumário completo do vault")

    modo = input("\nModo [1]: ").strip() or "1"

    if modo == "1":
        pasta_str = input("📂 Pasta a indexar: ").strip()
        pasta = Path(pasta_str).expanduser().resolve()
        if not pasta.exists():
            print("❌ Pasta não encontrada.")
            return

        nome_pasta = pasta.name
        saida_str = input(f"💾 Arquivo de saída [{pasta / f'_folder_index_{nome_pasta}.md'}]: ").strip()
        if saida_str:
            saida = Path(saida_str).expanduser().resolve()
        else:
            saida = pasta / f"_folder_index_{nome_pasta}.md"

        notas = listar_notas(pasta)
        escrever_indice(notas, saida)

        total = sum(len(n) for n in notas.values())
        print(f"✅ Índice gerado: {saida}")
        print(f"📊 {len(notas)} pasta(s), {total} nota(s)")

    elif modo == "2":
        vault_str = input("🏛  Caminho do vault: ").strip()
        vault = Path(vault_str).expanduser().resolve()
        if not vault.exists():
            print("❌ Vault não encontrado.")
            return

        campo_hub = input("🏷  Campo HUB no frontmatter [HUB]: ").strip() or "HUB"
        saida_str = input(f"💾 Arquivo de saída [_index_notas.md]: ").strip() or "_index_notas.md"

        # Saída dentro do vault (comportamento original) ou no CALL_DIR
        usar_vault = input("Salvar dentro do vault? (s/N): ").strip().lower()
        if usar_vault == "s":
            saida = vault / saida_str
        else:
            saida = CALL_DIR / saida_str

        gerar_sumario_vault(vault, saida, campo_hub)
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()
