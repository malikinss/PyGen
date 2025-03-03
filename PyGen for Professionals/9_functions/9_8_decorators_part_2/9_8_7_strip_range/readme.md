# Strip Range Decorator

## Description 📝

The `strip_range()` decorator modifies the return value of the decorated function by replacing a specific range of characters (from the `start` index to the `end` index) with a specified character.
This is useful when you want to mask or alter parts of a string, such as anonymizing sensitive information.

## Purpose 🎯

The purpose of this decorator is to modify a string returned from a function by replacing characters within a specific index range.
It allows flexibility by providing the option to choose the character that will replace the characters within the specified range.

## How It Works 🔍

1. **Input**:

    - The decorator accepts three arguments:
        - `start`: The index (inclusive) from where to start replacing characters.
        - `end`: The index (exclusive) at which to stop replacing characters.
        - `char`: The character used to replace the characters in the specified range. It defaults to `.`.

2. **Processing**:

    - The `strip_range()` decorator wraps the original function and executes it to get the return value (a string).
    - The portion of the string from `start` to `end` is replaced by the specified `char` character.
    - The modified string is returned.

3. **Output**:
    - The output is the modified string with the characters in the specified range replaced by `char`.

## Example 📜

```python
# Define a function with the strip_range decorator
@strip_range(3, 7, '*')
def greet(name: str) -> str:
    """Greets a person with a message."""
    return f"Hello, {name}!"

# Call the decorated function
result = greet("Alice")
print(result)
```

### Output:

```text
Hel****, Alice!
```

In this example, the string returned by the function is altered by replacing the characters between index 3 (inclusive) and 7 (exclusive) with asterisks (`*`).

## Usage 📦

1. Define the `strip_range` decorator in your script.
2. Apply the decorator to any function that returns a string using the `@strip_range` syntax.
3. Pass the `start` and `end` indices, along with the optional `char` argument, to the decorator.
4. Call the decorated function, and it will return the modified string with the specified characters replaced.

## Conclusion 🚀

The `strip_range` decorator is a powerful tool for modifying strings returned by functions.
Whether for masking sensitive data or customizing output, it allows fine control over which part of the string gets altered.
The decorator maintains the clarity of your function's signature and docstring, ensuring the original intent is preserved.
