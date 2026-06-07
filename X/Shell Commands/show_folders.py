import os

css_path = "/home/val/Documentos/Notes/.obsidian/snippets/ux-customize.css"

if not os.path.exists(css_path):
    print("Arquivo não encontrado.")
    exit()

with open(css_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

if not lines:
    print("Arquivo vazio.")
    exit()

primeira = lines[0].rstrip()

if primeira.endswith("*/"):
    # Ativo → desativar: remover ' */' do final da primeira linha
    lines[0] = primeira[:-2].rstrip() + "\n"
    status = "DESATIVADO ❌"
else:
    # Inativo → ativar: adicionar ' */' no final da primeira linha
    lines[0] = primeira + " */\n"
    status = "ATIVADO ✅"

with open(css_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f">_ ux-customize.css {status}")

