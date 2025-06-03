---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
  - "[[hub-visualization-data]]"
link-to-lib: https://docs.streamlit.io/develop/s/architecture/forms
created: "[[2024-08-04]]"
---
## {{Objetivo da lib}}
Permitem entradas e atualizações sem ser necessário reiniciar a sessão
`import streamlit as st`
## {{Métodos}}

- map **Inputs and [[streamlit-widgets]]**
	- `form`
	- `st.number_input ` , `st.text_input` ,`st.write`, `st.text_area`
	- `st.slider` , `st.selectbox` 
	- `form_submit_button`

### Update de Frase
#### Code
```python
import streamlit as st

animal = st.form('my_animal')

# This is writing directly to the main body. Since the form container is
# defined above, this will appear below everything written in the form.
sound = st.selectbox('Sounds like', ['meow','woof','squeak','tweet'])

# These methods called on the form container, so they appear inside the form.
submit = animal.form_submit_button(f'Say it with {sound}!')
sentence = animal.text_input('Your sentence:', 'Where\'s the tuna?')
say_it = sentence.rstrip('.,!?') + f', {sound}!'
if submit:
    animal.subheader(say_it)
else:
    animal.subheader('&nbsp;')
```

#### Exemple
![Imgur](https://i.imgur.com/MMc5sJO.png)

```python
import streamlit as st

with st.form("my_form"):
   st.write("Inside the form")
   my_number = st.slider('Pick a number', 1, 10)
   my_color = st.selectbox('Pick a color', ['red','orange','green','blue','violet'])
   st.form_submit_button('Submit my picks')

  

# This is outside the form

st.write(my_number)
st.write(my_color)
```

### Sum Form
#### Code
```python
import streamlit as st

col1,col2 = st.columns([1,2])
col1.title('Sum:')

with st.form('addition'):
    a = st.number_input('a')
    b = st.number_input('b')
    submit = st.form_submit_button('add')

if submit:
    col2.title(f'{a+b:.2f}')
```

#### Exemple
![Imgur](https://i.imgur.com/TpPjHj4.png)

## {{Limitações}}
- Cada formulário deve conter um `st.form_submit_button`.
- `st.button`e `st.download_button`não pode ser adicionado a um formulário.
- `st.form`não pode ser incorporado dentro de outro `st.form`.
- Funções de retorno de chamada só podem ser atribuídas `st.form_submit_button`dentro de um formulário; nenhum outro widget em um formulário pode ter um retorno de chamada.
- Widgets interdependentes dentro de um formulário provavelmente não serão particularmente úteis. Se você passar `widget1`o valor de `widget2`quando ambos estiverem dentro de um formulário, então `widget2`só será atualizado quando o formulário for enviado.