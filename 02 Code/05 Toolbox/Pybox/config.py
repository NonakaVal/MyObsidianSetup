from pathlib import Path

PYBOX_ROOT = Path(__file__).resolve().parent
MODULES_DIR = PYBOX_ROOT / "modules"

MODULES = {
    "audio": {
        "label": "Audio Tools",
        "path": MODULES_DIR / "audio",
    },
    "file": {
        "label": "File Tools",
        "path": MODULES_DIR / "file_tools",
    },
    "gallery": {
        "label": "Gallery Tools",
        "path": MODULES_DIR / "gallery_tools",
    },
    "index": {
        "label": "Index Notes",
        "path": MODULES_DIR / "index_notes",
    },
    "manga": {
        "label": "Manga Reader",
        "path": MODULES_DIR / "manga_reader",
    },
    "obsidian": {
        "label": "Obsidian Tools",
        "path": MODULES_DIR / "obsidian_tools",
    },
    "shell": {
        "label": "Shell Tools",
        "path": MODULES_DIR / "shell_tools",
    },
}