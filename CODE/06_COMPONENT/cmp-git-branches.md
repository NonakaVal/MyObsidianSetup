---
HUB:
  - "[[hub-git]]"
tags:
  - component
---
### **1. Criar uma nova branch**

Para criar uma branch, use o comando:

```bash
git branch nome-da-branch
```

> Isso cria uma nova branch, mas você permanecerá na branch atual.

---

### **2. Alternar para outra branch**

Para mudar para a branch criada:

```bash
git checkout nome-da-branch
```

Ou, em versões mais recentes do Git, você pode criar e alternar em um só passo:

```bash
git switch -c nome-da-branch
```

---

### **3. Listar branches**

Para ver todas as branches do repositório:

```bash
git branch
```

- A branch ativa será marcada com um asterisco (*).

---

### **4. Renomear uma branch**

Para renomear a branch atual:

```bash
git branch -m novo-nome
```

Se quiser renomear uma branch que não está ativa:

```bash
git branch -m nome-antigo novo-nome
```

---

### **5. Mesclar branches**

Para unir as alterações de uma branch na branch principal (geralmente `main` ou `master`):

1. Certifique-se de estar na branch principal:
    
    ```bash
    git checkout main
    ```
    
2. Faça a mesclagem:
    
    ```bash
    git merge nome-da-branch
    ```
    

---

### **6. Excluir branches**

Após terminar o trabalho em uma branch, você pode excluí-la:

- Para excluir uma branch local:
    
    ```bash
    git branch -d nome-da-branch
    ```
    
    Use `-D` para forçar a exclusão, caso haja alterações não mescladas.
    
- Para excluir uma branch remota:
    
    ```bash
    git push origin --delete nome-da-branch
    ```
    

---

### **7. Compartilhar uma branch**

Se você quiser enviar uma branch para o repositório remoto:

```bash
git push origin nome-da-branch
```

---

### **8. Atualizar uma branch com alterações da principal**

Mantenha sua branch atualizada com alterações da branch principal:

1. Altere para sua branch de trabalho:
    
    ```bash
    git checkout nome-da-branch
    ```
    
2. Integre as mudanças da branch principal:
    
    ```bash
    git merge main
    ```
    

---

