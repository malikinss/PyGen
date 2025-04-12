# AttrsNumberObject Class Dynamic Attribute Counter

## Description 📝

The `AttrsNumberObject` class is a versatile container that accepts an arbitrary number of named arguments during instantiation, setting them as instance attributes.
It includes a special attribute, `attrs_num`, which dynamically tracks the total number of attributes on the instance, including `attrs_num` itself.
This count updates automatically whenever attributes are added or removed, providing a real-time reflection of the object’s state.

## Purpose 🎯

This class is designed for scenarios where tracking the number of attributes on an object is essential, such as in debugging, object introspection, or data modeling with variable attribute sets.
It’s particularly valuable in educational contexts to illustrate Python’s attribute management and dynamic behavior, or in applications like configuration objects, metadata tracking, or flexible data structures where monitoring attribute counts enhances functionality and transparency.

## How It Works 🔍

-   **Initialization (`__init__`)**: Accepts arbitrary keyword arguments (`**kwargs`) to set as attributes:
    -   Initializes `attrs_num` to 1 (accounting for itself) using `object.__setattr__` to avoid triggering the custom `__setattr__` logic during setup.
    -   Iterates over `kwargs`, setting each key-value pair as an attribute with `object.__setattr__`.
    -   Calls `_update_attrs_num` after each attribute assignment to ensure `attrs_num` reflects the total count, including `attrs_num` and all `kwargs`.
-   **Attribute Setting (`__setattr__`)**: Overrides the default attribute assignment:
    -   Sets the attribute using `object.__setattr__(self, attr, value)` to store the value in the instance’s dictionary.
    -   Invokes `_update_attrs_num` to recalculate `attrs_num` based on the updated `__dict__`.
-   **Attribute Deletion (`__delattr__`)**: Overrides attribute removal:
    -   Deletes the attribute with `object.__delattr__(self, attr)` to remove it from `__dict__`.
    -   Calls `_update_attrs_num` to update `attrs_num` after deletion, ensuring the count remains accurate.
-   **Attribute Count Update (`_update_attrs_num`)**: A helper method that:
    -   Counts the number of keys in `self.__dict__` (all instance attributes).
    -   Sets `attrs_num` to this count using `object.__setattr__` to avoid recursive calls to `__setattr__`.
-   **Dynamic Tracking**: Ensures `attrs_num` always equals the total number of attributes, including itself, by updating after every attribute change (set or delete).

## Usage 📦

1. **Save the Code**: Store the `AttrsNumberObject` class in a Python file, e.g., `attrs_number_object.py`, for use in projects or submission to a testing system.
2. **Create and Test Instances**: Instantiate with named arguments and manipulate attributes to verify `attrs_num`:
    ```python
    from attrs_number_object import AttrsNumberObject
    obj = AttrsNumberObject(name="book", price=10)
    print(obj.attrs_num)  # 3 (name, price, attrs_num)
    obj.color = "red"
    print(obj.attrs_num)  # 4 (name, price, color, attrs_num)
    del obj.name
    print(obj.attrs_num)  # 3 (price, color, attrs_num)
    ```
3. **Apply in Context**: Use in dynamic data structures where tracking attribute counts is useful, such as configuration managers, object serialization, or debugging tools to monitor object complexity.
4. **Experiment with Changes**: Add or remove attributes dynamically (e.g., `obj.new_attr = 42`, `del obj.price`) to confirm that `attrs_num` updates correctly, testing with various types (strings, numbers, lists) to ensure flexibility.

## Conclusion 🚀

The `AttrsNumberObject` class offers a robust and dynamic solution for managing objects with an arbitrary number of attributes in Python, while maintaining an accurate count of those attributes via `attrs_num`.
By carefully overriding `__setattr__` and `__delattr__`, and using a helper method `_update_attrs_num`, it ensures that `attrs_num` reflects the exact number of attributes at all times, including itself, even as the object evolves.
This makes it an excellent tool for applications requiring introspection, such as tracking object state in testing frameworks, or for educational purposes to demonstrate Python’s attribute handling capabilities.
Its design is both efficient—avoiding unnecessary complexity—and flexible, supporting any attribute names and values without restriction.
While fully meeting the task’s requirements, the class could be extended with features like attribute validation, iteration over attributes, or logging changes, but its current implementation is clear, reliable, and ready to enhance any project needing dynamic attribute tracking with real-time counting.
