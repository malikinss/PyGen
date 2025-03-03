# Lesson 9.5: Nested Functions, Closures 🏗️

## Description 📝

This lesson covers **nested functions** and **closures** in Python.
It explains how an inner function can access variables from its outer function even after the outer function has finished executing.
It also introduces the `nonlocal` keyword and the `closure` attribute, crucial for understanding how variables from outer functions persist in inner functions.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand the concept of **nested functions** and how they work.  
✅ Learn about **closures** and how an inner function can remember and access variables from its enclosing scope.  
✅ Understand the use of the **`nonlocal`** keyword to modify variables in an outer but non-global scope.  
✅ Implement practical use cases such as **function generators** and **URL query string builders**.

## How It Works 🔍

This lesson explores the following concepts:

1. **Nested Functions**: Functions can be defined inside other functions, and the inner function can access the variables of the outer function.
2. **Closures**: A closure occurs when a nested function remembers the environment in which it was created, allowing it to access variables from the outer function even after the outer function has returned.
3. **`nonlocal` Keyword**: This keyword allows an inner function to modify variables in the outer function’s scope that are not global.

The lesson contains 5 practical programming tasks, where I will apply these concepts:

1.  **9_5_1_power**  
    **Goal**: Create a higher-order function `power(degree)` that returns a new function. This new function raises an integer to the power of `degree`.

-   This demonstrates **closures**, where the inner function has access to the `degree` variable from the outer function.

2.  **9_5_2_generator_square_polynom**  
    **Goal**: Define a generator `generator_square_polynom(a, b, c)` that returns a function representing the quadratic equation \( ax^2 + bx + c \).

-   This task shows how to generate different quadratic functions based on the coefficients. It’s a practical use case for **higher-order functions** and **closures**.

3.  **9_5_3_sourcetemplate**  
    **Goal**: Implement `sourcetemplate(url)` that returns a function which dynamically generates a URL with query parameters.

-   This task demonstrates **closures** and how they can be used to **generate dynamic URLs** based on input parameters.

4.  **9_5_4_date_formatter**  
    **Goal**: Create `date_formatter(country_code)` that returns a function for formatting dates according to a specified country's date format.

-   This task highlights the **use of closures** to create a function for formatting dates in different formats based on the country code.

5.  **9_5_5_priority_sort_key**  
    **Goal**: Define `sort_priority()` that sorts a list of numbers, prioritizing numbers from a specified group before sorting the rest.

-   This task illustrates **closures** in action, where the sorting function remembers the group and applies a specific sort order based on that.

## Output 📜

After completing this lesson, I will:  
✅ Understand how **nested functions** and **closures** allow inner functions to access outer function variables.  
✅ Be able to use the **`nonlocal`** keyword to modify variables in the enclosing function’s scope.  
✅ Implement **higher-order functions** and **closures** for practical purposes like **function generators**, **URL builders**, **date formatters**, and **sorting**.

## Conclusion 🚀

Mastering **nested functions** and **closures** significantly improves my ability to write more dynamic and efficient Python code.
Understanding how closures persist variables and how to modify them using the **`nonlocal`** keyword is essential for developing sophisticated Python applications, including function generators, dynamic URL builders, and date formatters.
These concepts form the foundation for many advanced Python features and patterns.
