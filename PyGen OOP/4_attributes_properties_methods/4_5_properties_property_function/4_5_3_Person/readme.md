# Person Class Name Manager

## Description 📝

The `Person` class represents a person with a first name and last name, initialized with these values upon instantiation.
It includes a read-write `fullname` property that combines the names into a single string and allows updating the individual names by setting a new full name, ensuring bidirectional synchronization.

## Purpose 🎯

This class is designed for managing personal name data, suitable for contact management systems, educational examples of properties, or applications requiring dynamic name handling.

## How It Works 🔍

-   **Initialization**: The `__init__` method sets the `name` and `surname` attributes.
-   **get_fullname() Method**: Returns the full name as a string: `<name> <surname>`.
-   **set_fullname() Method**: Splits a provided full name into `name` and `surname`, updating both attributes.
-   **Property**: `fullname` is defined as a read-write property using `property()`, linking to the getter and setter.

## Usage 📦

1. Save the class in a Python file, e.g., `person.py`.
2. Open a terminalS open a terminal and navigate to the directory where the file is saved.
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

The `Person` class provides a seamless way to manage a person’s name in Python, with its `fullname` property ensuring consistency between individual names and the combined form.
It’s a flexible tool that can be extended with additional attributes or validation for more complex identity management systems.
