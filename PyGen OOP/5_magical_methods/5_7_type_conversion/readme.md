# Lesson 5.7: Type Conversion 🔄

## Description 📝

This lesson covers:

-   Magic method **`__bool__()`** for boolean conversion
-   Magic methods **`__int__()`**, **`__float__()`**, and **`__complex__()`** for numeric conversions
-   Practical implementation of type conversion for objects

This lesson includes a detailed theoretical explanation, 3 programming practical tasks, and 8 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand how to implement type conversion using magic methods  
✅ Enable objects to behave like booleans and numbers in different contexts  
✅ Apply type conversion to practical scenarios like vectors, temperatures, and Roman numerals

## Concepts & Theory 🔍

### 🔹 **`__bool__()`** Magic Method

-   **Purpose**: Defines behavior for conversion to boolean (e.g., `bool(obj)`).
-   **When Used**: To determine truthiness in conditional statements.

### 🔹 **`__int__()`** Magic Method

-   **Purpose**: Defines behavior for conversion to integer (e.g., `int(obj)`).
-   **When Used**: To provide an integer representation of an object.

### 🔹 **`__float__()`** Magic Method

-   **Purpose**: Defines behavior for conversion to float (e.g., `float(obj)`).
-   **When Used**: To provide a real number representation of an object.

### 🔹 **`__complex__()`** Magic Method

-   **Purpose**: Defines behavior for conversion to complex number (e.g., `complex(obj)`).
-   **When Used**: To provide a complex number representation, typically for mathematical objects.

## Practical Task 🧪

### 1️⃣ **Type Conversion Across Classes**

The lesson includes 3 practical tasks, each implementing type conversion for a unique class:

1. **`Vector` Class**: Represents a 2D vector with `x` and `y` coordinates.

    - `__str__`: `(x, y)`
    - `bool`: True if nonzero
    - `int`: Integer magnitude
    - `float`: Real magnitude
    - `complex`: `x + yi`.

2. **`Temperature` Class**: Represents a temperature in Celsius.

    - `__str__`: Value to two decimals with °C
    - `bool`: True if above 0°C
    - `int`: Integer part
    - `float`: Real value
    - Includes methods for Fahrenheit conversion.

3. **`RomanNumeral` Class**: Represents a Roman numeral (e.g., `IV`).
    - `__str__`: Roman numeral string
    - `int`: Integer equivalent
    - Supports comparisons (`==`, `!=`, `<`, `>`, `<=`, `>=`) and arithmetic (`+`, `-`).

💡 These tasks demonstrate how type conversion integrates objects with Python’s type system.

## Benefits ✅

-   **`__bool__()`** enables intuitive use in conditionals.
-   Numeric conversions (`__int__()`, `__float__()`, `__complex__()`) allow seamless integration with math operations.
-   Type conversion enhances object versatility across contexts.
-   Custom conversions make objects more expressive and reusable.

## Output 📜

After completing this lesson, I now:  
✅ Implement type conversion using magic methods  
✅ Enable objects to act as booleans, integers, floats, and complex numbers  
✅ Apply type conversion to practical examples like vectors and Roman numerals

## Conclusion 🚀

Mastering type conversion with magic methods allows me to create objects that integrate seamlessly with Python’s type system.  
From evaluating vector magnitudes to converting Roman numerals, these tools enhance flexibility, making objects adaptable for diverse applications. 🧑‍💻✨
