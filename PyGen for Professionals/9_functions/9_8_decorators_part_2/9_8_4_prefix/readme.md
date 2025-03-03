# Prefix Decorator

## Description 📝

This Python program implements a `prefix` decorator that allows you to modify the return value of a decorated function by appending a string to it.
You can specify whether the string should be added at the beginning or the end of the return value by passing a boolean value.
The decorator also preserves the function's name and docstring.

## Purpose 🎯

The `prefix` decorator is useful when you need to modify the output of a function by adding a specified string either to the beginning or the end of the return value.
This is useful for formatting or altering the return value dynamically.

## How It Works 🔍

1. **Input**:

    - The `prefix` decorator accepts two parameters:
        - `string`: The string to be added to the return value.
        - `to_the_end`: A boolean value that determines where the string is added. If `True`, the string is appended to the end; otherwise, it is prepended to the beginning.

2. **Processing**:

    - The decorator wraps the original function in a `wrapper` that calls the function and modifies its return value by adding the string.

3. **Output**:
    - The modified return value is returned, with the string either at the beginning or the end depending on the `to_the_end` argument.

## Example 📜

```python
# Define a function with the prefix decorator
@prefix('Hello', to_the_end=True)
def greet(name: str) -> str:
    """Returns a greeting message."""
    return f"Hi {name}"

# Call the decorated function
print(greet("Alice"))
```

### Output:

```
Hi AliceHello
```

```python
# Another example with string prepended
@prefix('Start: ', to_the_end=False)
def display_number(number: int) -> str:
    """Returns a formatted number."""
    return str(number)

# Call the decorated function
print(display_number(42))
```

### Output:

```
Start: 42
```

## Usage 📦

1. Define the `prefix` decorator in your script.
2. Apply the decorator to any function with the `@prefix` syntax.
3. Pass the string to be added and optionally a boolean to specify where the string should be added.
4. Call the decorated function, and it will return the modified string.

## Conclusion 🚀

The `prefix` decorator allows you to easily modify the return value of a function by appending a specified string at the beginning or end of the return value.
This can be useful for formatting or altering output dynamically without modifying the original function logic.
The decorator ensures that the function’s metadata (name and docstring) is preserved, providing a clean and flexible way to enhance your functions.
