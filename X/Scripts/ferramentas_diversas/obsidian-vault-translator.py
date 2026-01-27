import os
from pathlib import Path
from openai import OpenAI

# === CONFIGURAÇÕES ===
SOURCE_LANG = "en"   # idioma de origem
TARGET_LANG = "pt"   # idioma de destino
BASE_DIR = Path(r"C:\Users\nonak\Downloads\Ideaverse Pro 2\Ideaverse Pro 2\x\Packs")  # pasta base a ser varrida
OUTPUT_DIR = Path(r"C:\Users\nonak\Downloads\Ideaverse Pro 2\Ideaverse Pro 2\x\Packs\+")  # pasta onde salvar as traduções
MODEL = "gpt-4o-mini"  # modelo de tradução
CHUNK_SIZE = 8000  # número de caracteres por chunk

from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# === FUNÇÃO DE TRADUÇÃO ===
def translate_text(text: str) -> str:
    prompt = f"Traduza o seguinte texto de {SOURCE_LANG} para {TARGET_LANG}, mantendo formatação Markdown:\n\n{text}"
    response = client.responses.create(
        model=MODEL,
        input=prompt
    )
    return response.output_text.strip()

# === FUNÇÃO PRINCIPAL ===
def translate_markdown_files():
    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".md"):
                input_path = Path(root) / file
                relative_path = input_path.relative_to(BASE_DIR)
                output_path = OUTPUT_DIR / relative_path

                # Criar pastas destino se necessário
                output_path.parent.mkdir(parents=True, exist_ok=True)

                # Ler conteúdo
                with open(input_path, "r", encoding="utf-8") as f:
                    content = f.read()

                print(f"🔄 Traduzindo: {relative_path}")

                # Dividir se o arquivo for muito grande
                chunks = [content[i:i+CHUNK_SIZE] for i in range(0, len(content), CHUNK_SIZE)]
                translated_chunks = [translate_text(chunk) for chunk in chunks]
                translated_text = "\n".join(translated_chunks)

                # Escrever resultado
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(translated_text)

                print(f"✅ Tradução salva em: {output_path}\n")

if __name__ == "__main__":
    translate_markdown_files()

