---
tags:
  - learning
  - tocomplete/explicar
HUB:
  - "[[hub-statistic]]"
  - "[[hub-ml-models]]"
  - "[[hub-python]]"
created: "[[21-01-2024]]"
---



```python
from statsmodels.stats.weightstats import ztest
ztest(notas1.rating, value = 3.4320503405352594)
```

```python
np.random.seed(75241)
temp = notas1.sample(frac =1).rating

def calcula_teste(i):
    media  = temp[0:i].mean()
    stats , p = ztest(temp[0:i], value = 3.4320503405352594) 
    return (i , media, p)

medias = np.array([calcula_teste(i)for i in range(2, len(temp))])

plt.figure(figsize = (10 ,5))
plt.plot(medias[:,0],medias[:,1])
plt.plot(medias[:,0],medias[:,2])
plt.hlines(y = 0.05, xmin = 2, xmax = len(temp), colors = 'r')

plt.grid(True)
```

