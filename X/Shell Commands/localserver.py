import os
import re
import io
import time
import shutil
import zipfile
import socket
import mimetypes
from pathlib import Path
from urllib.parse import quote
import atexit
import signal

from flask import (
    Flask, request, render_template_string, jsonify,
    send_file, abort, Response
)

APP_TITLE = "Windows7 Storage"
HOST = "0.0.0.0"
PORT = 5000
PID_FILE = Path("/tmp/local-storage.pid")

HOME = Path.home().resolve()

BASE_DIR = Path(
    os.environ.get(
        "HOMELAB_BASE_DIR",
        str(HOME)
    )
).resolve()

BROWSABLE_ROOTS = {
    "home": HOME,
    "videos": (HOME / "Vídeos").resolve(),
    "music": (HOME / "Músicas").resolve(),
    "templates": (HOME / "Modelos").resolve(),
    "images": (HOME / "Imagens").resolve(),
    "downloads": (HOME / "Downloads").resolve(),
    "documents": (HOME / "Documentos").resolve(),
    "desktop": (HOME / "Área de trabalho").resolve(),
    "appimages": (HOME / "AppImages").resolve(),
}

MAX_PREVIEW_TEXT = 1024 * 1024 * 2  # 2 MB
app = Flask(__name__)
BASE_DIR.mkdir(parents=True, exist_ok=True)


def available_roots():
    roots = {}
    for key, path in BROWSABLE_ROOTS.items():
        try:
            if path.exists():
                roots[key] = path.resolve()
        except Exception:
            pass
    return roots


def safe_name(name: str) -> str:
    name = (name or "").strip().replace("\\", "/").split("/")[-1]
    name = re.sub(r"[\x00-\x1f]", "", name)
    name = re.sub(r"[<>:\"|?*]", "_", name)
    name = name.strip(" .")
    return name or f"item_{int(time.time())}"


def safe_rel_path(rel: str) -> str:
    rel = (rel or "").strip().replace("\\", "/").strip("/")
    parts = [safe_name(p) for p in rel.split("/") if p not in ("", ".", "..")]
    return "/".join(parts)


def is_subpath(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except Exception:
        return False


def get_root_and_rel():
    root_key = request.args.get("root", "home")
    rel = safe_rel_path(request.args.get("path", ""))
    roots = available_roots()
    root = roots.get(root_key)
    if not root:
        abort(404, "Raiz inválida")
    return root_key, root, rel


def resolve_path(root: Path, rel: str) -> Path:
    target = (root / safe_rel_path(rel)).resolve()
    if not is_subpath(target, root):
        abort(400, "Caminho inválido")
    return target


def resolve_child(root: Path, rel: str, name: str) -> Path:
    current = resolve_path(root, rel)
    target = (current / safe_name(name)).resolve()
    if not is_subpath(target, root):
        abort(400, "Caminho inválido")
    return target


def ensure_unique_path(dest: Path) -> Path:
    if not dest.exists():
        return dest
    stem = dest.stem
    suffix = dest.suffix
    parent = dest.parent
    i = 1
    while True:
        cand = parent / f"{stem}_{i}{suffix}"
        if not cand.exists():
            return cand
        i += 1


def human_size(n: int) -> str:
    n = float(n)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} PB"


def file_icon(name: str, is_dir=False):
    if is_dir:
        return "📁"
    ext = Path(name).suffix.lower()
    icons = {
        ".pdf": "📄", ".txt": "📝", ".md": "📝",
        ".jpg": "🖼", ".jpeg": "🖼", ".png": "🖼", ".gif": "🖼", ".webp": "🖼", ".svg": "🖼", ".bmp": "🖼",
        ".mp4": "🎬", ".mov": "🎬", ".avi": "🎬", ".mkv": "🎬", ".webm": "🎬",
        ".mp3": "🎵", ".wav": "🎵", ".ogg": "🎵", ".flac": "🎵", ".aac": "🎵", ".m4a": "🎵",
        ".zip": "🗜", ".tar": "🗜", ".gz": "🗜", ".rar": "🗜", ".7z": "🗜",
        ".py": "🐍", ".js": "⚡", ".ts": "⚡", ".html": "🌐", ".css": "🎨", ".json": "📦",
        ".xml": "📦", ".csv": "📊", ".xlsx": "📊", ".xls": "📊", ".docx": "📃", ".doc": "📃",
        ".pptx": "📊", ".ppt": "📊", ".sh": "⚙️", ".apk": "📱",
    }
    return icons.get(ext, "📄")


def file_type_group(name: str, is_dir=False):
    if is_dir:
        return "dir"
    ext = Path(name).suffix.lower()
    if ext in {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp"}:
        return "image"
    if ext in {".mp4", ".mov", ".avi", ".mkv", ".webm"}:
        return "video"
    if ext in {".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a"}:
        return "audio"
    if ext in {".txt", ".py", ".js", ".ts", ".css", ".json", ".xml", ".csv", ".sh", ".log", ".yaml", ".yml"}:
        return "text"
    if ext == ".md":
        return "markdown"
    if ext == ".html" or ext == ".htm":
        return "html"
    if ext in {".zip", ".tar", ".gz", ".rar", ".7z"}:
        return "zip"
    return "file"


def can_preview(path: Path, kind: str):
    if path.is_dir():
        return False
    return kind in {"image", "video", "audio", "text", "markdown", "html"}


def list_items(root: Path, rel: str):
    current = resolve_path(root, rel)
    if not current.exists() and root == BASE_DIR:
        current.mkdir(parents=True, exist_ok=True)
    elif not current.exists():
        abort(404, "Pasta não encontrada")

    items = []
    for p in sorted(current.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower())):
        try:
            stat = p.stat()
            is_dir = p.is_dir()
            size_bytes = 0 if is_dir else stat.st_size
            kind = file_type_group(p.name, is_dir)
            items.append({
                "name": p.name,
                "is_dir": is_dir,
                "type": kind,
                "icon": file_icon(p.name, is_dir),
                "size_bytes": size_bytes,
                "size": "—" if is_dir else human_size(size_bytes),
                "mtime": int(stat.st_mtime),
                "preview": can_preview(p, kind),
            })
        except Exception:
            pass
    return items


def breadcrumbs(rel: str):
    crumbs = [{"name": "Início", "path": ""}]
    if not rel:
        return crumbs
    acc = []
    for part in [p for p in rel.split("/") if p]:
        acc.append(part)
        crumbs.append({"name": part, "path": "/".join(acc)})
    return crumbs


def storage_info(path: Path):
    try:
        usage = shutil.disk_usage(path)
        return {
            "total_bytes": usage.total,
            "used_bytes": usage.used,
            "free_bytes": usage.free,
            "total": human_size(usage.total),
            "used": human_size(usage.used),
            "free": human_size(usage.free),
            "pct_used": round((usage.used / usage.total) * 100, 1) if usage.total else 0,
        }
    except Exception:
        return {
            "total_bytes": 0, "used_bytes": 0, "free_bytes": 0,
            "total": "—", "used": "—", "free": "—", "pct_used": 0,
        }

def write_pid():
    PID_FILE.write_text(str(os.getpid()), encoding="utf-8")

def remove_pid():
    try:
        if PID_FILE.exists():
            PID_FILE.unlink()
    except Exception:
        pass

def handle_exit(*_):
    remove_pid()
    raise SystemExit


HTML = r"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>Windows7 Storage</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
:root {
  --bg: #0f1117;
  --surface: #181b23;
  --surface2: #1e2230;
  --surface3: #252a3a;
  --border: #2a3045;
  --border2: #353d55;
  --text: #e2e8f0;
  --text2: #94a3b8;
  --text3: #64748b;
  --accent: #4ade80;
  --accent-dim: #22c55e33;
  --accent2: #38bdf8;
  --danger: #f87171;
  --warn: #fbbf24;
  --mono: 'IBM Plex Mono', monospace;
  --sans: 'IBM Plex Sans', sans-serif;
  --radius: 6px;
}
html, body { background: var(--bg); color: var(--text); font-family: var(--sans); height: 100%; overflow: hidden; font-size: 13px; }
.app { display: flex; flex-direction: column; height: 100vh; overflow: hidden; }

/* HEADER */
.header {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 0 16px;
  display: flex; align-items: center; gap: 12px;
  height: 48px; flex-shrink: 0;
}
.menu-btn { background: none; border: none; color: var(--text2); cursor: pointer; padding: 6px; border-radius: 4px; font-size: 16px; }
.menu-btn:hover { background: var(--surface2); color: var(--text); }
.logo { font-family: var(--mono); font-size: 14px; color: var(--accent); letter-spacing: -0.5px; }
.logo span { color: var(--text3); }
.spacer { flex: 1; }
.header-btn { background: none; border: 1px solid var(--border); color: var(--text2); cursor: pointer; padding: 5px 10px; border-radius: var(--radius); font-size: 12px; font-family: var(--mono); }
.header-btn:hover { background: var(--surface2); color: var(--text); border-color: var(--border2); }

/* LAYOUT */
.main-container { display: flex; flex: 1; overflow: hidden; position: relative; }
.sidebar { width: 300px; background: var(--surface); border-right: 1px solid var(--border); display: flex; flex-direction: column; overflow-y: auto; flex-shrink: 0; transition: transform 0.2s ease, width 0.2s ease; }
.sidebar.closed { width: 0; overflow: hidden; transform: translateX(-100%); position: absolute; height: 100%; z-index: 10; }
.content { flex: 1; display: flex; flex-direction: column; overflow: hidden; min-width: 0; }

/* SIDEBAR */
.sidebar-section { padding: 14px; border-bottom: 1px solid var(--border); }
.sidebar-label { font-family: var(--mono); font-size: 10px; color: var(--text3); letter-spacing: 1px; text-transform: uppercase; margin-bottom: 10px; }
.root-item { display: flex; align-items: center; gap: 10px; padding: 7px 10px; border-radius: var(--radius); cursor: pointer; color: var(--text2); transition: all 0.1s; }
.root-item:hover { background: var(--surface2); color: var(--text); }
.root-item.active { background: var(--accent-dim); color: var(--accent); }
.root-icon { font-size: 16px; line-height: 1; }
.root-name { font-family: var(--mono); font-size: 12px; }

/* STORAGE BAR */
.storage-card { background: var(--surface2); border-radius: var(--radius); padding: 12px; border: 1px solid var(--border); }
.storage-row { display: flex; justify-content: space-between; font-family: var(--mono); font-size: 11px; color: var(--text2); margin-bottom: 8px; }
.storage-row span:last-child { color: var(--text3); }
.bar-track { height: 3px; background: var(--surface3); border-radius: 2px; overflow: hidden; margin-bottom: 6px; }
.bar-fill { height: 100%; background: var(--accent); border-radius: 2px; width: 0; transition: width 0.3s; }
.storage-sub { font-family: var(--mono); font-size: 10px; color: var(--text3); }

