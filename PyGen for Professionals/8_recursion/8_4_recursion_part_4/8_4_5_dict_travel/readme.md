# Traverse Nested Dictionary and Print Key-Value Pairs 🧭

## Description 📝

The `dict_travel()` function recursively traverses a nested dictionary and prints all key-value pairs in lexicographical order.
If a dictionary contains nested dictionaries, it prints the key-value pairs of those child dictionaries in the following format: `parent_key.child_key: value`.
The function ensures that all key-value pairs are printed in lexicographically sorted order, providing a clear view of the nested structure.

## Purpose 🎯

The function is designed to:

-   Traverse deeply nested dictionaries, handling both strings and numbers as values.
-   Print key-value pairs in lexicographical order.
-   Support nested structures, displaying keys in a dot-separated path format.

## How It Works 🔍

1. **Input Parameters**:

    - `nested_dicts`: A dictionary that can contain numbers, strings, or other dictionaries as values.

2. **Recursive Traversal**:

    - The function uses a helper function `traverse_recursive()` to recursively explore each key-value pair in the dictionary.
    - If a value is a dictionary, the function continues traversing its key-value pairs.
    - The function constructs the full key path using dot notation (e.g., `parent.child`).
    - All keys are sorted lexicographically before being printed.

3. **Printing the Result**:
    - Once all key-value pairs are collected, the function prints each key-value pair in the format `key: value`.

For example, given the input:

```python
{'name': 'Arthur', 'grades': {'math': 4, 'chemistry': 3}}
```

The output will be:

```
grades.chemistry: 3
grades.math: 4
name: Arthur
```

## Output 📜

For example:

```python
data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}
dict_travel(data)
```

The output will be:

```
b.a: 10
b.b.d: 40
b.b.e: 50
b.c: 30
```

## Usage 📦

1. Call the function `dict_travel()` with:

    - A nested dictionary `nested_dicts` that contains other dictionaries or arbitrary objects.

2. Example usage:

    ```python
    data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}
    dict_travel(data)
    ```

3. The function will print all key-value pairs in lexicographical order, including the full paths of keys in nested dictionaries.

## Conclusion 🚀

The `dict_travel()` function efficiently handles nested dictionaries, ensuring that key-value pairs are printed in a clear, lexicographically sorted manner.
It's a useful tool for exploring and printing the contents of nested data structures with multiple levels of hierarchy.
