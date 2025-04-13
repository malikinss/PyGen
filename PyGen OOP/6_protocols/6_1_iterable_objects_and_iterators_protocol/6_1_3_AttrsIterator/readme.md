# AttrsIterator Class Object Attribute Explorer

## Description 📝

The `AttrsIterator` class creates an iterator that traverses the attributes of a given object, yielding each as a tuple containing the attribute name and its value.
It is initialized with a single argument, `obj`, and generates tuples in the order defined by the object’s `__dict__`.
By implementing the iterator protocol with `__iter__` and `__next__`, it ensures seamless integration with Python’s iteration mechanisms, such as for-loops or `next()` calls, providing a structured way to inspect an object’s attributes.

## Purpose 🎯

This class is designed for introspecting object attributes in a controlled, sequential manner, making it ideal for debugging, serialization, or dynamic analysis in applications like data processing, object inspection tools, or configuration auditing.
Its iterator-based approach allows efficient attribute access without modifying the source object, and it serves as an educational example for teaching Python’s iterator protocol and dictionary iteration, offering a practical demonstration of custom iterator design.

## How It Works 🔍

-   **Initialization (`__init__`)**:
    -   Takes an arbitrary object (`obj`) as input.
    -   Creates a list of attribute name-value pairs by calling `obj.__dict__.items()` and storing it in `self._pairs`, preserving the order of attributes as they appear in `__dict__`.
    -   Initializes an index (`self._index`) to 0, which tracks the current position during iteration.
    -   Converts `items()` to a list to ensure a stable snapshot of attributes, avoiding issues if `__dict__` changes during iteration.
-   **Iterator Protocol (`__iter__`)**:
    -   Returns `self`, identifying the instance as its own iterator, adhering to Python’s iterator protocol and enabling use in iteration contexts like for-loops.
-   **Next Item (`__next__`)**:
    -   Checks if the current index (`self._index`) is within the bounds of `self._pairs`.
    -   If exhausted (`self._index >= len(self._pairs)`), raises `StopIteration` to signal the end of iteration.
    -   Otherwise, retrieves the tuple at `self._pairs[self._index]`, increments `self._index`, and returns the tuple, which contains the attribute name (string) and value (any type).
    -   Maintains the order of `__dict__` entries, ensuring consistent attribute traversal.
-   **Attribute Order**: Relies on `__dict__.items()` to dictate the order, which in modern Python (3.7+) preserves insertion order, aligning with the task’s requirement to match `__dict__`’s sequence.

## Usage 📦

1. **Save the Code**: Store the `AttrsIterator` class in a Python file, e.g., `attrs_iterator.py`, for use in projects or submission to a testing system.
2. **Create and Test Instances**: Instantiate with an object and iterate over its attributes:

    ```python
    from attrs_iterator import AttrsIterator
    class Test:
        def __init__(self):
            self.name = "book"
            self.price = 10
            self.count = 5

    obj = Test()
    iterator = AttrsIterator(obj)
    print(list(iterator))  # [('name', 'book'), ('price', 10), ('count', 5)]
    iterator = AttrsIterator(obj)  # Reset iterator
    print(next(iterator))  # ('name', 'book')
    print(next(iterator))  # ('price', 10)
    ```

3. **Apply in Context**: Use in debugging tools to log object attributes, in serialization to extract key-value pairs, or in data analysis to inspect object properties dynamically, leveraging the iterator for sequential processing.
4. **Test Flexibility**: Experiment with objects having varied attributes (e.g., strings, numbers, lists) or empty `__dict__` to confirm that the iterator handles all cases correctly, yielding tuples in `__dict__` order or raising `StopIteration` for empty objects.

## Conclusion 🚀

The `AttrsIterator` class provides a precise and efficient solution for iterating over an object’s attributes in Python, delivering name-value tuples in the order defined by `__dict__`.
Its implementation of the iterator protocol via `__iter__` and `__next__` ensures seamless integration with Python’s iteration tools, making it both user-friendly and robust for inspecting object state.
The class shines in scenarios requiring attribute traversal, such as debugging or data extraction, and serves as a clear educational example of custom iterators.
By storing a snapshot of `__dict__.items()`, it guarantees stable iteration, and its minimal design avoids unnecessary complexity while fully meeting the task’s requirements.
While it could be extended with features like filtering attributes or supporting nested objects, its current form is elegant, reliable, and ready to enhance any project needing structured access to object attributes with iterator-based simplicity.
