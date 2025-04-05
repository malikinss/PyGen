# Account Class Security Manager

## Description 📝

The `Account` class models an Internet user account with a login and a password stored as a hash value using the provided `hash_function()`.
It features a read-only `login` property and a read-write `password` property that manages the password’s hash, ensuring the actual password is never stored directly.

## Purpose 🎯

This class is designed for secure account management, ideal for educational examples of property usage and hashing, or as a component in systems requiring basic user authentication with security considerations.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets `_login` and computes `_password` as the hash of the initial password.
-   **login Property (Getter)**: Returns `_login` using `@property`.
-   **login Property (Setter)**: Raises an `AttributeError` with a custom message to prevent changes.
-   **password Property (Getter)**: Returns the stored `_password` hash.
-   **password Property (Setter)**: Updates `_password` with the hash of a new password using `hash_function()`.

## Usage 📦

1. Save the class in a Python file, e.g., `account.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from account import Account
acc = Account("user123", "pass123")
print(f"Login: {acc.login}")
print(f"Password hash: {acc.password}")
acc.password = "newpass456"
print(f"New password hash: {acc.password}")
```

## Conclusion 🚀

The `Account` class provides a secure and straightforward way to manage user credentials in Python, leveraging properties and hashing for data protection.
Its design prevents login changes and ensures password security, making it a solid foundation that can be extended with features like login attempts or additional authentication methods.
