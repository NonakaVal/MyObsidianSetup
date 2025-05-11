---
tags: []
HUB:
  - "[[hub-descriptive-analysis]]"
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---

> [!NOTE] Identificando e removendo outliers  
> [[medidas-separatrizes]].
> método 1.5 IIQ com [[seaborn-box-plot(diagrama-de-caixa)]].

### ![[iiiq-interquartil-method]]

# Exemplo

```css
dados_new.boxplot(['Valor'])
```

Identificando grupos:
```css
grupo_tipo = dados.groupby('Tipo')['Valor']
```

```css
q1 = grupo_tipo.quantile(.25)
q3 = grupo_tipo.quantile(.75)
IIq = q3 - q1
limite_inferior = q1 - 1.5 * IIq
limite_superior = q3 + 1.5 * IIq
```

```css
dados_new = pd.DataFrame()

for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor'] >=  limite_inferior[tipo]) & (dados['Valor'] <= limite_superior[tipo] )
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new, dados_selecao])
```

[[seaborn-box-plot(diagrama-de-caixa)]]
```css
dados_new.boxplot(['Valor'], by = ['Tipo'])
```
