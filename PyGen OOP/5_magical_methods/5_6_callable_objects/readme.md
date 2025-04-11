# Lesson 5.6: Callable Objects 📞

## Description 📝

This lesson covers:

-   Callable objects in Python
-   Magic method **`__call__()`** for enabling object invocation
-   Practical implementation of callable objects and decorators

This lesson includes a detailed theoretical explanation, 10 programming practical tasks, and 7 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand how to make objects callable using **`__call__()`**  
✅ Create callable objects for diverse tasks like arithmetic, formatting, and sorting  
✅ Use callable objects as decorators for function enhancement  
✅ Apply these concepts to simplify code and improve functionality

## Concepts & Theory 🔍

### 🔹 Callable Objects

-   **Purpose**: Objects that can be invoked like functions using parentheses.
-   **How It Works**: Any class with a **`__call__()`** method becomes callable.

### 🔹 **`__call__()`** Magic Method

-   **Purpose**: Defines behavior when an object is called (e.g., `obj(arg)`).
-   **When Used**: To give objects function-like behavior with custom logic.

## Practical Task 🧪

### 1️⃣ **Callable Objects Across Classes**

The lesson includes 10 practical tasks, each implementing callable objects for unique use cases:

1. **`Calculator` Class**: Performs arithmetic operations (`+`, `-`, `*`, `/`).

    - Callable with two numbers and an operator, raises `ValueError` for division by zero.

2. **`RaiseTo` Class**: Raises a number to a fixed exponent.

    - Initialized with `degree`, called with `x` to compute `x ** degree`.

3. **`Dice` Class**: Simulates a die roll.

    - Initialized with sides, returns random integer from 1 to sides when called.

4. **`QuadraticPolynomial` Class**: Evaluates a quadratic polynomial `ax^2 + bx + c`.

    - Initialized with coefficients, called with `x` to compute the result.

5. **`Strip` Class**: Removes specified characters from a string.

    - Initialized with `chars`, called with a string to strip matching characters.

6. **`Filter` Class**: Filters iterables based on a predicate.

    - Initialized with optional predicate (defaults to `bool`), returns filtered list when called.

7. **`DateFormatter` Class**: Formats dates by country code.

    - Initialized with `country_code`, formats `date` objects (e.g., `ru`: DD.MM.YYYY).

8. **`CountCalls` Class**: Decorator to count function calls.

    - Tracks invocations via `calls` attribute, works with any arguments.

9. **`CachedFunction` Class**: Decorator to cache function results.

    - Stores results in `cache` dictionary for positional arguments, optimizes repeated calls.

10. **`SortKey` Class**: Simplifies sorting by object attributes.
    - Initialized with attribute names, returns tuple of values for sorting.

💡 These tasks showcase the versatility of callable objects in arithmetic, data processing, and function enhancement.

## Benefits ✅

-   **`__call__()`** enables function-like behavior for objects.
-   Callable objects simplify complex logic with intuitive interfaces.
-   Decorators like `CountCalls` and `CachedFunction` enhance function performance and tracking.
-   Classes like `SortKey` improve code readability for common tasks.

## Output 📜

After completing this lesson, I now:  
✅ Create callable objects using **`__call__()`**  
✅ Implement callable classes for arithmetic, formatting, and sorting  
✅ Use decorators to track and optimize function behavior

## Conclusion 🚀

Mastering callable objects with **`__call__()`** empowers me to design flexible, function-like Python classes.  
From simulating dice rolls to optimizing sort operations, these tools simplify code, enhance performance, and unlock creative solutions across diverse applications. 🧑‍💻✨
