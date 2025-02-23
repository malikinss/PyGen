# ChainMap Key Retrieval 📝

## Description 📝

This program implements a function `get_value()` that retrieves the value associated with a key in a `ChainMap` object.
The search direction can be controlled using the `from_left` argument, which allows you to search from the first dictionary to the last, or from the last dictionary to the first.

## Purpose 🎯

The purpose of this function is to search for a key in a `ChainMap` and return the corresponding value based on the specified search direction.
It provides flexibility in how the search is conducted and returns `None` if the key is not found.

## How It Works 🔍

1. The function `get_value()` takes three arguments:
    - `chainmap`: A `ChainMap` object containing multiple dictionaries.
    - `key`: The key to look up in the `ChainMap`.
    - `from_left`: A boolean value that determines the direction of the search. If `True`, the search will be from left to right (first to last dictionary). If `False`, it will be from right to left (last to first dictionary).
2. Depending on the value of `from_left`, the function iterates over the dictionaries in the `ChainMap`:
    - If `from_left` is `True`, it searches from the first dictionary to the last.
    - If `from_left` is `False`, it searches from the last dictionary to the first (using `reversed()`).
3. If the key is found in a dictionary, the corresponding value is returned.
4. If the key is not found in any dictionary, the function returns `None`.

## Output 📜

The function returns:

-   The value associated with the key if found.
-   `None` if the key is not found.

### Example:

**Input 1:**

```python
from collections import ChainMap

chainmap = ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
key = 'b'

print(get_value(chainmap, key))  # Default search from left
```

**Output 1:**

```python
2
```

**Input 2:**

```python
print(get_value(chainmap, key, from_left=False))  # Search from right
```

**Output 2:**

```python
3
```

## Usage 📦

1. Create a `ChainMap` object containing dictionaries.
2. Call the `get_value()` function with the `ChainMap`, key, and the optional `from_left` argument.
3. The function will return the value for the key from the appropriate direction (left to right or right to left). If the key is not found, it will return `None`.

## Conclusion 🚀

The `get_value()` function provides a flexible way to search for keys in a `ChainMap`.
By allowing the search direction to be controlled, it offers a more tailored approach to handling key-value lookups in multiple dictionaries.
