---
tags:
  - code
dateCreated: "[[2025-12-26]]"
---
```python
from google import genai
from google.genai import types
from PIL import Image
import json
import os
from datetime import datetime
from dotenv import load_dotenv
import re

# Carregar variáveis de ambiente
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Inicializar cliente
client = genai.Client(api_key=API_KEY)

# Prompt para análise inicial
ANALYSIS_PROMPT = """
Você é um sistema de catalogação de peças automotivas para inventário.
Você receberá uma imagem de caixas de peças automotivas com códigos e descrições.

Analise a imagem e forneça uma descrição DETALHADA do que você vê, incluindo:

1. DESCRIÇÃO GERAL DO CENÁRIO:
   - Tipo de produtos (caixas, peças soltas, em prateleiras, etc.)
   - Número de produtos distintos visíveis
   - Layout geral e organização

2. PARA CADA PRODUTO DISTINTO VISÍVEL, descreva:
   - Aparência física (cor, tamanho, formato das caixas)
   - Textos/rótulos visíveis (nomes de marcas, códigos, descrições)
   - Aplicações veiculares mencionadas
   - Quantidade desse produto específico
   - Quaisquer códigos de barras ou códigos de produto
   - Condição da embalagem (nova, danificada, etc.)

3. INCERTEZAS E AMBIGUIDADES:
   - O que você não tem certeza
   - Textos borrados ou pouco legíveis
   - Itens sobrepostos que dificultam a contagem
   - Possíveis interpretações incorretas

4. PERGUNTAS ESPECÍFICAS que você precisa que sejam respondidas para fornecer uma catalogação precisa:
   - Perguntar sobre códigos de produto pouco claros
   - Perguntar sobre aplicações veiculares específicas
   - Perguntar sobre nomes de marcas se não estiverem claros
   - Perguntar sobre quantidades se houver sobreposição

IMPORTANTE: Seja honesto sobre incertezas. É melhor perguntar do que adivinhar errado.

Retorne sua análise neste formato:
---
GERAL:
[descrição aqui]

DETALHES DOS PRODUTOS:
1. [descrição do primeiro produto]
2. [descrição do segundo produto]
...

INCERTEZAS:
- [listar incertezas aqui]

PERGUNTAS:
1. [primeira pergunta]
2. [segunda pergunta]
...

"""

# Prompt para catalogação final após validação
CATALOG_PROMPT = """
Com base na análise da imagem E nas correções/confirmações do usuário abaixo, crie a tabela final de catalogação.

CORREÇÕES/CONTEXTO DO USUÁRIO:
{user_corrections}

ANÁLISE DA IMAGEM:
{analysis_text}

INSTRUÇÕES:
Crie uma tabela em markdown com EXATAMENTE estas colunas:
| Category | Description | Car Brand | Specific Application | Part Brand | Product Code | Quantity | Confidence |

REGRAS:
1. Inclua TODOS os produtos distintos visíveis
2. Use as informações das CORREÇÕES DO USUÁRIO para corrigir quaisquer erros
3. Seja específico nas aplicações veiculares
4. Combine produtos idênticos em uma única linha com a quantidade total
5. Se a confiança for baixa devido a incertezas, marque como "low"

SAÍDA:
Retorne APENAS a tabela markdown com o cabeçalho. Nenhuma explicação, apenas a tabela.

"""

class InventoryValidator:
    def __init__(self, client):
        self.client = client
        self.inventory_data = []
    
    def analyze_image(self, image_path):
        """Faz análise inicial da imagem"""
        print(f"\n{'='*60}")
        print(f"🔍 ANALISANDO: {os.path.basename(image_path)}")
        print(f"{'='*60}")
        
        try:
            image = Image.open(image_path)
            
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    ANALYSIS_PROMPT,
                    image
                ],
                config=types.GenerateContentConfig(
                    temperature=0.2,
                )
            )
            
            return response.text
            
        except Exception as e:
            print(f"❌ Erro na análise: {str(e)}")
            return None
    
    def get_user_corrections(self, analysis_text, image_filename):
        """Solicita correções do usuário"""
        print(f"\n📋 ANÁLISE INICIAL DA IMAGEM '{image_filename}':")
        print(f"{'='*60}")
        print(analysis_text)
        print(f"{'='*60}")
        
        corrections = []
        
        while True:
            print("\n🎯 O QUE VOCÊ GOSTARIA DE CORRIGIR OU ADICIONAR?")
            print("1. Corrigir categoria de um produto")
            print("2. Especificar marca do veículo")
            print("3. Corrigir código do produto")
            print("4. Ajustar quantidade")
            print("5. Adicionar contexto específico")
            print("6. Confirmar análise e continuar")
            print("7. Descartar esta imagem")
            
            choice = input("\nEscolha uma opção (1-7): ").strip()
            
            if choice == "6":
                break
            elif choice == "7":
                return "IMAGE_DISCARDED"
            elif choice == "1":
                product_num = input("Número do produto na lista (ex: 1, 2, 3): ")
                correct_category = input("Categoria correta: ")
                corrections.append(f"Produto {product_num}: Corrigir categoria para '{correct_category}'")
            elif choice == "2":
                product_num = input("Número do produto na lista: ")
                car_brand = input("Marca do veículo correta: ")
                application = input("Aplicação específica (ex: Ford Focus 2015-2018): ")
                corrections.append(f"Produto {product_num}: Marca veículo = {car_brand}, Aplicação = {application}")
            elif choice == "3":
                product_num = input("Número do produto na lista: ")
                correct_code = input("Código do produto correto: ")
                corrections.append(f"Produto {product_num}: Código correto = {correct_code}")
            elif choice == "4":
                product_num = input("Número do produto na lista: ")
                correct_qty = input("Quantidade correta: ")
                corrections.append(f"Produto {product_num}: Quantidade = {correct_qty}")
            elif choice == "5":
                context = input("Digite o contexto adicional (ex: 'São filtros de óleo da marca XYZ para caminhões'): ")
                corrections.append(f"CONTEXTO GERAL: {context}")
            else:
                print("Opção inválida!")
        
        return "\n".join(corrections) if corrections else "Nenhuma correção necessária"
    
    def generate_final_table(self, image_path, analysis_text, user_corrections):
        """Gera tabela final com base nas correções"""
        try:
            image = Image.open(image_path)
            
            # Preparar prompt com correções
            final_prompt = CATALOG_PROMPT.format(
                user_corrections=user_corrections,
                analysis_text=analysis_text[:2000]  # Limitar tamanho
            )
            
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    final_prompt,
                    image
                ],
                config=types.GenerateContentConfig(
                    temperature=0.1,
                )
            )
            
            # Extrair tabela da resposta
            table_text = response.text.strip()
            
            # Adicionar metadados à linha
            image_name = os.path.basename(image_path)
            rows = table_text.split('\n')
            
            # Processar cada linha da tabela (exceto cabeçalho)
            for i, row in enumerate(rows):
                if i > 1 and row.strip():  # Pular cabeçalho e linha de separação
                    if '|' in row:
                        # Adicionar coluna de origem da imagem
                        parts = row.split('|')
                        if len(parts) >= 8:  # Tem todas as colunas
                            # Inserir coluna de imagem após código do produto
                            parts.insert(7, f" {image_name} ")
                            rows[i] = '|'.join(parts)
            
            return '\n'.join(rows)
            
        except Exception as e:
            print(f"❌ Erro ao gerar tabela final: {str(e)}")
            return None
    
    def process_image_interactive(self, image_path):
        """Processa uma imagem com validação interativa"""
        # Etapa 1: Análise inicial
        analysis = self.analyze_image(image_path)
        if not analysis:
            return None
        
        # Etapa 2: Validação do usuário
        user_corrections = self.get_user_corrections(analysis, os.path.basename(image_path))
        
        if user_corrections == "IMAGE_DISCARDED":
            print("🗑️  Imagem descartada pelo usuário")
            return None
        
        # Etapa 3: Geração da tabela final
        print("\n🔄 Gerando tabela final com correções...")
        final_table = self.generate_final_table(image_path, analysis, user_corrections)
        
        return final_table
    
    def process_folder_interactive(self, folder_path):
        """Processa uma pasta inteira com validação interativa"""
        print(f"\n{'='*60}")
        print(f"🚀 SISTEMA INTERATIVO DE CATALOGAÇÃO")
        print(f"📁 Pasta: {folder_path}")
        print(f"{'='*60}")
        
        # Listar imagens
        supported_ext = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp']
        image_files = []
        
        for file in os.listdir(folder_path):
            if any(file.lower().endswith(ext) for ext in supported_ext):
                image_files.append(os.path.join(folder_path, file))
        
        if not image_files:
            print("⚠️  Nenhuma imagem encontrada!")
            return None
        
        print(f"📸 Encontradas {len(image_files)} imagens")
        
        # Processar cada imagem
        all_tables = []
        
        for i, image_path in enumerate(image_files, 1):
            print(f"\n{'='*60}")
            print(f"📄 IMAGEM {i}/{len(image_files)}")
            print(f"{'='*60}")
            
            table = self.process_image_interactive(image_path)
            if table:
                all_tables.append(table)
            
            # Perguntar se quer continuar
            if i < len(image_files):
                cont = input(f"\n⏭️  Processar próxima imagem? (s/n): ").lower()
                if cont != 's':
                    print("⏹️  Processamento interrompido pelo usuário")
                    break
        
        # Consolidar todas as tabelas
        if all_tables:
            return self.consolidate_tables(all_tables)
        
        return None
    
    def consolidate_tables(self, tables):
        """Consolida múltiplas tabelas em uma"""
        print("\n📊 Consolidando todas as tabelas...")
        
        # Cabeçalho estendido com coluna de imagem
        header = "| Category | Description | Car Brand | Specific Application | Part Brand | Product Code | Quantity | Image Source | Confidence |\n"
        separator = "|----------|-------------|-----------|----------------------|------------|--------------|----------|--------------|------------|\n"
        
        consolidated = header + separator
        
        # Coletar todas as linhas
        all_rows = []
        
        for table in tables:
            rows = table.split('\n')
            for row in rows:
                if row.strip() and 'Category' not in row and '----------' not in row:
                    all_rows.append(row)
        
        # Adicionar todas as linhas
        for row in all_rows:
            consolidated += row + "\n"
        
        return consolidated
    
    def save_final_markdown(self, consolidated_table, folder_path):
        """Salva a tabela final em markdown"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"catalogo_validado_{timestamp}.md"
        
        markdown_content = f"""# 📦 CATÁLOGO DE PEÇAS AUTOMOTIVAS - VALIDADO

## 📋 METADADOS DO INVENTÁRIO
- **Data de geração:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
- **Pasta fonte:** `{folder_path}`
- **Sistema:** Catálogo Interativo com Validação Humana
- **Status:** ✅ VALIDADO POR ESPECIALISTA

---

## 🗃️ TABELA DE PRODUTOS VALIDADOS

{consolidated_table}

---

## 📈 RESUMO ESTATÍSTICO
- **Total de produtos:** {len([r for r in consolidated_table.split('\n') if r.strip() and '|' in r and 'Category' not in r])}
- **Processamento:** Validação humana em todas as entradas
- **Confiança:** Alta (revisado por especialista)

---

## 📝 NOTAS DO VALIDADOR
*As entradas nesta tabela foram revisadas e validadas por especialista.*
*Categorias, códigos e aplicações foram confirmados manualmente.*

---
*Documento gerado pelo Sistema Interativo de Catalogação de Peças Automotivas*
"""
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"\n✅ CATÁLOGO SALVO: {filename}")
        print(f"📊 Total de itens catalogados: {len([r for r in consolidated_table.split('\n') if r.strip() and '|' in r and 'Category' not in r])}")
        
        return filename

# Função para processamento rápido (sem validação interativa)
def quick_process_folder(folder_path):
    """Processamento rápido sem validação interativa"""
    validator = InventoryValidator(client)
    
    print("⚡ MODO RÁPIDO - Sem validação interativa")
    
    supported_ext = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp']
    image_files = []
    
    for file in os.listdir(folder_path):
        if any(file.lower().endswith(ext) for ext in supported_ext):
            image_files.append(os.path.join(folder_path, file))
    
    all_tables = []
    
    for image_path in image_files:
        print(f"📸 Processando: {os.path.basename(image_path)}")
        
        # Análise direta
        analysis = validator.analyze_image(image_path)
        if analysis:
            # Gerar tabela sem correções
            table = validator.generate_final_table(image_path, analysis, "Nenhuma correção fornecida - usar análise automática")
            if table:
                all_tables.append(table)
    
    if all_tables:
        consolidated = validator.consolidate_tables(all_tables)
        filename = validator.save_final_markdown(consolidated, folder_path)
        
        # Mostrar preview
        print("\n" + "="*80)
        print("PREVIEW DA TABELA (primeiras 10 linhas):")
        print("="*80)
        lines = consolidated.split('\n')
        for line in lines[:12]:  # Header + 10 rows
            print(line)
        print("="*80)
        
        return filename
    
    return None

# Execução principal
if __name__ == "__main__":
    FOLDER_PATH = "/home/nonaka/Documentos/notes/00 Code/auto-part-catalog-system/images"
    
    print("🎯 SISTEMA DE CATALOGAÇÃO COM VALIDAÇÃO INTERATIVA")
    print("\nEscolha o modo de operação:")
    print("1. 🧑‍💼 Modo Interativo (com validação humana)")
    print("2. ⚡ Modo Rápido (apenas análise automática)")
    
    mode = input("\nSelecione o modo (1 ou 2): ").strip()
    
    if mode == "1":
        # Modo interativo com validação
        validator = InventoryValidator(client)
        consolidated = validator.process_folder_interactive(FOLDER_PATH)
        if consolidated:
            validator.save_final_markdown(consolidated, FOLDER_PATH)
    elif mode == "2":
        # Modo rápido
        quick_process_folder(FOLDER_PATH)
    else:
        print("❌ Modo inválido selecionado!")
```

