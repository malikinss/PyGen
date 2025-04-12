# Logger Class Attribute Tracker

## Description 📝

The `Logger` class is a utility designed to monitor and log modifications to its instance attributes without requiring initialization arguments.
Whenever an attribute is set or updated, it prints a message indicating the attribute name and its new value.
Similarly, when an attribute is deleted, it logs the deletion event with the attribute’s name.
This implementation corrects any prior incorrect attempts by properly handling attribute operations using Python’s special methods.

## Purpose 🎯

This class is tailored for debugging, auditing, or tracking changes to object state in Python applications.
It’s ideal for scenarios where developers need visibility into attribute modifications, such as in configuration management, testing environments, or educational settings to illustrate dynamic attribute handling.
Its logging behavior provides a clear audit trail for attribute interactions, enhancing transparency in object lifecycle management.

## How It Works 🔍

-   **Initialization (`__init__`)**: Defined as an empty method since the class requires no arguments at instantiation, ensuring a lightweight setup that prepares the object to accept arbitrary attributes dynamically.
-   **Attribute Setting (`__setattr__`)**: Overrides Python’s default attribute assignment to include logging:
    -   Takes the attribute name (`attr`) and new value (`value`) as arguments.
    -   Prints a message in the format `Изменение значения атрибута <attr> на <value>`, using Russian as implied by the code’s output strings.
    -   Uses `object.__setattr__(self, attr, value)` to set the attribute on the instance’s dictionary, avoiding infinite recursion that would occur if `self.__dict__[attr] = value` or `self.attr = value` were used directly within `__setattr__`.
-   **Attribute Deletion (`__delattr__`)**: Overrides attribute removal to log the event:
    -   Takes the attribute name (`attr`) to be deleted.
    -   Prints `Удаление атрибута <attr>` to indicate the deletion.
    -   Calls `object.__delattr__(self, attr)` to perform the actual removal, ensuring safe deletion without triggering recursive calls to `__delattr__`.
-   **Dynamic Behavior**: Since no attributes are predefined, the class can handle any attribute names dynamically, logging all set and delete operations as they occur.

## Usage 📦

1. **Save the Code**: Store the `Logger` class in a Python file, e.g., `logger.py`, for integration into projects or submission to a testing system.
2. **Create and Test Logger Instances**: Instantiate and manipulate attributes to observe logging:
    ```python
    from logger import Logger
    log = Logger()
    log.name = "test"     # Prints: Изменение значения атрибута name на test
    log.value = 42        # Prints: Изменение значения атрибута value на 42
    log.name = "new"      # Prints: Изменение значения атрибута name на new
    del log.name          # Prints: Удаление атрибута name
    ```
3. **Apply in Context**: Use in debugging scenarios to track object state changes, such as monitoring configuration settings in a system or logging variable assignments in a script.
4. **Explore Flexibility**: Assign various data types (strings, numbers, lists) to attributes and delete them to confirm consistent logging, noting that all operations are logged regardless of the value’s type.

## Conclusion 🚀

The `Logger` class delivers a robust and straightforward solution for tracking attribute modifications in Python, correcting any prior implementation errors by properly leveraging `__setattr__` and `__delattr__`.
Its logging of set and delete operations provides valuable insight into an object’s state changes, making it a powerful tool for developers needing to monitor dynamic attribute interactions.
The use of `object`’s base methods ensures safe attribute manipulation without recursion issues, while the absence of predefined attributes allows complete flexibility in usage.
This class shines in debugging or auditing tasks and serves as an excellent educational example of Python’s special methods.
While already fully functional, it could be extended with features like logging to a file, timestamping events, or filtering specific attributes, but its current form meets the task’s requirements with precision and clarity, ready to enhance any project requiring attribute change visibility.
