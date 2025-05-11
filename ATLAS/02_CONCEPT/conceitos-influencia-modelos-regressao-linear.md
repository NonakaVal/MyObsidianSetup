---
tags:
  - learning/book
HUB:
  - "[[hub-statistic]]"
created: "[[2024-08-14]]"
---
Principais conceitos de influência em modelos de regressão linear

- Alavancagem : O potencial de um ponto influenciar o modelo com base na sua posição no espaço das variáveis independentes
- Resíduos : o erro entre o valor observado e o valor previsto.
- Influência : combinação de alta alavancagem e grande resíduo resulta em alta influência. ou seja.

métricas comuns de influência
- distancia de cook : mede a influência de cada observação sobre os coeficientes da regressão.

# $$D_i=\frac{r^2_i}{p\cdot MSE}\cdot \frac{h_i}{(1-h_i)^2}$$


