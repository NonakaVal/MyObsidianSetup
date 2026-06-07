#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
file_tools/media_indexer.py
Varre uma pasta e gera um índice Markdown de mídias (imagens, vídeos, áudios).
Útil para pastas do Instagram, downloads, etc.
Saída no diretório onde o comando foi chamado.
"""

import os
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# ── Ambiente PyBox ────────────────────────────────────────────────────────
CALL_DIR = Path(os.environ.get("PYBOX_CALL_DIR", Path.cwd()))

# ── Categorias ────────────────────────────────────────────────────────────
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".heic", ".tiff", ".svg"}
VIDEO_EXT = {".mov", ".mkv", ".webm", ".avi", ".flv", ".m4v"}
AUDIO_EXT = {".mp4", ".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac"}

PASTAS_IGNORAR = {".obsidian", ".git", "__pycache__", ".vscode"}

REGEX_PASTAS = [
    (r"your_instagram_activity/messages/inbox/([^_]+)_.*", r"\1"),
    (r"your_instagram_activity/messages/inbox/(.+)", r"\1"),
    (r"your_instagram_activity/(.+)", r"\1"),
    (r"([^/]+)/.*", r"\1"),
]


# ── Helpers ───────────────────────────────────────────────────────────────

def deve_ignorar(nome: str) -> bool:
    return any(p in nome for p in PASTAS_IGNORAR)


def limpar_nome_pasta(nome: str) -> str:
    if not nome:
        return "📁 Raiz"
    for pattern, replacement in REGEX_PASTAS:
        try:
            novo = re.sub(pattern, replacement, nome)
            if novo != nome:
                return novo
        except Exception:
            continue
    return nome.split("/")[-1] if "/" in nome else nome


def categorizar(fname: str) -> str:
    ext = Path(fname).suffix.lower()
    if ext in IMAGE_EXT:
        return "🖼️ Imagens"
    if ext in VIDEO_EXT:
        return "🎬 Vídeos"
    if ext in AUDIO_EXT:
        return "🔊 Áudios"
    return "📄 Outros"


def link_obsidian(caminho_relativo: str, nome: str) -> str:
    ext = Path(nome).suffix.lower()
    if ext in IMAGE_EXT | VIDEO_EXT | AUDIO_EXT:
        return f"![[{caminho_relativo}]]"
    return f"[[{caminho_relativo}]]"


# ── Varredura ─────────────────────────────────────────────────────────────

def scan(root: Path) -> dict:
    root = root.resolve()
    conteudo: dict = defaultdict(lambda: defaultdict(list))

    for dirpath, _, filenames in os.walk(root):
        if deve_ignorar(dirpath):
            continue
        rel_dir = os.path.relpath(dirpath, root)
        if rel_dir == ".":
            rel_dir = ""
        pasta_limpa = limpar_nome_pasta(rel_dir)

        for fname in filenames:
            fp = Path(dirpath) / fname
            if not fp.exists():
                continue
            categoria = categorizar(fname)
            rel_path = os.path.relpath(fp, root).replace(os.sep, "/")
            conteudo[pasta_limpa][categoria].append({"nome": fname, "caminho_relativo": rel_path})

    return dict(conteudo)


# ── Geração do Markdown ───────────────────────────────────────────────────

def gerar_markdown(conteudo: dict, output_path: Path, titulo: str = "Lista de Mídias"):
    ordem = ["🖼️ Imagens", "🎬 Vídeos", "🔊 Áudios", "📄 Outros"]

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# 📸 {titulo}\n\n")
        f.write(f"*Atualizado em {datetime.now().strftime('%d/%m/%Y')}*\n\n")

        f.write("## 📂 Pastas Encontradas\n\n")
        for pasta in sorted(conteudo.keys()):
            emoji = "🏠" if pasta in ("📁 Raiz", "") else "📁"
            f.write(f"- {emoji} **{pasta}**\n")
        f.write("\n---\n\n")

        for pasta in sorted(conteudo.keys()):
            conteudo_pasta = conteudo[pasta]
            if not any(conteudo_pasta.values()):
                continue

            f.write(f"## 📁 {pasta}\n\n")

            for categoria in ordem:
                itens = conteudo_pasta.get(categoria, [])
                if not itens:
                    continue
                f.write(f"### {categoria} ({len(itens)})\n\n")

                if categoria == "🖼️ Imagens":
                    f.write("<div style='display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:15px;margin:20px 0;'>\n")
                    for item in sorted(itens, key=lambda x: x["nome"]):
                        lnk = link_obsidian(item["caminho_relativo"], item["nome"])
                        f.write(f"<div style='text-align:center;'>{lnk}<br><small>{item['nome'][:20]}...</small></div>\n")
                    f.write("</div>\n\n")
                else:
                    for item in sorted(itens, key=lambda x: x["nome"]):
                        lnk = link_obsidian(item["caminho_relativo"], item["nome"])
                        if categoria in ("🎬 Vídeos", "🔊 Áudios"):
                            f.write(f"{lnk}\n**Arquivo:** {item['nome']}\n\n")
                        else:
                            f.write(f"- {lnk}\n")
                f.write("\n")
            f.write("---\n\n")

        # Resumo
        total_pastas = len(conteudo)
        total_arqs = sum(len(itens) for cat in conteudo.values() for itens in cat.values())
        f.write("## 📊 Resumo\n\n")
        f.write(f"- **Pastas:** {total_pastas}\n")
        f.write(f"- **Arquivos:** {total_arqs}\n")
        f.write(f"- **Data:** {datetime.now().strftime('%d/%m/%Y')}\n")

    print(f"✅ Índice gerado: {output_path}")


# ── Entrypoint ────────────────────────────────────────────────────────────

def main():
    print("\n╭──────────────────────────────────────╮")
    print("│  Media Indexer                       │")
    print("╰──────────────────────────────────────╯\n")

    pasta_str = input("📂 Pasta a varrer: ").strip()
    root = Path(pasta_str).expanduser().resolve()
    if not root.exists():
        print("❌ Pasta não encontrada.")
        return

    titulo = input("📝 Título do índice [Lista de Mídias]: ").strip() or "Lista de Mídias"
    saida_nome = input(f"💾 Nome do arquivo de saída [media_index.md]: ").strip() or "media_index.md"
    output_path = CALL_DIR / saida_nome

    print(f"\n🔍 Varrendo: {root}")
    conteudo = scan(root)

    total_arqs = sum(len(itens) for cat in conteudo.values() for itens in cat.values())
    print(f"📊 {len(conteudo)} pasta(s), {total_arqs} arquivo(s) encontrado(s).")

    gerar_markdown(conteudo, output_path, titulo)
    print(f"📂 Salvo em: {output_path}")


if __name__ == "__main__":
    main()
