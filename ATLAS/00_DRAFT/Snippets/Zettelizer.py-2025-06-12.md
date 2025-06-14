```python
import os
import re

PREFIXO = "prefix-"  # Prefixo para os arquivos criados
FRONTMATTER = """---

---"""

# Defina o caminho diretamente aqui
CAMINHO_ARQUIVO = "/caminho/para/o/seu/arquivo.md"



def sanitizar_nome_arquivo(nome):
    nome = re.sub(r'[\\/#%&{}<>*?$\'":@]', '', nome)
    nome = nome.strip().lower().replace(' ', '-')
    nome = re.sub(r'-+', '-', nome)
    return nome

def extrair_secoes(conteudo):
    padrao = r"(## .+?)(?=\n## |\Z)"
    return re.findall(padrao, conteudo, flags=re.DOTALL)

def processar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    nome_base = os.path.splitext(os.path.basename(caminho_arquivo))[0]
    pasta_destino = os.path.dirname(caminho_arquivo)
    secoes = extrair_secoes(conteudo)
    novo_conteudo = conteudo

    for secao in secoes:
        linha_header = secao.splitlines()[0]
        titulo = linha_header.replace("###", "").strip()
        nome_formatado = sanitizar_nome_arquivo(titulo)
        nome_arquivo = f"{PREFIXO}{nome_formatado}.md"
        caminho_novo = os.path.join(pasta_destino, nome_arquivo)

        secao_completa = (
            f"{FRONTMATTER}\n\n"
            f"{secao.strip()}\n\n"
            f"← Parte de [[{nome_base}]]"
        )

        with open(caminho_novo, 'w', encoding='utf-8') as f_out:
            f_out.write(secao_completa)

        print(f"✅ Criado: {caminho_novo}")

        novo_conteudo = novo_conteudo.replace(secao.strip(), f"# [[{PREFIXO}{nome_formatado}]]")

    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write(novo_conteudo)

    print(f"📝 Atualizado: {caminho_arquivo}")



if __name__ == "__main__":
    if os.path.isfile(CAMINHO_ARQUIVO) and CAMINHO_ARQUIVO.endswith(".md"):
        processar_arquivo(CAMINHO_ARQUIVO)
    else:
        print("❌ Caminho inválido ou arquivo não encontrado.")

```