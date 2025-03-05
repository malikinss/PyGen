# Check if Object is an Iterator

## Description 📝

This Python script defines the `is_iterator()` function, which checks if a given object is an iterator.
An iterator is an object that implements the `__next__()` method and is used to iterate over a sequence of elements.

## Purpose 🎯

The goal of this function is to determine whether an object is an iterator.
Iterators are objects that support the `__next__()` method, allowing them to return the next value in a sequence each time `next()` is called.

## How It Works 🔍

1. **Input**: The function takes a single argument `obj`, which can be any object.
2. **Check for Iterator**: The function checks if the object has the `__next__()` method, which is a defining characteristic of an iterator.
3. **Output**: The function returns `True` if the object is an iterator and `False` otherwise.

## Output 📜

The function returns a boolean value:

-   `True` if the object is an iterator (i.e., it implements the `__next__()` method).
-   `False` if the object is not an iterator.

Example:

```python
print(is_iterator(iter([1, 2, 3])))  # True
print(is_iterator([1, 2, 3]))  # False
```

## Usage 📦

1. Save the code to a file named `check_iterator.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
    ```python
    python check_iterator.py
    ```
5. Call the function `is_iterator()` with any object you want to check.
   Example:
    ```python
    print(is_iterator(iter('hello')))  # True
    print(is_iterator(123))  # False
    ```

## Conclusion 🚀

This function helps in checking whether an object is an iterator, which is useful when working with iterable objects and managing custom iterators in Python.
