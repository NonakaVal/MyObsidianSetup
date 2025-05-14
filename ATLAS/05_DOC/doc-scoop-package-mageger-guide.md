---
tags:
  - doc
HUB:
  - "[[hub-tec]]"
---
https://scoop.sh/
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri [https://get.scoop.sh/](https://get.scoop.sh/ "https://get.scoop.sh/") | Invoke-Expression
scoop bucket add extras
scoop install mpv
scoope install ani-cli
scoop install fzf
```

# **Scoop Package Manager Guide**  

Scoop is a **command-line package manager** for Windows that simplifies the installation and management of software. Unlike traditional installers, Scoop:  
✅ **Installs apps without admin rights** (by default, to `~/scoop`)  
✅ **Manages dependencies automatically**  
✅ **Avoids cluttering the system** (apps are isolated in their own directories)  
✅ **Supports buckets** (repositories for different types of software)  

---

## **🛠️ Installation Steps**  

### **1️⃣ Enable Script Execution (One-Time Setup)**
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
- **Why?** Windows restricts script execution by default. This command allows trusted scripts (like Scoop’s installer) to run.  
- `RemoteSigned` = Allows local scripts + downloaded scripts with trusted signatures.  
- `-Scope CurrentUser` = Applies only to your account (no admin needed).  

---

### **2️⃣ Install Scoop**
```powershell
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```
- Downloads and runs the Scoop installer.  
- Installs to `~\scoop` (user directory).  

---

### **3️⃣ Add Buckets (App Repositories)**
```powershell
scoop bucket add extras
```
- **Buckets** = Collections of software (like package repositories in Linux).  
- `main` → Default bucket (basic CLI tools).  
- `extras` → Popular GUI apps (MPV, VLC, etc.).  
- Other useful buckets:  
  ```powershell
  scoop bucket add versions  # For multiple versions (Python, Node.js)
  scoop bucket add nerd-fonts  # Fonts for developers
  ```

---

### **4️⃣ Install Apps**
```powershell
scoop install mpv ani-cli fzf
```
- **MPV**: Lightweight, powerful media player.  
- **ani-cli**: Watch anime from the terminal.  
- **fzf**: Fuzzy finder (search files/commands quickly).  

#### **Other Useful Apps**
```powershell
scoop install git 7zip neovim sudo
```
- `sudo` → Run commands as admin when needed.  
- `git` → Version control.  
- `neovim` → Modern Vim editor.  

---

## **🔧 Common Commands**
| Command | Description |
|---------|-------------|
| `scoop search <app>` | Search for apps |
| `scoop install <app>` | Install an app |
| `scoop update *` | Update all apps |
| `scoop list` | List installed apps |
| `scoop uninstall <app>` | Remove an app |
| `scoop cleanup <app>` | Remove old versions |

---

## **⚡ Pro Tips**
1. **Faster Searches**  
   ```powershell
   scoop search | fzf  # Interactive fuzzy search
   ```
2. **Fix Issues**  
   ```powershell
   scoop cache rm *  # Clear download cache
   scoop cleanup *   # Remove old versions
   ```
3. **Install GUI Apps Without UAC Prompts**  
   ```powershell
   scoop install sudo
   sudo scoop install <app> --global  # Install for all users
   ```

---

## **🚀 Why Use Scoop?**
✔ **No Admin Rights Needed** (installs in user space)  
✔ **No Bloatware** (apps are isolated)  
✔ **Easy Updates** (`scoop update *` updates everything)  
✔ **Great for Developers** (CLI tools, programming languages, etc.)  

Try it out! 🚀  

> **Note**: If you prefer a GUI, check out **[Scoop's "scoop-search"](https://github.com/shilangyu/scoop-search)** for a visual app browser.
