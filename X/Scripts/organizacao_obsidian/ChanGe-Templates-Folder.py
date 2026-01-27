import json
import os

file_path = r"/home/nonaka/Documentos/Obsidian-Vault/.obsidian/plugins/templater-obsidian/data.json"

# Lista de possíveis valores
valores = ["X/Templates", "X/Templates/Snippet"]

if not os.path.exists(file_path):
    print("Arquivo não encontrado.")
    exit()

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

atual = data.get("templates_folder", "")

if atual in valores:
    proximo_indice = (valores.index(atual) + 1) % len(valores)
    data["templates_folder"] = valores[proximo_indice]
else:
    print(f"Valor inesperado: '{atual}'. Definindo primeiro valor como padrão.")
    data["templates_folder"] = valores[0]

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print(f'"Template Folder updated to: {data["templates_folder"]} ✅')