/* UPLOAD */
.drop-zone { border: 1px dashed var(--border2); border-radius: var(--radius); padding: 14px; text-align: center; cursor: pointer; color: var(--text3); transition: all 0.15s; margin-bottom: 10px; }
.drop-zone:hover, .drop-zone.drag { background: var(--accent-dim); border-color: var(--accent); color: var(--accent); }
.drop-title { font-size: 13px; margin-bottom: 4px; }
.drop-sub { font-size: 11px; }
.row-btns { display: flex; gap: 6px; margin-bottom: 8px; }
.sb-input { width: 100%; padding: 7px 10px; background: var(--surface2); border: 1px solid var(--border); color: var(--text); border-radius: var(--radius); font-size: 12px; font-family: var(--mono); margin-bottom: 8px; }
.sb-input:focus { outline: none; border-color: var(--accent); }
.sb-textarea { width: 100%; padding: 8px 10px; background: var(--surface2); border: 1px solid var(--border); color: var(--text); border-radius: var(--radius); font-size: 12px; font-family: var(--mono); resize: vertical; min-height: 72px; margin-bottom: 8px; }
.sb-textarea:focus { outline: none; border-color: var(--accent); }
.sb-btn { display: block; width: 100%; padding: 7px 12px; background: var(--surface2); border: 1px solid var(--border); color: var(--text2); border-radius: var(--radius); cursor: pointer; font-size: 12px; font-family: var(--mono); text-align: center; text-decoration: none; margin-bottom: 6px; transition: all 0.1s; }
.sb-btn:hover { background: var(--surface3); color: var(--text); border-color: var(--border2); }
.sb-btn.primary { background: var(--accent); color: #000; border-color: var(--accent); font-weight: 600; }
.sb-btn.primary:hover { opacity: 0.85; }
.sb-btn.danger { background: var(--danger); color: #fff; border-color: var(--danger); }
.sb-btn.half { flex: 1; margin-bottom: 0; }
.file-label { font-size: 11px; color: var(--text3); font-family: var(--mono); margin-bottom: 8px; min-height: 16px; }

/* TOOLBAR */
.toolbar { padding: 10px 14px; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 10px; background: var(--surface); flex-shrink: 0; flex-wrap: wrap; }
.breadcrumbs { display: flex; align-items: center; gap: 2px; flex: 1; overflow-x: auto; min-width: 0; }
.crumb { padding: 4px 6px; cursor: pointer; color: var(--text3); white-space: nowrap; border-radius: 4px; font-family: var(--mono); font-size: 12px; transition: color 0.1s; }
.crumb:hover { color: var(--accent); }
.crumb.cur { color: var(--text); }
.sep { color: var(--border2); font-size: 14px; }
.tb-actions { display: flex; gap: 6px; align-items: center; flex-shrink: 0; }
.tb-btn { background: none; border: 1px solid transparent; padding: 5px 8px; cursor: pointer; color: var(--text2); border-radius: var(--radius); font-size: 12px; font-family: var(--mono); transition: all 0.1s; white-space: nowrap; }
.tb-btn:hover { background: var(--surface2); color: var(--text); border-color: var(--border); }
.tb-btn.active { background: var(--accent-dim); color: var(--accent); border-color: var(--accent); }
.search-wrap { display: flex; align-items: center; gap: 6px; background: var(--surface2); border: 1px solid var(--border); border-radius: var(--radius); padding: 0 8px; }
.search-wrap:focus-within { border-color: var(--accent); }
.search-wrap input { background: none; border: none; padding: 6px 0; color: var(--text); font-family: var(--mono); font-size: 12px; width: 140px; }
.search-wrap input:focus { outline: none; }
.search-wrap input::placeholder { color: var(--text3); }
.sort-sel { background: var(--surface2); border: 1px solid var(--border); color: var(--text2); padding: 5px 8px; border-radius: var(--radius); font-family: var(--mono); font-size: 12px; cursor: pointer; }
.sort-sel:focus { outline: none; border-color: var(--accent); }

/* SELECTION BAR */
.sel-bar { display: none; padding: 8px 14px; background: var(--accent-dim); border-bottom: 1px solid var(--accent); align-items: center; gap: 10px; flex-shrink: 0; }
.sel-bar.show { display: flex; }
.sel-count { font-family: var(--mono); font-size: 12px; color: var(--accent); flex: 1; }
.sel-btn { padding: 5px 12px; border-radius: var(--radius); border: none; cursor: pointer; font-family: var(--mono); font-size: 12px; font-weight: 500; transition: all 0.1s; }
.sel-btn.dl { background: var(--accent); color: #000; }
.sel-btn.dl:hover { opacity: 0.8; }
.sel-btn.del { background: var(--danger); color: #fff; }
.sel-btn.del:hover { opacity: 0.8; }
.sel-btn.clr { background: var(--surface3); color: var(--text2); border: 1px solid var(--border2); }
.sel-btn.clr:hover { color: var(--text); }

/* FILE GRID */
.file-grid { flex: 1; overflow-y: auto; padding: 14px; }
.grid-view { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 8px; }
.grid-item { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 14px 10px 10px; cursor: pointer; transition: all 0.1s; text-align: center; position: relative; user-select: none; }
.grid-item:hover { background: var(--surface2); border-color: var(--border2); }
.grid-item.selected { background: var(--accent-dim); border-color: var(--accent); }
.grid-icon { font-size: 40px; margin-bottom: 8px; line-height: 1; }
.grid-name { font-size: 12px; word-break: break-word; color: var(--text); margin-bottom: 3px; font-family: var(--mono); }
.grid-meta { font-size: 10px; color: var(--text3); font-family: var(--mono); }
.item-check { position: absolute; top: 6px; left: 6px; width: 16px; height: 16px; border-radius: 3px; border: 1.5px solid var(--border2); background: var(--surface2); display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.1s; pointer-events: none; }
.grid-item:hover .item-check, .grid-item.selected .item-check { opacity: 1; }
.grid-item.selected .item-check { background: var(--accent); border-color: var(--accent); color: #000; }
.item-check::after { content: '✓'; font-size: 10px; font-weight: 700; }

/* LIST VIEW */
.list-view { width: 100%; border-collapse: collapse; }
.list-view th { text-align: left; padding: 10px 8px; border-bottom: 1px solid var(--border); color: var(--text3); font-weight: 500; font-family: var(--mono); font-size: 11px; letter-spacing: 0.5px; position: sticky; top: 0; background: var(--bg); z-index: 1; }
.list-view td { padding: 10px 8px; border-bottom: 1px solid var(--border); }
.list-view tr.list-row:hover { background: var(--surface2); }
.list-view tr.list-row.selected { background: var(--accent-dim); }
.list-row td:first-child { padding-left: 4px; }
.list-check { width: 16px; height: 16px; border-radius: 3px; border: 1.5px solid var(--border2); background: var(--surface2); display: inline-flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0; }
.list-row.selected .list-check, .list-check.checked { background: var(--accent); border-color: var(--accent); color: #000; }
.list-check.checked::after { content: '✓'; font-size: 9px; font-weight: 700; }
.list-name-cell { display: flex; align-items: center; gap: 10px; cursor: pointer; }
.list-icon { font-size: 18px; line-height: 1; }
.list-name { font-family: var(--mono); font-size: 12px; }
.list-size, .list-date { font-family: var(--mono); font-size: 11px; color: var(--text3); white-space: nowrap; }
.open-btn { padding: 3px 8px; background: none; border: 1px solid var(--border); border-radius: 4px; color: var(--text2); cursor: pointer; font-family: var(--mono); font-size: 11px; }
.open-btn:hover { background: var(--surface2); color: var(--text); }

/* EMPTY STATE */
.empty-state { text-align: center; padding: 60px 20px; color: var(--text3); font-family: var(--mono); }
.empty-icon { font-size: 40px; margin-bottom: 12px; }
.empty-text { font-size: 13px; }

/* MODAL */
.modal { position: fixed; inset: 0; background: rgba(0,0,0,0.85); display: none; align-items: center; justify-content: center; z-index: 1000; padding: 20px; }
.modal.open { display: flex; }
.modal-inner { background: var(--surface); border: 1px solid var(--border2); border-radius: 10px; width: 100%; max-width: 900px; max-height: 90vh; display: flex; flex-direction: column; overflow: hidden; }
.modal-head { padding: 12px 16px; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 10px; flex-shrink: 0; }
.modal-fname { flex: 1; font-family: var(--mono); font-size: 13px; color: var(--text); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.modal-type-badge { font-family: var(--mono); font-size: 10px; padding: 2px 7px; border-radius: 3px; background: var(--surface2); color: var(--text3); border: 1px solid var(--border); }
.modal-actions { display: flex; gap: 6px; }
.m-btn { padding: 5px 12px; border-radius: var(--radius); border: 1px solid var(--border); background: var(--surface2); color: var(--text2); cursor: pointer; font-family: var(--mono); font-size: 12px; text-decoration: none; transition: all 0.1s; }
.m-btn:hover { background: var(--surface3); color: var(--text); }
.m-btn.open-tab { background: var(--accent-dim); border-color: var(--accent); color: var(--accent); }
.modal-body { flex: 1; overflow: auto; position: relative; }
.modal-body img { max-width: 100%; height: auto; display: block; margin: auto; padding: 16px; }
.modal-body video, .modal-body audio { width: 100%; display: block; margin: auto; padding: 16px; }
.modal-body audio { margin-top: 40px; }
.modal-body pre { font-family: var(--mono); font-size: 12px; white-space: pre-wrap; word-break: break-word; padding: 16px; line-height: 1.6; color: var(--text2); }
.modal-body .md-render { padding: 24px; line-height: 1.7; max-width: 760px; margin: auto; }
.modal-body .md-render h1, .md-render h2, .md-render h3 { color: var(--text); margin: 1.2em 0 0.5em; font-family: var(--sans); }
.modal-body .md-render h1 { font-size: 22px; border-bottom: 1px solid var(--border); padding-bottom: 8px; }
.modal-body .md-render h2 { font-size: 17px; }
.modal-body .md-render h3 { font-size: 15px; }
.modal-body .md-render p { color: var(--text2); margin-bottom: 1em; }
.modal-body .md-render code { font-family: var(--mono); background: var(--surface2); padding: 2px 6px; border-radius: 3px; font-size: 11px; color: var(--accent); }
.modal-body .md-render pre { background: var(--surface2); padding: 14px; border-radius: var(--radius); border: 1px solid var(--border); margin-bottom: 1em; overflow-x: auto; }
.modal-body .md-render pre code { background: none; padding: 0; color: var(--text2); }
.modal-body .md-render a { color: var(--accent2); }
.modal-body .md-render blockquote { border-left: 3px solid var(--accent); padding-left: 14px; margin: 1em 0; color: var(--text3); font-style: italic; }
.modal-body .md-render ul, .md-render ol { padding-left: 1.4em; color: var(--text2); margin-bottom: 1em; }
.modal-body .md-render li { margin-bottom: 0.25em; }
.modal-body .md-render table { width: 100%; border-collapse: collapse; margin-bottom: 1em; }
.modal-body .md-render th { background: var(--surface2); padding: 8px 12px; border: 1px solid var(--border); font-size: 12px; }
.modal-body .md-render td { padding: 8px 12px; border: 1px solid var(--border); font-size: 12px; color: var(--text2); }
.html-frame { width: 100%; height: 100%; min-height: 400px; border: none; background: white; }

/* TOAST */
.toast { position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%) translateY(80px); background: var(--surface); border: 1px solid var(--border2); padding: 8px 18px; border-radius: 20px; font-family: var(--mono); font-size: 12px; color: var(--text); z-index: 2000; transition: transform 0.2s ease; white-space: nowrap; }
.toast.show { transform: translateX(-50%) translateY(0); }

/* SCROLLBARS */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--surface3); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--border2); }

/* UPLOAD PROGRESS */
.upload-prog { height: 3px; background: var(--border); border-radius: 2px; overflow: hidden; margin-bottom: 8px; }
.upload-prog-fill { height: 100%; background: var(--accent); width: 0; transition: width 0.1s; }

@media (max-width: 768px) {
  .sidebar { position: absolute; height: 100%; transform: translateX(-100%); z-index: 10; }
  .sidebar.open-mobile { transform: translateX(0); }
  .sidebar.closed { transform: translateX(-100%); width: 300px; }
  .grid-view { grid-template-columns: repeat(auto-fill, minmax(110px, 1fr)); }
  .search-wrap { order: 1; flex: 1; }
  .search-wrap input { width: 100%; }
  .list-date { display: none; }
}
</style>
</head>
<body>
<div class="app">
  <header class="header">
    <button class="menu-btn" onclick="toggleSidebar()" title="Menu">☰</button>
    <div class="logo">Local<span>/</span>Storage Host</div>
    <div class="spacer"></div>
    <button class="header-btn" onclick="refreshAll()">↻ atualizar</button>
    <button class="header-btn" onclick="copyCurrentUrl()">🔗 link</button>
  </header>

  <div class="main-container">
    <!-- SIDEBAR -->
    <div class="sidebar" id="sidebar">
      <div class="sidebar-section">
        <div class="sidebar-label">locais</div>
        <div id="root-buttons"></div>
      </div>
      <div class="sidebar-section">
        <div class="sidebar-label">armazenamento</div>
        <div class="storage-card">
          <div class="storage-row">
            <span>livre <strong id="free-space" style="color:var(--accent)">—</strong></span>
            <span>total <strong id="total-space">—</strong></span>
          </div>
          <div class="bar-track"><div class="bar-fill" id="usage-bar"></div></div>
          <div class="storage-sub" id="storage-detail">—</div>
        </div>
      </div>
      <div class="sidebar-section">
        <div class="sidebar-label">enviar</div>
        <div class="drop-zone" id="drop-zone">
          <div class="drop-title">📂 arrastar aqui</div>
          <div class="drop-sub">arquivos e pastas inteiras</div>
        </div>
        <input id="file-input" type="file" multiple style="display:none">
        <input id="folder-input" type="file" webkitdirectory directory multiple style="display:none">
        <div class="row-btns">
          <button class="sb-btn half" onclick="pickFiles()">📄 arquivos</button>
          <button class="sb-btn half" onclick="pickFolder()">📁 pasta</button>
        </div>
        <input class="sb-input" type="text" id="target-subdir" placeholder="subpasta destino (opcional)">
        <div class="file-label" id="selected-files">nenhum arquivo selecionado</div>
        <div class="upload-prog"><div class="upload-prog-fill" id="upload-bar"></div></div>
        <button class="sb-btn primary" onclick="uploadSelected()">⬆ enviar agora</button>
      </div>
      <div class="sidebar-section">
        <div class="sidebar-label">criar texto</div>
        <input class="sb-input" type="text" id="quick-name" placeholder="nome.txt / nota.md">
        <textarea class="sb-textarea" id="quick-text" placeholder="Conteúdo do arquivo..."></textarea>
        <button class="sb-btn" onclick="saveTextFile()">📝 salvar arquivo</button>
      </div>
      <div class="sidebar-section">
        <div class="sidebar-label">ações</div>
        <button class="sb-btn" onclick="createFolder()">📁 nova pasta</button>
        <button class="sb-btn" onclick="downloadCurrentAsZip()">🗜 baixar pasta como ZIP</button>
      </div>
    </div>

    <!-- CONTENT -->
    <div class="content">
      <!-- TOOLBAR -->
      <div class="toolbar">
        <div class="breadcrumbs" id="crumbs"></div>
        <div class="tb-actions">
          <div class="search-wrap">
            <span style="color:var(--text3)">🔍</span>
            <input type="search" id="search" placeholder="buscar..." oninput="renderItems()">
          </div>
          <select class="sort-sel" id="sort" onchange="renderItems()">
            <option value="dirs_first">nome</option>
            <option value="newest">recente</option>
            <option value="size_desc">tamanho</option>
          </select>
          <button class="tb-btn" id="btn-grid" onclick="setView('grid')" title="Grade">⊞</button>
          <button class="tb-btn" id="btn-list" onclick="setView('list')" title="Lista">≡</button>
        </div>
      </div>

      <!-- SELECTION BAR -->
      <div class="sel-bar" id="sel-bar">
        <span class="sel-count" id="sel-count">0 selecionados</span>
        <button class="sel-btn dl" onclick="downloadSelected()">↓ baixar</button>
        <button class="sel-btn del" id="sel-del-btn" onclick="deleteSelected()">🗑 excluir</button>
        <button class="sel-btn clr" onclick="clearSelection()">✕ limpar</button>
      </div>

      <div class="file-grid" id="file-grid"></div>
    </div>
  </div>
</div>

<!-- TOAST -->
<div class="toast" id="toast"></div>

<!-- MODAL -->
<div class="modal" id="modal" onclick="closeModalOutside(event)">
  <div class="modal-inner">
    <div class="modal-head">
      <span id="modal-icon" style="font-size:20px"></span>
      <div class="modal-fname" id="modal-title">—</div>
      <span class="modal-type-badge" id="modal-badge">—</span>
      <div class="modal-actions">
        <a class="m-btn open-tab" id="modal-newtab" href="#" target="_blank" rel="noopener">↗ abrir</a>
        <a class="m-btn" id="modal-download" href="#" download>↓ baixar</a>
        <button class="m-btn" onclick="closeModal()">✕</button>
      </div>
    </div>
    <div class="modal-body" id="modal-body"></div>
  </div>
</div>

<script>
// ── STATE ──────────────────────────────────────────────────────────────────
let state = { root: 'home', path: '', items: [], view: localStorage.getItem('hlab-view') || 'grid' };
let selected = new Set();
let queued = [];

// ── UTILS ──────────────────────────────────────────────────────────────────
const qs = o => new URLSearchParams(o).toString();
const esc = s => String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const fmtDate = ts => new Date(ts * 1000).toLocaleString('pt-BR', { dateStyle: 'short', timeStyle: 'short' });
const itemQS = name => qs({ root: state.root, path: state.path, name });

function toast(msg, dur = 2500) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(t._h);
  t._h = setTimeout(() => t.classList.remove('show'), dur);
}

async function api(path, opts = {}) {
  const r = await fetch(path, opts);
  const j = await r.json().catch(() => ({ ok: false, error: 'Erro' }));
  if (!r.ok || j.ok === false) throw new Error(j.error || 'Erro');
  return j;
}

// ── SIDEBAR ────────────────────────────────────────────────────────────────
function toggleSidebar() {
  const sb = document.getElementById('sidebar');
  if (window.innerWidth <= 768) sb.classList.toggle('open-mobile');
  else sb.classList.toggle('closed');
}

// ── VIEW ───────────────────────────────────────────────────────────────────
function setView(v) {
  state.view = v;
  localStorage.setItem('hlab-view', v);
  document.getElementById('btn-grid').classList.toggle('active', v === 'grid');
  document.getElementById('btn-list').classList.toggle('active', v === 'list');
  renderItems();
}

// ── REFRESH ────────────────────────────────────────────────────────────────
async function refreshAll() {
  try {
    await Promise.all([loadRoots(), loadStorage(), loadItems()]);
    clearSelection();
  } catch (e) { toast(e.message || 'Erro ao carregar'); }
}

// ── ROOTS ──────────────────────────────────────────────────────────────────
async function loadRoots() {
  const data = await api('/api/roots');
  const icons = {
    home: '🏠',
    videos: '🎬',
    music: '🎵',
    templates: '📐',
    images: '🖼',
    downloads: '⬇',
    documents: '📃',
    desktop: '🖥',
    appimages: '📦'
  };
  document.getElementById('root-buttons').innerHTML = Object.keys(data.roots).map(k => `
    <div class="root-item ${state.root === k ? 'active' : ''}" data-root="${esc(k)}">
      <span class="root-icon">${icons[k] || '📁'}</span>
      <span class="root-name">${esc(k)}</span>
    </div>`).join('');
  document.querySelectorAll('.root-item').forEach(el =>
    el.addEventListener('click', () => switchRoot(el.dataset.root)));
}

async function switchRoot(root) {
  state.root = root; state.path = '';
  clearSelection();
  await refreshAll();
  if (window.innerWidth <= 768) document.getElementById('sidebar').classList.remove('open-mobile');
}

// ── STORAGE ────────────────────────────────────────────────────────────────
async function loadStorage() {
  const data = await api('/api/storage?' + qs({ root: state.root, path: state.path }));
  const s = data.storage;
  document.getElementById('free-space').textContent = s.free;
  document.getElementById('total-space').textContent = s.total;
  document.getElementById('usage-bar').style.width = s.pct_used + '%';
  document.getElementById('storage-detail').textContent = `usado ${s.used} de ${s.total} (${s.pct_used}%)`;
}

// ── ITEMS ──────────────────────────────────────────────────────────────────
async function loadItems() {
  const data = await api('/api/list?' + qs({ root: state.root, path: state.path }));
  state.items = data.items;
  state.path = data.path;
  const crumbs = document.getElementById('crumbs');
  crumbs.innerHTML = data.breadcrumbs.map((c, i) => {
    const last = i === data.breadcrumbs.length - 1;
    return `<span class="crumb ${last ? 'cur' : ''}" data-path="${esc(c.path)}">${esc(c.name)}</span>${!last ? '<span class="sep">/</span>' : ''}`;
  }).join('');
  crumbs.querySelectorAll('.crumb').forEach(el => el.addEventListener('click', () => goPath(el.dataset.path || '')));
  renderItems();
}

function goPath(path) { state.path = path; clearSelection(); refreshAll(); }
function goInto(name) { state.path = state.path ? `${state.path}/${name}` : name; clearSelection(); refreshAll(); }

// ── RENDER ─────────────────────────────────────────────────────────────────
function renderItems() {
  let items = [...state.items];
  const q = document.getElementById('search').value.trim().toLowerCase();
  const sort = document.getElementById('sort').value;
  if (q) items = items.filter(x => x.name.toLowerCase().includes(q));
  items.sort((a, b) => {
    if (sort === 'dirs_first') {
      if (a.is_dir !== b.is_dir) return a.is_dir ? -1 : 1;
      return a.name.localeCompare(b.name, 'pt-BR');
    }
    if (sort === 'newest') return b.mtime - a.mtime;
    if (sort === 'size_desc') return (b.size_bytes || 0) - (a.size_bytes || 0);
    return 0;
  });

  const container = document.getElementById('file-grid');
  if (!items.length) {
    container.innerHTML = `<div class="empty-state"><div class="empty-icon">📭</div><div class="empty-text">pasta vazia</div></div>`;
    return;
  }

  if (state.view === 'grid') {
    container.innerHTML = `<div class="grid-view">${items.map(item => `
      <div class="grid-item ${selected.has(item.name) ? 'selected' : ''}" data-name="${esc(item.name)}" data-isdir="${item.is_dir}">
        <div class="item-check"></div>
        <div class="grid-icon">${item.icon}</div>
        <div class="grid-name">${esc(item.name)}</div>
        <div class="grid-meta">${item.is_dir ? 'pasta' : item.size}</div>
      </div>`).join('')}</div>`;
    container.querySelectorAll('.grid-item').forEach(el => {
      el.addEventListener('click', e => handleItemClick(el, e));
      el.addEventListener('contextmenu', e => { e.preventDefault(); toggleSelect(el.dataset.name); });
    });
  } else {
    container.innerHTML = `<table class="list-view"><thead><tr>
      <th style="width:24px"></th><th>nome</th><th>tamanho</th><th>modificado</th><th></th>
    </tr></thead><tbody>
    ${items.map(item => `
      <tr class="list-row ${selected.has(item.name) ? 'selected' : ''}" data-name="${esc(item.name)}" data-isdir="${item.is_dir}">
        <td><div class="list-check ${selected.has(item.name) ? 'checked' : ''}"></div></td>
        <td><div class="list-name-cell" data-navigate="1">
          <span class="list-icon">${item.icon}</span>
          <span class="list-name">${esc(item.name)}</span>
        </div></td>
        <td class="list-size">${item.is_dir ? '—' : item.size}</td>
        <td class="list-date">${fmtDate(item.mtime)}</td>
        <td><button class="open-btn" data-open="1">↗ abrir</button></td>
      </tr>`).join('')}
    </tbody></table>`;
    container.querySelectorAll('.list-row').forEach(el => {
      el.querySelector('.list-check').addEventListener('click', e => { e.stopPropagation(); toggleSelect(el.dataset.name); });
      el.querySelector('[data-navigate]').addEventListener('click', () => navigateItem(el.dataset.name, el.dataset.isdir === 'true'));
      const ob = el.querySelector('[data-open]');
      if (ob) ob.addEventListener('click', e => { e.stopPropagation(); openItemDirect(el.dataset.name, el.dataset.isdir === 'true'); });
    });
  }
  updateSelBar();
}

// ── ITEM INTERACTION ───────────────────────────────────────────────────────
function handleItemClick(el, e) {
  const name = el.dataset.name;
  const isDir = el.dataset.isdir === 'true';
  const rect = el.getBoundingClientRect();
  const localX = e.clientX - rect.left;
  const localY = e.clientY - rect.top;
  if (localX < 30 && localY < 30) { toggleSelect(name); return; }
  if (selected.size > 0) { toggleSelect(name); return; }
  navigateItem(name, isDir);
}

function navigateItem(name, isDir) {
  if (isDir) { goInto(name); return; }
  previewItem(name);
}

function openItemDirect(name, isDir) {
  if (isDir) { downloadZipItem(name); return; }
  const url = '/view?' + itemQS(name);
  window.open(url, '_blank', 'noopener');
}

// ── SELECTION ──────────────────────────────────────────────────────────────
function toggleSelect(name) {
  if (selected.has(name)) selected.delete(name);
  else selected.add(name);
  updateSelBar();
  renderItems();
}

function clearSelection() {
  selected.clear();
  updateSelBar();
}

function updateSelBar() {
  const bar = document.getElementById('sel-bar');
  const count = document.getElementById('sel-count');
  const delBtn = document.getElementById('sel-del-btn');
  if (selected.size > 0) {
    bar.classList.add('show');
    count.textContent = `${selected.size} selecionado${selected.size > 1 ? 's' : ''}`;
    delBtn.style.display = state.root === 'home' ? '' : 'none';
  } else {
    bar.classList.remove('show');
  }
}

async function downloadSelected() {
  const names = [...selected];
  if (!names.length) return;
  if (names.length === 1) {
    const item = state.items.find(x => x.name === names[0]);
    const url = item && item.is_dir
      ? '/download_zip?' + itemQS(names[0])
      : '/download?' + itemQS(names[0]);
    const a = document.createElement('a');
    a.href = url;
    if (!item || !item.is_dir) a.download = names[0];
    a.click();
    return;
  }
  toast(`⬇ preparando ${names.length} itens…`);
  const res = await fetch('/api/batch_zip?' + qs({ root: state.root, path: state.path }) + '&' + names.map(n => 'name=' + encodeURIComponent(n)).join('&'));
  if (!res.ok) { toast('Erro ao gerar ZIP'); return; }
  const blob = await res.blob();
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'homelab_selecao.zip';
  a.click();
  URL.revokeObjectURL(url);
}

async function deleteSelected() {
  if (state.root !== 'home') { toast('Exclusão apenas na área home'); return; }
  const names = [...selected];
  if (!names.length) return;
  if (!confirm(`Excluir ${names.length} item(s) permanentemente?`)) return;
  let ok = 0;
  for (const name of names) {
    try {
      await api('/api/delete', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ root: state.root, path: state.path, name }) });
      ok++;
    } catch (e) { toast(`Erro ao excluir ${name}: ${e.message}`); }
  }
  toast(`✓ ${ok} excluído(s)`);
  clearSelection();
  await refreshAll();
}

