# -*- coding: utf-8 -*-

import os
import re
import yaml
import sys
from datetime import datetime
from collections import defaultdict, Counter
from config import MAIN_PATH

# Forçar UTF-8 no terminal (Windows especialmente)
sys.stdout.reconfigure(encoding='utf-8')

################################## Configuração ##################################

MAIN_PATH
# Verify MAIN_PATH exists
if not os.path.exists(MAIN_PATH):
    raise ValueError(f"O diretório principal não existe: {MAIN_PATH}")

caminho_da_pasta = MAIN_PATH
caminho_arquivo_saida = os.path.join(caminho_da_pasta, "_index_notas.md")

# Palavras-chave para identificar templates
TEMPLATE_KEYWORDS = ["Templates", "Template", "Ideaverse-Templates"]

def is_template_path(path):
    """Verifica se o caminho é de template"""
    return any(keyword in path for keyword in TEMPLATE_KEYWORDS)

################################## Funções utilitárias ##################################

def formatar_numero(num, decimal_places=1):
    if isinstance(num, int):
        return f"{num:,}".replace(",", ".")
    else:
        return f"{num:,.{decimal_places}f}".replace(",", "X").replace(".", ",").replace("X", ".")

def sanitize_frontmatter(yaml_text):
    """
    Substitui placeholders {{...}} por valores seguros no YAML (sem aspas)
    """
    return re.sub(r'\{\{.*?\}\}', 'PLACEHOLDER', yaml_text)

################################## Análise de frontmatter ##################################

def analyze_frontmatter(directory):
    property_stats = defaultdict(Counter)
    property_presence = Counter()
    file_count = 0

    for root, _, files in os.walk(directory):
        # Ignorar templates completamente
        if is_template_path(root):
            continue

        for file in files:
            if file.endswith(".md") and file != "_index_notas.md":
                file_path = os.path.join(root, file)
                file_count += 1

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                if content.startswith("---"):
                    end_of_header = content.find("---", 3)
                    if end_of_header != -1:
                        header = content[3:end_of_header].strip()
                        try:
                            safe_header = sanitize_frontmatter(header)
                            data = yaml.safe_load(safe_header) or {}
                            for prop, value in data.items():
                                property_presence[prop] += 1
                                if isinstance(value, list):
                                    for item in value:
                                        property_stats[prop][str(item)] += 1
                                else:
                                    property_stats[prop][str(value)] += 1
                        except yaml.YAMLError as e:
                            print(f"⚠️ Erro ao ler frontmatter em {file_path}: {e}")
                            continue

    return {
        'property_stats': dict(property_stats),
        'property_presence': property_presence,
        'total_files': file_count
    }

################################## Listagem de notas ##################################

def listar_notas_markdown_organizadas(pasta_raiz):
    notas_por_pasta = defaultdict(list)
    datas_modificacao = []

    for raiz, _, arquivos in os.walk(pasta_raiz):
        # Ignorar templates completamente
        if is_template_path(raiz):
            continue
            
        caminho_relativo = os.path.relpath(raiz, pasta_raiz)
        if caminho_relativo == '.':
            continue

        for arquivo in arquivos:
            if arquivo.endswith(".md") and arquivo != "_index_notas.md":
                caminho_completo = os.path.join(raiz, arquivo)
                nome_nota = os.path.splitext(arquivo)[0]

                mod_time = os.path.getmtime(caminho_completo)
                datas_modificacao.append(datetime.fromtimestamp(mod_time))

                notas_por_pasta[caminho_relativo].append(nome_nota)

    return notas_por_pasta, datas_modificacao

################################## Funções de Hubs ##################################

def extrair_hub(caminho_arquivo):
    try:
        # Ignorar templates
        if is_template_path(caminho_arquivo):
            return []

        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

            if linhas and linhas[0].strip() == '---':
                yaml_linhas = []
                for linha in linhas[1:]:
                    if linha.strip() == '---':
                        break
                    yaml_linhas.append(linha)

                safe_yaml = sanitize_frontmatter("".join(yaml_linhas))
                frontmatter = yaml.safe_load(safe_yaml) or {}
                hub = frontmatter.get('subject')

                if isinstance(hub, list):
                    return hub
                elif isinstance(hub, str):
                    return [hub]
        return []
    except Exception as e:
        print(f"⚠️ Erro ao ler {caminho_arquivo}: {e}")
        return []

