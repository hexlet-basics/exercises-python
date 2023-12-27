
The function `get_type_of_sentence()` only distinguishes between question and normal sentences. Let's add support for exclamatory sentences to it:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'

    if last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'Sentence is ' + sentence_type

print(get_type_of_sentence('Who?'))  # => 'Sentence is normal'
print(get_type_of_sentence('No'))    # => 'Sentence is normal'
print(get_type_of_sentence('No!'))   # => 'Sentence is exclamation'
```

We have added an exclamation checker for exclamation sentences. Technically this feature works, but it treats question sentences incorrectly. There are also problems with it in terms of semantics:

* The exclamation point is checked in any case, even if there is already a question mark
* The `else` branch is described for the second condition, but not for the first. Therefore the question sentence becomes `normal'`.

To remedy the situation, let's take another possibility of conditional construction:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    elif last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'Sentence is ' + sentence_type

print(get_type_of_sentence('Who?'))  # => 'Sentence is question'
print(get_type_of_sentence('No'))    # => 'Sentence is normal'
print(get_type_of_sentence('No!'))   # => 'Sentence is exclamation'
```

Now all the conditions are lined up in a single construction. The `elif` means "if the previous condition is not satisfied, but the current condition is satisfied". This is the scheme:

* If the last letter is `? then `'question'`
* if the last letter is `!`, then `'exclamation'`
* other options are `` normal'``.

Only one of the code blocks that refers to the whole `if` construct will be executed.
