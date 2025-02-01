# Lesson 15.4: Functions as Objects

## Description 📝

This lesson delves into the concept of functions as first-class objects in Python, a core principle of functional programming.
In Python, functions can be treated as objects, meaning they can be assigned to variables, passed as arguments to other functions, and returned as values.
This flexibility opens up various possibilities in programming, such as higher-order functions, function composition, and more.

Key topics include:

-   **Functions as Objects**: Functions are objects in Python and can be manipulated like any other object.
-   **Functions as Arguments of Other Functions**: Functions can be passed as arguments to other functions to create reusable and modular code.
-   **Built-in Functions Taking Functions as Arguments**: Python has several built-in functions (e.g., `map()`, `filter()`, `sorted()`) that take functions as arguments, enabling more dynamic and functional approaches to solving problems.
-   **Functions as Return Values of Other Functions**: Functions can return other functions, enabling dynamic creation of new functions with customized behavior.

This lesson includes 7 practical tasks and 8 theoretical questions, which are focused on understanding and applying the concept of functions as objects.

## Purpose 🎯

This lesson helps me understand the flexibility of functions in Python, emphasizing their role as first-class citizens.
By exploring how functions can be passed as arguments, returned as values, and used as sorting criteria, I will gain deeper insights into functional programming techniques.
This knowledge enables me to write more efficient and modular code and unlocks advanced programming techniques such as higher-order functions and dynamic function generation.

## Practical Tasks 🔍

### 1. `get_avg() and min-max Arithmetic Mean Program`

This task involves calculating the arithmetic mean of tuples and using the built-in `min()` and `max()` functions to find tuples with the smallest and largest averages.
Demonstrates using `min()` and `max()` with a custom `key` function to find the tuples with the smallest and largest averages.

### 2. `Sorting Points by Distance from Origin`

This task sorts a list of points based on their distance from the origin (0, 0), calculated using the Euclidean distance formula.
Demonstrates how to sort a list of points by distance using a custom sorting key.

### 3. `Sorting Tuples by Sum of Min and Max Elements`

The goal is to sort a list of tuples based on the sum of their minimum and maximum elements.
Shows how to use a custom sorting key for sorting tuples based on the sum of their min and max elements.

### 4. `Sorting Athletes by Various Attributes`

This task involves sorting a list of athlete tuples by various attributes such as name, age, height, and weight, based on user input.
Demonstrates how to dynamically select sorting criteria for tuples using function mapping.

### 5. `Math Function Application Program`

The program allows the user to apply various mathematical operations (e.g., square, cube, square root) to a given number by selecting the operation dynamically.
Provides an example of using functions as arguments to dynamically apply mathematical operations.

### 6. `Sorting Numbers by Sum of Digits`

This task sorts numbers based on the sum of their digits in non-decreasing order.
Illustrates sorting numbers by the sum of their digits while maintaining the original order of numbers with equal digit sums.

### 7. `Sorting Numbers by Sum of Digits and Value`

This task sorts numbers by the sum of their digits. If two numbers have the same sum, they are sorted by their value.
Combines two sorting criteria—sum of digits and numerical value—demonstrating how to use multiple sorting keys.

## Conclusion 🚀

Mastering functions as objects is crucial for effective functional programming in Python.
This lesson provides the foundational knowledge required to treat functions as first-class objects, enhancing my ability to create modular, reusable, and dynamic code.
By understanding how to pass functions as arguments, return them from other functions, and utilize them in built-in functions, I open the door to more advanced techniques that allow for greater flexibility and efficiency in my programming.
