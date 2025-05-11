---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html
created: "[[2024-02-12]]"
---
2024-02-12 11:54

{{Objetivo do método}}
Aplica funções sobre séries em um determinado intervalo

{{assinatura básica}}

```python
DataFrame.rolling(window, min_periods=None, center=False, axis=0, closed=None)
```

{{parâmetros}}

- `window` - tamanho da janela móvel, sendo o numero de observações utilizadas para cada calculo 
- `min_periods` - Números minino de observações não nulas necessárias
- `center` - indica se a janela deve ser concentrada nas observações
- `axis` - eixo ao longo do qual as funções serão aplicadas
- `closed` - controla qual lado da janela é incluído
