---
created: "[[2025-06-14]]"
HUB:
  - "[[hub-regex]]"
  - "[[hub-linux]]"
connections:
  - "[[flow-build-setup-codeSearch-with-ripgrep-fzf-bat]]"
tags:
  - learning
  - workflow
---

## Advanced Workflows
```bash
# Multi-language search (run in sequence)
search_def "Database" go    # Check Go interfaces
search_def "Database" py    # Check Python classes
search_def "Database" java  # Check Java interfaces

# Find configuration patterns across different file types
search_all "timeout" yml
search_all "timeout" json
search_all "timeout" toml

# Audit security-related code
search_code "password" 
search_code "token"
search_todos "SECURITY"

# Refactoring helpers
search_def "Legacy"        # Find all legacy components
search_code "@deprecated"  # Find deprecated usage
```

← Parte de [[flow-build-setup-codeSearch-with-ripgrep-fzf-bat]]