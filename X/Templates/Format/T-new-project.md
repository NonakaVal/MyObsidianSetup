---
project: "[[<% tp.file.folder() %>]]"
tags:
type: project
created: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
---


---
## 🧾 Descrição do Projeto

<%tp.file.cursor()%>





___
## 🎯 Objetivo

1. 🟢 Resultado ideal do projeto  
	1. 
2. 🟠 Resultado aceitável  
	1. 

## ❓ Expectativas
1. 🟢 O que pode ajudar o projeto  
	1. 
2. 🟠 Obstáculos potenciais  
	1. 
3. 👶 Inexperiências / Suposições  
	1. 
4. 👨‍💻 Insights e aprendizados  
	1. 

## ✅ Tarefas  
- 

## 📦 Recursos  
- 

## 📂 Registros do Projeto  
- 




<%* tp.hooks.on_all_templates_executed(async () => { 
    const file = tp.file.find_tfile(tp.file.path(true)); 
    const task_tag_value = tp.file.folder().toLowerCase().split(" ").join("_");
    await app.fileManager.processFrontMatter(file, (frontmatter) => { 
        frontmatter["tags"] = `project/${task_tag_value}`; 
    }); 
}); -%>

