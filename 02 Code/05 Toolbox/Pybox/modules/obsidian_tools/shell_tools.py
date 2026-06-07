#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
shell/shell_tools.py
Ferramentas de shell e sistema:
 - Git commit assistant (GCA)
 - Git sync (pull/push automático)
 - Servidor local Flask para navegação de arquivos
 - Alternador de foco CSS (Obsidian snippets)
 - Toggle de snippet CSS (show/hide folders)
"""

import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# ── Ambiente PyBox ────────────────────────────────────────────────────────
CALL_DIR = Path(os.environ.get("PYBOX_CALL_DIR", Path.cwd()))


# ══════════════════════════════════════════════════════════════════════════
#  1 — GIT COMMIT ASSISTANT
# ══════════════════════════════════════════════════════════════════════════

COMMIT_OPTIONS = {
    "feat":     ["add new feature", "implement module", "create component", "integrate API"],
    "fix":      ["fix bug", "resolve performance issue", "adjust validation", "repair critical error"],
    "docs":     ["update documentation", "add examples", "fix typo", "improve explanation", "update readme"],
    "refactor": ["improve code structure", "optimize function", "remove duplicate code", "simplify logic"],
    "chore":    ["update dependencies", "configure environment", "adjust settings", "clean up old code"],
}


def run_cmd(cmd: list) -> bool:
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {e}")
        return False


def gca_commit_flow():
    if not Path(".git").exists():
        print("❌ Não é um repositório git.")
        return

    print("\n1. Commit guiado\n2. Mensagem personalizada\nq. Cancelar")
    ch = input("Opção: ").strip().lower()

    if ch == "1":
        tipos = list(COMMIT_OPTIONS.keys())
        print("\nTipo de commit:")
        for i, t in enumerate(tipos, 1):
            print(f"  {i}. {t}")
        try:
            tipo_idx = int(input("Tipo: ").strip()) - 1
            tipo = tipos[tipo_idx]
        except (ValueError, IndexError):
            tipo = "chore"

        opcoes = COMMIT_OPTIONS[tipo]
        print(f"\nOpções para '{tipo}':")
        for i, o in enumerate(opcoes, 1):
            print(f"  {i}. {o}")
        try:
            msg_idx = int(input("Mensagem: ").strip()) - 1
            msg_parte = opcoes[msg_idx]
        except (ValueError, IndexError):
            msg_parte = opcoes[-1]

    elif ch == "2":
        msg_custom = input("Mensagem: ").strip()
        tipo = "chore"
        for t in COMMIT_OPTIONS:
            if msg_custom.lower().startswith(t + ":"):
                tipo = t
                msg_custom = msg_custom[len(t) + 1:].strip()
                break
        msg_parte = msg_custom
    else:
        return

    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    commit_msg = f"{tipo}: {msg_parte} ({ts})"
    print(f"\n🔸 {commit_msg}")

    if input("Confirmar commit? (y/n): ").lower().strip() != "y":
        print("Cancelado.")
        return

    if run_cmd(["git", "add", "."]) and run_cmd(["git", "commit", "-m", commit_msg]):
        print("✅ Commit feito!")
        if input("Push? (y/n): ").lower().strip() == "y":
            if run_cmd(["git", "push"]):
                print("🚀 Push concluído!")


# ══════════════════════════════════════════════════════════════════════════
#  2 — GIT SYNC (pull/push)
# ══════════════════════════════════════════════════════════════════════════

def _configurar_ssh():
    uid = os.getuid()
    os.environ["SSH_AUTH_SOCK"] = f"/run/user/{uid}/ssh-agent.socket"


def git_pull(repo_path: Path):
    if not repo_path.is_dir():
        print(f"❌ Pasta não encontrada: {repo_path}")
        return
    os.chdir(repo_path)
    if not (repo_path / ".git").exists():
        print("❌ Não é um repositório git.")
        return
    _configurar_ssh()
    try:
        subprocess.run(["git", "pull", "--rebase", "--autostash"], check=True)
        print("⬇️  Pull concluído.")
    except subprocess.CalledProcessError:
        print("⚠️  Pull falhou. Verifique conflitos.")


def git_push(repo_path: Path):
    if not repo_path.is_dir():
        print(f"❌ Pasta não encontrada: {repo_path}")
        return
    os.chdir(repo_path)
    if not (repo_path / ".git").exists():
        print("❌ Não é um repositório git.")
        return
    _configurar_ssh()

    result = subprocess.run(["git", "status", "--porcelain"], stdout=subprocess.PIPE, text=True)
    if not result.stdout.strip():
        print("ℹ️  Sem alterações para enviar.")
        return

    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    msg = f"obsidian sync: {ts}"
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", msg], check=True)
        subprocess.run(["git", "push"], check=True)
        print("🚀 Push concluído.")
    except subprocess.CalledProcessError:
        print("⚠️  Push falhou.")


def modo_git_sync():
    repo_str = input("📂 Caminho do repositório git: ").strip()
    repo = Path(repo_str).expanduser().resolve()

    print("\n1. Pull\n2. Push\n3. Pull + Push")
    op = input("Operação: ").strip()

    if op == "1":
        git_pull(repo)
    elif op == "2":
        git_push(repo)
    elif op == "3":
        git_pull(repo)
        git_push(repo)
    else:
        print("Opção inválida.")


# ══════════════════════════════════════════════════════════════════════════
#  3 — LOCAL FILE SERVER (Flask)
# ══════════════════════════════════════════════════════════════════════════

def modo_local_server():
    try:
        from flask import Flask
    except ImportError:
        print("❌ Flask não instalado. Execute: pip install flask --break-system-packages")
        return

    print("\n⚙️  O servidor local é iniciado como processo separado.")
    port = input("🔌 Porta [5000]: ").strip() or "5000"

    # Localiza o script do servidor dentro do módulo shell
    server_script = Path(__file__).parent / "_localserver_app.py"
    if not server_script.exists():
        print("❌ Script do servidor não encontrado.")
        print("   Certifique-se que _localserver_app.py está em modules/shell/")
        return

    env = os.environ.copy()
    env["HOMELAB_PORT"] = port
    subprocess.Popen(
        [sys.executable, str(server_script)],
        env=env,
    )
    import time
    time.sleep(0.5)
    print(f"🟢 Servidor rodando em http://0.0.0.0:{port}")
    print("   (Pressione Ctrl+C para encerrar o servidor separadamente)")


# ══════════════════════════════════════════════════════════════════════════
#  4 — CSS FOCUS CYCLE (Obsidian)
# ══════════════════════════════════════════════════════════════════════════

MODES = ["ALL", "G1", "G2", "G3", "ZALL"]
LABELS = {"ALL": "●●●●", "G1": "●○○○", "G2": "○●○○", "G3": "○○●○", "ZALL": "○○○○"}

DEFAULT_HIDE: dict[str, list] = {
    "ALL": [],
    "G1":  ["Calendar & Review", "Index & Bases", "Knowlegde", "Memos",
            "V-01-Ideia", "V-02-Inspiracoes", "V-03-Roteiro", "V-04-Edicao", "V-05-Review", "Write"],
    "G2":  ["00 Code", "01 Snippets", "03 Config", "04 Workflow", "05 Toolbox",
            "06 Work", "07 AI", "08 Focus Areas", "TaskNotes",
            "V-01-Ideia", "V-02-Inspiracoes", "V-03-Roteiro", "V-04-Edicao", "V-05-Review", "Write"],
    "G3":  ["00 Code", "01 Snippets", "03 Config", "04 Workflow", "05 Toolbox",
            "06 Work", "07 AI", "08 Focus Areas", "Calendar & Review",
            "Index & Bases", "Knowlegde", "Memos"],
    "ZALL": [],
}


def _make_hide_block(mode: str, hide_map: dict) -> str:
    paths = hide_map.get(mode, [])
    if not paths:
        return f"/* FOCUS-HIDE: {mode} *//* FOCUS-HIDE-END */"
    sel = ",\n".join(f'div[data-path="{p}"]' for p in paths)
    return f"/* FOCUS-HIDE: {mode} */\n{sel} {{ display: none !important; }}\n/* FOCUS-HIDE-END */"


def _make_zall_block(mode: str) -> str:
    if mode == "ZALL":
        return '/* FOCUS-ZALL-START */\ndiv[data-path^="z-"] { display: flex !important; }\n/* FOCUS-ZALL-END */'
    return "/* FOCUS-ZALL-START *//* FOCUS-ZALL-END */"


def modo_css_focus():
    css_str = input("📄 Caminho do arquivo ux-focus.css: ").strip()
    css_path = Path(css_str).expanduser().resolve()
    if not css_path.exists():
        print("❌ Arquivo não encontrado.")
        return

    content = css_path.read_text(encoding="utf-8")
    m = re.search(r"/\* FOCUS-MODE: (\w+) \*/", content)
    current = m.group(1) if (m and m.group(1) in MODES) else "ALL"
    next_mode = MODES[(MODES.index(current) + 1) % len(MODES)]

    content = re.sub(r"/\* FOCUS-MODE: \w+ \*/", f"/* FOCUS-MODE: {next_mode} */", content)
    content = re.sub(
        r"/\* FOCUS-HIDE:.*?FOCUS-HIDE-END \*/",
        _make_hide_block(next_mode, DEFAULT_HIDE),
        content, flags=re.DOTALL,
    )
    content = re.sub(
        r"/\* FOCUS-ZALL-START \*/.*?/\* FOCUS-ZALL-END \*/",
        _make_zall_block(next_mode),
        content, flags=re.DOTALL,
    )
    css_path.write_text(content, encoding="utf-8")
    print(f"✅ Modo: {next_mode} {LABELS[next_mode]}")


# ══════════════════════════════════════════════════════════════════════════
#  5 — TOGGLE CSS SNIPPET (show/hide)
# ══════════════════════════════════════════════════════════════════════════

def modo_toggle_css():
    css_str = input("📄 Caminho do snippet CSS: ").strip()
    css_path = Path(css_str).expanduser().resolve()
    if not css_path.exists():
        print("❌ Arquivo não encontrado.")
        return

    lines = css_path.read_text(encoding="utf-8").splitlines(keepends=True)
    if not lines:
        print("❌ Arquivo vazio.")
        return

    primeira = lines[0].rstrip()
    if primeira.endswith("*/"):
        lines[0] = primeira[:-2].rstrip() + "\n"
        status = "DESATIVADO ❌"
    else:
        lines[0] = primeira + " */\n"
        status = "ATIVADO ✅"

    css_path.write_text("".join(lines), encoding="utf-8")
    print(f"✅ {css_path.name} — {status}")


# ══════════════════════════════════════════════════════════════════════════
#  MENU PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════

def main():
    print("\n╭──────────────────────────────────────╮")
    print("│  Shell Tools                         │")
    print("╰──────────────────────────────────────╯")
    print("\n1. Git Commit Assistant")
    print("2. Git Sync (pull/push)")
    print("3. Servidor local de arquivos (Flask)")
    print("4. Ciclo de foco CSS (Obsidian)")
    print("5. Toggle snippet CSS (on/off)")

    op = input("\nFerramenta: ").strip()

    if op == "1":
        gca_commit_flow()
    elif op == "2":
        modo_git_sync()
    elif op == "3":
        modo_local_server()
    elif op == "4":
        modo_css_focus()
    elif op == "5":
        modo_toggle_css()
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()
