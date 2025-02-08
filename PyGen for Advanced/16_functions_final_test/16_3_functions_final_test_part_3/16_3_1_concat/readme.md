# Concatenate Variable Arguments into a String 🔗

## Description 📝

The `concat()` function takes a variable number of arguments and concatenates them into a single string. You can also specify a separator, which is used between the elements. If no separator is provided, a space is used by default.

## Purpose 🎯

This function allows you to combine multiple string-like elements into a single string with a customizable separator. It's particularly useful when you need to concatenate an unknown number of elements, like user input or list elements, with a separator.

## How It Works 🔍

-   **Mandatory argument**:
    -   `*args`: A variable number of arguments that will be concatenated.
-   **Optional argument**:
    -   `sep`: A string used to separate the elements in the final string. Defaults to a space `' '` if not provided.
-   The function converts each argument to a string (if it's not already) and joins them together using the specified separator.

## Example Output:

```python
>>> concat('Hello', 'World')
'Hello World'

>>> concat('apple', 'orange', sep=', ')
'apple, orange'
```

## Usage 📦

1. Provide the values to be concatenated as arguments.
2. Optionally, specify a separator.
3. The function returns a concatenated string with the specified separator.

## Conclusion 🚀

The `concat()` function simplifies the process of joining multiple values into a single string with a specified separator. It can handle any number of arguments and is versatile enough to work with various types.
