---
file_path: "/home/val/.vscode/extensions/sirwanafifi.obsidian-clipper-0.0.1/src/commands/registerCommands.ts"
location: "lines 134-140"
priority: "Low"
scope: "Documentation"
clipped_at: "2026-04-16T12:44:59.494Z"
tags: [clipped]
---

Implement a quick pick menu in Visual Studio Code to select a development scope, with options for "Frontend," "Backend," "FullStack," "DevOps," and "Documentation."

[open the code](vscode://file/%2Fhome%2Fval%2F.vscode%2Fextensions%2Fsirwanafifi.obsidian-clipper-0.0.1%2Fsrc%2Fcommands%2FregisterCommands.ts:134)

```typescript
      const scope = await vscode.window.showQuickPick(
        ["Frontend", "Backend", "FullStack", "DevOps", "Documentation"],
        { placeHolder: "Scope" }
      );
      if (!scope) {
        return;
      }
```