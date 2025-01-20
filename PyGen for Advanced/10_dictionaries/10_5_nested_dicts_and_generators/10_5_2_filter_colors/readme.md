# Filter Colors Dictionary 📖

## Description 📝

This program filters out the key-value pairs from a dictionary where the value is `None`.
It produces a new dictionary that only contains the entries where the value is a valid color name.

## Purpose 🎯

The purpose of this program is to demonstrate how to filter a dictionary using a generator expression, removing entries with a `None` value.
This is useful in cases where you need to clean up data by eliminating invalid or missing values.

## How It Works 🔍

1. **Input**:
    - A dictionary where the keys represent color identifiers, and the values represent color names. Some of the values may be `None`.
2. **Processing**:
    - The program uses a dictionary comprehension to filter out the key-value pairs where the value is `None`.
3. **Output**:
    - The result is a dictionary containing only those key-value pairs where the value is a valid color name (not `None`).

## Output 📜

The program outputs a dictionary consisting of all the color identifiers and their corresponding color names, except those whose value is `None`.

### Example Input/Output:

**Input**:

```python
colors = {
    'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green',
    'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None,
    'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold',
    'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige',
    'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl',
    'c21': None, 'c22': 'Sand', 'c23': None
}
```

**Output**:

```python
{
    'c1': 'Red', 'c2': 'Grey', 'c4': 'Green', 'c5': 'Yellow',
    'c6': 'Pink', 'c7': 'Orange', 'c9': 'White', 'c10': 'Black',
    'c11': 'Violet', 'c12': 'Gold', 'c14': 'Amber', 'c15': 'Azure',
    'c16': 'Beige', 'c17': 'Bronze', 'c19': 'Lilac', 'c20': 'Pearl',
    'c22': 'Sand'
}
```

## Usage 📦

1. Copy the code into a Python file (e.g., `filter_colors.py`).
2. Call the `filter_colors` function, passing a dictionary of colors as an argument.
3. The program will return a dictionary with only the entries where the value is not `None`.

### Example Run:

```python
# Sample run
colors = {
    'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green',
    'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None,
    'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold',
    'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige',
    'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl',
    'c21': None, 'c22': 'Sand', 'c23': None
}
result = filter_colors(colors)
print(result)
```

**Output**:

```python
{
    'c1': 'Red', 'c2': 'Grey', 'c4': 'Green', 'c5': 'Yellow',
    'c6': 'Pink', 'c7': 'Orange', 'c9': 'White', 'c10': 'Black',
    'c11': 'Violet', 'c12': 'Gold', 'c14': 'Amber', 'c15': 'Azure',
    'c16': 'Beige', 'c17': 'Bronze', 'c19': 'Lilac', 'c20': 'Pearl',
    'c22': 'Sand'
}
```

## Conclusion 🚀

This program demonstrates an efficient way to filter out `None` values from a dictionary using a dictionary comprehension.
It provides a practical approach to cleaning up data and working with valid entries only.
