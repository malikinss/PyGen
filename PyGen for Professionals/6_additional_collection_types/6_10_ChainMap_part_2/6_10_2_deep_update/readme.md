# ChainMap Deep Update 📝

## Description 📝

This program implements a function `deep_update()` that updates all occurrences of a specified key in all dictionaries within a `ChainMap`.
If the key is not found, the function adds the key-value pair to the first dictionary in the `ChainMap`.

## Purpose 🎯

The function's purpose is to ensure that the value associated with a key is consistently updated across all dictionaries in a `ChainMap`.
If the key does not exist, it ensures the key-value pair is added to the first dictionary.

## How It Works 🔍

1. The function `deep_update()` takes three arguments:
    - `chain_map`: a `ChainMap` containing multiple dictionaries.
    - `key`: the hashable key to be updated.
    - `value`: the new value to be assigned to the key.
2. It iterates over each dictionary in the `ChainMap`.
3. If the key is found in any dictionary, the corresponding value is updated.
4. If the key is not found in any dictionary, the key-value pair is added to the first dictionary.
5. The function does not return any value (returns `None`).

## Output 📜

There is no return value. The function updates the `ChainMap` in place.

### Example:

**Input:**

```python
from collections import ChainMap

chainmap = ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5, 'b': 6})
key = 'b'
value = 10

deep_update(chainmap, key, value)
print(chainmap)
```

**Output:**

```python
ChainMap({'a': 1, 'b': 10}, {'b': 10, 'c': 4}, {'a': 5, 'b': 10})
```

## Usage 📦

1. Create a `ChainMap` object containing dictionaries.
2. Call the `deep_update()` function with the `ChainMap`, key, and value.
3. The function will update the key across all dictionaries in the `ChainMap`, or add the key-value pair to the first dictionary if the key is not present.

## Conclusion 🚀

The `deep_update()` function is a simple yet powerful tool for ensuring that all occurrences of a key in a `ChainMap` are consistently updated.
It modifies the `ChainMap` in place, providing an efficient way to manage key-value pairs across multiple dictionaries.
