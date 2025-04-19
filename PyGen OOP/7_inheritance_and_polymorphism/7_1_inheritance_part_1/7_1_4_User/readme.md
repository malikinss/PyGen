# User and PremiumUser Class Hierarchy

## Description 📝

The provided code implements two classes: `User` and `PremiumUser`.
The `User` class represents a basic user of an internet resource, initialized with a `name` (string) and featuring a `skip_ads` method that always returns `False`.
The `PremiumUser` class, a subclass of `User`, represents a user with a premium subscription, initialized identically to `User` and overriding `skip_ads` to always return `True`.

## Purpose 🎯

Intended to model users of an internet resource, distinguishing between standard and premium users based on their ability to skip ads.
This structure is suitable for applications like streaming platforms, content websites, or subscription-based services, as well as educational examples of inheritance and method overriding in Python.

## How It Works 🔍

-   **User Class**:
    -   **Initialization (`__init__`)**:
        -   Accepts `name` (string) and stores it as `self.name`.
    -   **Method (`skip_ads`)**:
        -   Returns `False`, indicating standard users cannot skip ads.
-   **PremiumUser Class**:
    -   Inherits from `User`, automatically inheriting the `__init__` method (same initialization process).
    -   **Method (`skip_ads`)**:
        -   Overrides `User.skip_ads` to return `True`, indicating premium users can skip ads.
-   **Behavior**:
    -   Both classes store a `name` attribute.
    -   `skip_ads` differentiates user types: `False` for `User`, `True` for `PremiumUser`.
    -   Inheritance ensures `PremiumUser` reuses `User`’s initialization logic.

## Verification ✅

Implementation satisfies requirements:

-   **User Class**:
    -   Initialization: `User("Alice")` creates an instance with `name="Alice"`.
    -   `skip_ads`: `user.skip_ads()` returns `False`.
-   **PremiumUser Class**:
    -   Initialization: `PremiumUser("Bob")` creates an instance with `name="Bob"`, matching `User`’s process.
    -   `skip_ads`: `premium_user.skip_ads()` returns `True`.
-   **Inheritance**:
    -   `PremiumUser` inherits from `User`, verified with `issubclass(PremiumUser, User)` → `True`.
    -   `PremiumUser` instances have `name` and overridden `skip_ads`.
-   **Documentation**: Each class and method includes clear docstrings.

## Potential Considerations 🛠️

-   **Correctness**: Exact match for initialization and `skip_ads` behavior; inheritance avoids code duplication.
-   **Extensibility**: Classes can be extended with additional attributes (e.g., subscription details) or methods (e.g., `renew_subscription`).
-   **Design**: Simple inheritance and method overriding align with arbitrary implementation; docstrings enhance clarity.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create instances
user = User("Alice")
premium_user = PremiumUser("Bob")

# Test attributes and methods
print(user.name)  # Alice
print(user.skip_ads())  # False
print(premium_user.name)  # Bob
print(premium_user.skip_ads())  # True
print(isinstance(premium_user, User))  # True
```

## Conclusion 🚀

The `User` and `PremiumUser` implementation is accurate, providing a clear distinction between standard and premium users through inheritance and method overriding.
It’s ideal for modeling user types in subscription-based systems or inheritance education, fully compliant with the task’s requirements.
