#!/usr/bin/env python3
import subprocess
import os
import sys
from datetime import datetime

from config import REPO_PATH

def run(cmd):
    subprocess.run(cmd, check=True)

def has_changes():
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        stdout=subprocess.PIPE,
        text=True
    )
    return bool(result.stdout.strip())

def main():
    os.environ["SSH_AUTH_SOCK"] = f"/run/user/{os.getuid()}/ssh-agent.socket"

    if not os.path.isdir(REPO_PATH):
        print("❌ Vault não encontrada")
        sys.exit(1)

    os.chdir(REPO_PATH)

    if not has_changes():
        print("ℹ️ Nenhuma alteração local para enviar")
        sys.exit(0)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    commit_msg = f"obsidian sync: {timestamp}"

    try:
        run(["git", "add", "."])
        run(["git", "commit", "-m", commit_msg])
        run(["git", "push"])
        print("🚀 Vault enviada com sucesso (push on close)")
    except subprocess.CalledProcessError:
        print("⚠️ Push falhou — execute pull antes de tentar novamente")
        sys.exit(1)

if __name__ == "__main__":
    main()
