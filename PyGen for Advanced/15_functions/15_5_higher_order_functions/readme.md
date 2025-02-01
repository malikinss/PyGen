# Lesson 15.5: Higher-Order Functions

## Description 📝

This lesson focuses on **higher-order functions**, which are functions that can take other functions as arguments or return them as results.
Higher-order functions allow for greater flexibility and modularity in programming, enabling functional programming techniques such as `map()`, `filter()`, and `reduce()`.

Key topics covered in this lesson:

-   **Higher-Order Functions**: Understanding how functions can be passed as arguments and returned as values.
-   **Home-Written `map()`, `filter()`, and `reduce()`**: Implementing custom versions of Python’s built-in functional programming utilities.
-   **Applying Functional Programming Concepts**: Using built-in and custom higher-order functions for list transformations and aggregations.

This lesson includes **5 practical tasks** and **8 theoretical questions** to reinforce the concepts.

## Purpose 🎯

The goal of this lesson is to introduce the power of higher-order functions in Python and demonstrate their application in solving real-world problems.
By mastering these concepts, I will learn how to write cleaner, more modular, and efficient code by leveraging function composition and abstraction.

## Practical Tasks 🔍

### 1. `Rounding Numbers to 2 Decimal Places Using map()`

-   **Description**: This task involves rounding a list of floating-point numbers to 2 decimal places using the `map()` function.
-   **Purpose**: Demonstrates how to apply the same function to every element in a list using `map()`.

### 2. `Filtering and Cubing Numbers Divisible by 5 with Remainder 2`

-   **Description**: The program filters a list of numbers to find three-digit numbers that leave a remainder of 2 when divided by 5, then computes their cubes.
-   **Purpose**: Uses `filter()` to select specific elements and `map()` to transform them.

### 3. `Sum of Squares of Elements in the List`

-   **Description**: This task calculates the sum of squares of numbers in a list using two approaches:
    1. The `reduce()` function.
    2. A combination of `map()` and `sum()`.
-   **Purpose**: Demonstrates different approaches to aggregating values in functional programming.

### 4. `Sum of Squares of Two-Digit Numbers Divisible by 7`

-   **Description**: The program filters a list for two-digit numbers divisible by 7, squares them, and computes their sum.
-   **Purpose**: Showcases the use of `filter()`, `map()`, and `sum()` for data transformation.

### 5. `Function to Apply a Given Function to Each Item in a List`

-   **Description**: This task defines `func_apply()`, a function that takes another function and a list as arguments, applying the function to each list element.
-   **Purpose**: Provides a flexible way to apply transformations dynamically, demonstrating the power of higher-order functions.

## Conclusion 🚀

Higher-order functions are a fundamental concept in functional programming that enables code reusability, abstraction, and cleaner design patterns. By understanding how to use `map()`, `filter()`, and `reduce()`, along with writing custom implementations, I will be able to write more expressive and efficient Python programs.
