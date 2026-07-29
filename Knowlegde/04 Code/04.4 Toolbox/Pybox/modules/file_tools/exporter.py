#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
file_tools/exporter.py
Exporta arquivos de texto/código de uma ou mais pastas para TXT consolidado.
Cada subpasta gera um arquivo .txt no diretório onde o comando foi chamado.
"""

import os
from pathlib import Path
from collections import defaultdict

CALL_DIR = Path(os.environ.get("PYBOX_CALL_DIR", Path.cwd()))

EXTENSOES_TEXTO = {
    ".md", ".txt", ".py", ".js", ".ts", ".json", ".yaml", ".yml",
    ".html", ".css", ".sh", ".bash", ".zsh",
    ".c", ".cpp", ".h", ".hpp",
    ".java", ".kt", ".rs", ".go", ".qml",
    ".php", ".rb", ".ini", ".toml", ".xml", ".rasi",
}

MAX_FILE_SIZE_MB = 2


def is_text_file(path: Path, extensoes: set) -> bool:
    if path.suffix.lower() not in extensoes:
        return False
    try:
        return path.stat().st_size / (1024 * 1024) <= MAX_FILE_SIZE_MB
    except Exception:
        return False


def read_safe(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        try:
            return path.read_text(encoding="latin-1")
        except Exception:
            return ""


def processar_frontmatter(texto: str) -> str:
    linhas = texto.splitlines()
    if linhas and linhas[0].strip() == "---":
        fm = []
        for i in range(1, len(linhas)):
            if linhas[i].strip() == "---":
                conteudo = "\n".join(linhas[i + 1:]).strip()
                resumo = " | ".join(
                    f"**{k.strip()}:** {v.strip().strip('[]')}"
                    for k, v in (l.split(":", 1) for l in fm if ":" in l)
                )
                return (resumo + "\n\n" + conteudo).strip()
            fm.append(linhas[i])
    return texto.strip()


def sanitizar_nome(nome: str) -> str:
    return nome.replace("/", "_").replace("\\", "_").replace(" ", "_").replace(":", "_")


def coletar_arquivos(pasta: Path, extensoes: set) -> list[Path]:
    return sorted(p for p in pasta.rglob("*") if p.is_file() and is_text_file(p, extensoes))


def exportar_pasta(pasta: Path, saida_dir: Path, extensoes: set, prefixo: str = "") -> tuple[int, int]:
    if not pasta.exists():
        print(f"⚠ Pasta não existe: {pasta}")
        return 0, 0

    arquivos = coletar_arquivos(pasta, extensoes)
    if not arquivos:
        print(f"⚠ Nenhum arquivo encontrado em: {pasta}")
        return 0, 0

    grupos = defaultdict(list)
    for arq in arquivos:
        grupos[arq.parent].append(arq)

    total_arqs = 0
    total_txts = 0
    base_prefix = sanitizar_nome(prefixo or pasta.name or "root")

    for pasta_atual, arqs in sorted(grupos.items()):
        relativa = pasta_atual.relative_to(pasta)
        nome_unico = str(relativa).replace("/", "_").replace("\\", "_")
        if not nome_unico or nome_unico == ".":
            nome_unico = "root"

        nome_arquivo = f"{base_prefix}__{nome_unico}.txt"
        arquivo_saida = saida_dir / nome_arquivo

        with open(arquivo_saida, "w", encoding="utf-8") as f:
            f.write(f"# 📂 {pasta}\n")
            f.write(f"## Subpasta: {relativa}\n\n")

            for i, arq in enumerate(sorted(arqs)):
                conteudo = read_safe(arq)
                if not conteudo.strip():
                    continue
                f.write(f"## 📝 {arq.name}\n\n")
                f.write(processar_frontmatter(conteudo))
                if i < len(arqs) - 1:
                    f.write("\n\n---\n\n")

        total_arqs += len(arqs)
        total_txts += 1
        print(f"📄 {arquivo_saida.name}")

    print(f"✅ {pasta.name}: {total_txts} arquivo(s) TXT, {total_arqs} script(s) processado(s)")
    return total_txts, total_arqs


def main():
    print("\n╭──────────────────────────────────────╮")
    print("│  File Exporter                       │")
    print("╰──────────────────────────────────────╯\n")

    print("Informe os caminhos de entrada (um por linha, linha vazia para finalizar):")
    pastas = []
    while True:
        p = input("📂 Pasta: ").strip()
        if not p:
            break
        caminho = Path(p).expanduser().resolve()
        if caminho.exists():
            pastas.append(caminho)
        else:
            print(f"  ⚠ Não encontrada: {caminho}")

    if not pastas:
        print("❌ Nenhuma pasta válida informada.")
        return

    print(f"\nExtensões disponíveis: {', '.join(sorted(EXTENSOES_TEXTO))}")
    ext_input = input("🔧 Extensões (separadas por vírgula, ENTER para todas): ").strip()

    if ext_input:
        extensoes = {e.strip() if e.strip().startswith(".") else f".{e.strip()}"
                     for e in ext_input.split(",")}
    else:
        extensoes = EXTENSOES_TEXTO

    print(f"\n📤 Saída em: {CALL_DIR}\n")

    total_t, total_a = 0, 0
    for pasta in pastas:
        t, a = exportar_pasta(pasta, CALL_DIR, extensoes)
        total_t += t
        total_a += a

    print(f"\n🎉 Total: {total_t} TXT(s) | {total_a} arquivo(s) processado(s)")
    print(f"📂 Salvos em: {CALL_DIR}")


if __name__ == "__main__":
    main()