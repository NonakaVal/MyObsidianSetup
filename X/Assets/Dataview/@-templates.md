````tabs
tab: Format
```dataviewjs
const folderPath = "X/Template/Format";
let sortMode = "date";
let ascending = false;

const root = dv.el("div", "");
root.style.cssText = `
  background: #0d1117; border: 1px solid #21262d;
  padding: 12px 16px; border-radius: 10px;
  color: #e6edf3; font-size: 0.5rem; box-shadow: 0 2px 8px #00000040;
`;

const bar = document.createElement("div");
bar.style.cssText = "display:flex;align-items:center;gap:8px;margin-bottom:10px;flex-wrap:wrap";

const limitInput = document.createElement("input");
limitInput.type = "number"; limitInput.value = 100;
limitInput.style.cssText = `width:54px;background:#21262d;border:1px solid #30363d;
  border-radius:5px;color:#e6edf3;font-size:.8rem;padding:3px 6px`;

const btnStyle = (a) => `cursor:pointer;padding:3px 10px;border-radius:5px;font-size:.78rem;
  border:1px solid #30363d;color:#e6edf3;background:${a?"#1f6feb":"#21262d"}`;

const sortNameBtn = document.createElement("button");
sortNameBtn.textContent = "Nome ⬇️"; sortNameBtn.style.cssText = btnStyle(false);
const sortDateBtn = document.createElement("button");
sortDateBtn.textContent = "Data ⬇️"; sortDateBtn.style.cssText = btnStyle(true);

const counter = document.createElement("span");
counter.style.cssText = "margin-left:auto;color:#484f58;font-size:.75rem";

bar.append(limitInput, sortNameBtn, sortDateBtn, counter);
root.appendChild(bar);

const box = document.createElement("div");
root.appendChild(box);

function render() {
  const limit = parseInt(limitInput.value) || 100;
  let pages = dv.pages().where(p => p.file.path.startsWith(folderPath + "/")).array();

  pages.sort((a, b) => {
    if (sortMode === "name") {
      const na = a.file.name.toLowerCase(), nb = b.file.name.toLowerCase();
      return ascending ? na.localeCompare(nb) : nb.localeCompare(na);
    }
    const va = a.file.mtime?.ts || 0, vb = b.file.mtime?.ts || 0;
    return ascending ? va - vb : vb - va;
  });

  pages = pages.slice(0, limit);
  counter.textContent = `${pages.length} item${pages.length !== 1 ? "s" : ""}`;
  box.innerHTML = "";

  pages.forEach(p => {
    const row = document.createElement("div");
    row.style.cssText = `padding:5px 4px;border-top:1px solid #21262d;
      font-size:1rem;transition:background .1s;white-space:nowrap;
      overflow:hidden;text-overflow:ellipsis`;
    row.onmouseenter = () => row.style.background = "#161b22";
    row.onmouseleave = () => row.style.background = "";
    row.appendChild(dv.el("span", p.file.link));
    box.appendChild(row);
  });
}

limitInput.onchange = render;
sortNameBtn.onclick = () => {
  ascending = sortMode === "name" ? !ascending : false;
  sortMode = "name";
  sortNameBtn.textContent = `Nome ${ascending ? "⬆️" : "⬇️"}`;
  sortDateBtn.textContent = "Data ⬇️";
  sortNameBtn.style.cssText = btnStyle(true);
  sortDateBtn.style.cssText  = btnStyle(false);
  render();
};
sortDateBtn.onclick = () => {
  ascending = sortMode === "date" ? !ascending : false;
  sortMode = "date";
  sortDateBtn.textContent = `Data ${ascending ? "⬆️" : "⬇️"}`;
  sortNameBtn.textContent = "Nome ⬇️";
  sortDateBtn.style.cssText  = btnStyle(true);
  sortNameBtn.style.cssText = btnStyle(false);
  render();
};

render();
```

tab: Snippets
```dataviewjs
const folderPath = "X/Template/Snippet";
let sortMode = "date";
let ascending = false;

const root = dv.el("div", "");
root.style.cssText = `
  background: #0d1117; border: 1px solid #21262d;
  padding: 12px 16px; border-radius: 10px;
  color: #e6edf3; font-size: 0.6rem; box-shadow: 0 2px 8px #00000040;
`;

const bar = document.createElement("div");
bar.style.cssText = "display:flex;align-items:center;gap:8px;margin-bottom:10px;flex-wrap:wrap";

const limitInput = document.createElement("input");
limitInput.type = "number"; limitInput.value = 100;
limitInput.style.cssText = `width:54px;background:#21262d;border:1px solid #30363d;
  border-radius:5px;color:#e6edf3;font-size:.8rem;padding:3px 6px`;

const btnStyle = (a) => `cursor:pointer;padding:3px 10px;border-radius:5px;font-size:.78rem;
  border:1px solid #30363d;color:#e6edf3;background:${a?"#1f6feb":"#21262d"}`;

const sortNameBtn = document.createElement("button");
sortNameBtn.textContent = "Nome ⬇️"; sortNameBtn.style.cssText = btnStyle(false);
const sortDateBtn = document.createElement("button");
sortDateBtn.textContent = "Data ⬇️"; sortDateBtn.style.cssText = btnStyle(true);

const counter = document.createElement("span");
counter.style.cssText = "margin-left:auto;color:#484f58;font-size:.75rem";

bar.append(limitInput, sortNameBtn, sortDateBtn, counter);
root.appendChild(bar);

const box = document.createElement("div");
root.appendChild(box);

