---
tags:
  - component
HUB:
  - "[[hub-pkm]]"
  - "[[hub-jupyterNotebook]]"
---


# Requirements -  EditNotes

		

```python
import os
```

## Remover algum texto específico de **TODAS** as notas de uma pasta


```python
# Remover um texto específico de arquivos Markdown
def remove_text_from_markdown(directory, target_text):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                updated_content = content.replace(target_text, '')
                if content != updated_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f"Updated: {file_path}")

directory_to_scan = r"C:\Users\nonak\OneDrive\Área de Trabalho\ObsidianNotesF\DailyNotes"
target_text_to_remove = "[[!_atlas_math_statistics]]"

# remove_text_from_markdown(directory_to_scan, target_text_to_remove)
```

## Reescrever as propriedades de **TODAS** as notas de uma pasta


```python
# Remover e refazer cabeçalho em arquivos Markdown
def clean_and_update_markdown_notes(directory, new_header):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                if content.startswith("---"):
                    end_of_header = content.find("---", 3)
                    if end_of_header != -1:
                        content = content[end_of_header + 3:].lstrip()

                updated_content = new_header + "\n" + content

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"Updated: {file_path}")

directory_to_scan = r"C:\Users\nonak\OneDrive\Área de Trabalho\ObsidianNotesF\Assets\FirstVault\marketing"
new_header = """---
tags:
  - lab
HUB:
  - "[[hub-mkt]]"
---"""

# clean_and_update_markdown_notes(directory_to_scan, new_header)
```
