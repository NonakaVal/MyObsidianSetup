---
tags:
  - learning/review
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
  - "[[hub-logic]]"
---
# Introduction to error handling

```python
# Define shout_echo

def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word = ''
    shout_words = ''

    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = echo * word1
        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + '!!!'

    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.") 
    # Return shout_words
    return shout_words

# Call shout_echo
shout_echo("particle", echo="accelerator")

# Call shout_echo
shout_echo("particle", echo="accelerator")
```

```python
# Define shout_echo

def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise

    if echo < 0:
        raise ValueError('echo must be greater than or equal to 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word
# Call shout_echo

shout_echo("particle", echo=5)
```

```python
# Select retweets from the Twitter DataFrame: result

result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])
# Create list from filter object result: res_list

res_list = list(result)


# Print all retweets in res_list

for tweet in res_list:

    print(tweet)
```