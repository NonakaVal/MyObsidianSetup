import os
import nbformat
from nbconvert import MarkdownExporter
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import MAIN_PATH

def converter_notebook_para_markdown(caminho_notebook, caminho_destino):
    # Verifica se o caminho do notebook é válido
    if not os.path.isfile(caminho_notebook):
        print(f"O caminho {caminho_notebook} não é válido.")
        return

    # Verifica se o diretório de destino existe, se não, cria
    if not os.path.exists(caminho_destino):
        os.makedirs(caminho_destino)

    # Carregar o notebook com nbformat (não como uma string, mas como um objeto JSON)
    with open(caminho_notebook, 'r', encoding='utf-8') as notebook_file:
        notebook_content = nbformat.read(notebook_file, as_version=4)

    # Usar o MarkdownExporter do nbconvert para converter o conteúdo
    exporter = MarkdownExporter()
    markdown, resources = exporter.from_notebook_node(notebook_content)

    # Criar o caminho do arquivo de destino para o Markdown
    nome_arquivo_markdown = os.path.splitext(os.path.basename(caminho_notebook))[0] + ".md"
    caminho_arquivo_markdown = os.path.join(caminho_destino, nome_arquivo_markdown)

    # Salvar o conteúdo gerado em um arquivo .md
    with open(caminho_arquivo_markdown, 'w', encoding='utf-8') as md_file:
        md_file.write(markdown)

    print(f"Nota Markdown gerada em: {caminho_arquivo_markdown}")

# Exemplo de uso
caminho_do_notebook = r"C:\Users\nonak\Downloads\análise dados covid.ipynb"
caminho_destino = MAIN_PATH
converter_notebook_para_markdown(caminho_do_notebook, caminho_destino)

