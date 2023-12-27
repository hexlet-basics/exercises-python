
Now let's modify the function from the previous lesson so that it returns the whole string `Normal sentence` or `Question` instead of just the sentence type:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    else:
        sentence_type = 'normal'

    return "Sentence is " + sentence_type

print(get_type_of_sentence('Hodor'))   # => 'Sentence is normal'
print(get_type_of_sentence('Hodor?'))  # => 'Sentence is question'
```

We added `else` and a new block. It'll execute if the condition in `if` is false. You can also put other `if` conditions in the `else` block. 

`if-else' constructions can be arranged in two ways. Negation allows you to change the order of the blocks:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char != '?':
        sentence_type = 'normal'
    else:
        sentence_type = 'question'

    return "Sentence is " + sentence_type
```

To make it easier, try choosing non-negative checks and adjust the contents of the blocks to suit it.