def contar_hubs(diretorio):
    contador = Counter()
    total_md = 0
    com_frontmatter = 0
    com_hub = 0

    for raiz, _, arquivos in os.walk(diretorio):
        # Ignorar templates
        if is_template_path(raiz):
            continue

        for arquivo in arquivos:
            if arquivo.lower().endswith('.md') and arquivo != "_index_notas.md":
                total_md += 1
                caminho_arquivo = os.path.join(raiz, arquivo)

                with open(caminho_arquivo, 'r', encoding='utf-8') as arq:
                    linhas = arq.readlines()

                    if linhas and linhas[0].strip() == '---':
                        com_frontmatter += 1
                        hubs = extrair_hub(caminho_arquivo)

                        if hubs:
                            contador.update(hubs)
                            com_hub += 1

    return {
        'contador_hubs': contador,
        'total_md': total_md,
        'com_frontmatter': com_frontmatter,
        'com_hub': com_hub
    }

################################## Gerar Markdown ##################################

def salvar_em_markdown(notas_organizadas, datas_modificacao, frontmatter_data, caminho_saida):
    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
    
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        f.write(f"\n\n*Atualizado em {datetime.now().strftime('%Y/%m/%d %H:%M')}*\n\n")
        
        f.write(" ## 🗒️ Informações Gerais\n\n")
        total_notas = sum(len(n) for n in notas_organizadas.values())
        f.write(f"- **Total de Notas:** {formatar_numero(total_notas)}\n")
        f.write(f"- **Número de Pastas:** {formatar_numero(len(notas_organizadas))}\n")

        if notas_organizadas:
            pasta_mais_notas = max(notas_organizadas.items(), key=lambda x: len(x[1]))
            f.write(f"- **Pasta com mais notas:** `{pasta_mais_notas[0]}` ({formatar_numero(len(pasta_mais_notas[1]))} notas)\n")

        f.write("\n---\n\n## 🏷️ Hubs Mais Utilizados\n\n")
        hubs_data = contar_hubs(caminho_da_pasta)
        contador_hubs = hubs_data['contador_hubs']

        if contador_hubs:
            f.write("| Hub | Contagem |\n")
            f.write("|------|----------|\n")
            for hub, quantidade in contador_hubs.most_common(100):
                f.write(f"| `{hub}` | {quantidade} |\n")
        else:
            f.write("Nenhum hub encontrado nos frontmatters.\n")

        f.write("\n---\n\n## 🔍 Propriedades no Frontmatter\n\n")

        if frontmatter_data['property_presence']:
            f.write("| Propriedade | Arquivos | Cobertura |\n")
            f.write("|--------------|----------|-----------|\n")
            for prop, count in frontmatter_data['property_presence'].most_common(10):
                coverage = (count / frontmatter_data['total_files']) * 100 if frontmatter_data['total_files'] else 0
                f.write(f"| `{prop}` | {count} | {coverage:.1f}% |\n")
        else:
            f.write("Nenhuma propriedade encontrada no frontmatter.\n")

        f.write("\n---\n\n# 🗂️ Pastas e Notas\n\n")

        pastas_escritas = set()
        icones_pasta = {
            1: "📁",
            2: "📂",
            3: "📘",
            4: "📙",
            5: "📗",
            6: "📄",
        }

        for caminho_completo, notas in sorted(notas_organizadas.items()):
            partes = caminho_completo.split(os.sep)
            caminho_acumulado = []

            for i, parte in enumerate(partes):
                caminho_acumulado.append(parte)
                chave = os.sep.join(caminho_acumulado)

                if chave not in pastas_escritas:
                    header_level = min(i + 1, 6)
                    icone = icones_pasta.get(header_level, "📦")
                    f.write(f"{'#' * header_level} {icone} {parte}\n\n")
                    pastas_escritas.add(chave)

            for nome_nota in sorted(notas):
                f.write(f"- 📄 [{nome_nota}]\n")

        f.write("\n---\n")

################################## Execução Principal ##################################

if __name__ == "__main__":
    if not os.path.exists(caminho_da_pasta):
        print(f"Erro: O diretório '{caminho_da_pasta}' não existe!")
        sys.exit(1)

    notas_organizadas, datas_modificacao = listar_notas_markdown_organizadas(caminho_da_pasta)
    frontmatter_data = analyze_frontmatter(caminho_da_pasta)

    try:
        salvar_em_markdown(
            notas_organizadas,
            datas_modificacao,
            frontmatter_data,
            caminho_arquivo_saida
        )
        print(f"✅ Arquivo {caminho_arquivo_saida} gerado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao gerar o arquivo: {e}")
        sys.exit(1)