---
created: "[[2025-07-09]]"
connections:
  - "[[! py Lazy Commits]]"
---
---

# 🚀 Rodar o script globalmente no Arch Linux / EndeavourOS com Git (SSH)

## 1️⃣ Salve o script e torne-o executável

```bash
nano ~/gca.py
```

### script gca.py
```python
#!/usr/bin/env python3
import subprocess
from datetime import datetime
import os
import sys

# Commit type and their detailed options
COMMIT_OPTIONS = {
    'feat': ['add new feature', 'implement module', 'create component', 'integrate API'],
    'fix': ['fix bug', 'resolve performance issue', 'adjust validation', 'repair critical error'],
    'docs': ['update documentation', 'add examples', 'fix typo', 'improve explanation'],
    'refactor': ['improve code structure', 'optimize function', 'remove duplicate code', 'simplify logic'],
    'chore': ['update dependencies', 'configure environment', 'adjust settings', 'clean up old code'],
}

def run_command(command: list[str], show_error=True) -> bool:
    """Executa um comando de terminal e retorna sucesso ou falha."""
    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        if show_error:
            print(f"\n❌ Error: {e}")
        return False

def select_option(prompt: str, options: list[str], allow_quit=False) -> int | None:
    """Mostra opções e retorna o índice escolhido pelo usuário."""
    print(f"\n{prompt}")
    for i, option in enumerate(options, 1):
        print(f"{i}: {option}")

    choice = input("\nEnter number" + (" (or 'q' to quit): " if allow_quit else ": ")).strip().lower()

    if allow_quit and choice == 'q':
        return None

    if choice.isdigit():
        idx = int(choice)
        if 1 <= idx <= len(options):
            return idx - 1

    print("⚠️ Invalid choice. Defaulting to last option.")
    return len(options) - 1

def generate_commit_message(commit_type: str, message_part: str) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"{commit_type}: {message_part} ({timestamp})"

def commit_changes(message: str):
    print(f"\nGenerated commit message:\n🔸 {message}")
    if input("Confirm commit? (y/n): ").lower().strip() != 'y':
        print("\n❌ Commit canceled")
        return

    if run_command(['git', 'add', '.']) and run_command(['git', 'commit', '-m', message]):
        print("\n✅ Commit successful!")
        if input("Push to remote? (y/n): ").lower().strip() == 'y':
            if run_command(['git', 'push']):
                print("\n🚀 Successfully pushed to remote!")
            else:
                print("\n❌ Push failed")

def create_custom_commit():
    print("\nEnter your commit message (type will be automatically detected):")
    custom_msg = input("Message: ").strip()
    
    # Auto-detect commit type from the message
    commit_type = "chore"  # default
    for t in COMMIT_OPTIONS.keys():
        if custom_msg.lower().startswith(t + ":"):
            commit_type = t
            custom_msg = custom_msg[len(t)+1:].strip()
            break
    
    commit_msg = generate_commit_message(commit_type, custom_msg)
    commit_changes(commit_msg)
    return True

def create_commit_flow():
    print("\nChoose commit method:")
    print("1: Use guided commit (select from options)")
    print("2: Write custom commit message")
    print("q: Cancel")
    
    choice = input("Select option: ").strip().lower()
    
    if choice == '1':
        types = list(COMMIT_OPTIONS.keys())
        type_index = select_option("SELECT FIRST PART (commit type):", types, allow_quit=True)
        if type_index is None:
            return False

        commit_type = types[type_index]
        message_options = COMMIT_OPTIONS[commit_type]
        message_index = select_option(f"SELECT SECOND PART ({commit_type} options):", message_options)
        message_part = message_options[message_index]

        commit_msg = generate_commit_message(commit_type, message_part)
        commit_changes(commit_msg)
        return True
    elif choice == '2':
        return create_custom_commit()
    elif choice == 'q':
        return False
    else:
        print("Invalid option")
        return True

def check_git_repo():
    """Check if current directory is a git repository"""
    if not os.path.exists(".git"):
        print("❌ Error: This is not a git repository")
        print("Please run this command in a git repository directory")
        sys.exit(1)

def main():
    check_git_repo()
    print("🐙 Git Commit Assistant")
    while True:
        print("\n1: Start new commit")
        print("2: Exit")
        user_input = input("Select option: ").strip()
        if user_input == '1':
            if not create_commit_flow():
                break
        elif user_input == '2':
            print("\n👋 Goodbye!")
            break
        else:
            print("Invalid option, please try again")

if __name__ == "__main__":
    main()

```



## 2️⃣ Tornar o script executável

```bash
chmod +x ~/gca.py
```

Teste rodando diretamente:

```bash
~/gca.py
```

Aí está a peça que falta, Val 👇

Se o `gca` funciona **no terminal atual**, mas some quando você fecha e abre outro, isso significa que o `PATH` com `~/.local/bin` não está sendo carregado no início da sessão.

---

# 🔧 Como deixar **global para sempre** (persistente)

### 1. Confirme se `~/.local/bin` está no PATH

Rode:

```bash
echo $PATH
```

Se **não aparecer** `~/.local/bin`, precisamos adicionar de forma persistente.

---

### 2. Adicione o PATH no shell de login

👉 Se você usa **Bash** (padrão no EndeavourOS):

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bash_profile
```

👉 Se você usa **Zsh**:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
```

---

### 3. Recarregue a configuração

Sem reiniciar, basta:

```bash
source ~/.bashrc   # ou ~/.zshrc, dependendo do shell
```

Agora o `PATH` vai ser carregado **toda vez que abrir o terminal**.

---

### 4. Teste

Abra um **novo terminal**, e rode:

```bash
which gca
```

Se aparecer:

```
/home/seuusuario/.local/bin/gca
```

