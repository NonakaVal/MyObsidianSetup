---
tags:
  - learning/review
HUB:
  - "[[hub-python]]"
---
[[nested-contexts]]
### Nested functions
```python
# Define three_shouts

def three_shouts(word1, word2, word3):

    """Returns a tuple of strings

    concatenated with '!!!'."""
    # Define inner

    def inner(word):

        """Returns a string concatenated with '!!!'."""

        return word + '!!!'

    # Return a tuple of strings

    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print

print(three_shouts('a', 'b', 'c'))
```

```python
# Define echo_shout()

def echo_shout(word):

    """Change the value of a nonlocal variable"""
    # Concatenate word with itself: echo_word
    echo_word = word*2
    # Print echo_word
    print(echo_word)

    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""
        # Use echo_word in nonlocal scope
        nonlocal echo_word
        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'
    # Call function shout()
    shout()
    # Print echo_word
    print(echo_word)
# Call function echo_shout() with argument 'hello'

echo_shout('hello')
```

