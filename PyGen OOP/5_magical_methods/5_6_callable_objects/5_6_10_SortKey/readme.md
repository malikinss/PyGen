# SortKey Class Attribute-Based Sorting Tool

## Description 📝

The `SortKey` class simplifies sorting objects by their attributes, acting as a callable key for Python’s `sorted()` function.
It accepts attribute names during instantiation, prioritizing them in order, and returns a tuple of their values when called with an object, enabling multi-level sorting based on natural comparison.

## Purpose 🎯

This class eliminates the need for lambda functions in sorting, enhancing readability and maintainability.
It’s ideal for sorting custom class instances (e.g., users by age or name) in data processing or educational contexts.

## How It Works 🔍

-   **Initialization**: Takes `*attributes` (strings) and stores them in `self.attributes` for sorting priority.
-   **Call**: Returns a tuple of attribute values from an object’s `__dict__`, used by Python’s sorting to compare objects sequentially.

## Usage 📦

1. Save in `sort_key.py`.
2. Use with a class like `User`:

    ```python
    class User:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def __repr__(self):
            return f'User({self.name}, {self.age})'

    users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20)]
    print(sorted(users, key=SortKey('age')))  # [User(Arthur, 20), User(Timur, 30), User(Gvido, 67)]
    print(sorted(users, key=SortKey('name', 'age')))  # [User(Arthur, 20), User(Gvido, 67), User(Timur, 30)]
    ```

## Conclusion 🚀

`SortKey` provides a concise, reusable way to sort objects by attributes, supporting single or multi-level sorts with clarity.
It’s perfect for data tasks or teaching, with room to grow via features like reverse sorting.
