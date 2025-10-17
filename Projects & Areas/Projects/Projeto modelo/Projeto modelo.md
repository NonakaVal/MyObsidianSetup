---
project: "[[Projeto modelo]]"
tags: project/projeto_modelo
type: project
created: "[[2025-10-15]]"
inicio: 2025-10-15
entrega: 2025-10-20
status: to start
---

| Data Início                                              | Data Entrega                                              | Status                                                                                                         |
| -------------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `INPUT[datePicker(showcase, defaultValue(null)):inicio]` | `INPUT[datePicker(showcase, defaultValue(null)):entrega]` | `INPUT[inlineSelect(option('In Progress'), option('Finished'), option('waiting'), option('to start')):status]` |

---

 `BUTTON[TEMPLATE-CRIAR-NOVA-NOTA-PROJETO]`
```meta-bind-button
label: Criar Nota de Projeto
icon: plus
hidden: true
class: ""
id: TEMPLATE-CRIAR-NOVA-NOTA-PROJETO
style: default
actions:
  - type: command
    command: quickadd:choice:e7c0cfff-583f-4da9-a201-79b4d5a12de4
```



