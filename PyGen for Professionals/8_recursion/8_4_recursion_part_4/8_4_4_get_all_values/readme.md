# Retrieve All Values from a Nested Dictionary 🗂️

## Description 📝

The `get_all_values()` function recursively retrieves all values associated with a given key in a nested dictionary.
The dictionary may contain arbitrary objects or other dictionaries, and the key can be present at any level of nesting.
The function returns a set of all unique values found that correspond to the provided key.

## Purpose 🎯

The function is designed to:

-   Access all occurrences of a key in a deeply nested dictionary.
-   Return all values associated with the key as a set (ensuring uniqueness).
-   Demonstrate the use of recursion for traversing nested dictionaries and working with sets.

## How It Works 🔍

1. **Input Parameters**:

    - `nested_dicts`: A dictionary that may contain other dictionaries or arbitrary objects.
    - `key`: A hashable object (like a string, integer, etc.) that represents the key whose values are to be retrieved.

2. **Recursive Flow**:

    - The function first checks if the `key` exists at the current level of the dictionary. If found, the corresponding value is added to the result set.
    - If any dictionary values are found, the function recursively searches through them.
    - The values are collected in a set, ensuring that duplicates are automatically excluded.

3. **Return Value**:
    - A set containing all unique values corresponding to the provided key. If no values are found, an empty set is returned.

For example, given the input:

```python
{
    'Arthur': {'hobby': 'videogames', 'drink': 'cacao'},
    'Timur': {'hobby': 'math'},
    'Dima': {
        'hobby': 'CS',
        'sister': {
            'name': 'Anna',
            'hobby': 'TV',
            'age': 14
        }
    }
}
```

The function call:

```python
get_all_values(data, 'hobby')
```

Will return:

```
{'videogames', 'math', 'CS', 'TV'}
```

## Output 📜

For example:

```python
my_dict = {
    'Arthur': {'hobby': 'videogames', 'drink': 'cacao'},
    'Timur': {'hobby': 'math'},
    'Dima': {
        'hobby': 'CS',
        'sister': {
            'name': 'Anna',
            'hobby': 'TV',
            'age': 14
        }
    }
}

result = get_all_values(my_dict, 'hobby')
print(*sorted(result))
```

The output will be:

```
CS  TV  videogames  math
```

## Usage 📦

1. Call the function `get_all_values()` with:

    - A nested dictionary `nested_dicts` containing other dictionaries or objects.
    - A key `key` whose values you want to retrieve.

2. Example usage:

    ```python
    result = get_all_values(my_dict, 'hobby')
    print(*sorted(result))  # Output: 'CS', 'TV', 'videogames', 'math'
    ```

3. The function will return a set containing all values associated with the provided key. Duplicates are automatically removed due to the nature of a set.

## Conclusion 🚀

The `get_all_values()` function is an efficient and effective way to retrieve all occurrences of a given key from a deeply nested dictionary.
By utilizing recursion and sets, it ensures that the values are unique and that no occurrences are missed, regardless of the depth of nesting.
