---
tags:
  - learning
  - 
HUB:
  - "[[hub-sql]]"
---
```
Margem bruta % VAR =
VAR FaturamentoTotal = SUM(FaturamentoTotal)
VAR CustoTotal = SUM(Livros[CustoTotal])
VAR MargemBruta = FaturamentoTotal - CustoTotal
Return
MargemBruta/FaturamentoTotal 
```

```DAX
Classificação da margem =
IF('Livros'[Margem bruta %] > 0.4,
    "Margem alta", # if trur
    "Margem baixa" # if false
)
```

```objectivec
Classificação do faturamento =
SWITCH(
    TRUE(),
    'Livros'[Faturamento total] > 20000, "Faturamento alto",
    'Livros'[Faturamento total] > 15000, "Faturamento médio",
    "Faturamento baixo"
)
```

```ini
Leadtime = INT('registro_vendas'[Data_Entrega] = 'registro_vendas'[Data_Compra])
```

```DAX
goldvolume21 = CALCULATE(
	SUM(commoditties[volume],
	FILTER(commoditties, commoditties[symbol] = 'gold'))
	FILTER(commoditties, YEAR(commoditties[Date]) = 2001
))
```


```
gold21vs20 = 
VAR Goldvolume20 = CALCULATE (
SUM ( commoditties[volume]),
FILTER(commoditties, commoditties[symbol] = 'gold')
FILTER(commoditties, YEAR(commoditties[Date]) = 2020)
)
RETURN DIVIDE([goldvolume21] - Goldvolume20, Goldvolume20 )
```