function downloadZipItem(name) {
  window.location.href = '/download_zip?' + itemQS(name);
}

// ── PREVIEW MODAL ──────────────────────────────────────────────────────────
async function previewItem(name) {
  try {
    const data = await api('/api/preview?' + itemQS(name));
    const item = state.items.find(x => x.name === name) || {};
    const dl = '/download?' + itemQS(name);
    const viewUrl = '/view?' + itemQS(name);

    document.getElementById('modal-icon').textContent = item.icon || '📄';
    document.getElementById('modal-title').textContent = name;
    document.getElementById('modal-badge').textContent = data.kind || 'file';
    document.getElementById('modal-download').href = dl;
    document.getElementById('modal-download').download = name;
    document.getElementById('modal-newtab').href = viewUrl;
    document.getElementById('modal-newtab').textContent = '↗ abrir';

    const body = document.getElementById('modal-body');
    body.innerHTML = '';

    if (data.kind === 'image') {
      body.innerHTML = `<img src="${dl}" alt="">`;
    } else if (data.kind === 'video') {
      body.innerHTML = `<video src="${dl}" controls playsinline></video>`;
    } else if (data.kind === 'audio') {
      body.innerHTML = `<audio src="${dl}" controls></audio>`;
    } else if (data.kind === 'html') {
      body.innerHTML = `<iframe class="html-frame" src="${viewUrl}" sandbox="allow-scripts allow-same-origin"></iframe>`;
      document.getElementById('modal-newtab').textContent = '↗ abrir página';
    } else if (data.kind === 'markdown') {
      body.innerHTML = `<div class="md-render">${renderMarkdown(data.content || '')}</div>`;
    } else {
      body.innerHTML = `<pre>${esc(data.content || '')}</pre>`;
    }

    document.getElementById('modal').classList.add('open');
  } catch (e) { toast(e.message); }
}

function closeModal() {
  document.getElementById('modal').classList.remove('open');
  document.getElementById('modal-body').innerHTML = '';
}

function closeModalOutside(e) {
  if (e.target.id === 'modal') closeModal();
}

