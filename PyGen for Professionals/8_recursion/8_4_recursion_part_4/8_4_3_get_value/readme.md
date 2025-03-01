# Retrieve Value from a Nested Dictionary 🗂️

## Description 📝

The `get_value()` function recursively retrieves the value associated with a given key in a nested dictionary.
The dictionary may contain arbitrary objects or other dictionaries, and the key can be present at any level of nesting.
The function ensures that if the key is found, it will return the corresponding value from the deepest level.

## Purpose 🎯

The function is designed to:

-   Access deeply nested values within a dictionary.
-   Demonstrate recursion in the context of dictionary traversal.
-   Handle arbitrary levels of nesting and varying data types within the dictionary.

## How It Works 🔍

1. **Input Parameters**:

    - `nested_dict`: A dictionary that may contain other dictionaries or objects.
    - `key`: A hashable object (like a string, integer, etc.) that represents the key whose value is to be retrieved.

2. **Recursive Flow**:

    - The function first checks if the `key` is directly present in the current level of the dictionary.
    - If not, it recursively searches through all dictionary values. If any value is itself a dictionary, the function calls `get_value()` again on that nested dictionary.

3. **Return Value**:
    - When the key is found, the corresponding value is returned.
    - The function guarantees that the key will always be found in exactly one location within the nested structure.

For example, given the input:

```python
{
    'firstName': 'John',
    'address': {
        'city': 'New York',
        'postalCode': '10001',
        'location': {
            'latitude': 40.7128,
            'longitude': -74.0060
        }
    }
}
```

The function call:

```python
get_value(data, 'latitude')
```

Will return:

```
40.7128
```

## Output 📜

For example:

```python
data = {
    'firstName': 'Тимур',
    'lastName': 'Гуев',
    'birthDate': {
        'day': 10,
        'month': 'October',
        'year': 1993
    },
    'address': {
        'streetAddress': 'Часовая 25, кв. 127',
        'city': {
            'region': 'Московская область',
            'type': 'город',
            'cityName': 'Москва'
        },
        'postalCode': '125315'
    }
}

get_value(data, 'cityName')
```

The output will be:

```
'Москва'
```

## Usage 📦

1. Call the function `get_value()` with:

    - A nested dictionary `nested_dict` containing other dictionaries or objects.
    - A key `key` that is guaranteed to exist in one of the dictionaries.

2. Example usage:

    ```python
    get_value(data, 'cityName')  # Output: 'Москва'
    ```

3. The function will return the value associated with the provided key, even if the key is nested deeply.

## Conclusion 🚀

The `get_value()` function effectively demonstrates the power of recursion to handle arbitrary levels of nesting in a dictionary.
This makes it a valuable tool for extracting deeply nested information from complex data structures.
