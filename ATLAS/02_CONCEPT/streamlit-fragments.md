---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
  - "[[hub-data-visualization]]"
link-to-lib: https://docs.streamlit.io/develop/s/architecture/fragments
created: "[[2024-08-04]]"
---
## {{Objetivo da lib}}
Aumentar a eficiência de múltiplos modulo 



### Chamando a Função
`@st.fragment()`
`.file_uploader` , 

```python
import streamlit as st

@st.fragment()
def fragment_function():
    if st.button("Hi!"):
        st.write("Hi back!")

fragment_function()
```

```python
with st.sidebar: 
	fragment_function()
```


## {{Métodos}}


- `run_every` 
```python
@st.fragment(run_every = "10s" ) # atualiza automaticamente
def auto_function():
		# This will update every 10 seconds!
		df = get_latest_updates()
		st.line_chart(df)

auto_function()
```

### Exemplos
```python
import streamlit as st

st.title("My Awesome App")

@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter text")

@st.fragment()
def filter_and_file():
    cols = st.columns(2)
    cols[0].checkbox("Filter")
    cols[1].file_uploader("Upload image")

toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("Select", [1,2,3], None)
cols[1].button("Update")

filter_and_file()
```

![Imgur|500](https://i.imgur.com/4bl3K77.png)


## Limitações e comportamento sem suporte

- Fragmentos não conseguem detectar uma mudança em valores de entrada. É melhor usar Session State para entrada e saída dinâmicas para funções de fragmento.
- Não há suporte para chamar fragmentos dentro de fragmentos.
- O uso de cache e fragmentos na mesma função não é suportado.
- O uso de fragmentos dentro de funções de retorno de chamada não é suportado.
- Fragmentos não podem renderizar widgets em contêineres criados externamente; os widgets só podem estar no corpo principal de um fragmento.