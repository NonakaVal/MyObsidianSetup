---
file_path: "/home/val/.vscode/extensions/sirwanafifi.obsidian-clipper-0.0.1/src/commands/registerCommands.ts"
location: "lines 126-132"
priority: "Low"
scope: "Documentation"
clipped_at: "2026-04-16T12:45:52.021Z"
tags: [clipped]
---

Implement a feature to prompt the user to select a priority level ("High", "Medium", "Low") using a dropdown, and handle the case where no selection is made.

[open the code](vscode://file/%2Fhome%2Fval%2F.vscode%2Fextensions%2Fsirwanafifi.obsidian-clipper-0.0.1%2Fsrc%2Fcommands%2FregisterCommands.ts:126)

```typescript
      const priority = await vscode.window.showQuickPick(
        ["High", "Medium", "Low"],
        { placeHolder: "Priority" }
      );
      if (!priority) {
        return;
      }
```