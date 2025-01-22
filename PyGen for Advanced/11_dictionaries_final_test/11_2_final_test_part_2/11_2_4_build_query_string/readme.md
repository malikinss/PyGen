# Query String Builder 📝

## Description 📝

This program takes a dictionary of query parameters and returns a properly formatted query string that can be appended to a URL.
The query string is generated in lexicographic order of the dictionary keys.

## Purpose 🎯

The purpose of this program is to build a query string for URLs from a given dictionary, ensuring the parameters are sorted in lexicographic order and formatted correctly.

## How It Works 🔍

1. **Input**:
    - The program accepts a dictionary where each key-value pair represents a query parameter and its value.
2. **Processing**:
    - The dictionary is sorted by the keys in lexicographic order.
    - The key-value pairs are then formatted as `key=value` and joined using the `&` symbol.
3. **Output**:
    - The program returns a string representing the query string that can be added to a URL.

## Output 📜

The output is a query string formatted as `key=value` pairs separated by `&`, with keys sorted lexicographically.

### Example Input/Output:

**Input**:

```python
params = {'name': 'timur', 'color': 'green'}
query_string = build_query_string(params)
print(query_string)
```

**Output**:

```
color=green&name=timur
```

### Explanation:

-   The dictionary keys `'name'` and `'color'` are sorted lexicographically.
-   The query string is constructed as `color=green&name=timur`.

## Usage 📦

1. Copy the code into a Python file (e.g., `query_string_builder.py`).
2. Define a dictionary with query parameters.
3. Call the `build_query_string()` function to get the query string.

### Example Run:

```python
params = {'name': 'timur', 'color': 'green'}
query_string = build_query_string(params)
print(query_string)
```

**Output**:

```python
color=green&name=timur
```

## Conclusion 🚀

This program is a helpful tool to generate query strings for URLs.
It ensures the query parameters are properly formatted and sorted for easy use in web applications.
