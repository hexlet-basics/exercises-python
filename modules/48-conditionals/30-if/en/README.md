
In this lesson, we'll look at how you can use conditional constructs to change the behavior of a program, which can be made to act based on the result of a condition it checks. This allows you to write complex programs that behave depending on the situation.

As an example, consider a function that determines the type of sentence passed to it. First, it'll distinguish between normal sentences and questions:

```python
def get_type_of_sentence(sentence):
  last_char = sentence[-1]
  if last_char == '?':
      return 'question'
  return 'normal'

print(get_type_of_sentence('Hodor'))   # => normal
print(get_type_of_sentence('Hodor?'))  # => question
```

`if` is a language construct that controls the procedure of how instructions are executed. After the word `if` it passes a predicate expression, followed by a colon at the end. Next, we pass a block of code. It will execute if the predicate is true.

If the predicate is false, the code block is skipped and the function continues to be executed. In our case, the next line of code, `return 'normal'`, will make the function return a string and terminate.

`return` can be anywhere in a function, even inside a code block with a condition.
