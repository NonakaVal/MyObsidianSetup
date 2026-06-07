```dataviewjs
const TERMO        = "<% tp.system.prompt("Termo de busca")%>";  // ← altere aqui
const PASTA        = "";                // ← pasta ou vazio para vault todo
const LINHAS_CTX   = 9;                 // ← linhas antes/depois de cada ocorrência

const esc = s => s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
const re  = new RegExp(TERMO.replace(/[.*+?^${}()|[\]\\]/g,"\\$&"), "gi");

// ── coleta ────────────────────────────────────────────────────────────────────
const resultados = [];
for (const p of dv.pages(PASTA ? `"${PASTA}"` : "")) {
  const raw = await dv.io.load(p.file.path);
  if (!raw) continue;
  const linhas = raw.replace(/^---[\s\S]*?---\n?/,"").split("\n");
  let secao = "", ocs = [];

  for (let i = 0; i < linhas.length; i++) {
    const l = linhas[i];
    const hd = l.match(/^#{1,6}\s+(.+)/);
    if (hd) { secao = hd[1]; continue; }
    if (!re.test(l)) { re.lastIndex = 0; continue; }
    re.lastIndex = 0;

    // janela de linhas: [antes] [hit] [depois]
    const ini = Math.max(0, i - LINHAS_CTX);
    const fim = Math.min(linhas.length - 1, i + LINHAS_CTX);
    const ctx = [];
    for (let j = ini; j <= fim; j++) {
      const txt   = linhas[j].replace(/\*\*|__|~~|`/g,"");
      const isHit = j === i;
      if (!isHit) { ctx.push({ n: j+1, txt, isHit: false }); continue; }

      // destaca termo na linha hit
      const idx = txt.search(new RegExp(TERMO.replace(/[.*+?^${}()|[\]\\]/g,"\\$&"),"i"));
      if (idx < 0) { ctx.push({ n: j+1, txt, isHit: true }); continue; }
      ctx.push({
        n: j+1, isHit: true,
        pre: txt.slice(0, idx),
        mid: txt.slice(idx, idx + TERMO.length),
        pos: txt.slice(idx + TERMO.length)
      });
    }
    ocs.push({ secao: secao || "—", ctx });
  }
  if (ocs.length) resultados.push({ p, ocs });
}

// ── render ────────────────────────────────────────────────────────────────────
const total = resultados.reduce((a,r) => a + r.ocs.length, 0);
const wrap  = dv.el("div","");
wrap.style.cssText = "background:rgba(10,12,20,0.97);border-radius:8px;padding:12px 14px;color:#fff;width:100%;box-sizing:border-box;font-family:inherit";

// cabeçalho global
wrap.innerHTML = `
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
    <span style="font-size:.85em;font-weight:700;color:#38bdf8">🔍 "<span style="color:#facc15">${esc(TERMO)}</span>"</span>
    <span style="font-size:.65em;opacity:.35">${resultados.length} nota${resultados.length!==1?"s":""} · ${total} ocorrência${total!==1?"s":""}${PASTA?" · 📁 "+PASTA:""}</span>
  </div>`;

if (!resultados.length) {
  wrap.innerHTML += `<div style="font-size:.8em;opacity:.3;text-align:center;padding:10px 0">Nenhuma ocorrência encontrada.</div>`;
  dv.container.appendChild(wrap); return;
}

// uma seção colapsável por nota
for (const { p, ocs } of resultados) {
  const url    = `obsidian://open?vault=${encodeURIComponent(app.vault.getName())}&file=${encodeURIComponent(p.file.path)}`;
  const bloco  = document.createElement("div");
  bloco.style.cssText = "border-top:1px solid rgba(255,255,255,.06);margin-top:6px;padding-top:6px";

  // ── header clicável ────────────────────────────────────────────────────────
  const header = document.createElement("div");
  header.style.cssText = "display:flex;align-items:center;justify-content:space-between;cursor:pointer;padding:4px 0;user-select:none";
  header.innerHTML = `
    <div style="display:flex;align-items:center;gap:8px">
      <span class="chevron" style="font-size:.7em;opacity:.5;transition:transform .2s">▶</span>
      <a href="${url}" onclick="event.stopPropagation()"
         style="color:#38bdf8;font-size:.85em;font-weight:700;text-decoration:none"
         onmouseover="this.style.textDecoration='underline'" onmouseout="this.style.textDecoration='none'">
        📄 ${esc(p.file.name)}</a>
    </div>
    <span style="font-size:.62em;opacity:.28">${ocs.length} ocorrência${ocs.length>1?"s":""}</span>`;

  // ── corpo (ocorrências) ────────────────────────────────────────────────────
  const corpo = document.createElement("div");
  corpo.style.cssText = "display:none;padding-top:6px";

  let secAnterior = null;
  for (const oc of ocs) {
    // label de seção quando muda
    if (oc.secao !== secAnterior) {
      secAnterior = oc.secao;
      const secEl = document.createElement("div");
      secEl.style.cssText = "font-size:.62em;color:#818cf8;margin:8px 0 3px;opacity:.8";
      secEl.textContent   = `§ ${oc.secao}`;
      corpo.appendChild(secEl);
    }

    // bloco de linhas de contexto
    const ctxBloco = document.createElement("div");
    ctxBloco.style.cssText = "border-left:2px solid rgba(129,140,248,.18);padding:4px 0 4px 10px;margin-bottom:6px";

    for (const ln of oc.ctx) {
      const row = document.createElement("div");
      row.style.cssText = `display:flex;gap:8px;align-items:baseline;padding:1px 0;${ln.isHit?"background:rgba(250,204,21,.04);border-radius:3px":"opacity:.45"}`;

      const num = document.createElement("span");
      num.style.cssText = "font-size:.58em;opacity:.4;flex-shrink:0;min-width:28px;text-align:right;font-variant-numeric:tabular-nums";
      num.textContent = `${ln.n}`;

      const txt = document.createElement("span");
      txt.style.cssText = `font-size:.78em;line-height:1.6;white-space:pre-wrap;word-break:break-word`;
      if (ln.isHit && ln.mid) {
        txt.innerHTML = esc(ln.pre) +
          `<mark style="background:#facc1522;color:#facc15;border-radius:2px;padding:0 2px;font-weight:700">${esc(ln.mid)}</mark>` +
          esc(ln.pos);
      } else {
        txt.textContent = ln.txt;
      }

      row.appendChild(num); row.appendChild(txt);
      ctxBloco.appendChild(row);
    }
    corpo.appendChild(ctxBloco);
  }

  // ── toggle collapse ────────────────────────────────────────────────────────
  let aberto = false;
  header.addEventListener("click", () => {
    aberto = !aberto;
    corpo.style.display        = aberto ? "block" : "none";
    header.querySelector(".chevron").style.transform = aberto ? "rotate(90deg)" : "rotate(0deg)";
  });

  bloco.appendChild(header);
  bloco.appendChild(corpo);
  wrap.appendChild(bloco);
}

dv.container.appendChild(wrap);
```
