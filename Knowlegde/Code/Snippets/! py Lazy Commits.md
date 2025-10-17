import subprocess

from datetime import datetime

  

# Commit type and their detailed options

#########################################################################################################

# This dictionary defines the commit types and their corresponding options.    

  
  

COMMIT_OPTIONS = {

    'feat': ['add new feature', 'implement module', 'create component', 'integrate API'],

    'fix': ['fix bug', 'resolve performance issue', 'adjust validation', 'repair critical error'],

    'docs': ['update documentation', 'add examples', 'fix typo', 'improve explanation'],

    'refactor': ['improve code structure', 'optimize function', 'remove duplicate code', 'simplify logic'],

    'chore': ['update dependencies', 'configure environment', 'adjust settings', 'clean up old code'],

}

  

#########################################################################################################

#########################################################################################################

# Funções auxiliares para executar comandos e interagir com o usuário

#########################################################################################################

  

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

  
  

###########################################################################################################

# Funções principais para o fluxo de commit

#########################################################################################################

  
  

def create_commit_flow():

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

  
  

##########################################################################################################

# Função principal para iniciar o assistente de commit

  

def main():

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