# NonNegativeObject Class Positive Attribute Setter

## Description 📝

The `NonNegativeObject` class is a flexible container that accepts an arbitrary number of named arguments during instantiation, setting them as instance attributes.
For any attribute value that is a negative number (integer or float), it automatically converts it to its positive equivalent by taking the absolute value, while non-numeric or non-negative values are stored unchanged.
This ensures all numeric attributes are non-negative, providing a consistent and predictable object state.

## Purpose 🎯

This class is designed for scenarios where objects must maintain non-negative numeric attributes, such as in financial applications (e.g., ensuring positive balances), simulations (e.g., non-negative distances or quantities), or educational exercises demonstrating dynamic attribute manipulation in Python.
Its ability to transparently handle negative inputs makes it valuable for robust data modeling where negative values are invalid or undesirable, simplifying downstream logic.

## How It Works 🔍

-   **Initialization (`__init__`)**: Accepts arbitrary keyword arguments (`**kwargs`) to set as attributes:
    -   Iterates over each key-value pair in `kwargs`, where the key is the attribute name and the value is the attribute value.
    -   Checks if the value is a number (`isinstance(value, (int, float))`) and negative (`value < 0`).
    -   If both conditions are true, assigns the negated value (`-value`) to make it positive, effectively computing the absolute value.
    -   If the value is not a negative number (i.e., non-numeric, zero, or positive), assigns it as-is.
    -   Uses `object.__setattr__(self, attr, value)` to set each attribute directly on the instance, bypassing any potential custom `__setattr__` method (though none is defined here, it’s a safe practice for clarity and future-proofing).
-   **Attribute Storage**: Stores all attributes in the instance’s dictionary, accessible via standard dot notation (e.g., `obj.attr`), with numeric values guaranteed to be non-negative.
-   **Type Handling**: Specifically targets `int` and `float` for negativity checks, leaving other types (strings, lists, etc.) untouched, ensuring flexibility for mixed-type attributes.

## Usage 📦

1. **Save the Code**: Store the `NonNegativeObject` class in a Python file, e.g., `non_negative_object.py`, for integration into projects or submission to a testing system.
2. **Create and Test Instances**: Instantiate with various named arguments to verify non-negative behavior:
    ```python
    from non_negative_object import NonNegativeObject
    obj = NonNegativeObject(a=-5, b=3, c=-2.5, d="text", e=0)
    print(obj.a)    # 5
    print(obj.b)    # 3
    print(obj.c)    # 2.5
    print(obj.d)    # text
    print(obj.e)    # 0
    ```
3. **Apply in Context**: Use in applications like inventory systems to ensure quantities are non-negative, financial tools to enforce positive balances, or data processing pipelines where negative metrics need correction to positive values.
4. **Experiment with Inputs**: Test with diverse inputs, such as mixed types (`obj = NonNegativeObject(x=-10, y="hello", z=-3.14)`), to confirm that only negative numbers are adjusted while other values remain intact.

## Conclusion 🚀

The `NonNegativeObject` class provides a straightforward and reliable mechanism for creating objects with guaranteed non-negative numeric attributes in Python, seamlessly converting negative numbers to their positive counterparts during initialization.
Its use of `**kwargs` allows unlimited flexibility in attribute naming and values, while the targeted logic for `int` and `float` ensures precise handling of numeric data without affecting other types. This makes it an excellent choice for applications requiring positive-only numbers, such as budgeting tools or physical simulations, as well as a clear educational example of dynamic attribute assignment.
The implementation is intentionally minimal, focusing on the core requirement with no unnecessary complexity, yet it’s robust enough to handle real-world use cases effectively.
While already complete, it could be enhanced with features like attribute update methods or logging for changes, but its current form fully satisfies the task with clarity and efficiency, ready to support any project needing enforced non-negative attributes with ease.
