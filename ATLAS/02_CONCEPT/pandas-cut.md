---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.cut.html
created: "[[30-01-2024]]"
---
2024-01-30 18:32

{{Objetivo do método}}
Usado  para segmentar e categorizar dados em intervalos, ele é frequentemente usado para discretizar variáveis continuas
![Imgur](https://i.imgur.com/oirbUeF.png)

{{assinatura básica}}

```python
pandas.cut(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise', ordered=True)
```

{{parâmetros}}

- `x` - a variável contínua a que você deseja discretizar
- `bins` - especifica os intervalos para categorizar os dados
- `right` - indica se os intervalos são fechados á direita(padrão) ou a esquerda
- `labels` - rótulos para os intervalos resultantes
- `retbins` - se True retorna os intervalos usados
- `precision` - numero de casas decimais a serem usadas para arrendondar os valores
- `include_lowest` - se True inclui o limite inferiordo primeiro intervalo
- `duplicates` - como lidar com os valores duplicados, (raise,drop ou raise)
- `ordered` - se os intervalos devem ser ordenados

