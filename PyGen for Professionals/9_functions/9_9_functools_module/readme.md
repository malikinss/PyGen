# Lesson 9.9: functools module 📝

## Description 📝

In this lesson, I explore the **functools** module, which provides higher-order functions and operations on callable objects.
I will learn about several key functions in the module that help with functional programming, such as `partial()`, `update_wrapper()`, and decorators like `wraps`, as well as caching and memoization techniques with `lru_cache` and `cache`.
These tools allow me to improve performance and reusability of my functions and work with partial applications efficiently.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Learn how to use **partial functions** to create reusable and customizable functions.  
✅ Understand the role of **wrapping functions** with `update_wrapper()` and `wraps` for better documentation.  
✅ Understand **caching** and **memoization** techniques to optimize performance using `lru_cache` and `cache`.  
✅ Be able to solve problems using these techniques to improve code efficiency and flexibility.

## How It Works 🔍

This lesson covers the following key topics:

1. **functools module**: I’ll get familiar with the `functools` module, which offers various tools to work with functions, such as partial applications and decorators.
2. **partial() function**: Learn how to create partial functions by fixing some function arguments and leaving others to be filled in later.
3. **update_wrapper() function**: This function is used to update metadata for wrapped functions.
4. **wraps decorator**: A decorator that simplifies the process of copying over function attributes (like docstrings and names) to the decorated function.
5. **Caching and memoization**: I will study techniques to speed up functions by storing and reusing previously computed results.
6. **lru_cache decorator**: This decorator helps cache the results of expensive function calls, keeping the most recent ones in memory.
7. **cache decorator**: A simpler cache decorator that stores the results of function calls to avoid recalculating.

This lesson includes 3 practical tasks that help demonstrate these concepts:

1.  **9_9_1_send_email**

**Goal**: Implement email sending using **partial functions** from the `functools` module.

-   This task shows how I can fix certain parameters (like recipient name and email address) and allow others (like email text) to remain flexible. The result is reusable, customizable functions for email-sending tasks.

2.  **9_9_2_process_words**

**Goal**: Use `functools` to process an arbitrary number of words, arranging each word’s letters in **lexicographic (alphabetical)** order.

-   This task helps me understand how I can use functions like `sorted()` in combination with the power of `functools` for efficient word processing.

3.  **9_9_3_count_ways**

**Goal**: Calculate the number of distinct ways Dima can climb to the nth step, where he can only take 1, 3, or 4 steps at a time.

-   This task demonstrates how I can optimize a recursive function using **memoization** techniques like `lru_cache` to avoid redundant calculations and improve performance.

## Output 📜

After completing this lesson, I will:  
✅ Understand how to use **partial functions** to simplify and reuse code.  
✅ Be able to apply the `update_wrapper()` and `wraps` to preserve function metadata when working with decorators.  
✅ Have hands-on experience with **memoization** techniques using `lru_cache` and `cache` to optimize code.  
✅ Learn to use **functools** tools to improve function performance, readability, and reusability.

## Conclusion 🚀

The **functools** module is a powerful toolkit in Python that allows me to write more efficient, reusable, and maintainable code.
By mastering techniques like **partial functions**, **decorators**, and **memoization**, I can greatly improve the performance and flexibility of my functions.
This lesson not only enhances my understanding of functional programming concepts but also provides practical tools for optimizing real-world applications.
