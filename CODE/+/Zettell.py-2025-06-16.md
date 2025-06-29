```python
def sanitizar_nome_arquivo(nome: str) -> str:
    """Remove caracteres especiais e normaliza nomes de arquivos."""
    nome = re.sub(r'[\\/#%&{}<>*?$\'":@\[\]]', '', nome)  # Remove símbolos indesejados
    nome = nome.strip().lower().replace(' ', '-')         # Converte para slug
    return re.sub(r'-+', '-', nome) or "untitled"         # Evita nomes em branco
```




```python
def extrair_secoes(conteudo: str) -> list[str]:
    """Extrai blocos iniciados por '##' até a próxima ocorrência."""
    padrao = r"(## .+?)(?=\n## |\Z)"
    return re.findall(padrao, conteudo, flags=re.DOTALL)
```

```python
def salvar_nova_nota(destino: Path, nome_arquivo: str, conteudo: str):
    """Cria uma nova nota com o conteúdo extraído."""
    caminho = destino / nome_arquivo
    try:
        with open(caminho, 'w', encoding='utf-8') as f_out:
            f_out.write(conteudo)
        print(f"✅ Criado: {nome_arquivo}")
    except Exception as e:
        print(f"❌ Erro ao criar arquivo: {e}")
```

```python
def atualizar_arquivo_original(caminho: Path, conteudo: str):
    """Atualiza o arquivo principal com links para as novas notas."""
    try:
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        print(f"📝 Atualizado: {caminho.name}")
    except Exception as e:
        print(f"❌ Erro ao atualizar arquivo original: {e}")
```