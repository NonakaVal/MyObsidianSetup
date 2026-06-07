import os
import re

# =============================================================
#  CONFIGURAÇÃO — ajuste o caminho do seu vault
# =============================================================
CSS_PATH = os.path.join(
    os.path.expanduser("~"),
    "Documentos", "Notes", ".obsidian", "snippets", "ux-focus.css"
)

MODES = ["ALL", "G1", "G2", "G3", "ZALL"]

# Output visual para a status bar
# ● = ativo   ○ = inativo
LABELS = {
    "ALL":  "●●●●",
    "G1":   "●○○○",
    "G2":   "○●○○",
    "G3":   "○○●○",
    "ZALL": "○○○○",
}

HIDE = {
    "ALL": [],
    "G1":  ["Calendar & Review",
            "Index & Bases","Knowlegde",
            "Memos",
            "V-01-Ideia",
            "V-02-Inspiracoes",
            "V-03-Roteiro","V-04-Edicao",
            "V-05-Review","Write"],

    "G2":  ["00 Code","01 Snippets","03 Config","04 Workflow","05 Toolbox",
            "06 Work","07 AI","08 Focus Areas","TaskNotes","V-01-Ideia","V-02-Inspiracoes",
            "V-03-Roteiro","V-04-Edicao","V-05-Review","Write"],

    "G3":  ["00 Code","01 Snippets","03 Config","04 Workflow","05 Toolbox",
            "06 Work","07 AI","08 Focus Areas","Calendar & Review",
            "Index & Bases","Knowlegde","Memos"],

    "ZALL": [],
}

# =============================================================
if not os.path.exists(CSS_PATH):
    print(f"arquivo não encontrado:\n  {CSS_PATH}")
    exit(1)

content = open(CSS_PATH, encoding="utf-8").read()

m = re.search(r"/\* FOCUS-MODE: (\w+) \*/", content)
current = m.group(1) if (m and m.group(1) in MODES) else "ALL"
next_mode = MODES[(MODES.index(current) + 1) % len(MODES)]

# --- bloco principal FOCUS-HIDE (pastas ocultas por modo) ---
def make_hide_block(mode):
    paths = HIDE[mode]
    if not paths:
        return "/* FOCUS-HIDE: none *//* FOCUS-HIDE-END */"
    sel = ",\n".join(f'div[data-path="{p}"]' for p in paths)
    return f"/* FOCUS-HIDE: {mode} */\n{sel} {{ display: none !important; }}\n/* FOCUS-HIDE-END */"

# --- bloco FOCUS-ZALL: override das pastas z- quando modo é ZALL ---
# Fica APÓS o seletor estático no CSS, então vence na cascata
def make_zall_block(mode):
    if mode == "ZALL":
        return '/* FOCUS-ZALL-START */\ndiv[data-path^="z-"] { display: flex !important; }\n/* FOCUS-ZALL-END */'
    return "/* FOCUS-ZALL-START *//* FOCUS-ZALL-END */"

content = re.sub(r"/\* FOCUS-MODE: \w+ \*/", f"/* FOCUS-MODE: {next_mode} */", content)
content = re.sub(
    r"/\* FOCUS-HIDE:.*?FOCUS-HIDE-END \*/",
    make_hide_block(next_mode),
    content,
    flags=re.DOTALL,
)
content = re.sub(
    r"/\* FOCUS-ZALL-START \*/.*?/\* FOCUS-ZALL-END \*/",
    make_zall_block(next_mode),
    content,
    flags=re.DOTALL,
)

open(CSS_PATH, "w", encoding="utf-8").write(content)
print(LABELS[next_mode])

