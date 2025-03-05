# Check if Object is Iterable

## Description 📝

This Python script defines the `is_iterable()` function, which checks whether a given object is iterable.
The function returns `True` if the object can be iterated over (like a list, tuple, or string), and `False` otherwise.

## Purpose 🎯

The purpose of this function is to determine whether an object supports iteration.
Iterables are objects like lists, tuples, and strings that can be used in loops and other iterating contexts.

## How It Works 🔍

1. **Input**: The function takes a single argument `obj`, which can be any object.
2. **Check for Iterability**: The function checks if the object has the `__iter__` attribute, which is a marker for iterability in Python.
3. **Output**: The function returns `True` if the object is iterable and `False` otherwise.

## Output 📜

The function returns a boolean value:

-   `True` if the object is iterable (e.g., a list, string, dictionary, or set).
-   `False` if the object is not iterable (e.g., an integer, float, or other non-iterable object).

Example:

```python
print(is_iterable([1, 2, 3]))  # True
print(is_iterable(123))  # False
```

## Usage 📦

1. Save the code to a file named `check_iterable.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
    ```python
    python check_iterable.py
    ```
5. Call the function `is_iterable()` with any object you want to check.
   Example:
    ```python
    print(is_iterable('Hello'))  # True
    print(is_iterable(100))  # False
    ```

## Conclusion 🚀

This function is a simple and effective way to check whether an object can be iterated over in Python.
It helps with handling different types of objects in a flexible and dynamic way.
