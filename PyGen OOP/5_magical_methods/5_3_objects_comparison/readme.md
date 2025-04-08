# Lesson 5.3: Comparison of Objects ⚖️

## Description 📝

This lesson covers:

-   Magic methods **`__eq__()`** and **`__ne__()`** for equality and inequality
-   The **`NotImplemented`** constant for unsupported comparisons
-   Magic methods **`__lt__()`** and **`__gt__()`** for less than and greater than
-   Magic methods **`__le__()`** and **`__ge__()`** for less than or equal and greater than or equal
-   The **`@total_ordering`** decorator for complete comparison support
-   Practical implementation of object comparison

Link to the lesson: [Stepik Lesson 5.3](https://stepik.org/lesson/805771/step/1?unit=808896)

This lesson includes a detailed theoretical explanation, 4 programming practical tasks, and 14 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand how to implement object comparison using magic methods  
✅ Use **`NotImplemented`** to handle invalid comparison cases  
✅ Apply **`@total_ordering`** to simplify comparison logic  
✅ Be able to compare objects in practical scenarios like vectors, words, dates, and versions

## Concepts & Theory 🔍

### 🔹 **`__eq__()`** and **`__ne__()`** Magic Methods

-   **Purpose**: Define equality (`==`) and inequality (`!=`) for objects.
-   **When Used**: To check if two objects are equal or different based on custom criteria.

### 🔹 **`NotImplemented`** Constant

-   **Purpose**: Signals that a comparison operation is not supported for a given type.
-   **When Used**: Returned in magic methods when comparing incompatible objects.

### 🔹 **`__lt__()`** and **`__gt__()`** Magic Methods

-   **Purpose**: Define less than (`<`) and greater than (`>`) comparisons.
-   **When Used**: To establish ordering between objects.

### 🔹 **`__le__()`** and **`__ge__()`** Magic Methods

-   **Purpose**: Define less than or equal (`<=`) and greater than or equal (`>=`) comparisons.
-   **When Used**: To extend ordering with equality checks.

### 🔹 **`@total_ordering`** Decorator

-   **Purpose**: Automatically generates missing comparison methods if `__eq__()` and one ordering method (e.g., `__lt__()`) are defined.
-   **How It Works**: Reduces boilerplate code for full comparison support.

## Practical Task 🧪

### 1️⃣ **Object Comparison Across Classes**

The lesson includes 4 practical tasks, each implementing comparison for a unique class:

1. **`Vector` Class**: Represents a 2D vector with `x` and `y` coordinates.

    - `__repr__`: `Vector(x, y)`
    - Supports `==` and `!=`, returning `NotImplemented` for invalid types.

2. **`Word` Class**: Represents a word with length-based comparisons.

    - `__repr__`: `Word('word')`
    - `__str__`: Capitalized word
    - Uses `@total_ordering` for full comparison (`==`, `!=`, `<`, `>`, `<=`, `>=`).

3. **`Month` Class**: Represents a month with year and number.

    - `__repr__`: `Month(year, month)`
    - `__str__`: `year-month`
    - Uses `@total_ordering` for chronological comparisons.

4. **`Version` Class**: Represents a software version (e.g., `2.8.1`).
    - `__repr__` & `__str__`: Version string
    - Uses `@total_ordering` for hierarchical version comparisons.

💡 These tasks demonstrate tailored comparison logic for diverse use cases.

## Benefits ✅

-   **`__eq__()`** and **`__ne__()`** enable custom equality checks.
-   **`NotImplemented`** ensures robust handling of unsupported comparisons.
-   Ordering methods (`__lt__()`, `__gt__()`, etc.) provide flexible object sorting.
-   **`@total_ordering`** simplifies implementation of complete comparison logic.

## Output 📜

After completing this lesson, I now:  
✅ Implement comparison magic methods for custom object ordering  
✅ Use **`NotImplemented`** to manage invalid comparisons  
✅ Apply **`@total_ordering`** to streamline comparison code  
✅ Compare objects effectively in real-world scenarios

## Conclusion 🚀

Mastering object comparison with magic methods and **`@total_ordering`** is crucial for creating ordered, comparable Python objects.  
These tools enable precise equality checks, robust ordering, and efficient code design, applicable to everything from geometric vectors to software versioning. 🧑‍💻✨
