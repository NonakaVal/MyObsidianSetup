```dataviewjs
//-----------------------------------------------------------
// 🧩 DETECTOR DE LINKS NÃO CRIADOS (saída melhorada)
//-----------------------------------------------------------

const minRefs = 2;
let d = {};

const ignoredFolders = ["X"];

function isIgnored(path) {
  return ignoredFolders.some(f =>
    path.toLowerCase().includes(f.toLowerCase())
  );
}

function linkInFrontmatter(file, link) {
  const cache = app.metadataCache.getCache(file);
  if (!cache?.frontmatterLinks) return false;
  return cache.frontmatterLinks.some(l => l.link === link);
}

function process(origin, targets) {
  if (isIgnored(origin)) return;

  Object.keys(targets).forEach(target => {
    if (isIgnored(target)) return;
    if (linkInFrontmatter(origin, target)) return;

    if (!d[target]) d[target] = [];
    d[target].push(dv.fileLink(origin));
  });
}

Object.entries(dv.app.metadataCache.unresolvedLinks)
  .filter(([k, v]) => !isIgnored(k) && Object.keys(v).length)
  .forEach(([k, v]) => process(k, v));

// ---------- SAÍDA ----------
dv.table(
  ["📄 Nota inexistente", "🔢", "🔗"],
  Object.entries(d)
    .filter(([_, v]) => v.length >= minRefs)
    .sort((a, b) =>
      b[1].length - a[1].length || a[0].localeCompare(b[0])
    )
    .map(([note, refs]) => [
      dv.fileLink(note),
      refs.length >= 5 ? `🔥 ${refs.length}` : refs.length,
      refs.join("<br>")
    ])
);

```