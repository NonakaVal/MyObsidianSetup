---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-ml-models]]"
  - "[[hub-statistic]]"
---
Dimension reduction GOAL : diminuir o numero de characteristics de variáveis 

Principal component analysis (PCA)
- algoritmo de  redução de dimension reduction
- transforma variáveis em componentes
- os componentes podem ser determinados pela porcentagem de variância explicada (quanto maior melhor)
- escolher componentes é mais uma arte do que uma ciência 

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.decomposition import PCA
```

### Transformação de Variáveis Dummy
[[pandas-get-dummies]]

```python
# get dummies
dataset[['animal',-'furniture']] = pd.get_dummies(dataset[['animal',-'furniture']], drop_first = True)
dataset[['animal',-'furniture']] = dataset[['animal',-'furniture']].astype(int)
```

```python
import pandas as pd

# Criando um DataFrame de exemplo
data = {'Categoria': ['A', 'B', 'A', 'C', 'B']}
df = pd.DataFrame(data)

# Aplicando get_dummies para converter a variável categórica em variáveis dummy
df_dummies = pd.get_dummies(df['Categoria'], prefix='Categoria', dtype = 'int')

# Concatenando as variáveis dummy ao DataFrame original
df = pd.concat([df, df_dummies], axis=1)
# Exibindo o DataFrame resultante
print(df)
```
- Converte variáveis categóricas em variáveis dummy (0 ou 1).

### Visualizar a matriz de correlação ajuda a entender a relação entre as variáveis
[[concept-ml-python-correlacao]]
```python
# correletion

X = dataset.drop(columns = 'rent amount')
X.head(1)
```

```python
sns.heatmap(X.corr(),
           annot = True,
           fmt = '.1g',
           center = 0,
           cmap ='coolwarm',
           linewidths =1,
           linecolor = 'black')
```
- Matriz de Correlação e Heatmap

### Normalização das Variáveis:
- Normaliza as variáveis para a mesma escala usando Min-Max scaling.
```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns = X.columns)
X_scaled.head()
```
Normalizar as variáveis é importante para garantir que todas as variáveis tenham a mesma escala, evitando que algumas variáveis dominem outras durante a análise.

### Análise de PCA - Explained Variance Ratio:
```python
model = PCA(random_state =1502).fit(X_scaled)
# Plot explained variance ratio for each component
plt.plot(model.explained_variance_ratio_, linewidth=4)
plt.xlabel('Number of Components')
plt.ylabel('Explained Variance Ratio')
plt.title('Explained Variance for Each Component')
plt.show()
```
Analisar a razão de variância explicada ajuda a decidir quantos componentes principais retêm informações significativas. Isso é crucial para entender a dimensionalidade dos dados.

```python
# cumulative
plt.plot(np.cumsum(model.explained_variance_ratio_), linewidth=4)
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Explained Variance vs. Number of Components')
plt.show()
```

### Seleção do Número de Componentes e Novo PCA
```python
# pca
model = PCA(n_components=4, 
           random_state= 1502).fit(X_scaled)

model_interpretation = pd.DataFrame(model.components_, columns = X.columns)
model_interpretation
```

### Transformação dos Dados com PCA:
```python
components = model.transform(X_scaled)
components = pd.DataFrame(components, columns = ['city', 'animals','rural small places', 'fantastic houses' ])
components.head()
```

### Concatenação dos Componentes com o Conjunto de Dados Original
```python
# merge
final_dataset = pd.concat([components, dataset], axis = 1)
final_dataset
```

### Redução de Dimensionalidade com t-SNE
```python
# manifold learn

from sklearn.manifold import TSNE
model = TSNE(n_components=2,
            random_state= 1503)
components = model.fit_transform(X)
components
```

```python
# plot

plt.scatter(components[:,0],
           components[:,1],
           cmap = 'hsv',
           c = dataset['rent amount'])
plt.title('tsne scater plot')
plt.show()
```

