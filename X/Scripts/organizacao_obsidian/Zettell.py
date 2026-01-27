#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZETTELIZER - Divisão de notas em seções
----------------------------------------
- Extrai seções de um arquivo Markdown (nível ##).
- Cria uma nota separada para cada seção.
- Insere um frontmatter customizável.
- Atualiza o arquivo original substituindo seções por links.
"""

import re
import sys
from pathlib import Path
from config import MAIN_PATH

# ==========================
# ⚙️ CONFIGURAÇÕES
# ==========================
RELATIVE_PATH = "+/cssSnippets/_OF_cssSnippets_.md"
PREFIXO = ""
TEMPLATE_FRONTMATTER = """---
tags: cssSnippetCollection
---"""

# Garantir UTF-8 no terminal (principalmente no Windows)
sys.stdout.reconfigure(encoding="utf-8")


# ==========================
# 🛠 FUNÇÕES UTILITÁRIAS
# ==========================
def sanitizar_nome_arquivo(nome: str) -> str:
    """Transforma título em nome válido de arquivo Markdown."""
    nome = re.sub(r'[\\/#%&{}<>*?$\'":@\[\]]', '', nome)  # remove especiais
    nome = nome.strip().lower().replace(' ', '-')        # troca espaço por hífen
    return re.sub(r'-+', '-', nome) or "untitled"


def extrair_secoes(conteudo: str) -> list[str]:
    """Retorna lista de blocos iniciados por ## até a próxima seção."""
    padrao = r"(## .+?)(?=\n## |\Z)"
    return re.findall(padrao, conteudo, flags=re.DOTALL)


def salvar_arquivo(destino: Path, conteudo: str):
    """Escreve conteúdo em arquivo garantindo que o diretório existe."""
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(conteudo, encoding="utf-8")
    print(f"✅ Criado: {destino.name}")


def atualizar_arquivo_original(caminho: Path, conteudo: str):
    """Substitui conteúdo no arquivo original pelo atualizado."""
    salvar_arquivo(caminho, conteudo)
    print(f"📝 Atualizado: {caminho.name}")


# ==========================
# 📄 PROCESSAMENTO
# ==========================
def processar_arquivo(caminho_arquivo: Path):
    """Lê, divide em seções, cria novas notas e atualiza arquivo original."""
    try:
        conteudo = caminho_arquivo.read_text(encoding="utf-8")
    except Exception as e:
        print(f"❌ Erro ao ler arquivo: {e}")
        return

    secoes = extrair_secoes(conteudo)
    novo_conteudo = conteudo
    nome_base = caminho_arquivo.stem
    pasta_destino = caminho_arquivo.parent

    for secao in secoes:
        titulo = secao.splitlines()[0].replace("##", "").strip()
        nome_formatado = sanitizar_nome_arquivo(titulo)
        nome_arquivo = f"{PREFIXO}{nome_formatado}.md"

        # Nova nota com frontmatter + seção + backlink
        secao_completa = (
            f"{TEMPLATE_FRONTMATTER}\n\n"
            f"{secao.strip()}\n\n"
            f"← Parte de [[{nome_base}]]"
        )

        salvar_arquivo(pasta_destino / nome_arquivo, secao_completa)

        # Substitui seção original por link
        novo_conteudo = novo_conteudo.replace(secao.strip(), f"- [[{PREFIXO}{nome_formatado}]]")

    atualizar_arquivo_original(caminho_arquivo, novo_conteudo)


def construir_caminho(relativo: str) -> Path:
    """Monta caminho absoluto a partir de MAIN_PATH + relativo (compatível com OS)."""
    return Path(MAIN_PATH) / Path(*relativo.split('/'))


# ==========================
# 🚀 EXECUÇÃO
# ==========================
def main():
    print("📁 Zettelizer - Criação de notas a partir de seções Markdown")
    print(f"📍 Caminho base: {MAIN_PATH}")

    caminho_completo = construir_caminho(RELATIVE_PATH)
    print(f"\n🔍 Caminho completo: {caminho_completo}")

    if caminho_completo.is_file() and caminho_completo.suffix == ".md":
        print("\nIniciando processamento...\n")
        processar_arquivo(caminho_completo)
    else:
        print("\n❌ Arquivo não encontrado ou inválido")
        print("Verifique:")
        print(f"1. Caminho base: {MAIN_PATH}")
        print(f"2. Arquivo: {caminho_completo}")
        print("3. Formato do input (ex: ATLAS/02_CONCEPT/arquivo.md)")


if __name__ == "__main__":
    main()
