# Lesson 10.5: Generators (Part 1) 📝

## Description 📝

In this lesson, I explore **generator functions** in Python, which allow for lazy evaluation of sequences and memory-efficient handling of large data.
I will study the `yield` keyword, the creation of simple and recursive generator functions, and the advantages of using generators for various tasks, such as generating sequences, processing large datasets, and more.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand the basics of **generator functions**.  
✅ Learn how to use the `yield` keyword for creating generators.  
✅ Study the use cases and limitations of generators.  
✅ Be able to implement **recursive generators** and use **`yield from`** for simplification.  
✅ Practice solving problems with practical generator-based tasks.

## How It Works 🔍

This lesson covers:

1. **Generator Functions**: Functions that use `yield` to return values one at a time.
2. **The `yield` Keyword**: This keyword allows a function to return values lazily, enabling it to produce a sequence without storing it in memory entirely.
3. **Generator Functions with Side Actions**: Using generators for more complex operations and side effects during iteration.
4. **Features and Limitations**: Discussing how generators are memory-efficient and how they can only be iterated once.
5. **Examples of Using Generator Functions**: Implementing practical generators for different sequences and tasks.
6. **`yield from` Construction**: Simplifying nested generator code by delegating iteration to another iterator.
7. **Recursive Generator Functions**: How to use recursion with generators to generate sequences.

## Practical Tasks 🔧

The lesson includes 9 practical tasks that will help me understand and implement generator functions:

1.  **10_5_1_simple_sequence**  
    **Goal**: Create a generator that generates a sequence of natural numbers, where each number appears as many times as its value.  
    Example sequence: `1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, ...`

-   This generator demonstrates how to generate an **infinite sequence** with repetitive patterns.

2.  **10_5_2_alternating_sequence**  
    **Goal**: Create a generator that produces an alternating sequence of numbers where the sign of each number alternates between positive and negative.  
    Example sequence: `1, -2, 3, -4, 5, -6, 7, -8, 9, -10, ...`

-   This task is useful for generating **oscillating behaviors**.

3.  **10_5_3_primes**  
    **Goal**: Generate a sequence of **prime numbers** within a given range `[left, right]`.

-   This task helps with efficient **prime number generation** and can be used in various **mathematical problems**.

4.  **10_5_4_reverse**  
    **Goal**: Generate the elements of a given sequence (like a list, string, or tuple) in **reverse order**.

-   This task shows how to use generators for **efficient traversal** in reverse without modifying the original sequence.

5.  **10_5_5_dates**  
    **Goal**: Create a generator that produces a sequence of **consecutive dates** starting from a given start date.

-   This generator is useful for **time-based simulations**, **data processing**, or **scheduling tasks**.

6.  **10_5_6_card_deck**  
    **Goal**: Create a generator for a **deck of cards** excluding a specified suit.

-   This task simulates a **custom card game** and is useful for **card-related simulations**.

7.  **10_5_7_matrix_by_elem**  
    **Goal**: Refactor the `matrix_by_elem` function to use `yield from` for yielding elements of a matrix (list of lists).

-   This demonstrates how to simplify code and improve **readability** using **delegation** in generators.

8.  **10_5_8_palindromes**  
    **Goal**: Create a generator that produces an **infinite sequence of palindromic numbers**.

-   Palindromic numbers are those that read the same backward as forward (e.g., 121, 333, etc.). This is useful in **number theory** and **algorithmic problems**.

9.  **10_5_9_flatten**  
    **Goal**: Create a generator that **flattens a nested list** into a sequence of integers.

-   This is especially useful when working with **deeply nested data structures** and processing them as a **flat sequence**.

## Output 📜

By the end of this lesson, I will:  
✅ Be proficient in creating and using **generator functions** with `yield`.  
✅ Understand how to implement both **simple and recursive generators**.  
✅ Know how to use **`yield from`** for simplifying code.  
✅ Be able to implement generators for various tasks, such as **sequence generation**, **prime numbers**, **date iteration**, and **flattening nested data**.

## Conclusion 🚀

Generators provide an efficient and memory-friendly way to work with sequences in Python.
By using `yield` and understanding its capabilities, I can handle large datasets and generate infinite sequences without overwhelming memory.
Mastering generators is essential for working with data streams, lazy evaluation, and creating efficient algorithms in Python.
