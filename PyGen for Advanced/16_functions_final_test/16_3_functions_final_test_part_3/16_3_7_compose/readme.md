# Function Composition 🎯

## Description 📝

The `compose()` function takes two one-argument functions `f` and `g`, and returns a new function that applies `f` to the result of applying `g` to an input `x`. In other words, the new function computes `f(g(x))`.

## Purpose 🎯

The function composition is a standard operation in mathematics and programming, allowing you to combine multiple functions into one. This is useful for creating complex transformations by chaining simpler functions together.

## How It Works 🔍

1. **`func1` and `func2`**: The input functions are passed as arguments.
2. **Lambda Expression**: The lambda function `lambda x: func1(func2(x))` defines a new function that first applies `func2(x)` and then applies `func1` to the result.
3. **Returning the Function**: The resulting function applies `g(x)` first and then `f` to that result.

## Example Usage:

```python
>>> def add1(x):
...     return x + 1
>>> def multiply2(x):
...     return x * 2
>>> composed_function = compose(add1, multiply2)
>>> composed_function(5)
11  # First multiply 5 by 2 to get 10, then add 1 to get 11
```

In this example:

-   `compose(add1, multiply2)` creates a new function that applies `multiply2(x)` first, followed by `add1(x)`.
-   For input `5`, it first calculates `multiply2(5)` to get `10`, and then applies `add1(10)` to get `11`.

## Conclusion 🚀

The `compose()` function is a powerful tool for combining functions in a modular and flexible way, enabling you to chain operations without manually nesting function calls.
