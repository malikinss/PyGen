# Const Class Immutable Attribute Container

## Description 📝

The `Const` class is a robust utility designed to create objects with immutable attributes in Python, accepting an arbitrary number of named arguments during instantiation.
These arguments are set as attributes, which can be retrieved but neither modified nor deleted.
Attempting to change an attribute’s value raises an `AttributeError` with the message "Changing the attribute value is not allowed," and attempting to delete an attribute raises an `AttributeError` with "Deleting the attribute is not allowed," ensuring strict immutability after initialization.

## Purpose 🎯

This class is crafted for scenarios requiring constant, unchangeable data, such as configuration settings, fixed metadata, or immutable data structures in applications like scientific computing, configuration management, or secure data handling.
It’s also an excellent educational tool for demonstrating Python’s attribute access control, offering a clear example of how to enforce immutability in object-oriented programming, making it valuable for developers aiming to prevent unintended modifications in critical systems.

## How It Works 🔍

-   **Initialization (`__init__`)**: Accepts arbitrary keyword arguments (`**kwargs`) to define the initial attributes:
    -   Iterates over each key-value pair in `kwargs`, setting them as attributes using `object.__setattr__(self, attr, value)` to bypass the custom `__setattr__` logic, ensuring safe initialization without triggering immutability checks prematurely.
    -   Establishes the object’s initial state with all provided attributes, which become immutable once set.
-   **Attribute Setting (`__setattr__`)**: Overrides Python’s default attribute assignment to enforce immutability:
    -   Checks if the attribute (`attr`) already exists in `self.__dict__`, indicating an attempt to modify an existing attribute.
    -   If the attribute exists, raises an `AttributeError` with the message "Changing the attribute value is not allowed," preventing any changes to established attributes.
    -   If the attribute is new (i.e., not in `__dict__`), allows setting it with `object.__setattr__(self, attr, value)`, supporting dynamic attribute addition post-initialization where permitted (though typically all attributes are set during `__init__` per usage).
-   **Attribute Deletion (`__delattr__`)**: Overrides attribute removal to maintain immutability:
    -   Unconditionally raises an `AttributeError` with "Deleting the attribute is not allowed" for any attempt to delete an attribute, ensuring no attributes can be removed from the instance.
-   **Immutability Guarantee**: The combination of `__setattr__` and `__delattr__` ensures that once an attribute is set (during initialization or later if allowed), it cannot be changed or deleted, preserving the object’s state as a constant.

## Usage 📦

1. **Save the Code**: Store the `Const` class in a Python file, e.g., `const.py`, for integration into projects or submission to a testing system.
2. **Create and Test Instances**: Instantiate with named arguments and attempt attribute operations to verify immutability:
    ```python
    from const import Const
    obj = Const(name="book", price=10, count=5)
    print(obj.name)       # book
    print(obj.price)      # 10
    print(obj.count)      # 5
    # obj.price = 20      # Raises AttributeError: Changing the attribute value is not allowed
    # del obj.name        # Raises AttributeError: Deleting the attribute is not allowed
    ```
3. **Apply in Context**: Use in applications requiring fixed configurations, such as defining constant parameters in a simulation, securing API keys, or maintaining immutable records in a database-like structure where changes must be explicitly prevented.
4. **Test Immutability**: Experiment with various attribute types (e.g., `Const(id=1, label="test", data=[1, 2])`) and attempt modifications or deletions to confirm that the class enforces its immutability rules consistently across all attributes.

## Conclusion 🚀

The `Const` class delivers a powerful and elegant solution for creating immutable objects in Python, ensuring that attributes set during initialization (or later, if intentionally allowed) remain unchangeable and undeletable.
By leveraging `__setattr__` to block modifications and `__delattr__` to prevent deletions, it provides a bulletproof mechanism for maintaining constant data, with clear error messages to guide users when rules are violated.
This makes it an ideal choice for applications where data integrity is paramount, such as in configuration management or immutable data modeling, and it serves as a compelling educational example of Python’s attribute control capabilities.
The implementation is intentionally streamlined, focusing on the core immutability requirement without unnecessary overhead, yet it’s robust enough to handle diverse use cases with ease.
While already complete, it could be extended with features like freezing nested objects or listing attributes, but its current form fully satisfies the task with precision and clarity, ready to safeguard critical data in any project needing constant, reliable attributes.
