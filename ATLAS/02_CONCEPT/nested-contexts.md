---
tags:
  - learning
HUB:
  - "[[hub-python]]"
created: "[[2024-02-23]]"
---
2024-02-23  11:15



```python
def copy(src, dst):
    """Copy the contents of one file to another

    Args:
        src (str): File name of the file to be copied
        dst (str): Where to write the new file
    """
    # Abrir ambos os arquivos
    with open(src, 'r') as f_src:  # Modificado para 'r' para leitura
        with open(dst, 'w') as f_dst:  # Modificado para 'w' para escrita
            # Ler e escrever
            for line in f_src:
                f_dst.write(line)

```

Handling errors

```python
try:
except:
finally:
```