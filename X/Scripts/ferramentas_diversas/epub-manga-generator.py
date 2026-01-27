import os
import shutil
from PIL import Image
from ebooklib import epub
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


def criar_epub(pasta_imagens, saida):
    """Cria um arquivo EPUB a partir de imagens."""
    book = epub.EpubBook()
    book.set_identifier("id123456")
    book.set_title("Meu Livro de Imagens")
    book.set_language("pt")

    spine = ['nav']
    for idx, nome in enumerate(sorted(os.listdir(pasta_imagens))):
        if nome.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            caminho = os.path.join(pasta_imagens, nome)
            img_item = epub.EpubItem(
                uid=f"img{idx}",
                file_name=f"images/{nome}",
                media_type=f"image/{nome.split('.')[-1]}"
            )
            with open(caminho, 'rb') as f:
                img_item.content = f.read()
            book.add_item(img_item)

            page = epub.EpubHtml(title=f"Imagem {idx+1}", file_name=f"page_{idx}.xhtml")
            page.content = f'<html><body><img src="images/{nome}" alt="Imagem {idx+1}" style="width:100%;height:auto;"/></body></html>'
            book.add_item(page)
            spine.append(page)

    book.spine = spine
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    epub.write_epub(saida, book)
    print(f"✅ EPUB criado com sucesso: {saida}")


def criar_pdf(pasta_imagens, saida):
    """Cria um arquivo PDF a partir de imagens (ajustadas à página)."""
    c = canvas.Canvas(saida, pagesize=A4)
    largura_pagina, altura_pagina = A4

    for nome in sorted(os.listdir(pasta_imagens)):
        if nome.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            caminho = os.path.join(pasta_imagens, nome)
            img = Image.open(caminho)
            largura_img, altura_img = img.size

            escala = min(largura_pagina / largura_img, altura_pagina / altura_img)
            nova_largura = largura_img * escala
            nova_altura = altura_img * escala
            x = (largura_pagina - nova_largura) / 2
            y = (altura_pagina - nova_altura) / 2

            c.drawImage(ImageReader(img), x, y, nova_largura, nova_altura)
            c.showPage()

    c.save()
    print(f"✅ PDF criado com sucesso: {saida}")


def criar_html(pasta_imagens, saida):
    """Cria um arquivo HTML com as imagens copiadas para uma subpasta (Webtoon style)."""
    base_dir = os.path.dirname(saida)
    pasta_destino = os.path.join(base_dir, "images")
    os.makedirs(pasta_destino, exist_ok=True)

    # Copiar imagens
    imagens = [img for img in sorted(os.listdir(pasta_imagens)) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    for nome in imagens:
        shutil.copy(os.path.join(pasta_imagens, nome), os.path.join(pasta_destino, nome))

    # Criar HTML
    html = [
        "<!DOCTYPE html>",
        "<html lang='pt'>",
        "<head>",
        "<meta charset='UTF-8'>",
        "<meta name='viewport' content='width=device-width, initial-scale=1.0'>",
        "<title>Webtoon Viewer</title>",
        "<style>",
        "body { background: #111; color: #fff; margin: 0; }",
        "img { width: 100%; height: auto; display: block; margin: 0 auto; }",
        "</style>",
        "</head>",
        "<body>",
    ]

    for nome in imagens:
        html.append(f"<img src='images/{nome}' alt='{nome}'>")

    html.append("</body></html>")

    with open(saida, "w", encoding="utf-8") as f:
        f.write("\n".join(html))

    print(f"✅ HTML (Webtoon) criado com sucesso: {saida}")
    print(f"🖼️ As imagens foram copiadas para: {pasta_destino}")
    print("💡 Abra o arquivo HTML no navegador para leitura em rolagem contínua.")


def main():
    print("=== Criador de Livro de Imagens ===")
    pasta_imagens = input("📁 Caminho da pasta com as imagens: ").strip()
    formato = input("📘 Escolha o formato de saída (epub/pdf/html): ").strip().lower()
    pasta_saida = input("📂 Caminho da pasta de saída: ").strip()

    if not os.path.isdir(pasta_imagens):
        print("❌ Pasta de imagens inválida.")
        return
    if not os.path.isdir(pasta_saida):
        print("❌ Pasta de saída inválida.")
        return

    nome_saida = input("💾 Nome do arquivo de saída (sem extensão): ").strip()
    if not nome_saida:
        nome_saida = "livro_imagens"

    caminho_saida = os.path.join(pasta_saida, f"{nome_saida}.{formato}")

    if formato == "epub":
        criar_epub(pasta_imagens, caminho_saida)
    elif formato == "pdf":
        criar_pdf(pasta_imagens, caminho_saida)
    elif formato == "html":
        criar_html(pasta_imagens, caminho_saida)
    else:
        print("❌ Formato inválido. Escolha 'epub', 'pdf' ou 'html'.")


if __name__ == "__main__":
    main()
