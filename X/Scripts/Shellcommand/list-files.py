# -*- coding: utf-8 -*-
import os
import sys
from config import VAULT_PATH

PASTA_ARQUIVOS = os.path.join(
    VAULT_PATH,
    r"Projects & Areas/Areas/NonakaLab Channel/Sticks/recortadas"
)

EXTS_IMAGEM = [".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"]
EXT_MD = ".md"

if not os.path.exists(PASTA_ARQUIVOS):
    print(f"Erro: a pasta '{PASTA_ARQUIVOS}' não existe!")
    sys.exit(1)

links = []

for root, _, files in os.walk(PASTA_ARQUIVOS):
    for f in files:
        ext = os.path.splitext(f)[1].lower()

        # ---------- MARKDOWN ----------
        if ext == EXT_MD:
            nome_base = os.path.splitext(f)[0]  # remove .md
            links.append(nome_base)

        # ---------- IMAGENS ----------
        elif ext in EXTS_IMAGEM:
            caminho_completo = os.path.join(root, f)
            caminho_relativo = os.path.relpath(caminho_completo, VAULT_PATH)
            caminho_relativo = caminho_relativo.replace("\\", "/")
            links.append(caminho_relativo)

# Output Obsidian
for link in sorted(links):
    print(f"![[{link}]]")
