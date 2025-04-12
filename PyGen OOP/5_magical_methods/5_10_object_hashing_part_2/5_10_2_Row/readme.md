# Row Class Immutable Attribute Record

## Description 📝

The `Row` class encapsulates a fixed set of named attributes, set during instantiation with arbitrary keyword arguments.
It enforces strict immutability by prohibiting the addition, modification, or deletion of attributes, raising specific `AttributeError` exceptions for each violation: "It isn't possible to set a new attribute," "It isn't possible to change the attribute value," and "It isn't possible to delete an attribute."
The class provides a formal string representation as `Row(attr1=value1, attr2=value2, ...)`, with string values quoted, supports equality comparisons (`==`, `!=`) based on identical attribute sets (names, values, and order), and computes a hash value using all attributes, making instances hashable for use in sets or dictionaries.

## Purpose 🎯

This class is designed for scenarios requiring immutable, structured data records, such as database rows, configuration snapshots, or event logs in applications like data processing, auditing systems, or functional programming patterns.
Its immutability ensures data integrity, while equality and hashing enable efficient storage and comparison, making it ideal for deduplication or indexing.
It’s also a valuable educational tool for teaching Python’s advanced features, including attribute control, custom representations, and hashable objects.

## How It Works 🔍

-   **Initialization (`__init__`)**: Accepts arbitrary keyword arguments (`**kwargs`):
    -   Sets each key-value pair as an attribute using `object.__setattr__` to bypass the custom `__setattr__` logic, ensuring safe initialization without triggering immutability checks.
    -   Establishes the immutable attribute set that defines the instance.
-   **Attribute Setting (`__setattr__`)**: Enforces immutability:
    -   Checks if the attribute (`attr`) exists using `hasattr(self, attr)`.
    -   If it doesn’t exist, raises `AttributeError` with "It isn't possible to set a new attribute," preventing new attributes post-initialization.
    -   If it exists, raises `AttributeError` with "It isn't possible to change the attribute value," blocking modifications to existing attributes.
-   **Attribute Deletion (`__delattr__`)**: Prevents removal:
    -   Raises `AttributeError` with "It isn't possible to delete an attribute" for any deletion attempt, ensuring no attributes can be removed.
-   **Formal Representation (`__repr__`)**:
    -   Generates a string like `Row(attr1=value1, attr2=value2, ...)` by iterating over `self.__dict__`.
    -   Quotes string values (e.g., `name='text'`) using `isinstance(v, str)`, while non-string values are formatted directly (e.g., `count=5`).
    -   Returns `Row()` for empty instances, ensuring a consistent format.
-   **Equality Comparison (`__eq__`)**:
    -   Verifies if `other` is a `Row` instance with `isinstance(other, Row)`.
    -   Compares the sorted attribute dictionaries as tuples (`tuple(self.__dict__.items())`) to ensure identical names, values, and order.
    -   Returns `True` for matching attributes, `False` otherwise, or `NotImplemented` for non-`Row` operands, enabling `__ne__` via fallback.
-   **Hashing (`__hash__`)**:
    -   Computes the hash of `tuple(self.__dict__.items())`, incorporating all attribute names and values in their order.
    -   Relies on the guarantee that attribute values are hashable, ensuring a consistent and unique hash for equal instances, suitable for hash-based collections.
-   **Immutability**: The combination of `__setattr__` and `__delattr__` guarantees that the attribute set remains fixed, aligning with hashability requirements and preventing runtime changes.

## Usage 📦

1. **Save the Code**: Store the `Row` class in a Python file, e.g., `row.py`, for use in projects or submission to a testing system.
2. **Create and Test Instances**: Instantiate with named arguments and verify behavior:
    ```python
    from row import Row
    r1 = Row(name="book", price=10)
    r2 = Row(name="book", price=10)
    r3 = Row(price=10, name="book")
    print(r1)              # Row(name='book', price=10)
    print(r1 == r2)        # True
    print(r1 == r3)        # False (different order)
    print(hash(r1) == hash(r2))  # True
    # r1.price = 20        # Raises AttributeError: It isn't possible to change the attribute value
    # r1.new = 1           # Raises AttributeError: It isn't possible to set a new attribute
    # del r1.name          # Raises AttributeError: It isn't possible to delete an attribute
    ```
3. **Apply in Context**: Use in data pipelines to represent immutable records, in sets for deduplication (e.g., `{r1, r2}`), or in dictionaries as keys, leveraging hashing and equality for efficient operations.
4. **Test Scenarios**: Experiment with varied attributes (e.g., `Row(id=1, label='test', active=True)`), empty instances (`Row()`), or comparisons with non-`Row` objects to confirm `NotImplemented` handling, ensuring robust behavior across use cases.

## Conclusion 🚀

The `Row` class delivers a robust and elegant solution for creating immutable, hashable records in Python, with a clear focus on enforcing attribute immutability through precise error handling.
Its support for formal string representation, equality comparisons, and hashing makes it versatile for both practical applications—like storing fixed data snapshots—and educational purposes, demonstrating Python’s advanced object customization.
The implementation ensures that all attributes, their order, and values contribute to equality and hashing, providing consistency in collections while the strict immutability rules safeguard data integrity.
While already complete, the class could be extended with iteration support or attribute access methods, but its current form fully satisfies the task with clarity and efficiency, ready to enhance any project needing reliable, immutable data structures with rich comparison and hashing capabilities.
