# ChainMap Value Retriever 📝

## Description 📝

This program implements a function `get_all_values()` that retrieves all values associated with a specific key from all the dictionaries in a `ChainMap`.
If the key is not found in any dictionary, it returns an empty set.

## Purpose 🎯

The purpose of this function is to provide an efficient way of retrieving all values associated with a specific key from multiple dictionaries stored in a `ChainMap`.

## How It Works 🔍

1. The function `get_all_values()` receives two arguments:
    - `chainmap`: a `ChainMap` object containing multiple dictionaries.
    - `key`: the key whose associated values need to be retrieved.
2. The function iterates over all the dictionaries in the `ChainMap`.
3. For each dictionary, it checks if the key is present.
4. If the key is found, its corresponding value is added to a set.
5. Finally, the function returns the set containing all values for the key. If the key is not found in any dictionary, an empty set is returned.

## Output 📜

The output is a set containing all values associated with the key across all dictionaries in the `ChainMap`. If the key is not found, an empty set is returned.

### Example:

**Input:**

```python
from collections import ChainMap

chainmap = ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5, 'b': 6})
key = 'b'
print(get_all_values(chainmap, key))
```

**Output:**

```python
{2, 3, 6}
```

## Usage 📦

1. Create a `ChainMap` object containing dictionaries.
2. Call the `get_all_values()` function with the `ChainMap` and the desired key.
3. The function will return a set of values corresponding to the key from all dictionaries in the `ChainMap`.

## Conclusion 🚀

This function provides a convenient way to retrieve all values associated with a key across multiple dictionaries, making it easy to handle cases where a key might appear in several different dictionaries.
