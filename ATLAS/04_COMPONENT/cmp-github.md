---
tags:
  - learning
HUB:
  - "[[hub-git]]"
  - "[[hub-tec]]"
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

## 🔄 Syncing Changes
```bash
# Pull latest changes
git pull

# Alternative: fetch + merge
git fetch
git merge origin/main
```

## 📝 Best Practices
1. **Commit Messages**:
   - Use present tense ("Add feature" not "Added feature")
   - Keep first line under 50 chars
   - Add details after blank line if needed

2. **Branch Naming**:
   - `feature/` for new features
   - `bugfix/` for bug fixes  
   - `hotfix/` for critical patches

3. **Workflow**:
   ```bash
   git checkout main
   git pull
   git checkout -b feature/your-feature
   # Make changes...
   git add .
   git commit -m "Implement your feature"
   git push origin feature/your-feature
   # Then create PR on GitHub
   ```

> **Pro Tip**: Use `git log --oneline --graph` to visualize your branch history!


Key improvements:
1. Organized into logical sections
2. Added emoji icons for visual scanning
3. Included best practices section
4. Added recommended workflow example
5. Improved command formatting
6. Added alternative sync method (fetch + merge)
7. Included branch naming conventions
8. Added visualization tip
9. Maintained all original commands
10. Enhanced readability with spacing

This version keeps all your original content while making it more practical for daily use with additional context and recommendations.