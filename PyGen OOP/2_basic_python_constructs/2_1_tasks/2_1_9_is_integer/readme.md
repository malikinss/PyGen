# Integer Validator Function 🔢

## Description 📝

The `is_integer()` function checks if a given string represents a valid integer.
It verifies that the string consists of digits, optionally preceded by a hyphen (`-`) to indicate a negative number.
The function returns `True` if the string is a valid integer and `False` otherwise.

## Purpose 🎯

The function is designed to validate whether a string represents an integer by checking for the presence of digits and an optional leading hyphen.
This can be useful for ensuring that input data is numeric before processing it.

## How It Works 🔍

1. The function uses a regular expression to check if the string matches the format of an integer.
2. The regular expression `r'^-?\d+$'` allows for:
    - Optional leading hyphen (`-?`).
    - One or more digits (`\d+`).
3. The function returns `True` if the string matches the integer pattern and `False` otherwise.

### Example Input:

```
"-123"
```

### Example Output:

```
True
```

## Output 📜

The function returns `True` if the input string represents a valid integer and `False` otherwise.

## Usage 📦

1. Pass a string to the `is_integer()` function.
2. The function will return `True` if the string is a valid integer or `False` otherwise.

### Example:

```python
is_integer("-123")  # Returns: True
is_integer("12a34")  # Returns: False
```

## Conclusion 🚀

The `is_integer()` function ensures that a given string can be confirmed as a valid integer, handling negative numbers and non-digit characters effectively.
