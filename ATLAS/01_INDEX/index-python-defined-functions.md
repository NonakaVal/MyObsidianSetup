---
tags:
  - learning/review
HUB:
  - "[[hub-python]]"
---
Here's the improved and organized version of your Python functions concepts:


# Python Functions Concepts

## [[concept-Writng-Functlons-In-Python|Writing Functions in Python]]
📌 **Best Practices**:
- Document with `function_name.__doc__` docstrings
- Follow DRY (Don't Repeat Yourself) principle
- Adhere to "Do One Thing" principle
- Use `yield` to create generator functions

## [[scope-of-a-function|Function Scope]]
🌐 **Variable Scope Types**:
- `global`: Access variables defined outside function
- `local`: Use variables defined within function
- `nonlocal`: Modify variables in enclosing (non-global) scope

## [[nested-functions---funcoes-aninhadas|Nested Functions]]
🔗 **Key Features**:
- Use `inner` functions to encapsulate logic
- Create closures with nested functions
- Implement decorators using nesting

## [[concept-python-functions-with-variable-length-arguments|Variable-Length Arguments]]
🔢 **Flexible Parameters**:
- `*args`: Accept arbitrary number of positional arguments
- `**kwargs`: Handle arbitrary keyword arguments as dictionary

## [[concept-python-lambda-functions|Lambda Functions]]
⚡ **Anonymous Functions**:
```python
shout_spells = map(lambda item: item + '!!!', spells)
```
- Single-expression functions
- Often used with `map()`, `filter()`, `sorted()`

## [[draft-introduction-to-error-handling|Error Handling]]
🛡️ **Exception Handling**:
```python
try:
    # Risky code
except Exception as e:
    # Error handling
finally:
    # Cleanup code
```

## [[concept-python-decorators-functions|Function Decorators]]
🎀 **Function Modifiers**:
- Functions that accept other functions
- Modify/extend behavior without changing source
- Use `@decorator` syntax

### Example Decorator:
```python
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time: {time.time()-start:.2f}s")
        return result
    return wrapper
```

> **Tip**: Combine these concepts to write clean, modular Python code!
```

Key improvements:
1. Added emoji icons for visual scanning
2. Organized into clear sections
3. Included code examples where relevant
4. Standardized link formatting
5. Added practical decorator example
6. Improved readability with consistent formatting
7. Maintained all original concepts while enhancing explanations
8. Added summary tip at the bottom