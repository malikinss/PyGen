# Lesson 10.1: Introduction to Dictionaries in Python 🗂️

## Description 📝

This lesson provides an introduction to dictionaries in Python, a new type of collection.
The lesson includes 13 theoretical questions available on the course page on the Stepik platform:  
[Stepik Course - Introduction to Dictionaries](https://stepik.org/lesson/488832/step/1?unit=480068).

## Purpose 🎯

The purpose of this lesson is to introduce me to dictionaries, their features, and their differences from other collections such as lists.
By understanding dictionaries, I will be able to use them in a wide range of tasks where key-value mappings are required.

## Key Concepts 📚

### What Are Dictionaries?

Dictionaries are a type of collection in Python that store data in key-value pairs.
Each key is unique and maps to a specific value.
Unlike lists, dictionaries are unordered.

### Differences Between Dictionaries and Lists

-   **Lists**: Use integer indices to access elements.
-   **Dictionaries**: Use keys (which can be of any hashable type) to access values.

### Creating Dictionaries

-   **Using curly braces**:

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
```

-   **Using the `dict()` function**:

```python
my_dict = dict(a=1, b=2, c=3)
```

-   **Creating from lists or tuples**:

```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
```

### Accessing Elements

-   Access a value by its key:

```python
print(my_dict['a'])  # Output: 1
```

-   Use `.get()` to avoid `KeyError` for missing keys:

```python
print(my_dict.get('d', 'Key not found'))  # Output: Key not found
```

### Empty Dictionary

-   Create an empty dictionary:

```python
empty_dict = {}
```

### Printing Dictionaries

-   Use `print()` to display the contents of a dictionary:

```python
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
```

### Features of Dictionaries

-   Keys must be unique and hashable (e.g., strings, numbers, tuples).
-   Values can be of any type and are not required to be unique.

## Conclusion 🚀

This lesson lays the foundation for understanding and working with dictionaries in Python.
By mastering the basics, I'll be able to use dictionaries for tasks that require efficient key-value storage and retrieval.
