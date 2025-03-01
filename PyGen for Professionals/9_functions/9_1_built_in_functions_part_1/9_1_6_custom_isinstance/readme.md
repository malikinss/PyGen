# Custom Instance Checker

## Description 📝

This program defines the `custom_isinstance()` function, which counts how many objects in a list match a given type or any type in a tuple of types.
The function efficiently checks the type of each object using the `isinstance()` function and returns the count of matching objects.

## Purpose 🎯

The purpose of this function is to count how many objects in a list belong to a specified type or any type from a tuple of types.
This is useful for type validation and filtering.

## How It Works 🔍

1. The function accepts two arguments:
    - `objects`: A list of arbitrary objects to check.
    - `typeinfo`: A single data type or a tuple of types to compare against.
2. The function checks if `typeinfo` is a tuple; if not, it converts it into one.
3. The function uses the `isinstance()` function to check if each object in the list matches any of the types in `typeinfo`.
4. It returns the count of objects that match the type(s).

## Output 📜

The function returns an integer representing the number of objects in the list that match the specified type or types.

## Usage 📦

1. Provide a list of objects and a type or tuple of types to the `custom_isinstance()` function.
2. The function will return the count of objects that belong to the specified type or any of the types in the tuple.

### Example:

```python
custom_isinstance([1, 2.0, 'abc', True], (int, float))  # Returns: 3
custom_isinstance([1, 2.0, 'abc', True], str)  # Returns: 1
```

## Conclusion 🚀

The `custom_isinstance()` function allows you to easily count the number of objects in a list that match a specified type or one of the types in a tuple, using Python's built-in `isinstance()` function for type checking.
