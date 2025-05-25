---
tags:
  - learning
  - resources
  - tocomplete
HUB:
  - "[[hub-python]]"
  - "[[hub-visualization-data]]"
  - "[[hub-descriptive-analysis]]"
  - "[[System/HUB/hub-tec]]"
link-to-lib: https://docs.streamlit.io/
created: "[[2024-08-04]]"
---
{{Objetivo da lib}}
Create dynamics dataApps

{{installation}}

### Streamlit

```python
pip install streamlit
```

```python
pip install --upgrade streamlit
pip install streamlit-nightly --upgrade
```

{{run}}
```python
streamlit run your_script.py
python -m streamlit run your_script.py

streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py

```


- [[streamlit-chache-system]]
	- permite que você pule uma função e retorne um valor previamente computado. Quando você usa caching, você executa tudo, exceto a função em cache (se você já a tiver executado antes).
Sessions state

- [[streamlit-forms]]
	- **Os formulários** permitem que os usuários interajam com widgets sem executar novamente seu aplicativo. O Streamlit não envia ações do usuário dentro de um formulário para o backend Python do seu aplicativo até que o formulário seja enviado. Os widgets dentro de um formulário não podem atualizar dinamicamente outros widgets (dentro ou fora do formulário) em tempo real.
- [[streamlit-fragments]]
	- **Fragmentos** são executados independentemente do resto do seu código. Conforme seus usuários interagem com widgets de fragmento, suas ações são imediatamente processadas pelo backend Python do seu aplicativo e seu código de fragmento é executado novamente. Widgets dentro de um fragmento podem atualizar dinamicamente outros widgets dentro do mesmo fragmento em tempo real.










{{Métodos}}