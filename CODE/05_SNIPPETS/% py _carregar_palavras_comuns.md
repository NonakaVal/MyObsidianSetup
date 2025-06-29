def _carregar_palavras_comuns(self):
	"""Lista de palavras comuns em português e inglês para ignorar"""
	return {
		'o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas',
		'de', 'do', 'da', 'dos', 'das', 'em', 'no', 'na', 
		'nos', 'nas', 'por', 'para', 'com', 'sem', 'sob',
		'the', 'and', 'or', 'of', 'to', 'in', 'on', 'at'
	}