---
dg-publish: true
---

Bem-vindo(a) ao seu guia visual para a jornada em Ciência de Dados! 🚀

Este checklist utiliza um formato onde cada tópico principal ou subtópico é um **link direto** para o recurso de estudo primário recomendado. Links adicionais e alternativos estão disponíveis nas **notas de rodapé** no final do documento. Use os checkboxes `[ ]` para marcar seu progresso!

---

## 🎓 Fase 1: Alicerces do Conhecimento – A Base Indispensável

### **🔢 Matemática**

- [ ] [**Álgebra Linear**](https://pt.khanacademy.org/math/linear-algebra) [^1]
    - [ ] Vetores
    - [ ] Matrizes
    - [ ] Transformações Linearess

- [ ] [**Cálculo**](https://pt.khanacademy.org/math/calculus-all-analytics) [^2]
    - [ ] Derivadas
    - [ ] Integrais
    - [ ] Otimização

***

### **📊 Estatística**

- [ ] [**Tópicos Fundamentais**](https://pt.khanacademy.org/math/statistics-probability) [^3]
    - [ ] *Estatística Descritiva* (média, mediana, desvio padrão, etc.)
    - [ ] *Probabilidade*
    - [ ] *Distribuições de Probabilidade*
    - [ ] *Inferência Estatística*
        - [ ] Estimação
        - [ ] Testes de Hipótese (paramétricos e não paramétricos)

***

### **💻 Programação**

- [ ] **Linguagens de Programação**
    - [ ] [🐍 **Python** (Proficiência)](https://docs.python.org/pt-br/3/tutorial/) [^4]
    - [ ] [🇷 **R** (Familiaridade ou Proficiência)](https://r4ds.had.co.nz/) [^5]

- [ ] **Fundamentos de Programação**
    - [ ] Sintaxe da Linguagem
    - [ ] Estruturas de Dados (listas, dicionários, arrays, etc.)
    - [ ] Algoritmos Básicos
    - [ ] Paradigmas de Programação (ex: Orientação a Objetos)
    - [ ] Boas Práticas de Desenvolvimento

- [ ] **Bibliotecas Essenciais (Python)**
    - [ ] [NumPy](https://numpy.org/doc/stable/user/quickstart.html)
    - [ ] [Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
    - [ ] [Matplotlib](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)
    - [ ] [Seaborn](https://seaborn.pydata.org/tutorial.html)

- [ ] **Bibliotecas Essenciais (R)**
    - [ ] [Tidyverse](https://www.tidyverse.org/packages/)
    - [ ] [ggplot2](https://ggplot2.tidyverse.org/)

***

### **💾 Bancos de Dados e SQL**

- [ ] [**SQL (Structured Query Language)**](https://pt.khanacademy.org/computing/computer-programming/sql) [^6]
    - [ ] Consultas (`SELECT`, `FROM`, `WHERE`)
    - [ ] Filtragem e Ordenação (`ORDER BY`, `LIMIT`)
    - [ ] Agregação (`GROUP BY`, `COUNT`, `SUM`, `AVG`)
    - [ ] Junções (`JOIN`s)
    - [ ] Manipulação de Dados (`INSERT`, `UPDATE`, `DELETE` - básico)

- [ ] **Modelagem de Dados** (Conceitos básicos)
- [ ] **Tipos de Bancos de Dados** (Diferenças entre Relacionais e NoSQL)

---
---

## 🛠️ Fase 2: Dominando o Fluxo de Trabalho da Ciência de Dados

### **📥 Coleta de Dados**

- [ ] **Técnicas**
    - [ ] Extração de Bancos de Dados (via SQL)
    - [ ] [Consumo de APIs (REST, etc.)](https://requests.readthedocs.io/en/latest/)
    - [ ] [Web Scraping (BeautifulSoup)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) [^7]
    - [ ] [Utilização de Datasets Públicos](https://www.kaggle.com/datasets) [^8]

***

### **🧹 Limpeza e Pré-processamento de Dados**

- [ ] [**Técnicas Essenciais**](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html) [^9]
    - [ ] Tratamento de Valores Ausentes (Imputação, Remoção)
    - [ ] Tratamento de Outliers (Identificação, Remoção/Ajuste)
    - [ ] Transformação de Variáveis (Normalização, Padronização, Codificação)
    - [ ] Engenharia de Features (Criação de novas variáveis)
    - [ ] Formatação e Estruturação de Dados

***

### **🔍 Análise Exploratória de Dados (EDA)**

- [ ] [**Explorando seus Dados**](https://www.ibm.com/br-pt/think/topics/exploratory-data-analysis) [^10]
    - [ ] Técnicas Descritivas
    - [ ] Identificação de Padrões e Relações
    - [ ] Teste de Suposições
    - [ ] Geração de Hipóteses

***

### **📈 Visualização de Dados**

- [ ] [**Princípios e Ferramentas Visuais**](https://www.datacamp.com/tracks/data-visualization-with-python) [^11]
    - [ ] Tipos de Gráficos e Quando Usá-los
    - [ ] Ferramentas (*Python*: Matplotlib, Seaborn, Plotly; *R*: ggplot2)

---
---

## 🧠 Fase 3: Introdução ao Machine Learning

### **🤖 Fundamentos de ML**

- [ ] [**Conceitos Chave**](https://www.coursera.org/specializations/machine-learning-introduction) [^12]
    - [ ] O que é ML?
    - [ ] Tipos de Aprendizado (Supervisionado, Não Supervisionado, Por Reforço)
    - [ ] *Overfitting vs Underfitting*
    - [ ] *Viés vs Variância (Bias-Variance Tradeoff)*

***

### **🎯 Aprendizado Supervisionado**

- [ ] [**Regressão e Classificação**](https://scikit-learn.org/stable/supervised_learning.html) [^13]
    - [ ] *Regressão* (Linear, Polinomial, SVR, Árvores, Random Forests, Boosting)
    - [ ] *Classificação* (Logística, KNN, SVC, Naive Bayes, Árvores, Random Forests, Boosting)

***

### **🧩 Aprendizado Não Supervisionado**

- [ ] [**Agrupamento (Clustering)**](https://scikit-learn.org/stable/modules/clustering.html) [^14]
    - [ ] K-Means
    - [ ] DBSCAN
    - [ ] Agrupamento Hierárquico
- [ ] [**Redução de Dimensionalidade**](https://scikit-learn.org/stable/modules/decomposition.html#pca) [^15]
    - [ ] Principal Component Analysis (PCA)
    - [ ] t-Distributed Stochastic Neighbor Embedding (t-SNE)

***

### **✅ Avaliação de Modelos**

- [ ] [**Métricas e Técnicas de Validação**](https://scikit-learn.org/stable/modules/model_evaluation.html) [^16]
    - [ ] *Métricas* (Regressão: MSE, RMSE, MAE, R²; Classificação: Matriz de Confusão, Acurácia, Precisão, Recall, F1, ROC, AUC)
    - [ ] *Técnicas de Validação* (Holdout, Validação Cruzada)
    - [ ] *Ajuste de Hiperparâmetros* (Grid Search, Random Search)

---
---

## 🚀 Fase 4: Aprofundamento e Especialização

### **🌌 Deep Learning (DL)**

- [ ] [**Fundamentos e Frameworks Avançados**](https://www.coursera.org/specializations/deep-learning) [^17]
    - [ ] Redes Neurais (MLP, Funções de Ativação, Backpropagation, Otimização)
    - [ ] Arquiteturas (CNNs, RNNs, LSTMs, GRUs, Transformers)
    - [ ] Frameworks (*TensorFlow*, *Keras*, *PyTorch*)

***

### **⏳ Modelagem de Séries Temporais**

- [ ] [**Análise e Previsão Temporal**](https://otexts.com/fpp3/) [^18]
    - [ ] Conceitos (Estacionariedade, Autocorrelação)
    - [ ] Modelos Clássicos (ARIMA, SARIMA, Exponencial Smoothing)
    - [ ] Modelos Baseados em ML/DL (Prophet, RNNs/LSTMs)

***

### **🗣️ Processamento de Linguagem Natural (NLP)**

- [ ] [**Compreendendo a Linguagem Humana**](https://www.coursera.org/specializations/natural-language-processing) [^19]
    - [ ] Pré-processamento de Texto
    - [ ] Representação de Texto (BoW, TF-IDF, Embeddings)
    - [ ] Modelos de Linguagem
    - [ ] Aplicações (Análise de Sentimentos, Classificação, NER, Tradução)
    - [ ] Transformers (BERT, GPT)

***

### **☁️ Big Data**

- [ ] [**Lidando com Grandes Volumes de Dados**](https://spark.apache.org/docs/latest/) [^20]
    - [ ] Conceitos (3 Vs: Volume, Velocidade, Variedade)
    - [ ] Ecossistema Hadoop (Conceitos)
    - [ ] *Apache Spark* (RDDs, DataFrames, Spark SQL, MLlib)
    - [ ] Plataformas (Databricks, Cloud Providers)

***

### **⚡ Real-Time Analytics**

- [ ] [**Análise em Tempo Real**](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [^21]
    - [ ] Spark Streaming
    - [ ] Kafka

***

### **🧬 Análise Multivariada**

- [ ] [**Explorando Múltiplas Variáveis**](https://www.amazon.com/Applied-Multivariate-Statistical-Analysis-6th/dp/0131877151) [^22]
    - [ ] Análise Fatorial
    - [ ] Análise de Componentes Principais (PCA - aprofundado)
    - [ ] Análise de Cluster (aprofundado)

---
---

## 🛠️ Fase 5: Da Teoria à Prática – Construindo Experiência e Portfólio

### **💡 Desenvolvimento de Projetos Pessoais**

- [ ] [**Guia para Construir Projetos**](https://blog.dsacademy.com.br/como-construir-um-portfolio-de-projetos-em-data-science/)
    - [ ] Definir problema
    - [ ] Coletar e preparar dados
    - [ ] Aplicar fluxo DS/ML
    - [ ] Documentar e Publicar (GitHub/Blog)

***

### **🏆 Participação em Competições**

- [ ] [**Plataformas (ex: Kaggle)**](https://www.kaggle.com/competitions) [^23]
    - [ ] Entender problema
    - [ ] Explorar dados/kernels
    - [ ] Desenvolver e submeter modelos
    - [ ] Aprender com resultados/discussões

***

### **🤝 Contribuição para Projetos Open Source**

- [ ] [**Como Contribuir (Guia)**](https://opensource.guide/how-to-contribute/)
    - [ ] Encontrar projetos de interesse
    - [ ] Contribuir (código, documentação, testes)

***

### **💼 Construção de Portfólio**

- [ ] [**Guia para Criar seu Portfólio**](https://www.datacamp.com/pt/blog/how-to-build-a-great-data-science-portfolio-with-examples) [^24]
    - [ ] Organizar projetos no *GitHub*
    - [ ] Criar um blog ou site pessoal (Opcional)
    - [ ] Preparar um resumo claro dos projetos e habilidades

---
---

## 🌟 Fase 6: Além do Código – Habilidades Complementares Essenciais

### **📈 Entendimento do Negócio (Business Acumen)**

- [ ] **Habilidades Chave**
    - [ ] Compreender o contexto do problema
    - [ ] Identificar KPIs relevantes
    - [ ] Alinhar soluções técnicas com objetivos de negócio

***

### **🗣️ Comunicação**

- [ ] [**Data Storytelling (Livro Essencial)**](https://www.storytellingwithdata.com/books) [^25]
    - [ ] Explicação de conceitos técnicos para público não técnico
    - [ ] Apresentação eficaz de resultados (oral e escrita)
    - [ ] Habilidade de escrita (Relatórios, Documentação)

***

### **👥 Colaboração**

- [ ] [**Controle de Versão (Git/GitHub)**](https://guides.github.com/introduction/git-handbook/) [^26]
    - [ ] Trabalho em equipe multidisciplinar
    - [ ] Metodologias Ágeis (Scrum, Kanban - Familiaridade)

***

### **⚖️ Ética em Dados**

- [ ] [**Princípios e Práticas Éticas**](https://www.coursera.org/learn/data-science-ethics) [^27]
    - [ ] Consciência sobre privacidade de dados (LGPD, GDPR)
    - [ ] Identificação e mitigação de viés algorítmico
    - [ ] Princípios de justiça e transparência em ML

---
---

## 📚 Aprendizado Contínuo

### **📰 Manter-se Atualizado**

- [ ] [**Fontes de Informação (ex: Towards Data Science)**](https://towardsdatascience.com/) [^28]
    - [ ] Ler artigos científicos (arXiv, conferências)
    - [ ] Acompanhar blogs e publicações especializadas
    - [ ] Seguir pesquisadores e profissionais influentes

***

### **🔬 Experimentação**

- [ ] **Práticas Essenciais**
    - [ ] Testar novas bibliotecas e ferramentas
    - [ ] Aplicar novas técnicas em projetos pessoais

***

### **🌐 Comunidade e Networking**

- [ ] [**Engajamento na Comunidade (ex: Meetup)**](https://www.meetup.com/) [^29]
    - [ ] Participar de cursos de atualização, workshops
    - [ ] Participar de conferências (online ou presenciais)
    - [ ] Engajar em comunidades online (Stack Overflow, Reddit, Discord)

---

## 📝 Notas de Rodapé (Recursos Adicionais)

> Aqui você encontra links alternativos ou complementares para os tópicos principais.

[^1]: **Álgebra Linear:** [Essence of Linear Algebra (3Blue1Brown - YouTube)](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab), [Udemy - Álgebra Linear com Python](https://www.udemy.com/course/algebra-linear-com-python/)
[^2]: **Cálculo:** [Essence of Calculus (3Blue1Brown - YouTube)](https://www.youtube.com/playlist?list=PLZHQObOWTQDNPOjrT6KVlfJuKtYTftqH6), [MIT OpenCourseware - Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/)
[^3]: **Estatística:** [StatQuest with Josh Starmer (YouTube)](https://www.youtube.com/user/joshstarmer), [Livro: Estatística Prática para Cientistas de Dados](https://www.amazon.com.br/Estat%C3%ADstica-Pr%C3%A1tica-Para-Cientistas-Dados/dp/855080603X), [DataCamp - Introduction to Statistics](https://www.datacamp.com/courses/introduction-to-statistics)
[^4]: **Python:** [Codecademy - Learn Python 3](https://www.codecademy.com/learn/learn-python-3), [Data Science Academy - Python Fundamentos](https://www.datascienceacademy.com.br/course/fundamentos-de-linguagem-python-para-analise-de-dados-e-data-science), [Alura - Formação Python para Data Science](https://www.alura.com.br/formacao-data-science-python), [Livro: Python para Análise de Dados](https://www.amazon.com.br/Python-para-An%C3%A1lise-Dados-Tratamento/dp/8575226475)
[^5]: **R:** [DataCamp - Introduction to R](https://www.datacamp.com/courses/free-introduction-to-r)
[^6]: **SQL:** [Mode Analytics - SQL Tutorial](https://mode.com/sql-tutorial/), [DataCamp - Introduction to SQL](https://www.datacamp.com/courses/introduction-to-sql), [Data Science Academy - SQL para Análise de Dados](https://www.datascienceacademy.com.br/course/sql-para-analise-de-dados-e-data-science), [W3Schools - SQL Tutorial](https://www.w3schools.com/sql/)
[^7]: **Web Scraping:** [Documentação do Scrapy](https://docs.scrapy.org/en/latest/)
[^8]: **Datasets:** [Google Dataset Search](https://datasetsearch.research.google.com/)
[^9]: **Limpeza/Pré-processamento:** [DataCamp - Data Cleaning in Python](https://www.datacamp.com/courses/data-cleaning-in-python), [Towards Data Science - Feature Engineering Guide](https://towardsdatascience.com/feature-engineering-for-machine-learning-3a5e293a5114), [Artigo: Pré-processamento de dados (DataCamp Blog)](https://www.datacamp.com/pt/blog/data-preprocessing)
[^10]: **EDA:** [Towards Data Science - EDA Tutorial](https://towardsdatascience.com/exploratory-data-analysis-eda-python-87178e35b14), [Livro: R for Data Science - Chapter 7](https://r4ds.had.co.nz/exploratory-data-analysis.html)
[^11]: **Visualização:** [Documentação Matplotlib](https://matplotlib.org/stable/tutorials/index.html), [Documentação Seaborn](https://seaborn.pydata.org/tutorial.html), [Documentação Plotly Python](https://plotly.com/python/), [Documentação ggplot2 (R)](https://ggplot2.tidyverse.org/), [Livro: Storytelling with Data](https://www.storytellingwithdata.com/books)
[^12]: **Fundamentos ML:** [Google - Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course?hl=pt-br), [Livro: Introduction to Statistical Learning](https://www.statlearning.com/), [Livro: Hands-On Machine Learning](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/)
[^13]: **Aprendizado Supervisionado:** [DataCamp - Supervised Learning with scikit-learn](https://www.datacamp.com/courses/supervised-learning-with-scikit-learn), [StatQuest - Playlists (YouTube)](https://www.youtube.com/user/joshstarmer/playlists)
[^14]: **Clustering:** [DataCamp - Unsupervised Learning in Python](https://www.datacamp.com/courses/unsupervised-learning-in-python), [StatQuest - Playlist (YouTube)](https://www.youtube.com/user/joshstarmer/playlists)
[^15]: **Redução de Dimensionalidade:** [DataCamp - Unsupervised Learning in Python](https://www.datacamp.com/courses/unsupervised-learning-in-python), [StatQuest - Playlist (YouTube)](https://www.youtube.com/user/joshstarmer/playlists)
[^16]: **Avaliação de Modelos:** [Documentação Scikit-Learn - Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html), [Documentação Scikit-Learn - Tuning hyper-parameters](https://scikit-learn.org/stable/modules/grid_search.html), [Google ML Crash Course - Validation](https://developers.google.com/machine-learning/crash-course/validation?hl=pt-br)
[^17]: **Deep Learning:** [Fast.ai](https://course.fast.ai/), [Livro: Deep Learning Book](https://www.deeplearningbook.org/), [Documentação TensorFlow](https://www.tensorflow.org/tutorials?hl=pt-br), [Documentação PyTorch](https://pytorch.org/tutorials/), [Livro: Deep Learning com Python (Chollet)](https://www.amazon.com.br/Deep-Learning-com-Python-Chollet/dp/8575227218)
[^18]: **Séries Temporais:** [Documentação Statsmodels](https://www.statsmodels.org/stable/tsa.html), [Documentação Prophet](https://facebook.github.io/prophet/docs/quick_start.html), [DataCamp - Time Series Track](https://www.datacamp.com/tracks/time-series-with-python)
[^19]: **NLP:** [Documentação NLTK](https://www.nltk.org/), [Documentação spaCy](https://spacy.io/usage), [Hugging Face - Transformers](https://huggingface.co/docs/transformers/index), [Livro: Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/), [DataCamp - NLP Track](https://www.datacamp.com/tracks/natural-language-processing-in-python)
[^20]: **Big Data:** [DataCamp - Big Data with PySpark Track](https://www.datacamp.com/tracks/big-data-with-pyspark), [Databricks Academy - Free Courses](https://www.databricks.com/learn/training/catalog/free-courses), [AWS Big Data Blog](https://aws.amazon.com/pt/blogs/big-data/)
[^21]: **Real-Time Analytics:** [Documentação Apache Kafka](https://kafka.apache.org/documentation/)
[^22]: **Análise Multivariada:** [StatQuest - PCA Explained (YouTube)](https://www.youtube.com/watch?v=FgakZw6K1QQ)
[^23]: **Competições:** [DataCamp Projects](https://www.datacamp.com/projects), [DrivenData Competitions](https://www.drivendata.org/competitions/)
[^24]: **Portfólio:** [GitHub Guides - Building a Portfolio](https://docs.github.com/pt/get-started/exploring-projects-on-github/setting-up-and-managing-your-github-profile/managing-your-profile-readme), [Artigo: Como Construir um Portfólio (DSA Blog)](https://blog.dsacademy.com.br/como-construir-um-portfolio-de-projetos-em-data-science/)
[^25]: **Comunicação:** [Artigo: Soft Skills (Ilumeo)](https://ilumeo.com.br/categorias/2022-03-22-soft-skills-no-contexto-da-ciencia-de-dados/), [Artigo: Soft Skills (Alura)](https://www.alura.com.br/artigos/soft-skills-mais-importantes-area-dados)
[^26]: **Colaboração:** [Artigo: Soft Skills (Ilumeo)](https://ilumeo.com.br/categorias/2022-03-22-soft-skills-no-contexto-da-ciencia-de-dados/), [Artigo: Soft Skills (Alura)](https://www.alura.com.br/artigos/soft-skills-mais-importantes-area-dados)
[^27]: **Ética:** [Livro: Weapons of Math Destruction](https://weaponsofmathdestructionbook.com/), [Artigo: Soft Skills (Ilumeo)](https://ilumeo.com.br/categorias/2022-03-22-soft-skills-no-contexto-da-ciencia-de-dados/), [Artigo: Soft Skills (Alura)](https://www.alura.com.br/artigos/soft-skills-mais-importantes-area-dados)
[^28]: **Atualização:** [arXiv - CS](https://arxiv.org/archive/cs), [Kaggle Blog](https://www.kaggle.com/blog), [Papers with Code](https://paperswithcode.com/), [Reddit - r/MachineLearning, r/datascience](https://www.reddit.com/)
[^29]: **Comunidade:** [Reddit - r/MachineLearning, r/datascience](https://www.reddit.com/), [Stack Overflow](https://stackoverflow.com/)

