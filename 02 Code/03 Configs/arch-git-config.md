---
subject:
  - "[[hub-git]]"
  - "[[hub-linux]]"
tags:
  - config
---
```
valdenirnonaka001@gmail.com 

```

```
git config --global user.name "NonakaVal"
```

```
git config --global user.email "valdenirnonaka001@gmail.com"
```


```
ssh-keygen -t ed25519 -C "valdenirnonaka001@gmail.com"
```


```
eval "$(ssh-agent -s)"
```


```
ssh-add ~/.ssh/id_ed25519
```


```
cat ~/.ssh/id_ed25519.pub
```

```

ssh -T git@github.com
```


```
git config --global url."git@github.com:".insteadOf https://github.com/
```