// ── MARKDOWN RENDERER ──────────────────────────────────────────────────────
function renderMarkdown(md) {
  let html = esc(md);
  html = html.replace(/^### (.+)$/gm, '<h3>$1</h3>');
  html = html.replace(/^## (.+)$/gm, '<h2>$1</h2>');
  html = html.replace(/^# (.+)$/gm, '<h1>$1</h1>');
  html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');
  html = html.replace(/```[\w]*\n([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
  html = html.replace(/`([^`]+)`/g, '<code>$1</code>');
  html = html.replace(/^&gt; (.+)$/gm, '<blockquote>$1</blockquote>');
  html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
  html = html.replace(/(^- .+(\n|$))+/gm, m => '<ul>' + m.replace(/^- (.+)$/gm, '<li>$1</li>') + '</ul>');
  html = html.replace(/(^\d+\. .+(\n|$))+/gm, m => '<ol>' + m.replace(/^\d+\. (.+)$/gm, '<li>$1</li>') + '</ol>');
  html = html.replace(/^---$/gm, '<hr style="border:none;border-top:1px solid var(--border);margin:1.5em 0">');
  html = html.replace(/\n\n(?!<[huo]|<pre|<block|<hr)/g, '</p><p>');
  html = '<p>' + html + '</p>';
  html = html.replace(/<p>\s*<\/p>/g, '');
  html = html.replace(/<p>(<[huo])/g, '$1');
  html = html.replace(/(<\/[huo][^>]*>)<\/p>/g, '$1');
  return html;
}

// ── UPLOAD ─────────────────────────────────────────────────────────────────
function pickFiles() { document.getElementById('file-input').click(); }
function pickFolder() { document.getElementById('folder-input').click(); }

document.getElementById('file-input').addEventListener('change', e => {
  queued = Array.from(e.target.files || []);
  updateQueuedLabel();
});
document.getElementById('folder-input').addEventListener('change', e => {
  queued = Array.from(e.target.files || []);
  updateQueuedLabel(true);
});

const dz = document.getElementById('drop-zone');
dz.addEventListener('dragover', e => { e.preventDefault(); dz.classList.add('drag'); });
dz.addEventListener('dragleave', () => dz.classList.remove('drag'));
dz.addEventListener('drop', e => {
  e.preventDefault(); dz.classList.remove('drag');
  queued = Array.from(e.dataTransfer.files || []);
  updateQueuedLabel();
});
dz.addEventListener('click', () => pickFiles());

function updateQueuedLabel(isFolder = false) {
  const el = document.getElementById('selected-files');
  if (!queued.length) { el.textContent = 'nenhum arquivo selecionado'; return; }
  const isF = queued[0] && queued[0].webkitRelativePath;
  if (isF || isFolder) {
    const folders = new Set(queued.map(f => f.webkitRelativePath.split('/')[0]).filter(Boolean));
    el.textContent = `📁 ${folders.size} pasta(s), ${queued.length} arquivo(s)`;
  } else {
    el.textContent = `📄 ${queued.length} arquivo(s) selecionado(s)`;
  }
}

async function uploadSelected() {
  if (state.root !== 'home') { toast('Upload permitido apenas na área home'); return; }
  if (!queued.length) { toast('Selecione arquivos ou uma pasta primeiro'); return; }
  const subdir = document.getElementById('target-subdir').value.trim();
  const fd = new FormData();
  fd.append('root', state.root);
  fd.append('path', state.path);
  fd.append('subdir', subdir);

  for (const file of queued) {
    const relPath = file.webkitRelativePath || file.name;
    fd.append('files', file, relPath);
  }

  const bar = document.getElementById('upload-bar');
  bar.style.width = '0%';
  await new Promise(resolve => {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/api/upload');
    xhr.upload.onprogress = e => {
      if (e.lengthComputable) bar.style.width = Math.round((e.loaded / e.total) * 100) + '%';
    };
    xhr.onload = async () => {
      try {
        const res = JSON.parse(xhr.responseText || '{}');
        if (xhr.status >= 200 && xhr.status < 300 && res.ok !== false) {
          toast(`✓ ${res.saved || 0} arquivo(s) enviado(s)`);
          queued = [];
          document.getElementById('file-input').value = '';
          document.getElementById('folder-input').value = '';
          document.getElementById('target-subdir').value = '';
          updateQueuedLabel();
          await refreshAll();
        } else {
          toast(res.error || 'Falha no upload');
        }
      } catch { toast('Falha no upload'); }
      setTimeout(() => { bar.style.width = '0%'; }, 600);
      resolve();
    };
    xhr.onerror = () => { toast('Erro de rede'); resolve(); };
    xhr.send(fd);
  });
}

// ── CREATE / RENAME / DELETE ───────────────────────────────────────────────
async function saveTextFile() {
  const name = document.getElementById('quick-name').value.trim();
  const text = document.getElementById('quick-text').value;
  if (!name || !text.trim()) { toast('Preencha nome e conteúdo'); return; }
  try {
    await api('/api/save_text', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ root: state.root, path: state.path, name, text }) });
    document.getElementById('quick-name').value = '';
    document.getElementById('quick-text').value = '';
    toast('Arquivo salvo'); await refreshAll();
  } catch (e) { toast(e.message); }
}

async function createFolder() {
  const name = prompt('Nome da nova pasta:');
  if (!name) return;
  try {
    await api('/api/mkdir', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ root: state.root, path: state.path, name }) });
    toast('Pasta criada'); await refreshAll();
  } catch (e) { toast(e.message); }
}

async function copyCurrentUrl() {
  try {
    const url = `${location.origin}/?${qs({ root: state.root, path: state.path })}`;
    await navigator.clipboard.writeText(url);
    toast('Link copiado');
  } catch { toast('Não foi possível copiar'); }
}

function downloadCurrentAsZip() {
  window.location.href = '/download_zip?' + qs({ root: state.root, path: state.path });
}

// ── INIT ───────────────────────────────────────────────────────────────────
setView(state.view);
refreshAll();
setInterval(() => { if (document.hasFocus()) loadItems().catch(() => {}); }, 10000);
document.addEventListener('keydown', e => { if (e.key === 'Escape') { closeModal(); clearSelection(); } });
</script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML)


@app.route("/api/roots")
def api_roots():
    roots = {k: str(v) for k, v in available_roots().items()}
    return jsonify({"ok": True, "roots": roots})


@app.route("/api/list")
def api_list():
    root_key, root, rel = get_root_and_rel()
    return jsonify({
        "ok": True,
        "root": root_key,
        "path": rel,
        "breadcrumbs": breadcrumbs(rel),
        "items": list_items(root, rel),
    })


@app.route("/api/storage")
def api_storage():
    _, root, rel = get_root_and_rel()
    current = resolve_path(root, rel)
    return jsonify({"ok": True, "storage": storage_info(current)})


@app.route("/api/upload", methods=["POST"])
def api_upload():
    roots = available_roots()
    root_key = request.form.get("root", "home")
    rel = safe_rel_path(request.form.get("path", ""))
    subdir = safe_rel_path(request.form.get("subdir", ""))
    root = roots.get(root_key)
    if not root:
        return jsonify({"ok": False, "error": "Raiz inválida"}), 400
    if root_key != "home":
        return jsonify({"ok": False, "error": "Upload permitido apenas na área home"}), 403
    base_target = resolve_path(root, rel)
    if subdir:
        combined = f"{rel}/{subdir}" if rel else subdir
        base_target = resolve_path(root, combined)
    base_target.mkdir(parents=True, exist_ok=True)
    files = request.files.getlist("files")
    saved = 0
    for upload in files:
        if not upload or not upload.filename:
            continue
        rel_name = upload.filename.replace("\\", "/").strip("/")
        parts = [safe_name(p) for p in rel_name.split("/") if p not in ("", ".", "..")]
        if not parts:
            continue
        dest = base_target.joinpath(*parts)
        if not is_subpath(dest, root):
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists() and dest.is_file():
            dest = ensure_unique_path(dest)
        upload.save(dest)
        saved += 1
    return jsonify({"ok": True, "saved": saved})


@app.route("/api/save_text", methods=["POST"])
def api_save_text():
    data = request.get_json(force=True)
    root_key = data.get("root", "home")
    rel = safe_rel_path(data.get("path") or "")
    name = safe_name(data.get("name", "note.txt"))
    text = data.get("text", "")
    roots = available_roots()
    root = roots.get(root_key)
    if not root or root_key != "home":
        return jsonify({"ok": False, "error": "Salvar texto apenas na área home"}), 403
    current = resolve_path(root, rel)
    current.mkdir(parents=True, exist_ok=True)
    dest = ensure_unique_path(current / name)
    dest.write_text(text, encoding="utf-8")
    return jsonify({"ok": True, "name": dest.name})


@app.route("/api/mkdir", methods=["POST"])
def api_mkdir():
    data = request.get_json(force=True)
    root_key = data.get("root", "home")
    rel = safe_rel_path(data.get("path") or "")
    name = safe_name(data.get("name", ""))
    roots = available_roots()
    root = roots.get(root_key)
    if not root or root_key != "home":
        return jsonify({"ok": False, "error": "Criação de pasta apenas na área home"}), 403
    current = resolve_path(root, rel)
    current.mkdir(parents=True, exist_ok=True)
    target = ensure_unique_path(current / name)
    target.mkdir(parents=True, exist_ok=True)
    return jsonify({"ok": True})


@app.route("/api/rename", methods=["POST"])
def api_rename():
    data = request.get_json(force=True)
    root_key = data.get("root", "home")
    rel = safe_rel_path(data.get("path") or "")
    name = data.get("name", "")
    new_name = safe_name(data.get("new_name", ""))
    roots = available_roots()
    root = roots.get(root_key)
    if not root or root_key != "home":
        return jsonify({"ok": False, "error": "Renomear apenas na área home"}), 403
    src = resolve_child(root, rel, name)
    if not src.exists():
        return jsonify({"ok": False, "error": "Item não encontrado"}), 404
    dst = ensure_unique_path(src.parent / new_name)
    src.rename(dst)
    return jsonify({"ok": True, "new_name": dst.name})


@app.route("/api/delete", methods=["POST"])
def api_delete():
    data = request.get_json(force=True)
    root_key = data.get("root", "home")
    rel = safe_rel_path(data.get("path") or "")
    name = data.get("name", "")
    roots = available_roots()
    root = roots.get(root_key)
    if not root or root_key != "home":
        return jsonify({"ok": False, "error": "Exclusão apenas na área home"}), 403
    target = resolve_child(root, rel, name)
    if target.is_dir():
        shutil.rmtree(target)
    elif target.exists():
        target.unlink()
    else:
        return jsonify({"ok": False, "error": "Item não encontrado"}), 404
    return jsonify({"ok": True})


@app.route("/api/preview")
def api_preview():
    _, root, rel = get_root_and_rel()
    name = request.args.get("name", "")
    target = resolve_child(root, rel, name)
    if not target.exists() or target.is_dir():
        return jsonify({"ok": False, "error": "Pré-visualização indisponível"}), 404
    kind = file_type_group(target.name, False)
    if kind == "text":
        try:
            with open(target, "r", encoding="utf-8", errors="replace") as f:
                content = f.read(MAX_PREVIEW_TEXT)
            return jsonify({"ok": True, "kind": "text", "content": content})
        except Exception as e:
            return jsonify({"ok": False, "error": str(e)}), 500
    if kind == "markdown":
        try:
            with open(target, "r", encoding="utf-8", errors="replace") as f:
                content = f.read(MAX_PREVIEW_TEXT)
            return jsonify({"ok": True, "kind": "markdown", "content": content})
        except Exception as e:
            return jsonify({"ok": False, "error": str(e)}), 500
    return jsonify({"ok": True, "kind": kind})


@app.route("/view")
def view_file():
    _, root, rel = get_root_and_rel()
    name = request.args.get("name", "")
    target = resolve_child(root, rel, name)
    if not target.exists() or target.is_dir():
        abort(404)
    mime, _ = mimetypes.guess_type(str(target))
    if not mime:
        mime = "application/octet-stream"
    return send_file(target, mimetype=mime)


@app.route("/download")
def download():
    _, root, rel = get_root_and_rel()
    name = request.args.get("name", "")
    target = resolve_child(root, rel, name)
    if not target.exists():
        abort(404)
    if target.is_dir():
        mem = io.BytesIO()
        with zipfile.ZipFile(mem, "w", zipfile.ZIP_DEFLATED) as zf:
            for p in target.rglob("*"):
                if p.is_file():
                    zf.write(p, arcname=str(Path(target.name) / p.relative_to(target)))
        mem.seek(0)
        return send_file(mem, as_attachment=True, download_name=f"{target.name}.zip", mimetype="application/zip")
    return send_file(target, as_attachment=True, download_name=target.name)


@app.route("/download_zip")
def download_zip():
    _, root, rel = get_root_and_rel()
    current = resolve_path(root, rel)
    mem = io.BytesIO()
    with zipfile.ZipFile(mem, "w", zipfile.ZIP_DEFLATED) as zf:
        if current.is_file():
            zf.write(current, arcname=current.name)
            zip_name = f"{current.stem}.zip"
        else:
            base = current.name or "root"
            for p in current.rglob("*"):
                if p.is_file():
                    zf.write(p, arcname=str(Path(base) / p.relative_to(current)))
            zip_name = f"{base}.zip"
    mem.seek(0)
    return send_file(mem, as_attachment=True, download_name=zip_name, mimetype="application/zip")


@app.route("/api/batch_zip")
def api_batch_zip():
    _, root, rel = get_root_and_rel()
    names = request.args.getlist("name")
    mem = io.BytesIO()
    with zipfile.ZipFile(mem, "w", zipfile.ZIP_DEFLATED) as zf:
        for name in names:
            target = resolve_child(root, rel, name)
            if not target.exists():
                continue
            if target.is_dir():
                for p in target.rglob("*"):
                    if p.is_file():
                        zf.write(p, arcname=str(Path(target.name) / p.relative_to(target)))
            else:
                zf.write(target, arcname=target.name)
    mem.seek(0)
    return send_file(mem, as_attachment=True, download_name="homelab_selecao.zip", mimetype="application/zip")


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


import os
import re
import io
import time
import shutil
import zipfile
import socket
import mimetypes
from pathlib import Path
from urllib.parse import quote

