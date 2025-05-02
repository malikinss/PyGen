# Lesson 8.4: Decorators (Part 1) 🎨

## Description 📝

This lesson covers:

-   Decorators in Python
-   Decorating methods with class-based decorators
-   Creating decorator classes for advanced functionality

This lesson includes a detailed theoretical explanation, 7 programming practical tasks, and 8 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand how decorators enhance function behavior  
✅ Create class-based decorators for methods and functions  
✅ Implement decorators for argument validation, exception handling, and call limits  
✅ Apply decorators to practical scenarios like type checking and error management

## Concepts & Theory 🔍

### 🔹 Decorators

-   **Purpose**: Wrap functions or methods to modify their behavior.
-   **How They Work**: Use callable objects to intercept and augment function calls.

### 🔹 Decorating Methods

-   **Purpose**: Apply decorators to instance or class methods.
-   **Challenges**: Handle `self` or `cls` correctly in the decorator logic.

### 🔹 Decorator Classes

-   **Purpose**: Use classes as decorators for stateful or complex wrapping logic.
-   **Benefits**: Enable reusable, configurable decorator implementations.

## Practical Task 🧪

### 1️⃣ **Class-Based Decorators**

The lesson includes 7 practical tasks, each implementing a class-based decorator:

1. **`reverse_args` Decorator**: Reverses positional argument order.

    - Preserves metadata with `functools.update_wrapper`.

2. **`limited_calls` Decorator**: Limits function calls to `n`.

    - Raises `MaxCallsException` when limit exceeded.

3. **`takes_numbers` Decorator**: Ensures arguments are `int` or `float`.

    - Raises `TypeError` for non-numeric arguments.

4. **`returns` Decorator**: Validates return value type.

    - Raises `TypeError` for invalid return types.

5. **`exception_decorator` Decorator**: Captures execution outcome.

    - Returns `(value, None)` or `(None, errortype)`.

6. **`ignore_exception` Decorator**: Suppresses specified exceptions.

    - Prints exception message and returns `None`.

7. **`type_check` Decorator**: Matches argument types to a list.
    - Raises `TypeError` for type mismatches.

💡 These tasks demonstrate decorators for argument manipulation, type safety, and error handling.

## Benefits ✅

-   Decorators enhance functions without modifying their core logic.
-   Class-based decorators offer stateful, reusable solutions.
-   Metadata preservation ensures compatibility with introspection tools.
-   Type and exception handling improve code robustness.

## Output 📜

After completing this lesson, I now:  
✅ Create class-based decorators for methods and functions  
✅ Implement decorators for validation, limits, and error handling  
✅ Apply decorators to practical use cases like type-safe APIs

## Conclusion 🚀

Mastering decorators empowers me to write modular, reusable Python code.  
From argument validation to exception management, class-based decorators provide powerful tools for enhancing function behavior in diverse applications. 🧑‍💻✨
