# Person Class Name Manager

## Description 📝

The `Person` class represents a person with a first name and last name, initialized with these values upon instantiation.
It features a `fullname` property, implemented using the `@property` decorator, which provides read-write access to the full name as a string, ensuring synchronization between the full name and individual name components.

## Purpose 🎯

This class is designed for managing personal name data, ideal for contact lists, educational demonstrations of Python decorators, or systems requiring dynamic name updates.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets the `name` and `surname` attributes.
-   **fullname Property (Getter)**: Uses `@property` to return the full name as `<name> <surname>`.
-   **fullname Property (Setter)**: Uses `@fullname.setter` to split a new full name into `name` and `surname`, updating both attributes.

## Usage 📦

1. Save the class in a Python file, e.g., `person.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from person import Person
person = Person("John", "Doe")
print(f"Full name: {person.fullname}")
person.name = "Jane"
print(f"Updated full name: {person.fullname}")
person.fullname = "Alice Smith"
print(f"New full name: {person.fullname}")
```

## Conclusion 🚀

The `Person` class leverages Python’s `@property` decorator to elegantly manage a person’s name, ensuring seamless updates between the full name and its components.
It’s a practical tool for name handling, easily extensible with additional features like validation or middle names for more complex applications.