from flask import (
    Flask, request, render_template_string, jsonify,
    send_file, abort, Response
)

APP_TITLE = "Local Storage Host"
HOST = "0.0.0.0"
PORT = 5000

HOME = Path.home().resolve()

BASE_DIR = Path(
    os.environ.get(
        "HOMELAB_BASE_DIR",
        str(HOME)
    )
).resolve()

BROWSABLE_ROOTS = {
    "home": HOME,
    "videos": (HOME / "Vídeos").resolve(),
    "music": (HOME / "Músicas").resolve(),
    "templates": (HOME / "Modelos").resolve(),
    "images": (HOME / "Imagens").resolve(),
    "downloads": (HOME / "Downloads").resolve(),
    "documents": (HOME / "Documentos").resolve(),
    "desktop": (HOME / "Área de trabalho").resolve(),
    "appimages": (HOME / "AppImages").resolve(),
}

MAX_PREVIEW_TEXT = 1024 * 1024 * 2  # 2 MB
app = Flask(__name__)
BASE_DIR.mkdir(parents=True, exist_ok=True)


def available_roots():
    roots = {}
    for key, path in BROWSABLE_ROOTS.items():
        try:
            if path.exists():
                roots[key] = path.resolve()
        except Exception:
            pass
    return roots


def safe_name(name: str) -> str:
    name = (name or "").strip().replace("\\", "/").split("/")[-1]
    name = re.sub(r"[\x00-\x1f]", "", name)
    name = re.sub(r"[<>:\"|?*]", "_", name)
    name = name.strip(" .")
    return name or f"item_{int(time.time())}"


def safe_rel_path(rel: str) -> str:
    rel = (rel or "").strip().replace("\\", "/").strip("/")
    parts = [safe_name(p) for p in rel.split("/") if p not in ("", ".", "..")]
    return "/".join(parts)


def is_subpath(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except Exception:
        return False


def get_root_and_rel():
    root_key = request.args.get("root", "home")
    rel = safe_rel_path(request.args.get("path", ""))
    roots = available_roots()
    root = roots.get(root_key)
    if not root:
        abort(404, "Raiz inválida")
    return root_key, root, rel


def resolve_path(root: Path, rel: str) -> Path:
    target = (root / safe_rel_path(rel)).resolve()
    if not is_subpath(target, root):
        abort(400, "Caminho inválido")
    return target


def resolve_child(root: Path, rel: str, name: str) -> Path:
    current = resolve_path(root, rel)
    target = (current / safe_name(name)).resolve()
    if not is_subpath(target, root):
        abort(400, "Caminho inválido")
    return target


def ensure_unique_path(dest: Path) -> Path:
    if not dest.exists():
        return dest
    stem = dest.stem
    suffix = dest.suffix
    parent = dest.parent
    i = 1
    while True:
        cand = parent / f"{stem}_{i}{suffix}"
        if not cand.exists():
            return cand
        i += 1


def human_size(n: int) -> str:
    n = float(n)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} PB"


def file_icon(name: str, is_dir=False):
    if is_dir:
        return "📁"
    ext = Path(name).suffix.lower()
    icons = {
        ".pdf": "📄", ".txt": "📝", ".md": "📝",
        ".jpg": "🖼", ".jpeg": "🖼", ".png": "🖼", ".gif": "🖼", ".webp": "🖼", ".svg": "🖼", ".bmp": "🖼",
        ".mp4": "🎬", ".mov": "🎬", ".avi": "🎬", ".mkv": "🎬", ".webm": "🎬",
        ".mp3": "🎵", ".wav": "🎵", ".ogg": "🎵", ".flac": "🎵", ".aac": "🎵", ".m4a": "🎵",
        ".zip": "🗜", ".tar": "🗜", ".gz": "🗜", ".rar": "🗜", ".7z": "🗜",
        ".py": "🐍", ".js": "⚡", ".ts": "⚡", ".html": "🌐", ".css": "🎨", ".json": "📦",
        ".xml": "📦", ".csv": "📊", ".xlsx": "📊", ".xls": "📊", ".docx": "📃", ".doc": "📃",
        ".pptx": "📊", ".ppt": "📊", ".sh": "⚙️", ".apk": "📱",
    }
    return icons.get(ext, "📄")


def file_type_group(name: str, is_dir=False):
    if is_dir:
        return "dir"
    ext = Path(name).suffix.lower()
    if ext in {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp"}:
        return "image"
    if ext in {".mp4", ".mov", ".avi", ".mkv", ".webm"}:
        return "video"
    if ext in {".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a"}:
        return "audio"
    if ext in {".txt", ".py", ".js", ".ts", ".css", ".json", ".xml", ".csv", ".sh", ".log", ".yaml", ".yml"}:
        return "text"
    if ext == ".md":
        return "markdown"
    if ext == ".html" or ext == ".htm":
        return "html"
    if ext in {".zip", ".tar", ".gz", ".rar", ".7z"}:
        return "zip"
    return "file"


def can_preview(path: Path, kind: str):
    if path.is_dir():
        return False
    return kind in {"image", "video", "audio", "text", "markdown", "html"}


def list_items(root: Path, rel: str):
    current = resolve_path(root, rel)
    if not current.exists() and root == BASE_DIR:
        current.mkdir(parents=True, exist_ok=True)
    elif not current.exists():
        abort(404, "Pasta não encontrada")

    items = []
    for p in sorted(current.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower())):
        try:
            stat = p.stat()
            is_dir = p.is_dir()
            size_bytes = 0 if is_dir else stat.st_size
            kind = file_type_group(p.name, is_dir)
            items.append({
                "name": p.name,
                "is_dir": is_dir,
                "type": kind,
                "icon": file_icon(p.name, is_dir),
                "size_bytes": size_bytes,
                "size": "—" if is_dir else human_size(size_bytes),
                "mtime": int(stat.st_mtime),
                "preview": can_preview(p, kind),
            })
        except Exception:
            pass
    return items


def breadcrumbs(rel: str):
    crumbs = [{"name": "Início", "path": ""}]
    if not rel:
        return crumbs
    acc = []
    for part in [p for p in rel.split("/") if p]:
        acc.append(part)
        crumbs.append({"name": part, "path": "/".join(acc)})
    return crumbs


def storage_info(path: Path):
    try:
        usage = shutil.disk_usage(path)
        return {
            "total_bytes": usage.total,
            "used_bytes": usage.used,
            "free_bytes": usage.free,
            "total": human_size(usage.total),
            "used": human_size(usage.used),
            "free": human_size(usage.free),
            "pct_used": round((usage.used / usage.total) * 100, 1) if usage.total else 0,
        }
    except Exception:
        return {
            "total_bytes": 0, "used_bytes": 0, "free_bytes": 0,
            "total": "—", "used": "—", "free": "—", "pct_used": 0,
        }


HTML = r"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>Local Storage Host</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
:root {
  --bg: #0f1117;
  --surface: #181b23;
  --surface2: #1e2230;
  --surface3: #252a3a;
  --border: #2a3045;
  --border2: #353d55;
  --text: #e2e8f0;
  --text2: #94a3b8;
  --text3: #64748b;
  --accent: #4ade80;
  --accent-dim: #22c55e33;
  --accent2: #38bdf8;
  --danger: #f87171;
  --warn: #fbbf24;
  --mono: 'IBM Plex Mono', monospace;
  --sans: 'IBM Plex Sans', sans-serif;
  --radius: 6px;
}
html, body { background: var(--bg); color: var(--text); font-family: var(--sans); height: 100%; overflow: hidden; font-size: 13px; }
.app { display: flex; flex-direction: column; height: 100vh; overflow: hidden; }

/* HEADER */
.header {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 0 16px;
  display: flex; align-items: center; gap: 12px;
  height: 48px; flex-shrink: 0;
}
.menu-btn { background: none; border: none; color: var(--text2); cursor: pointer; padding: 6px; border-radius: 4px; font-size: 16px; }
.menu-btn:hover { background: var(--surface2); color: var(--text); }
.logo { font-family: var(--mono); font-size: 14px; color: var(--accent); letter-spacing: -0.5px; }
.logo span { color: var(--text3); }
.spacer { flex: 1; }
.header-btn { background: none; border: 1px solid var(--border); color: var(--text2); cursor: pointer; padding: 5px 10px; border-radius: var(--radius); font-size: 12px; font-family: var(--mono); }
.header-btn:hover { background: var(--surface2); color: var(--text); border-color: var(--border2); }

/* LAYOUT */
.main-container { display: flex; flex: 1; overflow: hidden; position: relative; }
.sidebar { width: 300px; background: var(--surface); border-right: 1px solid var(--border); display: flex; flex-direction: column; overflow-y: auto; flex-shrink: 0; transition: transform 0.2s ease, width 0.2s ease; }
.sidebar.closed { width: 0; overflow: hidden; transform: translateX(-100%); position: absolute; height: 100%; z-index: 10; }
.content { flex: 1; display: flex; flex-direction: column; overflow: hidden; min-width: 0; }

/* SIDEBAR */
.sidebar-section { padding: 14px; border-bottom: 1px solid var(--border); }
.sidebar-label { font-family: var(--mono); font-size: 10px; color: var(--text3); letter-spacing: 1px; text-transform: uppercase; margin-bottom: 10px; }
.root-item { display: flex; align-items: center; gap: 10px; padding: 7px 10px; border-radius: var(--radius); cursor: pointer; color: var(--text2); transition: all 0.1s; }
.root-item:hover { background: var(--surface2); color: var(--text); }
.root-item.active { background: var(--accent-dim); color: var(--accent); }
.root-icon { font-size: 16px; line-height: 1; }
.root-name { font-family: var(--mono); font-size: 12px; }

/* STORAGE BAR */
.storage-card { background: var(--surface2); border-radius: var(--radius); padding: 12px; border: 1px solid var(--border); }
.storage-row { display: flex; justify-content: space-between; font-family: var(--mono); font-size: 11px; color: var(--text2); margin-bottom: 8px; }
.storage-row span:last-child { color: var(--text3); }
.bar-track { height: 3px; background: var(--surface3); border-radius: 2px; overflow: hidden; margin-bottom: 6px; }
.bar-fill { height: 100%; background: var(--accent); border-radius: 2px; width: 0; transition: width 0.3s; }
.storage-sub { font-family: var(--mono); font-size: 10px; color: var(--text3); }

