#!/usr/bin/env python3
import subprocess
import os
import sys
from config import REPO_PATH


def run(cmd):
    subprocess.run(cmd, check=True)

def main():
    os.environ["SSH_AUTH_SOCK"] = f"/run/user/{os.getuid()}/ssh-agent.socket"

    if not os.path.isdir(REPO_PATH):
        print("❌ Vault não encontrada")
        sys.exit(1)

    os.chdir(REPO_PATH)

    if not os.path.isdir(".git"):
        print("❌ Diretório não é um repositório git")
        sys.exit(1)

    try:
        run(["git", "pull", "--rebase", "--autostash"])
        print("⬇️ Vault atualizada com sucesso (pull on open)")
    except subprocess.CalledProcessError:
        print("⚠️ Pull falhou — pode haver conflito que exige revisão manual")
        sys.exit(1)

if __name__ == "__main__":
    main()
