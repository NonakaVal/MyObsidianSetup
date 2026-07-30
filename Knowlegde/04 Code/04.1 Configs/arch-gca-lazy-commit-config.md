---
related:
  - "[[Lazy Commits]]"
subject:
  - "[[hub-git]]"
  - "[[hub-linux]]"
tags:
  - config
---
```bash
nano ~/gca.py
```

Cole o código do script e adicione no topo:
[[arch-gca.py]]

```python
#!/usr/bin/env python3
```

Depois:


```bash
chmod +x ~/gca.py
```

2️⃣ Torne o comando global:

```bash
mkdir -p ~/.local/bin
ln -s ~/gca.py ~/.local/bin/gca
```

3️⃣ Garanta que `~/.local/bin` está no seu PATH:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```