/* UPLOAD */
.drop-zone { border: 1px dashed var(--border2); border-radius: var(--radius); padding: 14px; text-align: center; cursor: pointer; color: var(--text3); transition: all 0.15s; margin-bottom: 10px; }
.drop-zone:hover, .drop-zone.drag { background: var(--accent-dim); border-color: var(--accent); color: var(--accent); }
.drop-title { font-size: 13px; margin-bottom: 4px; }
.drop-sub { font-size: 11px; }
.row-btns { display: flex; gap: 6px; margin-bottom: 8px; }
.sb-input { width: 100%; padding: 7px 10px; background: var(--surface2); border: 1px solid var(--border); color: var(--text); border-radius: var(--radius); font-size: 12px; font-family: var(--mono); margin-bottom: 8px; }
.sb-input:focus { outline: none; border-color: var(--accent); }
.sb-textarea { width: 100%; padding: 8px 10px; background: var(--surface2); border: 1px solid var(--border); color: var(--text); border-radius: var(--radius); font-size: 12px; font-family: var(--mono); resize: vertical; min-height: 72px; margin-bottom: 8px; }
.sb-textarea:focus { outline: none; border-color: var(--accent); }
.sb-btn { display: block; width: 100%; padding: 7px 12px; background: var(--surface2); border: 1px solid var(--border); color: var(--text2); border-radius: var(--radius); cursor: pointer; font-size: 12px; font-family: var(--mono); text-align: center; text-decoration: none; margin-bottom: 6px; transition: all 0.1s; }
.sb-btn:hover { background: var(--surface3); color: var(--text); border-color: var(--border2); }
.sb-btn.primary { background: var(--accent); color: #000; border-color: var(--accent); font-weight: 600; }
.sb-btn.primary:hover { opacity: 0.85; }
.sb-btn.danger { background: var(--danger); color: #fff; border-color: var(--danger); }
.sb-btn.half { flex: 1; margin-bottom: 0; }
.file-label { font-size: 11px; color: var(--text3); font-family: var(--mono); margin-bottom: 8px; min-height: 16px; }

/* TOOLBAR */
.toolbar { padding: 10px 14px; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 10px; background: var(--surface); flex-shrink: 0; flex-wrap: wrap; }
.breadcrumbs { display: flex; align-items: center; gap: 2px; flex: 1; overflow-x: auto; min-width: 0; }
.crumb { padding: 4px 6px; cursor: pointer; color: var(--text3); white-space: nowrap; border-radius: 4px; font-family: var(--mono); font-size: 12px; transition: color 0.1s; }
.crumb:hover { color: var(--accent); }
.crumb.cur { color: var(--text); }
.sep { color: var(--border2); font-size: 14px; }
.tb-actions { display: flex; gap: 6px; align-items: center; flex-shrink: 0; }
.tb-btn { background: none; border: 1px solid transparent; padding: 5px 8px; cursor: pointer; color: var(--text2); border-radius: var(--radius); font-size: 12px; font-family: var(--mono); transition: all 0.1s; white-space: nowrap; }
.tb-btn:hover { background: var(--surface2); color: var(--text); border-color: var(--border); }
.tb-btn.active { background: var(--accent-dim); color: var(--accent); border-color: var(--accent); }
.search-wrap { display: flex; align-items: center; gap: 6px; background: var(--surface2); border: 1px solid var(--border); border-radius: var(--radius); padding: 0 8px; }
.search-wrap:focus-within { border-color: var(--accent); }
.search-wrap input { background: none; border: none; padding: 6px 0; color: var(--text); font-family: var(--mono); font-size: 12px; width: 140px; }
.search-wrap input:focus { outline: none; }
.search-wrap input::placeholder { color: var(--text3); }
.sort-sel { background: var(--surface2); border: 1px solid var(--border); color: var(--text2); padding: 5px 8px; border-radius: var(--radius); font-family: var(--mono); font-size: 12px; cursor: pointer; }
.sort-sel:focus { outline: none; border-color: var(--accent); }

/* SELECTION BAR */
.sel-bar { display: none; padding: 8px 14px; background: var(--accent-dim); border-bottom: 1px solid var(--accent); align-items: center; gap: 10px; flex-shrink: 0; }
.sel-bar.show { display: flex; }
.sel-count { font-family: var(--mono); font-size: 12px; color: var(--accent); flex: 1; }
.sel-btn { padding: 5px 12px; border-radius: var(--radius); border: none; cursor: pointer; font-family: var(--mono); font-size: 12px; font-weight: 500; transition: all 0.1s; }
.sel-btn.dl { background: var(--accent); color: #000; }
.sel-btn.dl:hover { opacity: 0.8; }
.sel-btn.del { background: var(--danger); color: #fff; }
.sel-btn.del:hover { opacity: 0.8; }
.sel-btn.clr { background: var(--surface3); color: var(--text2); border: 1px solid var(--border2); }
.sel-btn.clr:hover { color: var(--text); }

/* FILE GRID */
.file-grid { flex: 1; overflow-y: auto; padding: 14px; }
.grid-view { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 8px; }
.grid-item { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 14px 10px 10px; cursor: pointer; transition: all 0.1s; text-align: center; position: relative; user-select: none; }
.grid-item:hover { background: var(--surface2); border-color: var(--border2); }
.grid-item.selected { background: var(--accent-dim); border-color: var(--accent); }
.grid-icon { font-size: 40px; margin-bottom: 8px; line-height: 1; }
.grid-name { font-size: 12px; word-break: break-word; color: var(--text); margin-bottom: 3px; font-family: var(--mono); }
.grid-meta { font-size: 10px; color: var(--text3); font-family: var(--mono); }
.item-check { position: absolute; top: 6px; left: 6px; width: 16px; height: 16px; border-radius: 3px; border: 1.5px solid var(--border2); background: var(--surface2); display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.1s; pointer-events: none; }
.grid-item:hover .item-check, .grid-item.selected .item-check { opacity: 1; }
.grid-item.selected .item-check { background: var(--accent); border-color: var(--accent); color: #000; }
.item-check::after { content: '✓'; font-size: 10px; font-weight: 700; }

/* LIST VIEW */
.list-view { width: 100%; border-collapse: collapse; }
.list-view th { text-align: left; padding: 10px 8px; border-bottom: 1px solid var(--border); color: var(--text3); font-weight: 500; font-family: var(--mono); font-size: 11px; letter-spacing: 0.5px; position: sticky; top: 0; background: var(--bg); z-index: 1; }
.list-view td { padding: 10px 8px; border-bottom: 1px solid var(--border); }
.list-view tr.list-row:hover { background: var(--surface2); }
.list-view tr.list-row.selected { background: var(--accent-dim); }
.list-row td:first-child { padding-left: 4px; }
.list-check { width: 16px; height: 16px; border-radius: 3px; border: 1.5px solid var(--border2); background: var(--surface2); display: inline-flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0; }
.list-row.selected .list-check, .list-check.checked { background: var(--accent); border-color: var(--accent); color: #000; }
.list-check.checked::after { content: '✓'; font-size: 9px; font-weight: 700; }
.list-name-cell { display: flex; align-items: center; gap: 10px; cursor: pointer; }
.list-icon { font-size: 18px; line-height: 1; }
.list-name { font-family: var(--mono); font-size: 12px; }
.list-size, .list-date { font-family: var(--mono); font-size: 11px; color: var(--text3); white-space: nowrap; }
.open-btn { padding: 3px 8px; background: none; border: 1px solid var(--border); border-radius: 4px; color: var(--text2); cursor: pointer; font-family: var(--mono); font-size: 11px; }
.open-btn:hover { background: var(--surface2); color: var(--text); }

/* EMPTY STATE */
.empty-state { text-align: center; padding: 60px 20px; color: var(--text3); font-family: var(--mono); }
.empty-icon { font-size: 40px; margin-bottom: 12px; }
.empty-text { font-size: 13px; }

/* MODAL */
.modal { position: fixed; inset: 0; background: rgba(0,0,0,0.85); display: none; align-items: center; justify-content: center; z-index: 1000; padding: 20px; }
.modal.open { display: flex; }
.modal-inner { background: var(--surface); border: 1px solid var(--border2); border-radius: 10px; width: 100%; max-width: 900px; max-height: 90vh; display: flex; flex-direction: column; overflow: hidden; }
.modal-head { padding: 12px 16px; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 10px; flex-shrink: 0; }
.modal-fname { flex: 1; font-family: var(--mono); font-size: 13px; color: var(--text); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.modal-type-badge { font-family: var(--mono); font-size: 10px; padding: 2px 7px; border-radius: 3px; background: var(--surface2); color: var(--text3); border: 1px solid var(--border); }
.modal-actions { display: flex; gap: 6px; }
.m-btn { padding: 5px 12px; border-radius: var(--radius); border: 1px solid var(--border); background: var(--surface2); color: var(--text2); cursor: pointer; font-family: var(--mono); font-size: 12px; text-decoration: none; transition: all 0.1s; }
.m-btn:hover { background: var(--surface3); color: var(--text); }
.m-btn.open-tab { background: var(--accent-dim); border-color: var(--accent); color: var(--accent); }
.modal-body { flex: 1; overflow: auto; position: relative; }
.modal-body img { max-width: 100%; height: auto; display: block; margin: auto; padding: 16px; }
.modal-body video, .modal-body audio { width: 100%; display: block; margin: auto; padding: 16px; }
.modal-body audio { margin-top: 40px; }
.modal-body pre { font-family: var(--mono); font-size: 12px; white-space: pre-wrap; word-break: break-word; padding: 16px; line-height: 1.6; color: var(--text2); }
.modal-body .md-render { padding: 24px; line-height: 1.7; max-width: 760px; margin: auto; }
.modal-body .md-render h1, .md-render h2, .md-render h3 { color: var(--text); margin: 1.2em 0 0.5em; font-family: var(--sans); }
.modal-body .md-render h1 { font-size: 22px; border-bottom: 1px solid var(--border); padding-bottom: 8px; }
.modal-body .md-render h2 { font-size: 17px; }
.modal-body .md-render h3 { font-size: 15px; }
.modal-body .md-render p { color: var(--text2); margin-bottom: 1em; }
.modal-body .md-render code { font-family: var(--mono); background: var(--surface2); padding: 2px 6px; border-radius: 3px; font-size: 11px; color: var(--accent); }
.modal-body .md-render pre { background: var(--surface2); padding: 14px; border-radius: var(--radius); border: 1px solid var(--border); margin-bottom: 1em; overflow-x: auto; }
.modal-body .md-render pre code { background: none; padding: 0; color: var(--text2); }
.modal-body .md-render a { color: var(--accent2); }
.modal-body .md-render blockquote { border-left: 3px solid var(--accent); padding-left: 14px; margin: 1em 0; color: var(--text3); font-style: italic; }
.modal-body .md-render ul, .md-render ol { padding-left: 1.4em; color: var(--text2); margin-bottom: 1em; }
.modal-body .md-render li { margin-bottom: 0.25em; }
.modal-body .md-render table { width: 100%; border-collapse: collapse; margin-bottom: 1em; }
.modal-body .md-render th { background: var(--surface2); padding: 8px 12px; border: 1px solid var(--border); font-size: 12px; }
.modal-body .md-render td { padding: 8px 12px; border: 1px solid var(--border); font-size: 12px; color: var(--text2); }
.html-frame { width: 100%; height: 100%; min-height: 400px; border: none; background: white; }

/* TOAST */
.toast { position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%) translateY(80px); background: var(--surface); border: 1px solid var(--border2); padding: 8px 18px; border-radius: 20px; font-family: var(--mono); font-size: 12px; color: var(--text); z-index: 2000; transition: transform 0.2s ease; white-space: nowrap; }
.toast.show { transform: translateX(-50%) translateY(0); }

/* SCROLLBARS */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--surface3); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--border2); }

/* UPLOAD PROGRESS */
.upload-prog { height: 3px; background: var(--border); border-radius: 2px; overflow: hidden; margin-bottom: 8px; }
.upload-prog-fill { height: 100%; background: var(--accent); width: 0; transition: width 0.1s; }

@media (max-width: 768px) {
  .sidebar { position: absolute; height: 100%; transform: translateX(-100%); z-index: 10; }
  .sidebar.open-mobile { transform: translateX(0); }
  .sidebar.closed { transform: translateX(-100%); width: 300px; }
  .grid-view { grid-template-columns: repeat(auto-fill, minmax(110px, 1fr)); }
  .search-wrap { order: 1; flex: 1; }
  .search-wrap input { width: 100%; }
  .list-date { display: none; }
}
</style>
</head>
<body>
<div class="app">
  <header class="header">
    <button class="menu-btn" onclick="toggleSidebar()" title="Menu">☰</button>
    <div class="logo">Local<span>/</span>Storage Host</div>
    <div class="spacer"></div>
    <button class="header-btn" onclick="refreshAll()">↻ atualizar</button>
    <button class="header-btn" onclick="copyCurrentUrl()">🔗 link</button>
  </header>

  <div class="main-container">
    <!-- SIDEBAR -->
    <div class="sidebar" id="sidebar">
      <div class="sidebar-section">
        <div class="sidebar-label">locais</div>
        <div id="root-buttons"></div>
      </div>
      <div class="sidebar-section">
        <div class="sidebar-label">armazenamento</div>
        <div class="storage-card">
          <div class="storage-row">
            <span>livre <strong id="free-space" style="color:var(--accent)">—</strong></span>
            <span>total <strong id="total-space">—</strong></span>
          </div>
          <div class="bar-track"><div class="bar-fill" id="usage-bar"></div></div>
          <div class="storage-sub" id="storage-detail">—</div>
        </div>
      </div>
      <div class="sidebar-section">
        <div class="sidebar-label">enviar</div>
        <div class="drop-zone" id="drop-zone">
          <div class="drop-title">📂 arrastar aqui</div>
          <div class="drop-sub">arquivos e pastas inteiras</div>
        </div>
        <input id="file-input" type="file" multiple style="display:none">
        <input id="folder-input" type="file" webkitdirectory directory multiple style="display:none">
        <div class="row-btns">
          <button class="sb-btn half" onclick="pickFiles()">📄 arquivos</button>
          <button class="sb-btn half" onclick="pickFolder()">📁 pasta</button>
        </div>
        <input class="sb-input" type="text" id="target-subdir" placeholder="subpasta destino (opcional)">
        <div class="file-label" id="selected-files">nenhum arquivo selecionado</div>
        <div class="upload-prog"><div class="upload-prog-fill" id="upload-bar"></div></div>
        <button class="sb-btn primary" onclick="uploadSelected()">⬆ enviar agora</button>
      </div>
      <div class="sidebar-section">
        <div class="sidebar-label">criar texto</div>
        <input class="sb-input" type="text" id="quick-name" placeholder="nome.txt / nota.md">
        <textarea class="sb-textarea" id="quick-text" placeholder="Conteúdo do arquivo..."></textarea>
        <button class="sb-btn" onclick="saveTextFile()">📝 salvar arquivo</button>
      </div>
      <div class="sidebar-section">
        <div class="sidebar-label">ações</div>
        <button class="sb-btn" onclick="createFolder()">📁 nova pasta</button>
        <button class="sb-btn" onclick="downloadCurrentAsZip()">🗜 baixar pasta como ZIP</button>
      </div>
    </div>

    <!-- CONTENT -->
    <div class="content">
      <!-- TOOLBAR -->
      <div class="toolbar">
        <div class="breadcrumbs" id="crumbs"></div>
        <div class="tb-actions">
          <div class="search-wrap">
            <span style="color:var(--text3)">🔍</span>
            <input type="search" id="search" placeholder="buscar..." oninput="renderItems()">
          </div>
          <select class="sort-sel" id="sort" onchange="renderItems()">
            <option value="dirs_first">nome</option>
            <option value="newest">recente</option>
            <option value="size_desc">tamanho</option>
          </select>
          <button class="tb-btn" id="btn-grid" onclick="setView('grid')" title="Grade">⊞</button>
          <button class="tb-btn" id="btn-list" onclick="setView('list')" title="Lista">≡</button>
        </div>
      </div>

      <!-- SELECTION BAR -->
      <div class="sel-bar" id="sel-bar">
        <span class="sel-count" id="sel-count">0 selecionados</span>
        <button class="sel-btn dl" onclick="downloadSelected()">↓ baixar</button>
        <button class="sel-btn del" id="sel-del-btn" onclick="deleteSelected()">🗑 excluir</button>
        <button class="sel-btn clr" onclick="clearSelection()">✕ limpar</button>
      </div>

      <div class="file-grid" id="file-grid"></div>
    </div>
  </div>
</div>

<!-- TOAST -->
<div class="toast" id="toast"></div>

<!-- MODAL -->
<div class="modal" id="modal" onclick="closeModalOutside(event)">
  <div class="modal-inner">
    <div class="modal-head">
      <span id="modal-icon" style="font-size:20px"></span>
      <div class="modal-fname" id="modal-title">—</div>
      <span class="modal-type-badge" id="modal-badge">—</span>
      <div class="modal-actions">
        <a class="m-btn open-tab" id="modal-newtab" href="#" target="_blank" rel="noopener">↗ abrir</a>
        <a class="m-btn" id="modal-download" href="#" download>↓ baixar</a>
        <button class="m-btn" onclick="closeModal()">✕</button>
      </div>
    </div>
    <div class="modal-body" id="modal-body"></div>
  </div>
</div>

<script>
// ── STATE ──────────────────────────────────────────────────────────────────
let state = { root: 'home', path: '', items: [], view: localStorage.getItem('hlab-view') || 'grid' };
let selected = new Set();
let queued = [];

// ── UTILS ──────────────────────────────────────────────────────────────────
const qs = o => new URLSearchParams(o).toString();
const esc = s => String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const fmtDate = ts => new Date(ts * 1000).toLocaleString('pt-BR', { dateStyle: 'short', timeStyle: 'short' });
const itemQS = name => qs({ root: state.root, path: state.path, name });

function toast(msg, dur = 2500) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(t._h);
  t._h = setTimeout(() => t.classList.remove('show'), dur);
}

async function api(path, opts = {}) {
  const r = await fetch(path, opts);
  const j = await r.json().catch(() => ({ ok: false, error: 'Erro' }));
  if (!r.ok || j.ok === false) throw new Error(j.error || 'Erro');
  return j;
}

// ── SIDEBAR ────────────────────────────────────────────────────────────────
function toggleSidebar() {
  const sb = document.getElementById('sidebar');
  if (window.innerWidth <= 768) sb.classList.toggle('open-mobile');
  else sb.classList.toggle('closed');
}

// ── VIEW ───────────────────────────────────────────────────────────────────
function setView(v) {
  state.view = v;
  localStorage.setItem('hlab-view', v);
  document.getElementById('btn-grid').classList.toggle('active', v === 'grid');
  document.getElementById('btn-list').classList.toggle('active', v === 'list');
  renderItems();
}

// ── REFRESH ────────────────────────────────────────────────────────────────
async function refreshAll() {
  try {
    await Promise.all([loadRoots(), loadStorage(), loadItems()]);
    clearSelection();
  } catch (e) { toast(e.message || 'Erro ao carregar'); }
}

// ── ROOTS ──────────────────────────────────────────────────────────────────
async function loadRoots() {
  const data = await api('/api/roots');
  const icons = {
    home: '🏠',
    videos: '🎬',
    music: '🎵',
    templates: '📐',
    images: '🖼',
    downloads: '⬇',
    documents: '📃',
    desktop: '🖥',
    appimages: '📦'
  };
  document.getElementById('root-buttons').innerHTML = Object.keys(data.roots).map(k => `
    <div class="root-item ${state.root === k ? 'active' : ''}" data-root="${esc(k)}">
      <span class="root-icon">${icons[k] || '📁'}</span>
      <span class="root-name">${esc(k)}</span>
    </div>`).join('');
  document.querySelectorAll('.root-item').forEach(el =>
    el.addEventListener('click', () => switchRoot(el.dataset.root)));
}

async function switchRoot(root) {
  state.root = root; state.path = '';
  clearSelection();
  await refreshAll();
  if (window.innerWidth <= 768) document.getElementById('sidebar').classList.remove('open-mobile');
}

// ── STORAGE ────────────────────────────────────────────────────────────────
async function loadStorage() {
  const data = await api('/api/storage?' + qs({ root: state.root, path: state.path }));
  const s = data.storage;
  document.getElementById('free-space').textContent = s.free;
  document.getElementById('total-space').textContent = s.total;
  document.getElementById('usage-bar').style.width = s.pct_used + '%';
  document.getElementById('storage-detail').textContent = `usado ${s.used} de ${s.total} (${s.pct_used}%)`;
}

// ── ITEMS ──────────────────────────────────────────────────────────────────
async function loadItems() {
  const data = await api('/api/list?' + qs({ root: state.root, path: state.path }));
  state.items = data.items;
  state.path = data.path;
  const crumbs = document.getElementById('crumbs');
  crumbs.innerHTML = data.breadcrumbs.map((c, i) => {
    const last = i === data.breadcrumbs.length - 1;
    return `<span class="crumb ${last ? 'cur' : ''}" data-path="${esc(c.path)}">${esc(c.name)}</span>${!last ? '<span class="sep">/</span>' : ''}`;
  }).join('');
  crumbs.querySelectorAll('.crumb').forEach(el => el.addEventListener('click', () => goPath(el.dataset.path || '')));
  renderItems();
}

function goPath(path) { state.path = path; clearSelection(); refreshAll(); }
function goInto(name) { state.path = state.path ? `${state.path}/${name}` : name; clearSelection(); refreshAll(); }

// ── RENDER ─────────────────────────────────────────────────────────────────
function renderItems() {
  let items = [...state.items];
  const q = document.getElementById('search').value.trim().toLowerCase();
  const sort = document.getElementById('sort').value;
  if (q) items = items.filter(x => x.name.toLowerCase().includes(q));
  items.sort((a, b) => {
    if (sort === 'dirs_first') {
      if (a.is_dir !== b.is_dir) return a.is_dir ? -1 : 1;
      return a.name.localeCompare(b.name, 'pt-BR');
    }
    if (sort === 'newest') return b.mtime - a.mtime;
    if (sort === 'size_desc') return (b.size_bytes || 0) - (a.size_bytes || 0);
    return 0;
  });

  const container = document.getElementById('file-grid');
  if (!items.length) {
    container.innerHTML = `<div class="empty-state"><div class="empty-icon">📭</div><div class="empty-text">pasta vazia</div></div>`;
    return;
  }

  if (state.view === 'grid') {
    container.innerHTML = `<div class="grid-view">${items.map(item => `
      <div class="grid-item ${selected.has(item.name) ? 'selected' : ''}" data-name="${esc(item.name)}" data-isdir="${item.is_dir}">
        <div class="item-check"></div>
        <div class="grid-icon">${item.icon}</div>
        <div class="grid-name">${esc(item.name)}</div>
        <div class="grid-meta">${item.is_dir ? 'pasta' : item.size}</div>
      </div>`).join('')}</div>`;
    container.querySelectorAll('.grid-item').forEach(el => {
      el.addEventListener('click', e => handleItemClick(el, e));
      el.addEventListener('contextmenu', e => { e.preventDefault(); toggleSelect(el.dataset.name); });
    });
  } else {
    container.innerHTML = `<table class="list-view"><thead><tr>
      <th style="width:24px"></th><th>nome</th><th>tamanho</th><th>modificado</th><th></th>
    </tr></thead><tbody>
    ${items.map(item => `
      <tr class="list-row ${selected.has(item.name) ? 'selected' : ''}" data-name="${esc(item.name)}" data-isdir="${item.is_dir}">
        <td><div class="list-check ${selected.has(item.name) ? 'checked' : ''}"></div></td>
        <td><div class="list-name-cell" data-navigate="1">
          <span class="list-icon">${item.icon}</span>
          <span class="list-name">${esc(item.name)}</span>
        </div></td>
        <td class="list-size">${item.is_dir ? '—' : item.size}</td>
        <td class="list-date">${fmtDate(item.mtime)}</td>
        <td><button class="open-btn" data-open="1">↗ abrir</button></td>
      </tr>`).join('')}
    </tbody></table>`;
    container.querySelectorAll('.list-row').forEach(el => {
      el.querySelector('.list-check').addEventListener('click', e => { e.stopPropagation(); toggleSelect(el.dataset.name); });
      el.querySelector('[data-navigate]').addEventListener('click', () => navigateItem(el.dataset.name, el.dataset.isdir === 'true'));
      const ob = el.querySelector('[data-open]');
      if (ob) ob.addEventListener('click', e => { e.stopPropagation(); openItemDirect(el.dataset.name, el.dataset.isdir === 'true'); });
    });
  }
  updateSelBar();
}

// ── ITEM INTERACTION ───────────────────────────────────────────────────────
function handleItemClick(el, e) {
  const name = el.dataset.name;
  const isDir = el.dataset.isdir === 'true';
  const rect = el.getBoundingClientRect();
  const localX = e.clientX - rect.left;
  const localY = e.clientY - rect.top;
  if (localX < 30 && localY < 30) { toggleSelect(name); return; }
  if (selected.size > 0) { toggleSelect(name); return; }
  navigateItem(name, isDir);
}

function navigateItem(name, isDir) {
  if (isDir) { goInto(name); return; }
  previewItem(name);
}

function openItemDirect(name, isDir) {
  if (isDir) { downloadZipItem(name); return; }
  const url = '/view?' + itemQS(name);
  window.open(url, '_blank', 'noopener');
}

// ── SELECTION ──────────────────────────────────────────────────────────────
function toggleSelect(name) {
  if (selected.has(name)) selected.delete(name);
  else selected.add(name);
  updateSelBar();
  renderItems();
}

function clearSelection() {
  selected.clear();
  updateSelBar();
}

function updateSelBar() {
  const bar = document.getElementById('sel-bar');
  const count = document.getElementById('sel-count');
  const delBtn = document.getElementById('sel-del-btn');
  if (selected.size > 0) {
    bar.classList.add('show');
    count.textContent = `${selected.size} selecionado${selected.size > 1 ? 's' : ''}`;
    delBtn.style.display = state.root === 'home' ? '' : 'none';
  } else {
    bar.classList.remove('show');
  }
}

async function downloadSelected() {
  const names = [...selected];
  if (!names.length) return;
  if (names.length === 1) {
    const item = state.items.find(x => x.name === names[0]);
    const url = item && item.is_dir
      ? '/download_zip?' + itemQS(names[0])
      : '/download?' + itemQS(names[0]);
    const a = document.createElement('a');
    a.href = url;
    if (!item || !item.is_dir) a.download = names[0];
    a.click();
    return;
  }
  toast(`⬇ preparando ${names.length} itens…`);
  const res = await fetch('/api/batch_zip?' + qs({ root: state.root, path: state.path }) + '&' + names.map(n => 'name=' + encodeURIComponent(n)).join('&'));
  if (!res.ok) { toast('Erro ao gerar ZIP'); return; }
  const blob = await res.blob();
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'homelab_selecao.zip';
  a.click();
  URL.revokeObjectURL(url);
}

async function deleteSelected() {
  if (state.root !== 'home') { toast('Exclusão apenas na área home'); return; }
  const names = [...selected];
  if (!names.length) return;
  if (!confirm(`Excluir ${names.length} item(s) permanentemente?`)) return;
  let ok = 0;
  for (const name of names) {
    try {
      await api('/api/delete', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ root: state.root, path: state.path, name }) });
      ok++;
    } catch (e) { toast(`Erro ao excluir ${name}: ${e.message}`); }
  }
  toast(`✓ ${ok} excluído(s)`);
  clearSelection();
  await refreshAll();
}

