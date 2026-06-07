#!/usr/bin/env python3

import os
import sys
import subprocess
from pathlib import Path

from config import PYBOX_ROOT, MODULES_DIR, MODULES


def clear():
    os.system("clear")


def header(title):
    print()
    print("╭" + "─" * 60 + "╮")
    print(f"│ {title:<58} │")
    print("╰" + "─" * 60 + "╯")
    print()


def pause():
    input("\nENTER para continuar...")


def get_scripts(module_path: Path):
    if not module_path.exists():
        return []

    return sorted([
        p for p in module_path.rglob("*.py")
        if p.is_file() and not p.name.startswith("__")
    ])


def run_script(script: Path):
    env = os.environ.copy()
    env["PYBOX_ROOT"] = str(PYBOX_ROOT)
    env["PYBOX_MODULES"] = str(MODULES_DIR)
    env["PYBOX_SCRIPT"] = str(script)
    env["PYBOX_CALL_DIR"] = str(Path.cwd())

    clear()
    header(f"Rodando: {script.name}")

    print(f"📦 Script: {script}")
    print(f"📂 Local atual: {Path.cwd()}")
    print()

    subprocess.run(
        [sys.executable, str(script)],
        cwd=str(Path.cwd()),
        env=env,
        check=False,
    )

    pause()


def select_module():
    modules = list(MODULES.items())

    while True:
        clear()
        header("PyBox — Selecionar módulo")

        for i, (key, data) in enumerate(modules, start=1):
            print(f"{i:01d}. {data['label']}")

        print("\nq. sair")

        choice = input("\nEscolha o módulo: ").strip().lower()

        if choice == "q":
            sys.exit(0)

        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(modules):
                return modules[idx]

        print("Opção inválida.")
        pause()


def select_script(module_key, module_data):
    module_path = module_data["path"]
    scripts = get_scripts(module_path)

    while True:
        clear()
        header(f"PyBox — {module_data['label']}")

        if not scripts:
            print(f"Nenhum script Python encontrado em:\n{module_path}")
            pause()
            return

        for i, script in enumerate(scripts, start=1):
            rel = script.relative_to(module_path)
            print(f"{i:01d}. {rel}")

        print("\nb. voltar")
        print("q. sair")

        choice = input("\nEscolha o script: ").strip().lower()

        if choice == "b":
            return

        if choice == "q":
            sys.exit(0)

        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(scripts):
                run_script(scripts[idx])
                return

        print("Opção inválida.")
        pause()


def main():
    while True:
        module_key, module_data = select_module()
        select_script(module_key, module_data)


if __name__ == "__main__":
    main()