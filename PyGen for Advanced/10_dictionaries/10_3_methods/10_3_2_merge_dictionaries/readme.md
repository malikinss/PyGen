# Merge Dictionaries 📘

## Description 📝

This program combines the contents of two dictionaries based on specific rules:

1. If a key exists in both dictionaries, its value will be the sum of the corresponding values from both dictionaries.
2. If a key exists in only one of the dictionaries, its value will be taken as it is.

## Purpose 🎯

The purpose of this program is to merge two dictionaries efficiently while handling common keys by summing their values and keeping unique keys intact.

## How It Works 🔍

1. **Input**:
    - Two dictionaries (`dict1` and `dict2`).
2. **Processing**:
    - The function iterates through the keys of the second dictionary.
    - If a key is present in both dictionaries, the values are added.
    - If the key is only in one dictionary, it is added with its existing value.
3. **Output**:
    - A merged dictionary based on the rules above.

## Output 📜

The program does not print the result but stores it in the `result` variable.

### Example:

**Input**:

```python
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
```

**Output**:

```python
result = {
    'a': 400,
    'z': 999,
    'b': 400,
    'c': 312,
    'd': 445,
    'e': 98,
    't': 853,
    'q': 34,
    'f': 90,
    'm': 230,
    'p': 123,
    'w': 111
}
```

## Usage 📦

1. Save the code in a Python file, e.g., `merge_dictionaries.py`.
2. Define the dictionaries `dict1` and `dict2`.
3. Call the function `merge_dictionaries(dict1, dict2)` to merge them.

### Example Run:

```python
result = merge_dictionaries(dict1, dict2)
```

## Conclusion 🚀

This function offers an efficient way to merge two dictionaries while handling overlapping keys by summing their values and retaining unique keys.
