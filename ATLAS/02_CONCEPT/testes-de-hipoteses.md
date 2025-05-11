---
tags:
  - learning
HUB:
  - "[[hub-statistic]]"
  - "[[hub-hypothesis-testing]]"
---
O que fazem os testes de hipóteses ?

iremos admitir um valor hipotético para um parâmetro populacional, e com base nas afirmações da amostra realizaremos um teste estatístico, para aceitar ou rejeitar o valor hipotético. Como a decisão estará sujeita a erros, Estaremos tomando decisões de incerteza e, portanto, sujeitas a erro, Com base nos resultados obtidos em uma amostra, não é possível tomar decisões que sejam definitivamente corretas, podemos então só dimensionar a probabilidade

Hipóteses estatísticas 
trata-se da suposição quanto o valor de um parâmetro populacional, ou quanto à natureza das distribuição da probabilidade de uma variável populacional 

sempre serão feito hipóteses para parâmetros populacionais

o que são testes de hipóteses ?

é uma regra de decisão para aceitar ou rejeitar uma hipótese estatística com base nos elementos amostrais

para testar uma parâmetro populacional, devemos afirmar, cuidadosamente, um par de hipóteses, uma que representa a afirmação e outra que represente seu complemento, quando uma dessas hipóteses for falsa, a outra deve ser verdadeira, Essas duas hipóteses são chamadas de hipótese nula e hipótese alternativa

$H_0$ - hipótese nula - é uma hipótese estatística que contém uma afirmação de igualdade, tal como ''$\geq$, $=$ , $\leq$''

$H_1$ - hipótese alternativa - é, geralmente , o complemento da hipótese Nula, é a afirmação que deve ser verdadeira  se  $H_0$  for falsa e contém uma afirmação de desigualdade estrita, tal como $<$ , $\neq$ ,$>$

![Imgur](https://i.imgur.com/TiIXfSh.png)


<img src=https://emgotas.files.wordpress.com/2016/11/testes-de-hipc3b3testes-figura-1.jpg width='100%'>

---

### **Passo 1** - formulação das hipóteses $H_0$ e $H_1$;

> ### <font color='red'>Pontos importantes</font>
> - De maneira geral, o alvo do estudo deve ser formulado como a hipótese alternativa $H_1$.
> - A hipótese nula sempre afirma uma igualdade ou propriedade populacional, e $H_1$ a desigualdade que nega $H_0$.
> - No caso da hipótese nula $H_0$ a igualdade pode ser representada por uma igualdade simples "$=$" ou por "$\geq$" e "$\leq$". Sempre complementar ao estabelecido pela hipótese alternativa.
> - A hipótese alternativa $H_1$ deve definir uma desigualdade que pode ser uma diferença simples "$\neq$" ou dos tipos "$>$" e "$<$".


### **Passo 2** - escolha da distribuição amostral adequada;

> ### <font color='red'>Pontos importantes</font>
> - Quando o tamanho da amostra tiver 30 elementos ou mais, deve-se utilizar a distribuição normal, como estabelecido pelo **teorema do limite central**.
> - Para um tamanho de amostra menor que 30 elementos, e se pudermos afirmar que a população se distribui aproximadamente como uma normal e o desvio padrão populacional for conhecido, deve-se utilizar a distribuição normal.
> - Para um tamanho de amostra menor que 30 elementos, e se pudermos afirmar que a população se distribui aproximadamente como uma normal e o desvio padrão populacional for desconhecido, deve-se utilizar a distribuição t de Student.

<img src='https://caelum-online-public.s3.amazonaws.com/1229-estatistica-parte3/01/img003.png' width=70%>

### **Passo 3** - fixação da significância do teste ($\alpha$), que define as regiões de aceitação e rejeição das hipóteses (os valores mais freqüentes são 10%, 5% e 1%);

> ### <font color='red'>Pontos importantes</font>
> - O **nível de confiança** ($1 - \alpha$) representa a probabilidade de acerto da estimativa. De forma complementar o **nível de significância** ($\alpha$) expressa a probabilidade de erro da estimativa.
>
> ![Níveis de Confiança e significância](https://caelum-online-public.s3.amazonaws.com/1229-estatistica-parte3/01/img001.png)
>
> - O **nível de confiança** representa o grau de confiabilidade do resultado da estimativa estar dentro de determinado intervalo. Quando fixamos em uma pesquisa um **nível de confiança** de 95%, por exemplo, estamos assumindo que existe uma probabilidade de 95% dos resultados da pesquisa representarem bem a realidade, ou seja, estarem corretos.
>
> ![Áreas de Aceitação e Rejeição](https://caelum-online-public.s3.amazonaws.com/1229-estatistica-parte3/01/img002.png)

### **Passo 4** - cálculo da estatística-teste e verificação desse valor com as áreas de aceitação e rejeição do teste;

> ### <font color='red'>Pontos importantes</font>
> - Nos testes paramétricos, distância relativa entre a estatística amostral e o valor alegado como provável.
> - Neste passo são obtidas as estatísticas amostrais necessárias à execução do teste (média, desvio-padrão, graus de liberdade etc.)


### **Passo 5** - Aceitação ou rejeição da hipótese nula.

> ### <font color='red'>Pontos importantes</font>
> - No caso de o intervalo de aceitação conter a estatística-teste, aceita-se $H_0$ como estatisticamente válido e rejeita-se $H_1$ como tal.
> - No caso de o intervalo de aceitação não conter a estatística-teste, rejeita-se $H_0$ e aceita-se $H_1$ como provavelmente verdadeira. 
> - A aceitação também se verifica com a probabilidade de cauda (p-valor): se maior que $\alpha$, aceita-se $H_0$.


<img src='https://caelum-online-public.s3.amazonaws.com/1229-estatistica-parte3/01/img013.png' width=100%>
