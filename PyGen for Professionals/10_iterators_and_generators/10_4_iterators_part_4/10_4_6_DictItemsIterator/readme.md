# DictItemsIterator Class

## Description 📝

The `DictItemsIterator` class is an iterator that iterates over the key-value pairs of a dictionary.
It avoids using the built-in `items()`, `keys()`, or `values()` methods, and instead manually iterates through the dictionary while maintaining the original insertion order of the key-value pairs.

## Purpose 🎯

This iterator is designed to provide a way to iterate over a dictionary's key-value pairs without relying on the dictionary's built-in methods.
The order of iteration is preserved as it was inserted into the dictionary.

## How It Works 🔍

1. **Initialization (`__init__`)**:

    - Takes a dictionary (`data`) as input.
    - Extracts the list of keys from the dictionary to maintain the insertion order.
    - Initializes an index (`index`) to -1 to start the iteration before the first key-value pair.

2. **Iterator Protocol**:
    - `__iter__()`: Returns the iterator instance (`self`).
    - `__next__()`:
        - Increments the index and returns the current key-value pair as a tuple.
        - When all key-value pairs have been exhausted, raises a `StopIteration` exception.

## Output 📜

Example usage:

```python
info = {'name': 'Timur', 'age': 29, 'gender': 'Male'}
iterator = DictItemsIterator(info)

for pair in iterator:
    print(pair)  # Output: ('name', 'Timur'), ('age', 29), ('gender', 'Male')
```

## Usage 📦

1. Save the class in a file, e.g., `dict_items_iterator.py`.
2. Run the following code to iterate over a dictionary:

    ```python
    data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    iterator = DictItemsIterator(data)

    for key, value in iterator:
        print(key, value)
    ```

    **Expected Output:**

    ```
    name Alice
    age 30
    city New York
    ```

## Conclusion 🚀

The `DictItemsIterator` class provides a custom iterator for iterating over a dictionary's key-value pairs while maintaining the order of insertion.
It works without using the built-in `items()`, `keys()`, or `values()` methods, giving greater flexibility and control over iteration.
This can be particularly useful in scenarios where custom iteration behavior is needed.
