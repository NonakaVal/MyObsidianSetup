---
tags:
  - learning/review
  - 
HUB:
  - "[[hub-python]]"
---
### Scope and user-defined functions

- Scope - part of the program where an object or name may be accessible
	- global scope (outside the function)
	- local scope (inside the function)
	- buil-in scope (like `print()` )

```python
# Create a string: team

team = "teen titans"


# Define change_team()

def change_team():
    """Change the value of the global variable team."""
    # Use team in global scope
    global team
    # Change the value of team in global: team
    team = "justice league"

# Print team
print(team)  

# Call change_team()
change_team() 
# Print team
print(team)
```
