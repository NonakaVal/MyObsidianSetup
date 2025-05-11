---
tags:
  - learning
HUB:
  - "[[hub-tec]]"
---

## Ambientes virtuais Anaconda

[Anaconda](https://www.anaconda.com/)


```
conda activate nome_do_ambiente
conda deactivate
conda env list
conda create --name novo_ambiente
conda env remove --name nome_do_ambiente
```


- uma vez instalado o anaconda � preciso configurar os ambientes
#### Configurando Anaconda No terminal

- Configurando caminhos no path.
	- nas "configura��es avan�adas do sistema" = sistema de busca
		- buscar "vari�veis do ambiente"
			- ent�o "path"
				- criar os seguintes caminhos com "novo"

```css
C:\Users\Anaconda3
# meu caso C:\Users\nonak\anaconda3
and o Scripts
C:\Users\nonak\Anaconda3\Scripts
```



#### Criando Ambientes Conda
- no prompt de comando execute os seguintes comandos para:
```
conda create --name meuambiente python=3.11 # para criar o ambiente

```

```
activate meuambiente # para ativar o ambiente
```

```
deactivate # no ambiente para voltar ao ambiente padr�o
```

```
conda info --envs # lista os ambientes existentes
```

```
conda remove --name meuambiente --all # deleta o ambiente
```