function downloadZipItem(name) {
  window.location.href = '/download_zip?' + itemQS(name);
}

// ── PREVIEW MODAL ──────────────────────────────────────────────────────────
async function previewItem(name) {
  try {
    const data = await api('/api/preview?' + itemQS(name));
    const item = state.items.find(x => x.name === name) || {};
    const dl = '/download?' + itemQS(name);
    const viewUrl = '/view?' + itemQS(name);

    document.getElementById('modal-icon').textContent = item.icon || '📄';
    document.getElementById('modal-title').textContent = name;
    document.getElementById('modal-badge').textContent = data.kind || 'file';
    document.getElementById('modal-download').href = dl;
    document.getElementById('modal-download').download = name;
    document.getElementById('modal-newtab').href = viewUrl;
    document.getElementById('modal-newtab').textContent = '↗ abrir';

    const body = document.getElementById('modal-body');
    body.innerHTML = '';

    if (data.kind === 'image') {
      body.innerHTML = `<img src="${dl}" alt="">`;
    } else if (data.kind === 'video') {
      body.innerHTML = `<video src="${dl}" controls playsinline></video>`;
    } else if (data.kind === 'audio') {
      body.innerHTML = `<audio src="${dl}" controls></audio>`;
    } else if (data.kind === 'html') {
      body.innerHTML = `<iframe class="html-frame" src="${viewUrl}" sandbox="allow-scripts allow-same-origin"></iframe>`;
      document.getElementById('modal-newtab').textContent = '↗ abrir página';
    } else if (data.kind === 'markdown') {
      body.innerHTML = `<div class="md-render">${renderMarkdown(data.content || '')}</div>`;
    } else {
      body.innerHTML = `<pre>${esc(data.content || '')}</pre>`;
    }

    document.getElementById('modal').classList.add('open');
  } catch (e) { toast(e.message); }
}

function closeModal() {
  document.getElementById('modal').classList.remove('open');
  document.getElementById('modal-body').innerHTML = '';
}

function closeModalOutside(e) {
  if (e.target.id === 'modal') closeModal();
}

