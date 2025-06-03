---
tags:
  - learning
HUB:
  - "[[hub-git]]"
  - "[[System/HUB/hub-tec]]"
---

# Git Command Cheat Sheet

## 🛠️ Basic Setup
```bash
# Check Git version
git --version

# Initialize new repository
git init
```

## 📦 Staging & Committing
```bash
# Stage files (specific file or all changes)
git add <filename>  # or git add .

# Check current status
git status

# Commit staged changes
git commit -m "Descriptive message"
```

## ☁️ Remote Repositories
```bash
# Connect local repo to GitHub
git remote add origin <repository-url>

# Push to remote (first time)
git push -u origin main

# Subsequent pushes
git push
```

## 🌿 Branch Management
```bash
# Create and switch to new branch
git checkout -b feature/new-button

# Switch back to previous branch
git checkout -

# Push branch to remote
git push origin feature/new-button

# Merge branches (while on target branch)
git merge feature/new-button
```

