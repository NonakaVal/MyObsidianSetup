def quick_text_fix(texto, palavras_comuns=None, tags_ignoradas=None, min_tamanho_palavra=3):
    """
    Processa um texto completo:
    - Remove palavras comuns
    - Filtra por tamanho mínimo
    - Extrai tags (#tag) e links ([[link]])
    
    Parâmetros:
    - texto (str): Texto a ser processado.
    - palavras_comuns (set): Palavras a serem ignoradas.
    - tags_ignoradas (set): Tags e links a serem ignoradas.
    - min_tamanho_palavra (int): Tamanho mínimo para considerar a palavra relevante.
    
    Retorna:
    - dict com chaves: 'palavras_relevantes' e 'tags_links'
    """
    if palavras_comuns is None:
        palavras_comuns = {
            'o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas',
            'de', 'do', 'da', 'dos', 'das', 'em', 'no', 'na',
            'nos', 'nas', 'por', 'para', 'com', 'sem', 'sob',
            'the', 'and', 'or', 'of', 'to', 'in', 'on', 'at'
        }

    if tags_ignoradas is None:
        tags_ignoradas = set()

    texto_lower = texto.lower()
    palavras = re.findall(r'\b\w+\b', texto_lower)

    palavras_relevantes = [
        p for p in palavras 
        if p not in palavras_comuns and len(p) >= min_tamanho_palavra
    ]

    tags = set(re.findall(r'#(\w+)', texto_lower))
    links = set(re.findall(r'\[\[([^\|\]]+)', texto_lower))
    tags_links = tags.union(links) - tags_ignoradas

    return {
        'palavras_relevantes': palavras_relevantes,
        'tags_links': tags_links
    }
