# User Class for Internet Users

## Description 📝

The `User` class represents an Internet user with a name and a friend count.
It allows tracking of a user's friends by providing a method to increase the friend count.
The class is designed to be simple and functional, taking a name during instantiation and managing friend relationships through an `add_friends()` method.

## Purpose 🎯

This class serves as a basic model for simulating Internet user relationships, useful in educational contexts or as a building block for social network simulations.
It demonstrates proper class initialization and attribute manipulation in Python.

## How It Works 🔍

-   **Initialization**: The `__init__` method takes a `name` parameter and sets it as an instance attribute, while initializing `friends` to 0.
-   **add_friends() Method**: This method accepts an integer `n` and increases the `friends` attribute by that amount using the `+=` operator, correctly implementing the friend-adding functionality.

## Output 📜

Example usage:

```python
user = User("Alice")
print(user.friends)    # Output: 0
user.add_friends(3)
print(user.friends)    # Output: 3
```

## Usage 📦

1. Save the class in a Python file, e.g., `user.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from user import User
user = User("Bob")
user.add_friends(5)
print(f"{user.name} has {user.friends} friends")  # Output: Bob has 5 friends
```

## Conclusion 🚀

The `User` class provides a clean and efficient way to represent an Internet user and manage their friend count.
With its corrected `add_friends()` method, it reliably updates the `friends` attribute, making it a solid foundation for applications needing to track user relationships.
The implementation is straightforward and can be extended with additional features like removing friends or validating input if needed.
