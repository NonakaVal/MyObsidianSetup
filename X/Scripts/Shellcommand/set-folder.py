import json
import os

from config import data_json_path

# Lista de possíveis valores
valores = ["X/Templates", "X/Templates/Snippet"]

if not os.path.exists(data_json_path):
    print("Arquivo não encontrado.")
    exit()

with open(data_json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

atual = data.get("templates_folder", "")

if atual in valores:
    proximo_indice = (valores.index(atual) + 1) % len(valores)
    data["templates_folder"] = valores[proximo_indice]
else:
    print(f"Valor inesperado: '{atual}'. Definindo primeiro valor como padrão.")
    data["templates_folder"] = valores[0]

with open(data_json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print(f'">_ {data["templates_folder"]} ✅')

