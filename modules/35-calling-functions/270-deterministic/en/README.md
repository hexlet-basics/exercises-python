
Functions in every programming language have fundamental properties. These properties help predict the behavior of functions, how to test them, and where to use them. These properties include determinacy.

A deterministic function returns the same result every time if the input parameters are the same. For example, a function that counts the number of characters can be called deterministic:

```python
len('hexlet')  # 6
len('hexlet')  # 6

len('wow')  # 3
len('wow')  # 3
```

You can call this function and pass the value `'hexlet'` as many times as you want, and it will always return `6`.

Let's also look at the reverse case: nondeterministic functions. For example, a function that returns a random number belongs to this category: we will always get different results even if we use the same input. If at least one in a million calls to a function returns a different result, it is considered nondeterministic. This applies even if it doesn't take parameters:

```python
# Import syntax will be studied later in Hexlet
from random import random

# A function that returns a random number
random()  # 0.09856613113197676
random()  # 0.8839904367241888
```

Determinism is an important property of a function, as it affects many aspects. For example, deterministic functions are convenient to work with, as they're easy to optimize and test. If possible, it's better to make the function deterministic.