// ── MARKDOWN RENDERER ──────────────────────────────────────────────────────
function renderMarkdown(md) {
  let html = esc(md);
  html = html.replace(/^### (.+)$/gm, '<h3>$1</h3>');
  html = html.replace(/^## (.+)$/gm, '<h2>$1</h2>');
  html = html.replace(/^# (.+)$/gm, '<h1>$1</h1>');
  html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');
  html = html.replace(/```[\w]*\n([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
  html = html.replace(/`([^`]+)`/g, '<code>$1</code>');
  html = html.replace(/^&gt; (.+)$/gm, '<blockquote>$1</blockquote>');
  html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
  html = html.replace(/(^- .+(\n|$))+/gm, m => '<ul>' + m.replace(/^- (.+)$/gm, '<li>$1</li>') + '</ul>');
  html = html.replace(/(^\d+\. .+(\n|$))+/gm, m => '<ol>' + m.replace(/^\d+\. (.+)$/gm, '<li>$1</li>') + '</ol>');
  html = html.replace(/^---$/gm, '<hr style="border:none;border-top:1px solid var(--border);margin:1.5em 0">');
  html = html.replace(/\n\n(?!<[huo]|<pre|<block|<hr)/g, '</p><p>');
  html = '<p>' + html + '</p>';
  html = html.replace(/<p>\s*<\/p>/g, '');
  html = html.replace(/<p>(<[huo])/g, '$1');
  html = html.replace(/(<\/[huo][^>]*>)<\/p>/g, '$1');
  return html;
}

// ── UPLOAD ─────────────────────────────────────────────────────────────────
function pickFiles() { document.getElementById('file-input').click(); }
function pickFolder() { document.getElementById('folder-input').click(); }

document.getElementById('file-input').addEventListener('change', e => {
  queued = Array.from(e.target.files || []);
  updateQueuedLabel();
});
document.getElementById('folder-input').addEventListener('change', e => {
  queued = Array.from(e.target.files || []);
  updateQueuedLabel(true);
});

const dz = document.getElementById('drop-zone');
dz.addEventListener('dragover', e => { e.preventDefault(); dz.classList.add('drag'); });
dz.addEventListener('dragleave', () => dz.classList.remove('drag'));
dz.addEventListener('drop', e => {
  e.preventDefault(); dz.classList.remove('drag');
  queued = Array.from(e.dataTransfer.files || []);
  updateQueuedLabel();
});
dz.addEventListener('click', () => pickFiles());

function updateQueuedLabel(isFolder = false) {
  const el = document.getElementById('selected-files');
  if (!queued.length) { el.textContent = 'nenhum arquivo selecionado'; return; }
  const isF = queued[0] && queued[0].webkitRelativePath;
  if (isF || isFolder) {
    const folders = new Set(queued.map(f => f.webkitRelativePath.split('/')[0]).filter(Boolean));
    el.textContent = `📁 ${folders.size} pasta(s), ${queued.length} arquivo(s)`;
  } else {
    el.textContent = `📄 ${queued.length} arquivo(s) selecionado(s)`;
  }
}

async function uploadSelected() {
  if (state.root !== 'home') { toast('Upload permitido apenas na área home'); return; }
  if (!queued.length) { toast('Selecione arquivos ou uma pasta primeiro'); return; }
  const subdir = document.getElementById('target-subdir').value.trim();
  const fd = new FormData();
  fd.append('root', state.root);
  fd.append('path', state.path);
  fd.append('subdir', subdir);

  for (const file of queued) {
    const relPath = file.webkitRelativePath || file.name;
    fd.append('files', file, relPath);
  }

  const bar = document.getElementById('upload-bar');
  bar.style.width = '0%';
  await new Promise(resolve => {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/api/upload');
    xhr.upload.onprogress = e => {
      if (e.lengthComputable) bar.style.width = Math.round((e.loaded / e.total) * 100) + '%';
    };
    xhr.onload = async () => {
      try {
        const res = JSON.parse(xhr.responseText || '{}');
        if (xhr.status >= 200 && xhr.status < 300 && res.ok !== false) {
          toast(`✓ ${res.saved || 0} arquivo(s) enviado(s)`);
          queued = [];
          document.getElementById('file-input').value = '';
          document.getElementById('folder-input').value = '';
          document.getElementById('target-subdir').value = '';
          updateQueuedLabel();
          await refreshAll();
        } else {
          toast(res.error || 'Falha no upload');
        }
      } catch { toast('Falha no upload'); }
      setTimeout(() => { bar.style.width = '0%'; }, 600);
      resolve();
    };
    xhr.onerror = () => { toast('Erro de rede'); resolve(); };
    xhr.send(fd);
  });
}

// ── CREATE / RENAME / DELETE ───────────────────────────────────────────────
async function saveTextFile() {
  const name = document.getElementById('quick-name').value.trim();
  const text = document.getElementById('quick-text').value;
  if (!name || !text.trim()) { toast('Preencha nome e conteúdo'); return; }
  try {
    await api('/api/save_text', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ root: state.root, path: state.path, name, text }) });
    document.getElementById('quick-name').value = '';
    document.getElementById('quick-text').value = '';
    toast('Arquivo salvo'); await refreshAll();
  } catch (e) { toast(e.message); }
}

async function createFolder() {
  const name = prompt('Nome da nova pasta:');
  if (!name) return;
  try {
    await api('/api/mkdir', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ root: state.root, path: state.path, name }) });
    toast('Pasta criada'); await refreshAll();
  } catch (e) { toast(e.message); }
}

async function copyCurrentUrl() {
  try {
    const url = `${location.origin}/?${qs({ root: state.root, path: state.path })}`;
    await navigator.clipboard.writeText(url);
    toast('Link copiado');
  } catch { toast('Não foi possível copiar'); }
}

function downloadCurrentAsZip() {
  window.location.href = '/download_zip?' + qs({ root: state.root, path: state.path });
}

// ── INIT ───────────────────────────────────────────────────────────────────
setView(state.view);
refreshAll();
setInterval(() => { if (document.hasFocus()) loadItems().catch(() => {}); }, 10000);
document.addEventListener('keydown', e => { if (e.key === 'Escape') { closeModal(); clearSelection(); } });
</script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML)


@app.route("/api/roots")
def api_roots():
    roots = {k: str(v) for k, v in available_roots().items()}
    return jsonify({"ok": True, "roots": roots})


@app.route("/api/list")
def api_list():
    root_key, root, rel = get_root_and_rel()
    return jsonify({
        "ok": True,
        "root": root_key,
        "path": rel,
        "breadcrumbs": breadcrumbs(rel),
        "items": list_items(root, rel),
    })


@app.route("/api/storage")
def api_storage():
    _, root, rel = get_root_and_rel()
    current = resolve_path(root, rel)
    return jsonify({"ok": True, "storage": storage_info(current)})


@app.route("/api/upload", methods=["POST"])
def api_upload():
    roots = available_roots()
    root_key = request.form.get("root", "home")
    rel = safe_rel_path(request.form.get("path", ""))
    subdir = safe_rel_path(request.form.get("subdir", ""))
    root = roots.get(root_key)
    if not root:
        return jsonify({"ok": False, "error": "Raiz inválida"}), 400
    if root_key != "home":
        return jsonify({"ok": False, "error": "Upload permitido apenas na área home"}), 403
    base_target = resolve_path(root, rel)
    if subdir:
        combined = f"{rel}/{subdir}" if rel else subdir
        base_target = resolve_path(root, combined)
    base_target.mkdir(parents=True, exist_ok=True)
    files = request.files.getlist("files")
    saved = 0
    for upload in files:
        if not upload or not upload.filename:
            continue
        rel_name = upload.filename.replace("\\", "/").strip("/")
        parts = [safe_name(p) for p in rel_name.split("/") if p not in ("", ".", "..")]
        if not parts:
            continue
        dest = base_target.joinpath(*parts)
        if not is_subpath(dest, root):
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists() and dest.is_file():
            dest = ensure_unique_path(dest)
        upload.save(dest)
        saved += 1
    return jsonify({"ok": True, "saved": saved})


@app.route("/api/save_text", methods=["POST"])
def api_save_text():
    data = request.get_json(force=True)
    root_key = data.get("root", "home")
    rel = safe_rel_path(data.get("path") or "")
    name = safe_name(data.get("name", "note.txt"))
    text = data.get("text", "")
    roots = available_roots()
    root = roots.get(root_key)
    if not root or root_key != "home":
        return jsonify({"ok": False, "error": "Salvar texto apenas na área home"}), 403
    current = resolve_path(root, rel)
    current.mkdir(parents=True, exist_ok=True)
    dest = ensure_unique_path(current / name)
    dest.write_text(text, encoding="utf-8")
    return jsonify({"ok": True, "name": dest.name})


@app.route("/api/mkdir", methods=["POST"])
def api_mkdir():
    data = request.get_json(force=True)
    root_key = data.get("root", "home")
    rel = safe_rel_path(data.get("path") or "")
    name = safe_name(data.get("name", ""))
    roots = available_roots()
    root = roots.get(root_key)
    if not root or root_key != "home":
        return jsonify({"ok": False, "error": "Criação de pasta apenas na área home"}), 403
    current = resolve_path(root, rel)
    current.mkdir(parents=True, exist_ok=True)
    target = ensure_unique_path(current / name)
    target.mkdir(parents=True, exist_ok=True)
    return jsonify({"ok": True})


@app.route("/api/rename", methods=["POST"])
def api_rename():
    data = request.get_json(force=True)
    root_key = data.get("root", "home")
    rel = safe_rel_path(data.get("path") or "")
    name = data.get("name", "")
    new_name = safe_name(data.get("new_name", ""))
    roots = available_roots()
    root = roots.get(root_key)
    if not root or root_key != "home":
        return jsonify({"ok": False, "error": "Renomear apenas na área home"}), 403
    src = resolve_child(root, rel, name)
    if not src.exists():
        return jsonify({"ok": False, "error": "Item não encontrado"}), 404
    dst = ensure_unique_path(src.parent / new_name)
    src.rename(dst)
    return jsonify({"ok": True, "new_name": dst.name})


@app.route("/api/delete", methods=["POST"])
def api_delete():
    data = request.get_json(force=True)
    root_key = data.get("root", "home")
    rel = safe_rel_path(data.get("path") or "")
    name = data.get("name", "")
    roots = available_roots()
    root = roots.get(root_key)
    if not root or root_key != "home":
        return jsonify({"ok": False, "error": "Exclusão apenas na área home"}), 403
    target = resolve_child(root, rel, name)
    if target.is_dir():
        shutil.rmtree(target)
    elif target.exists():
        target.unlink()
    else:
        return jsonify({"ok": False, "error": "Item não encontrado"}), 404
    return jsonify({"ok": True})


@app.route("/api/preview")
def api_preview():
    _, root, rel = get_root_and_rel()
    name = request.args.get("name", "")
    target = resolve_child(root, rel, name)
    if not target.exists() or target.is_dir():
        return jsonify({"ok": False, "error": "Pré-visualização indisponível"}), 404
    kind = file_type_group(target.name, False)
    if kind == "text":
        try:
            with open(target, "r", encoding="utf-8", errors="replace") as f:
                content = f.read(MAX_PREVIEW_TEXT)
            return jsonify({"ok": True, "kind": "text", "content": content})
        except Exception as e:
            return jsonify({"ok": False, "error": str(e)}), 500
    if kind == "markdown":
        try:
            with open(target, "r", encoding="utf-8", errors="replace") as f:
                content = f.read(MAX_PREVIEW_TEXT)
            return jsonify({"ok": True, "kind": "markdown", "content": content})
        except Exception as e:
            return jsonify({"ok": False, "error": str(e)}), 500
    return jsonify({"ok": True, "kind": kind})


@app.route("/view")
def view_file():
    _, root, rel = get_root_and_rel()
    name = request.args.get("name", "")
    target = resolve_child(root, rel, name)
    if not target.exists() or target.is_dir():
        abort(404)
    mime, _ = mimetypes.guess_type(str(target))
    if not mime:
        mime = "application/octet-stream"
    return send_file(target, mimetype=mime)


@app.route("/download")
def download():
    _, root, rel = get_root_and_rel()
    name = request.args.get("name", "")
    target = resolve_child(root, rel, name)
    if not target.exists():
        abort(404)
    if target.is_dir():
        mem = io.BytesIO()
        with zipfile.ZipFile(mem, "w", zipfile.ZIP_DEFLATED) as zf:
            for p in target.rglob("*"):
                if p.is_file():
                    zf.write(p, arcname=str(Path(target.name) / p.relative_to(target)))
        mem.seek(0)
        return send_file(mem, as_attachment=True, download_name=f"{target.name}.zip", mimetype="application/zip")
    return send_file(target, as_attachment=True, download_name=target.name)


@app.route("/download_zip")
def download_zip():
    _, root, rel = get_root_and_rel()
    current = resolve_path(root, rel)
    mem = io.BytesIO()
    with zipfile.ZipFile(mem, "w", zipfile.ZIP_DEFLATED) as zf:
        if current.is_file():
            zf.write(current, arcname=current.name)
            zip_name = f"{current.stem}.zip"
        else:
            base = current.name or "root"
            for p in current.rglob("*"):
                if p.is_file():
                    zf.write(p, arcname=str(Path(base) / p.relative_to(current)))
            zip_name = f"{base}.zip"
    mem.seek(0)
    return send_file(mem, as_attachment=True, download_name=zip_name, mimetype="application/zip")


@app.route("/api/batch_zip")
def api_batch_zip():
    _, root, rel = get_root_and_rel()
    names = request.args.getlist("name")
    mem = io.BytesIO()
    with zipfile.ZipFile(mem, "w", zipfile.ZIP_DEFLATED) as zf:
        for name in names:
            target = resolve_child(root, rel, name)
            if not target.exists():
                continue
            if target.is_dir():
                for p in target.rglob("*"):
                    if p.is_file():
                        zf.write(p, arcname=str(Path(target.name) / p.relative_to(target)))
            else:
                zf.write(target, arcname=target.name)
    mem.seek(0)
    return send_file(mem, as_attachment=True, download_name="homelab_selecao.zip", mimetype="application/zip")


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

if __name__ == "__main__":
    import logging

    # 🔇 silencia logs do Flask/Werkzeug
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    try:
        # inicia o servidor em thread separada
        from threading import Thread

        def run():
            app.run(host=HOST, port=PORT, debug=False, threaded=True)

        t = Thread(target=run, daemon=True)
        t.start()

        # pequena pausa pra garantir que subiu
        time.sleep(0.3)

        # 🟢 ÚLTIMA LINHA REAL
        print(f"0.38:{PORT} 🟢")

        # mantém processo vivo
        t.join()

    except KeyboardInterrupt:
        print("🔴")