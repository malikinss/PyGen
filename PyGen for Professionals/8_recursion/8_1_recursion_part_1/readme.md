# Lesson 8.1: Recursion (Part 1) 🔁

## Description 📝

This lesson introduces me to the concept of **recursion**, a technique in programming where a function calls itself to solve smaller instances of the same problem.
It explains both **tail recursion** and general recursion concepts, providing me with the foundation needed to understand recursive algorithms.

## Purpose 🎯

By the end of this lesson, I will be able to:

-   Understand the basics of **recursion** and how it works in programming.
-   Differentiate between **general recursion** and **tail recursion**.
-   Apply recursion in solving problems that can be broken down into smaller subproblems.

## Study Material 🔍

1. **Introduction to Recursion** 📚  
   Recursion occurs when a function calls itself, either directly or indirectly, to solve smaller versions of the same problem.  
   The key parts of a recursive function are:

    - **Base Case:** The condition under which the function stops calling itself.
    - **Recursive Case:** The part where the function calls itself with modified arguments, gradually moving towards the base case.

    **Example:**

    - Factorial calculation is a classic example of recursion where the factorial of a number `n` is calculated as `n * factorial(n-1)`, with the base case being `factorial(0) = 1`.

2. **Tail Recursion** 🦷  
   Tail recursion is a special form of recursion where the recursive call is the last operation in the function. This allows for optimization by some programming languages and compilers, making the recursion behave like a loop and avoiding excessive stack usage.  
   The key here is that the recursive call doesn’t require any work after it returns.

    **Example:**  
     In a function like `factorial(n, result)`, the result is carried forward as a parameter, and the function does not need to do any further work after calling itself. This leads to efficient memory usage.

## Conclusion 🚀

This lesson introduces the concept of recursion, which is vital for solving problems that can be broken down into smaller, repetitive tasks.
Understanding both **general recursion** and **tail recursion** is crucial for writing efficient and readable recursive algorithms.
Recursion is a fundamental concept that I will continue to explore as I tackle more complex problems in programming.
