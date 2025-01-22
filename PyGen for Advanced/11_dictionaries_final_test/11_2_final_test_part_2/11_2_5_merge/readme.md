# Dictionary Merge 📝

## Description 📝

This program merges multiple dictionaries into a single dictionary.
Each key in the resulting dictionary contains a set of unique values collected from all the dictionaries in the provided list.
The merging process ensures that each value under a key is unique, eliminating duplicates.

## Purpose 🎯

The purpose of this program is to merge a list of dictionaries such that each key in the resulting dictionary holds a set of unique values, gathered from all input dictionaries.

## How It Works 🔍

1. **Input**:
    - The program accepts a list of dictionaries.
    - Each dictionary in the list contains key-value pairs where the values can be repeated across different dictionaries.
2. **Processing**:
    - The program iterates over each dictionary in the list.
    - For each key, it adds the corresponding value to a set (which automatically removes duplicates).
3. **Output**:
    - The program returns a dictionary where each key is associated with a set of unique values.

## Output 📜

The output is a dictionary where:

-   Each key holds a set of unique values from the input dictionaries.
-   If a key is not present in some dictionaries, it will not appear in the resulting dictionary.

### Example Input/Output:

**Input**:

```python
result = merge(
    [
        {'a': 1, 'b': 2}, {'b': 10, 'c': 100},
        {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}
    ]
)
print(result)
```

**Output**:

```python
{'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}
```

### Explanation:

-   The key `'a'` has the unique values `{1, 5}` from the dictionaries.
-   The key `'b'` has the unique values `{2, 10, 17}`.
-   The key `'c'` has the unique values `{50, 100}`.
-   The key `'d'` only appears in the last dictionary with the value `777`.

## Usage 📦

1. Copy the code into a Python file (e.g., `merge_dictionaries.py`).
2. Define a list of dictionaries that you want to merge.
3. Call the `merge()` function to get the merged dictionary.

### Example Run:

```python
values = [
    {'a': 1, 'b': 2},
    {'b': 10, 'c': 100},
    {'a': 1, 'b': 17, 'c': 50},
    {'a': 5, 'd': 777}
]
result = merge(values)
print(result)
```

**Output**:

```python
{'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}
```

## Conclusion 🚀

This program provides an efficient way to merge multiple dictionaries into one, ensuring that each key contains a set of unique values.
It is helpful when handling data from different sources where values might repeat across dictionaries.
