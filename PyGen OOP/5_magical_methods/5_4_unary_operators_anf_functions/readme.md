# Lesson 5.4: Unary Operators and Functions ➕➖

## Description 📝

This lesson covers:

-   Magic methods **`__pos__()`**, **`__neg__()`**, and **`__invert__()`** for unary operators
-   Magic methods **`__abs__()`**, **`__round__()`**, and similar functions
-   Practical implementation of unary operations on objects

This lesson includes a detailed theoretical explanation, 5 programming practical tasks, and 8 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand how to implement unary operators using magic methods  
✅ Use **`__abs__()`** and **`__round__()`** to extend object functionality  
✅ Apply unary operations to manipulate objects in practical scenarios  
✅ Be able to overload operators for custom behavior in classes

## Concepts & Theory 🔍

### 🔹 **`__pos__()`** Magic Method

-   **Purpose**: Defines behavior for the unary `+` operator (e.g., `+obj`).
-   **When Used**: To return a copy or affirm the object’s state.

### 🔹 **`__neg__()`** Magic Method

-   **Purpose**: Defines behavior for the unary `-` operator (e.g., `-obj`).
-   **When Used**: To negate or invert the object’s properties.

### 🔹 **`__invert__()`** Magic Method

-   **Purpose**: Defines behavior for the unary `~` operator (e.g., `~obj`).
-   **When Used**: To perform a custom inversion, such as swapping or bitwise operations.

### 🔹 **`__abs__()`** Magic Method

-   **Purpose**: Defines behavior for the `abs()` function.
-   **When Used**: To compute the magnitude or absolute value of an object.

### 🔹 **`__round__()`** Magic Method

-   **Purpose**: Defines behavior for the `round()` function.
-   **When Used**: To round numerical values within an object, optionally with precision.

## Practical Task 🧪

### 1️⃣ **Unary Operations Across Classes**

The lesson includes 5 practical tasks, each implementing unary operators for a unique class:

1. **`ReversibleString` Class**: Represents a string.

    - `__str__`: Original string
    - `-obj`: Reverses the string via `__neg__`.

2. **`Money` Class**: Represents an amount in rubles.

    - `__str__`: `<amount> rubles`
    - `+obj`: Non-negative amount via `__pos__`
    - `-obj`: Negative amount via `__neg__`.

3. **`Vector` Class**: Represents a 2D vector.

    - `__repr__`: `Vector(x, y)`
    - `__str__`: `(x, y)`
    - `+obj`: Same coordinates
    - `-obj`: Negated coordinates
    - `abs(obj)`: Vector modulus (`sqrt(x^2 + y^2)`).

4. **`ColoredPoint` Class**: Represents a colored point.

    - `__repr__`: Coordinates and RGB color
    - `__str__`: Coordinates only
    - `+obj`: Copy
    - `-obj`: Negate coordinates
    - `~obj`: Swap coordinates and invert color.

5. **`Matrix` Class**: Represents a 2D matrix.
    - `__repr__` & `__str__`: Matrix representation
    - `+obj`: Copy
    - `-obj`: Negate values
    - `~obj`: Transpose
    - `round(obj, n)`: Round values to `n` decimals.

💡 These tasks showcase diverse applications of unary operators and functions.

## Benefits ✅

-   **`__pos__()`** and **`__neg__()`** enable intuitive object manipulation.
-   **`__invert__()`** provides flexibility for custom inversions.
-   **`__abs__()`** and **`__round__()`** extend object utility with built-in functions.
-   Unary operator overloading enhances code expressiveness and functionality.

## Output 📜

After completing this lesson, I now:  
✅ Implement unary operators using magic methods  
✅ Use **`__abs__()`** and **`__round__()`** for advanced object behavior  
✅ Apply unary operations to practical examples like strings, vectors, and matrices

## Conclusion 🚀

Mastering unary operators and functions with magic methods empowers me to create intuitive, functional Python objects.  
From reversing strings to negating vectors and transposing matrices, these tools enhance object manipulation, making code more versatile and powerful. 🧑‍💻✨
