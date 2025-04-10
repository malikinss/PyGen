# Lesson 5.5: Arithmetic Operations 🧮

## Description 📝

This lesson covers:

-   Magic methods **`__add__()`**, **`__sub__()`**, and **`__mul__()`** for basic arithmetic
-   Magic methods **`__truediv__()`**, **`__floordiv__()`**, and **`__mod__()`** for division and modulo
-   Reflected arithmetic operations (e.g., handling `scalar * obj`)
-   In-place magic methods **`__iadd__()`**, **`__isub__()`**, **`__imul__()`**, **`__itruediv__()`**, **`__ifloordiv__()`**, and **`__imod__()`**
-   Practical implementation of arithmetic operations on objects
    This lesson includes a detailed theoretical explanation, 5 programming practical tasks, and 14 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand how to implement arithmetic operations using magic methods  
✅ Handle reflected arithmetic for flexible operand ordering  
✅ Use in-place operations for efficient object updates  
✅ Apply arithmetic operations to practical scenarios like nutrition, vectors, and queues

## Concepts & Theory 🔍

### 🔹 **`__add__()`**, **`__sub__()`**, **`__mul__()`** Magic Methods

-   **Purpose**: Define addition (`+`), subtraction (`-`), and multiplication (`*`) for objects.
-   **When Used**: To perform arithmetic between objects or with scalars.

### 🔹 **`__truediv__()`**, **`__floordiv__()`**, **`__mod__()`** Magic Methods

-   **Purpose**: Define true division (`/`), floor division (`//`), and modulo (`%`) operations.
-   **When Used**: To handle division-based calculations with custom logic.

### 🔹 Reflected Arithmetic Operations

-   **Purpose**: Handle cases where the object is the right operand (e.g., `scalar * obj`).
-   **How It Works**: Methods like `__rmul__()` enable commutative operations.

### 🔹 In-Place Magic Methods

-   **Purpose**: Define in-place operations (e.g., `+=`, `-=`) for modifying objects directly.
-   **When Used**: To optimize performance by avoiding new object creation.

### 🔹 **`NotImplemented`** Constant

-   **Purpose**: Signals unsupported operations for invalid operands.
-   **When Used**: Returned when arithmetic cannot be performed.

## Practical Task 🧪

### 1️⃣ **Arithmetic Operations Across Classes**

The lesson includes 5 practical tasks, each implementing arithmetic operations for a unique class:

1. **`FoodInfo` Class**: Represents nutritional values (proteins, fats, carbohydrates).

    - `__repr__`: Formal nutrient representation
    - `+`: Add nutrients
    - `*`, `/`, `//`: Scale nutrients by scalar
    - Returns `NotImplemented` for invalid operands.

2. **`Vector` Class**: Represents a 2D vector with `x` and `y` coordinates.

    - `__repr__`: `Vector(x, y)`
    - `+`, `-`: Vector addition/subtraction
    - `*`, `/`: Scalar multiplication/division (both orders)
    - Returns `NotImplemented` for invalid operands.

3. **`SuperString` Class**: Encapsulates a string.

    - `__str__`: Original string
    - `+`: Concatenation
    - `*`: Repetition (both orders)
    - `/`: Truncation
    - `<<`, `>>`: Trim end/start.

4. **`Time` Class**: Represents time in `HH:MM` format.

    - `__str__`: `HH:MM`
    - `+`, `+=`: Add time (new instance or in-place)
    - Returns `NotImplemented` for invalid operands.

5. **`Queue` Class**: Implements a FIFO queue.
    - `__str__`: Queue contents
    - `+`, `+=`: Append elements
    - `>>`: Drop initial elements
    - Supports equality checks (`==`, `!=`).

💡 These tasks demonstrate diverse arithmetic operations for real-world use cases.

## Benefits ✅

-   Arithmetic magic methods enable intuitive object calculations.
-   Reflected operations ensure flexibility with operand order.
-   In-place methods optimize performance for mutable objects.
-   Custom arithmetic enhances functionality for specialized classes.

## Output 📜

After completing this lesson, I now:  
✅ Implement arithmetic operations using magic methods  
✅ Handle reflected and in-place operations for flexibility and efficiency  
✅ Apply arithmetic logic to practical examples like vectors, time, and queues

## Conclusion 🚀

Mastering arithmetic operations with magic methods allows me to create expressive, efficient Python objects.  
From nutritional calculations to queue management, these tools enable powerful, intuitive arithmetic, enhancing code functionality across diverse applications. 🧑‍💻✨
