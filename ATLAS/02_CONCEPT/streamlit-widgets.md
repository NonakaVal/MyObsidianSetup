---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
  - "[[hub-data-visualization]]"
link-to-lib: https://docs.streamlit.io/
created: "[[2024-08-04]]"
---
## Anatomia de um widget

Há quatro partes a serem lembradas ao usar widgets:

1. O componente frontend visto pelo usuário.
2. O valor de backend ou valor visto através de `st.session_state`.
3. A chave do widget usada para acessar seu valor via `st.session_state`.
4. O valor de retorno fornecido pela função do widget.