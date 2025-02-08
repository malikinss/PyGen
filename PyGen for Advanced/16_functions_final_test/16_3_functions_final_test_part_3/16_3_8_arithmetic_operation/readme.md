# Arithmetic Operations Factory 🎯

## Description 📝

The `arithmetic_operation()` function takes a symbol representing one of the four basic arithmetic operations (`+`, `-`, `*`, `/`) and returns a function that performs the corresponding operation on two arguments.

## Purpose 🎯

This function enables dynamic creation of functions that perform specific arithmetic operations based on input symbols. It's a great way to simplify and centralize arithmetic operation logic.

## How It Works 🔍

1. **Mapping Operations**: The function maps each arithmetic operation symbol to its corresponding function from the `operator` module (`add`, `sub`, `mul`, `truediv`).
2. **Returning a Lambda**: The function then returns a lambda function that performs the operation using the appropriate function for the operation symbol.
3. **Handling Invalid Operations**: If the operation is not valid (i.e., not one of `+`, `-`, `*`, `/`), the function will raise a `ValueError`.

## Example Usage:

```python
>>> add_func = arithmetic_operation('+')
>>> add_func(3, 4)
7  # 3 + 4 = 7

>>> multiply_func = arithmetic_operation('*')
>>> multiply_func(3, 4)
12  # 3 * 4 = 12

>>> subtract_func = arithmetic_operation('-')
>>> subtract_func(10, 3)
7  # 10 - 3 = 7

>>> divide_func = arithmetic_operation('/')
>>> divide_func(10, 2)
5.0  # 10 / 2 = 5.0
```

## Conclusion 🚀

The `arithmetic_operation()` function provides a flexible way to create functions for basic arithmetic operations on the fly, enabling dynamic handling of mathematical tasks based on user input or other sources.
