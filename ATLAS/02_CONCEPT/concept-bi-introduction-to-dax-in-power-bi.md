---
tags:
  - learning/review
  - tocomplete/explicar
HUB:
  - "[[hub-bi]]"
---

[[concept-bi-dax-(dataanalysisxpressions)]]

[[concept-dax-formulas-context]]

[[concept-dax-bi-creating-dax-measures]]


```DAX
Fantasia Vendas Blank = IF(

    ISBLANK(

        CALCULATE('medidas'[total_faturamento],

            FILTER('registro_livros_marketing',

                'registro_livros_marketing'[Categoria] = "Fantasia"))),

    "Nenhuma venda nesta Categoria",

    'medidas'[f_vendas]

)
```


```
porcentagem =

VAR total_faturamento_editora = 'medidas'[total_faturamento]

VAR total_vendas_categorias = CALCULATE('medidas'[total_faturamento], ALL(registro_livros_marketing[Categoria]))

VAR porcentagem = DIVIDE( total_faturamento_editora , total_vendas_categorias)

RETURN porcentagem
```


```
Total de vendas Fantasia =

CALCULATE(

    'medidas'[total_faturamento],

    FILTER(

        'registro_livros_marketing',

        'registro_livros_marketing'[Categoria] IN {"Fantasia", "Mitologia e Fantasia"}

    )

)
```

