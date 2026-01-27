import os
from pathlib import Path
import sys
import io
from collections import defaultdict

# Garante que prints use UTF-8 (acentos, emojis, etc.)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# 📌 Caminhos fixos
PASTA_ENTRADA = Path(r"/home/nonaka/Documentos/Vaults/Notes/Projects & Areas/Projects/Archives/collectorsGuardian/")

PASTA_SAIDA   = Path(r"/home/nonaka/Documentos/Notes/+")

# Garante que a pasta de saída existe
PASTA_SAIDA.mkdir(parents=True, exist_ok=True)


def processar_frontmatter(texto: str) -> str:
    """
    Se existir frontmatter YAML, extrai os pares chave: valor e os formata em linha única.
    Retorna a string formatada + o conteúdo da nota.
    """
    linhas = texto.splitlines()
    if linhas and linhas[0].strip() == "---":
        frontmatter = []
        for i in range(1, len(linhas)):
            if linhas[i].strip() == "---":  # fim do frontmatter
                conteudo = "\n".join(linhas[i+1:]).strip()
                # monta resumo conciso
                resumo = " | ".join(
                    f"**{k.strip()}:** {v.strip().strip('[]')}"
                    for k, v in (linha.split(":", 1) for linha in frontmatter if ":" in linha)
                )
                return (resumo + "\n\n" + conteudo).strip()
            else:
                frontmatter.append(linhas[i])
    return texto.strip()


def juntar_markdowns(pasta_origem, arquivo_saida, separador="\n\n---\n\n", icone_pasta="📂", icone_nota="📝"):
    """
    Junta todos os arquivos .md de uma pasta (e subpastas) em um único arquivo,
    agrupando por pasta, adicionando ícones e formatando frontmatter.
    """
    pasta = Path(pasta_origem)
    arquivos_md = sorted(pasta.rglob("*.md"))  # pega recursivamente
    
    if not arquivos_md:
        print("⚠ Nenhum arquivo .md encontrado na pasta informada.")
        return
    
    # Agrupar arquivos por pasta
    grupos = defaultdict(list)
    for arq in arquivos_md:
        grupos[arq.parent].append(arq)
    
    arquivo_saida_path = Path(arquivo_saida)
    
    with open(arquivo_saida_path, "w", encoding="utf-8") as saida:
        for pasta_atual, arquivos in sorted(grupos.items()):
            # Header da pasta
            saida.write(f"# {icone_pasta} {pasta_atual.relative_to(pasta)}\n\n")
            
            for i, arquivo in enumerate(sorted(arquivos)):
                with open(arquivo, "r", encoding="utf-8") as f:
                    conteudo = f.read()
                
                conteudo_formatado = processar_frontmatter(conteudo)
                
                # título com o nome do arquivo + ícone 📝
                titulo = f"## {icone_nota} {arquivo.stem}\n\n"
                saida.write(titulo + conteudo_formatado)
                
                if i < len(arquivos) - 1:
                    saida.write(separador)
            
            # quebra de seção entre pastas
            saida.write("\n\n" + "="*50 + "\n\n")

    print(f"✅ Arquivo '{arquivo_saida_path}' criado com {len(arquivos_md)} notas em {len(grupos)} pastas.")


if __name__ == "__main__":
    nome_pasta = PASTA_ENTRADA.name  # pega apenas o nome da pasta de entrada
    arquivo_saida = PASTA_SAIDA / f"_OF_{nome_pasta}_.txt"
    juntar_markdowns(PASTA_ENTRADA, arquivo_saida)
