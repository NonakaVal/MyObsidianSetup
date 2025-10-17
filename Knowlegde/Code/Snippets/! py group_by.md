def group_by(data, *args,**kwargs):
"""
ex: df.groupby("Categoria")["Vendas"].sum()
ex2: sexo = pd.DataFrame(sexo['Notas'].mean().round(2))
"""
	grouped_data = data.groupby(list(args), **kwargs)
	return grouped_data


