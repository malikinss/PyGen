# Lesson 9.3: Anonymous Functions, Map(), Filter() Functions 🔧

## Description 📝

This lesson focuses on **anonymous functions** (lambda functions) and higher-order functions **`map()`** and **`filter()`**, which we previously encountered in the course.
These functions allow for cleaner and more functional code when manipulating and transforming data.

## Purpose 🎯

By the end of this lesson, I will:

-   Be able to use **anonymous functions (lambda functions)** for concise function definitions.
-   Understand how to apply **`map()`** and **`filter()`** functions to manipulate and filter data in Python.
-   Learn to combine **`map()`** and **`filter()`** with **lambda functions** to write more efficient and functional code.

## How It Works 🔍

This lesson covers the following concepts:

1. **Anonymous Functions (lambda)**: Simple, unnamed functions defined using the `lambda` keyword. They are typically used for short, one-off operations where defining a full function is unnecessary.
2. **`map()`**: A higher-order function that applies a given function to each item of an iterable (like a list) and returns an iterator that yields the results.
3. **`filter()`**: Another higher-order function that filters elements from an iterable based on a condition defined in a function, returning an iterator with the elements that meet the condition.

This lesson includes 6 programming tasks:

### 1. 9_3_1_get_rounded_nums

**Goal**: Process a list of arbitrary objects, filter out only integers and floats, and round down the float numbers.

-   This task demonstrates filtering and mapping data using lambda functions and the **`map()`** and **`filter()`** functions.

### 2. 9_3_2_sum_of_squares_of_filtered_numbers

**Goal**: Calculate the sum of the squares of all two-digit numbers divisible by 9.

-   This task demonstrates using **`filter()`** to filter numbers and **`map()`** to square them.

### 3. 9_3_3_filter_names_by_conditions

**Goal**: Filter a list of Russian names based on two conditions and sort them.

-   This program demonstrates how to use **`filter()`** and **`map()`** for filtering, sorting, and manipulating strings.

### 4. 9_3_4_fib

**Goal**: Calculate the n-th term of the Fibonacci sequence using recursion and lambda functions.

-   This program demonstrates recursive function calls using **lambda functions** to calculate Fibonacci numbers.

### 5. 9_3_5_print_operation_table

**Goal**: Print a table of results from applying a binary operation to row and column indices.

-   This task demonstrates how to use a lambda function in combination with **`map()`** to apply an operation across a table.

### 6. 9_3_6_verification

**Goal**: Verify whether a password meets certain criteria (uppercase, lowercase, digit).

-   This program demonstrates how to use **lambda functions** to check conditions in a password and **`all()`** to check multiple conditions at once.

## Output 📜

After completing this lesson, I will be able to:  
✅ Use **lambda functions** for creating concise, anonymous functions.  
✅ Apply **`map()`** and **`filter()`** functions for transforming and filtering data efficiently.  
✅ Combine these techniques to solve real-world problems with Python in a functional programming style.

## Conclusion 🚀

Mastering **anonymous functions** and **higher-order functions** like **`map()`** and **`filter()`** allows me to write more concise and expressive Python code.
These tools are powerful when working with iterables and can significantly improve the readability and maintainability of code by minimizing the need for explicit loops.
