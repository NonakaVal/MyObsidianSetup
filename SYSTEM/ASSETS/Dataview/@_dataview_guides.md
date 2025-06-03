
# 📄 Guia Rápido — Dataview Plugin (Obsidian)

## 🔍 Listas Simples

### ➕ Criar lista de todas as notas especificadas

```dataview
list
```

### 🗂️ Definir a origem das notas

```dataview
list
from
```

### 🔖 **Por TAG**

```dataview
list
from #tag
```

### 📁 **Por FOLDER**

```dataview
list
from "foldername"
```

### 🔗 **Por LINKS**

- Notas que apontam para uma nota:
    

```dataview
list
from [[Nota]]
```

- Notas que saem de uma nota:
    

```dataview
list
from outgoing([[Nota]])
```

## 🧠 Combinação de Fontes

- **AND**
    

```dataview
list
from #tag1 and #tag2
```

- **OR**
    

```dataview
list
from #tag1 or #tag2
```

- **EXCLUDE (-)**
    

```dataview
list
from -#tag
```

- **AND com exclusão**
    

```dataview
list
from [[Nota]] and -[[Nota]]
```

## 🧵 Concatenação de Strings

```dataview
list "File path: " + file.path + " ✅"
from #tag
```

## 🔗 Lista de Propriedades em Arrays

```dataview
list authors
from [[Nota]]
```

---

## ✅ Busca por Tarefas

Procura todas as checkboxes (`- [ ]`) no vault.

- **Por tag:**
    

```dataview
task from #tag
```

---

## 🎯 Filtros com WHERE

Permite refinar os resultados após o `from`.

- **Excluir uma nota específica:**
    

```dataview
list
where file.name != "000 Home"
```

- **Notas modificadas nas últimas 24 horas:**
    

```dataview
list
where file.mtime >= date(today) - dur(1 day)
```

- **Onde tarefa não está completa:**
    

```dataview
list from
where !complete
```

- **Onde não há data de atualização:**
    

```dataview
list from
where !date updated
```

---

## 📊 Tabelas

Exibe campos como tabela.

- **Tabela simples com nome dos arquivos:**
    

```dataview
table file.name
from [[Nota]]
```

- **Exemplos com propriedades personalizadas:**
    

```dataview
table autores, dificuldade
from [[Nota]]
```

---

## 🧭 Ordenação (SORT)

```dataview
table file.name
from [[Nota]]
sort file.name asc
```

---

## 🪄 Expandindo Arrays (FLATTEN)

Desenrola listas (arrays) dentro dos campos.

```dataview
table authors
from [[Nota]]
flatten authors
```

---


