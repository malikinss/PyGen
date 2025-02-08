# Lesson 15.9: Functions `any()`, `all()`, `zip()`, `enumerate()`

## Description 📝

In this lesson, I explore four essential built-in Python functions: **`any()`**, **`all()`**, **`zip()`**, and **`enumerate()`**.
These functions play a crucial role in efficiently handling iterables and checking conditions in Python.

The lesson contains 7 practical tasks where these functions are applied to real-world scenarios, including command filtering, validating IP addresses, and checking password strength.
The key topics are:

-   **`any()`**: Returns `True` if any element in the iterable is `True`.
-   **`all()`**: Returns `True` if all elements in the iterable are `True`.
-   **`zip()`**: Combines multiple iterables element-wise.
-   **`enumerate()`**: Adds a counter to an iterable, returning it as an enumerate object.

## Purpose 🎯

The aim of this lesson is to help me understand how to utilize these functions for various tasks, such as:

-   Checking conditions across multiple elements.
-   Combining iterables for parallel iteration.
-   Adding counters to iterables in a clean and efficient way.

These functions are integral to Python and can be used to simplify my code, making it more readable and efficient.

## Tasks 📜

1. **Ignore Command Filter 🛑**
   This program defines a function `ignore_command()` that checks whether a given command string contains any restricted substrings from a predefined list. It returns `True` if any word from the list is found, and `False` otherwise.

2. **Country Information 🌍**
   This program displays information about countries, including capitals and populations, using `zip()` for parallel iteration over three lists: `countries`, `capitals`, and `populations`.

3. **Sphere Point Location Checker 🌐**
   This program checks if a set of 3D points lie inside or on the surface of a sphere with a radius of 2 units. The equation used is \(x^2 + y^2 + z^2 \leq R^2\).

4. **IP Address Validator 🖥️**
   This program validates whether a given IPv4 address is correct by ensuring it consists of four decimal numbers (octets) between 0 and 255, separated by periods.

5. **Self-Dividing Numbers Finder 🔢**
   This program identifies all self-dividing numbers in a specified range. A self-dividing number is divisible by each of its non-zero digits.

6. **Password Strength Checker 🔐**
   This program checks if a password meets security criteria: a minimum length of 7 characters and containing at least one uppercase letter, one lowercase letter, and one digit.

7. **Teacher Timur's Test Checker 📚**
   This program checks if each class has at least one "excellent" student who scored a grade of 5. It uses `all()` and `any()` to verify if the conditions are met for each group.

## Conclusion 🚀

Mastering functions like `any()`, `all()`, `zip()`, and `enumerate()` is crucial for writing efficient, readable, and Pythonic code.
This lesson helps me apply these functions in various contexts, such as filtering commands, validating IPs, and checking password strength.
By using these functions, I'll be able to handle multiple iterables and conditions more efficiently in my projects.