function render() {
  const limit = parseInt(limitInput.value) || 100;
  let pages = dv.pages().where(p => p.file.path.startsWith(folderPath + "/")).array();

  pages.sort((a, b) => {
    if (sortMode === "name") {
      const na = a.file.name.toLowerCase(), nb = b.file.name.toLowerCase();
      return ascending ? na.localeCompare(nb) : nb.localeCompare(na);
    }
    const va = a.file.mtime?.ts || 0, vb = b.file.mtime?.ts || 0;
    return ascending ? va - vb : vb - va;
  });

  pages = pages.slice(0, limit);
  counter.textContent = `${pages.length} item${pages.length !== 1 ? "s" : ""}`;
  box.innerHTML = "";

  pages.forEach(p => {
    const row = document.createElement("div");
    row.style.cssText = `padding:5px 4px;border-top:1px solid #21262d;
      font-size:1rem;transition:background .1s;white-space:nowrap;
      overflow:hidden;text-overflow:ellipsis`;
    row.onmouseenter = () => row.style.background = "#161b22";
    row.onmouseleave = () => row.style.background = "";
    row.appendChild(dv.el("span", p.file.link));
    box.appendChild(row);
  });
}

limitInput.onchange = render;
sortNameBtn.onclick = () => {
  ascending = sortMode === "name" ? !ascending : false;
  sortMode = "name";
  sortNameBtn.textContent = `Nome ${ascending ? "⬆️" : "⬇️"}`;
  sortDateBtn.textContent = "Data ⬇️";
  sortNameBtn.style.cssText = btnStyle(true);
  sortDateBtn.style.cssText  = btnStyle(false);
  render();
};
sortDateBtn.onclick = () => {
  ascending = sortMode === "date" ? !ascending : false;
  sortMode = "date";
  sortDateBtn.textContent = `Data ${ascending ? "⬆️" : "⬇️"}`;
  sortNameBtn.textContent = "Nome ⬇️";
  sortDateBtn.style.cssText  = btnStyle(true);
  sortNameBtn.style.cssText = btnStyle(false);
  render();
};

render();
```

tab: Journaling
```dataviewjs
const folderPath = "X/Template/Journaling";
let sortMode = "date";
let ascending = false;

const root = dv.el("div", "");
root.style.cssText = `
  background: #0d1117; border: 1px solid #21262d;
  padding: 12px 16px; border-radius: 10px;
  color: #e6edf3; font-size: 0.6rem; box-shadow: 0 2px 8px #00000040;
`;

const bar = document.createElement("div");
bar.style.cssText = "display:flex;align-items:center;gap:8px;margin-bottom:10px;flex-wrap:wrap";

const limitInput = document.createElement("input");
limitInput.type = "number"; limitInput.value = 100;
limitInput.style.cssText = `width:54px;background:#21262d;border:1px solid #30363d;
  border-radius:5px;color:#e6edf3;font-size:.8rem;padding:3px 6px`;

const btnStyle = (a) => `cursor:pointer;padding:3px 10px;border-radius:5px;font-size:.78rem;
  border:1px solid #30363d;color:#e6edf3;background:${a?"#1f6feb":"#21262d"}`;

const sortNameBtn = document.createElement("button");
sortNameBtn.textContent = "Nome ⬇️"; sortNameBtn.style.cssText = btnStyle(false);
const sortDateBtn = document.createElement("button");
sortDateBtn.textContent = "Data ⬇️"; sortDateBtn.style.cssText = btnStyle(true);

const counter = document.createElement("span");
counter.style.cssText = "margin-left:auto;color:#484f58;font-size:.75rem";

bar.append(limitInput, sortNameBtn, sortDateBtn, counter);
root.appendChild(bar);

const box = document.createElement("div");
root.appendChild(box);

function render() {
  const limit = parseInt(limitInput.value) || 100;
  let pages = dv.pages().where(p => p.file.path.startsWith(folderPath + "/")).array();

  pages.sort((a, b) => {
    if (sortMode === "name") {
      const na = a.file.name.toLowerCase(), nb = b.file.name.toLowerCase();
      return ascending ? na.localeCompare(nb) : nb.localeCompare(na);
    }
    const va = a.file.mtime?.ts || 0, vb = b.file.mtime?.ts || 0;
    return ascending ? va - vb : vb - va;
  });

  pages = pages.slice(0, limit);
  counter.textContent = `${pages.length} item${pages.length !== 1 ? "s" : ""}`;
  box.innerHTML = "";

  pages.forEach(p => {
    const row = document.createElement("div");
    row.style.cssText = `padding:5px 4px;border-top:1px solid #21262d;
      font-size:1rem;transition:background .1s;white-space:nowrap;
      overflow:hidden;text-overflow:ellipsis`;
    row.onmouseenter = () => row.style.background = "#161b22";
    row.onmouseleave = () => row.style.background = "";
    row.appendChild(dv.el("span", p.file.link));
    box.appendChild(row);
  });
}

limitInput.onchange = render;
sortNameBtn.onclick = () => {
  ascending = sortMode === "name" ? !ascending : false;
  sortMode = "name";
  sortNameBtn.textContent = `Nome ${ascending ? "⬆️" : "⬇️"}`;
  sortDateBtn.textContent = "Data ⬇️";
  sortNameBtn.style.cssText = btnStyle(true);
  sortDateBtn.style.cssText  = btnStyle(false);
  render();
};
sortDateBtn.onclick = () => {
  ascending = sortMode === "date" ? !ascending : false;
  sortMode = "date";
  sortDateBtn.textContent = `Data ${ascending ? "⬆️" : "⬇️"}`;
  sortNameBtn.textContent = "Nome ⬇️";
  sortDateBtn.style.cssText  = btnStyle(true);
  sortNameBtn.style.cssText = btnStyle(false);
  render();
};

render();
```

````