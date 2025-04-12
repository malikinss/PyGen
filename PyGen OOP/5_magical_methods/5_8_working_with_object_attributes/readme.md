# Lesson 5.8: Working with Object Attributes 🔧

## Description 📝

This lesson covers:

-   Attribute operations in Python
-   Magic methods **`__getattribute__()`** and **`__getattr__()`** for attribute access
-   Magic method **`__setattr__()`** for attribute modification
-   Magic method **`__delattr__()`** for attribute deletion

This lesson includes a detailed theoretical explanation, 8 programming practical tasks, and 6 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand how to control attribute access, modification, and deletion  
✅ Implement custom attribute behavior using magic methods  
✅ Apply attribute operations to create flexible, secure, and dynamic objects  
✅ Use these techniques in practical scenarios like logging, immutability, and access control

## Concepts & Theory 🔍

### 🔹 **`__getattribute__()`** Magic Method

-   **Purpose**: Controls access to all attribute requests, invoked before checking if an attribute exists.
-   **When Used**: To customize or intercept every attribute access attempt.

### 🔹 **`__getattr__()`** Magic Method

-   **Purpose**: Handles access to non-existent attributes, invoked only if the attribute is not found.
-   **When Used**: To provide fallback behavior or dynamic attribute generation.

### 🔹 **`__setattr__()`** Magic Method

-   **Purpose**: Defines behavior for setting attribute values.
-   **When Used**: To enforce rules or perform actions when attributes are modified.

### 🔹 **`__delattr__()`** Magic Method

-   **Purpose**: Defines behavior for deleting attributes.
-   **When Used**: To control or restrict attribute removal.

## Practical Task 🧪

### 1️⃣ **Attribute Operations Across Classes**

The lesson includes 8 practical tasks, each implementing custom attribute handling for a unique class:

1. **`Item` Class**: Represents a product with `name`, `price`, and `quantity`.

    - Capitalizes `name` on access, computes `total` dynamically (`price * quantity`).

2. **`Logger` Class**: Tracks attribute modifications.

    - Logs attribute setting and deletion with name and value.

3. **`Ord` Class**: Returns Unicode code points for single-character attribute names.

    - Raises `AttributeError` for invalid names.

4. **`DefaultObject` Class**: Provides a fallback for non-existent attributes.

    - Returns a specified `default` value (defaults to `None`).

5. **`NonNegativeObject` Class**: Ensures numeric attributes are non-negative.

    - Converts negative numbers to positive using absolute value.

6. **`AttrsNumberObject` Class**: Tracks the number of attributes.

    - Updates `attrs_num` dynamically when attributes change.

7. **`Const` Class**: Enforces immutable attributes.

    - Raises `AttributeError` on attempts to modify or delete attributes.

8. **`ProtectedObject` Class**: Restricts access to attributes starting with `_`.
    - Raises `AttributeError` for protected attribute operations.

💡 These tasks demonstrate diverse applications of attribute management, from logging to immutability.

## Benefits ✅

-   **`__getattribute__()`** and **`__getattr__()`** enable flexible attribute access control.
-   **`__setattr__()`** enforces rules for attribute modification.
-   **`__delattr__()`** protects against unauthorized attribute removal.
-   Custom attribute handling enhances object robustness and functionality.

## Output 📜

After completing this lesson, I now:  
✅ Control attribute access, modification, and deletion with magic methods  
✅ Implement dynamic, secure, and immutable attribute behaviors  
✅ Apply attribute operations to practical examples like logging and protected objects

## Conclusion 🚀

Mastering attribute operations with magic methods empowers me to create dynamic, secure, and efficient Python objects.  
From enforcing immutability to logging changes and protecting sensitive data, these tools unlock advanced object-oriented design, making code more robust and versatile. 🧑‍💻✨
