import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import MAIN_PATH

def confirmar_acao(mensagem: str) -> bool:
    """Solicita confirmação do usuário para uma ação."""
    resposta = input(f"{mensagem} (digite 'confirmar' para prosseguir): ").strip().lower()
    return resposta == "confirmar"

def clean_and_update_markdown_notes(directory: str, new_header: str) -> None:
    """Remove e refaz o cabeçalho em arquivos Markdown com confirmações."""
    # Etapa 1: Confirmação do diretório
    print(f"\nDiretório a ser modificado: {directory}")
    caminho_digitado = input("Digite novamente o caminho ou parte dele para confirmar: ").strip()
    
    if caminho_digitado not in directory:
        print("Verificação do caminho falhou. Operação cancelada.")
        return
    
    # Etapa 2: Confirmação final
    if not confirmar_acao(f"\nVocê está prestes a modificar todos os arquivos .md em '{directory}'"):
        print("Operação cancelada pelo usuário.")
        return
    
    print("\nIniciando processamento...")
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Remove frontmatter existente
                    if content.startswith("---"):
                        end_of_header = content.find("---", 3)
                        if end_of_header != -1:
                            content = content[end_of_header + 3:].lstrip()

                    # Adiciona novo header
                    updated_content = new_header + "\n" + content

                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f"✓ Atualizado: {file_path}")
                
                except Exception as e:
                    print(f"! Erro ao processar {file_path}: {str(e)}")
    
    print("\nOperação concluída!")

if __name__ == "__main__":
    directory_to_scan = r"/home/nonaka/Documentos/GitHub/dg-pkm/Conceitos/Arquiteto & Jardineiro"

    new_header = """---
up: 
dg-publish: false
---"""
    
    clean_and_update_markdown_notes(directory_to_scan, new_header)