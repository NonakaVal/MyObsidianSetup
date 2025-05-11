---
tags:
  - learning
HUB:
  - "[[hub-descriptive-analysis]]"
  - "[[hub-python]]"
  - "[[hub-statistic]]"
---



> desvio médio absoluto ou (DMA) é uma medida de dispersão que quantifica a variabilidade dos dados em relação a média

# $$DM = \frac 1n\sum_{i=1}^{n}|X_i-\bar{X}|$$

ex1: dataframe com notas de fulano e ciclano:
> etapa por etapa criando [[concept-variaveis-no-dataframe-(colunas)]]
```css
notas_fulano = df[['fulano']]
nota_media_fulano = notas_fulano.mean()[0]
notas_fulano['Desvio'] = notas_fulano.Fulano - nota_media_fulano
notas_fulano['|Desvio|'] = notas_fulano['Desvio'].abs()
notas_fulano['|Desvio|'].mean()
```

>operação direta
```css
(df - df.mean()).abs().mean()
```

> [[concept-python-funcoes|funcao]] e numpy lib
```css
def mean_absolute_deviation(df):
    mean = np.mean(df, axis = 0)
    deviations = np.abs(df - mean)
    mad = np.mean(deviations, axis =0)
    return mad

mad = mean_absolute_deviation(df)
```
