# Lesson 7.2: Exception Handling Part 2 ⚠️

## Description 📝

This lesson continues the topic of **exception handling**, introducing the **try-except** construct and basic exception types.
You'll learn how to write error-resilient programs that can handle unexpected input gracefully.

## Purpose 🎯

The lesson will teach you how to:

-   Use the **try-except** construct to catch and handle exceptions.
-   Identify and manage **basic exception types**, such as `KeyError`, `IndexError`, and `ZeroDivisionError`.
-   Write programs that **continue running smoothly** even when errors occur.

## Study Material 🔍

1. **Exception Handling** 🚨

    - Understanding why exceptions occur and how to manage them effectively.
    - Using `try-except` blocks to **catch and handle exceptions** without breaking program execution.

2. **Basic Exception Types** 📝

    - `KeyError`: Handling missing dictionary keys.
    - `IndexError`: Avoiding crashes when accessing invalid list indices.
    - `ZeroDivisionError`: Preventing division errors.

3. **Practical Tasks** 💻
    - The lesson includes **4 hands-on tasks** where you'll apply exception handling techniques.

## Tasks and Code Snippets 🔍

1. **7_2_1_count_likes** - Calculate Total Likes with Error Handling 📝  
   The program calculates the total sum of the `'Likes'` values from a list of dictionaries. If a dictionary lacks the `'Likes'` key, the value is treated as `-1`.

    **Goal:** Implement a `try-except` block to handle missing keys and ensure the program doesn’t crash when encountering incomplete data.

2. **7_2_2_add_letter** - Extracting Fifth Letters with Error Handling 📝  
   The function extracts the **fifth letter** from each word in the `food` list. If a word has fewer than five letters, `_` is added instead.

    **Goal:** Use a `try-except` block to prevent `IndexError` when accessing out-of-range indices.

3. **7_2_3_ignore_zero** - Handling Division by Zero in Remainder Calculation 📝  
   The function computes the remainder when `36` is divided by each number in the `numbers` list. If a number is `0`, it is skipped to prevent a `ZeroDivisionError`.

    **Goal:** Ensure that division by zero does not crash the program by implementing exception handling.

4. **7_2_4_print_sum_and_non_numeric_count** - Summing Numeric Inputs and Counting Non-Numeric Values 📝  
   The program reads multiple lines of input, separates numeric values from non-numeric values, computes the sum of all numbers, and counts non-numeric inputs.

    **Goal:** Use `try-except` to distinguish between valid numbers and invalid input while maintaining correct calculations.

## Conclusion 🚀

By the end of this lesson, you'll have a solid grasp of **exception handling** and how to use **try-except** blocks to make your programs more **robust and error-tolerant**.
This is a crucial skill for writing **reliable** and **user-friendly** software.
