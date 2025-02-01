# Lesson 15.1: Optional and Named Arguments

## Description 📝

This lesson is dedicated to understanding and using optional and named arguments in Python functions.
You will learn about positional arguments, optional arguments (with default values), and named arguments, and how they improve the flexibility and readability of your code.

## Purpose 🎯

-   **Positional Arguments:** Learn how to pass arguments in the order expected by the function.
-   **Optional Arguments:** Understand how to define default values for function parameters so that they become optional.
-   **Named Arguments:** Discover how to pass arguments by name, enhancing clarity and allowing for flexible parameter ordering.

By mastering these concepts, you can write more versatile and maintainable functions.

## Practical Task

This lesson includes 1 practical task and 14 theoretical questions available on the [Stepik platform](https://stepik.org/lesson/503029/step/1?unit=494737).

### 15_1_1_matrix

This function, `matrix()`, dynamically creates and returns a matrix of a specified size, filled with a given value.
It provides flexibility in defining dimensions and default values.
The function is designed to generate matrices based on the number of rows and columns specified by the user.
If no dimensions are provided, it defaults to a `1×1` matrix filled with `0`.

## How It Works 🔍

-   **Positional Arguments:** The function parameters `rows`, `cols`, and `fill` can be provided in order.
-   **Optional Arguments:** Each parameter has a default value (`1` for `rows` and `cols`, `0` for `fill`), making them optional. If not provided, the function uses these defaults.
-   **Named Arguments:** You can call the function with arguments specified by name, e.g., `matrix(fill=5, rows=2, cols=3)`, improving readability.

## Theoretical Questions

In addition to the practical task, there are 14 theoretical questions available on the Stepik website that delve deeper into optional and named arguments. You can access them [here](https://stepik.org/lesson/503029/step/1?unit=494737).

## Conclusion 🚀

Understanding optional and named arguments allows you to write more flexible and understandable functions.
By using default parameter values and named arguments, you can create functions that are easier to use and maintain.
The `matrix()` function is a practical example that demonstrates these concepts in action.
