# User Class Profile Manager

## Description 📝

The `User` class represents an Internet user with a name and age, enforcing strict validation rules.
It requires a name (non-empty string of Latin or Russian letters) and age (integer 0-110) upon instantiation, and provides methods to access and update these attributes, raising `ValueError` exceptions for invalid inputs.

## Purpose 🎯

This class is designed for user profile management in applications where data integrity is critical, such as registration systems, educational examples of validation, or simple user databases.

## How It Works 🔍

-   **Initialization**: The `__init__` method validates and sets `_name` and `_age`, prioritizing name validation if both are invalid.
-   **get_name() Method**: Returns the current `_name`.
-   **set_name() Method**: Updates `_name` if the new value is valid.
-   **get_age() Method**: Returns the current `_age`.
-   **set_age() Method**: Updates `_age` if the new value is valid.
-   **Helper Methods**: `_validate_name()` uses regex to check for letters only; `_validate_age()` ensures age is an integer in [0; 110].

## Usage 📦

1. Save the class in a Python file, e.g., `user.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from user import User
user = User("Alice", 25)
print(f"Name: {user.get_name()}")
print(f"Age: {user.get_age()}")
user.set_age(30)
user.set_name("Bob")
print(f"Updated Name: {user.get_name()}")
print(f"Updated Age: {user.get_age()}")
```

## Conclusion 🚀

The `User` class provides a secure and reliable way to manage user data with strict validation in Python.
Its encapsulation and error handling make it a robust tool for maintaining user profiles, easily extensible with additional attributes or validation rules for more complex systems.
