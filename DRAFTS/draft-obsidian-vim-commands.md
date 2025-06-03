---
type: new_note
tags:
  - new_note
created: '[[2025-05-31]]'
---



## **1. Navegação Rápida em Arquivos .md**

### 🔹 **Navegar entre Headers (Títulos)**

| Ação                             | Comando Vim                                |
| -------------------------------- | ------------------------------------------ |
| **Ir para o próximo header**     | `]]`                                       |
| **Ir para o header anterior**    | `[[`                                       |
| **Ir para o topo do documento**  | `gg`                                       |
| **Ir para o final do documento** | `G`                                        |
| **Buscar um header específico**  | `/^#` (para nível 1) `/^##` (para nível 2) |

### 🔸 **Navegar entre Parágrafos**

| Ação                                    | Comando Vim |
| --------------------------------------- | ----------- |
| **Ir para o próximo parágrafo**         | `}`         |
| **Ir para o parágrafo anterior**        | `{`         |
| **Ir para o início do parágrafo atual** | `(`         |
| **Ir para o final do parágrafo atual**  | `)`         |
[^1]
### 🔹 **Navegar por Palavras, Sentenças e Caracteres**

| Ação                                    | Comando Vim |
| --------------------------------------- | ----------- |
| **Ir para a próxima palavra**           | `w`         |
| **Ir para o início da próxima palavra** | `e`         |
| **Ir para a palavra anterior**          | `b`         |
| **Ir para a próxima sentença**          | `)`         |
| **Ir para a sentença anterior**         | `(`         |

### 🔸 **Navegar entre Listas e Blocos de Texto**

| Ação                                 | Comando Vim |
| ------------------------------------ | ----------- |
| **Ir para o próximo item de lista**  | `]`         |
| **Ir para o item anterior de lista** | `[`         |



## **2. Alteração de Texto**

a## 🔹 **Modo de Inserção e Edição**

| Ação                                 | Comando Vim |
| ------------------------------------ | ----------- |
| **Entrar no modo de inserção**       | `i`         |
| **Entrar no início da linha**        | `I`         |
| **Inserir após o cursor**            | `a`         |
| **Inserir no final da linha**        | `A`         |
| **Deletar o caractere sob o cursor** | `x`         |
| **Deletar uma linha inteira**        | `dd`        |
| **Desfazer**                         | `u`         |
| **Refazer**                          | `Ctrl + r`  |
*1*
---

## **3. Seleção de Texto**

### 🔹 **Modo Visual para Seleção**

|Ação|Comando Vim|
|---|---|
|**Entrar no modo visual**|`v`|
|**Selecionar linha inteira**|`V`|
|**Selecionar bloco**|`Ctrl + v`|
|**Expandir seleção para palavra**|`w`|
|**Selecionar até o final da linha**|`Shift + $`|

### 🔸 **Copiar e Colar**

| Ação                                    | Comando Vim |
| --------------------------------------- | ----------- |
| **Copiar para a área de transferência** | `"+y`       |
| **Colar da área de transferência**      | `"+p`       |

---

## **4. Comandos de Pesquisa e Substituição**

|Ação|Comando Vim|
|---|---|
|**Buscar texto**|`/texto`|
|**Substituir no arquivo**|`:s/palavra1/palavra2/`|
|**Substituir em todo o documento**|`:%s/palavra1/palavra2/g`|

---

## **5. Atalhos de Navegação e Customização no `.obsidian.vimrc`**

Você pode personalizar sua navegação e atalhos no arquivo `.obsidian.vimrc`. Aqui estão alguns exemplos úteis de personalizações:

|Ação|Comando Vim|
|---|---|
|**Ir para o próximo header**|`nmap <C-j> ]]`|
|**Ir para o header anterior**|`nmap <C-k> [[`|
|**Ir para o próximo parágrafo**|`nmap <C-p> }`|
|**Ir para o parágrafo anterior**|`nmap <C-o> {`|
|**Ir para o topo do documento**|`nmap <C-t> gg`|
|**Ir para o final do documento**|`nmap <C-b> G`|
|**Copiar para a área de transferência**|`nmap <C-c> "+y`|
|**Colar da área de transferência**|`nmap <C-v> "+p`|

---

## **6. Sugestões de Personalização**

Além dos atalhos acima, você pode explorar as seguintes personalizações para melhorar ainda mais sua experiência de edição:

|Ação|Comando Vim|
|---|---|
|**Automatizar Tarefas Repetitivas**|Crie snippets de tarefas com macros.|
|**Adicionar Modo de Busca Avançada**|Personalize os atalhos de busca para procurar links ou tags rapidamente.|
|**Adicionar Funções de Formatação**|Crie atalhos para formatar negrito, itálico, listas, etc.|

---

## **Conclusão**

Com esses atalhos e personalizações, você pode navegar, alterar e selecionar texto de forma eficiente em arquivos `.md` no Obsidian usando o Vim. Esses comandos irão acelerar sua produtividade e melhorar sua experiência de edição.

Você pode salvar esse guia como um arquivo `.md` dentro do seu vault do Obsidian para acessá-lo sempre que necessário.

--

Este formato em tabelas facilita a visualização e uso dos comandos para que você possa aplicar de maneira simples e rápida enquanto trabalha no Obsidian com Vim. Se precisar de mais ajustes ou explicações, estarei à disposição! 😊

[^1]: 
