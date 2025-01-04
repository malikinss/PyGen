# Lesson 6.1: Tuples Introduction (tuple datatype) 🧑‍🏫

## Description 📝

This lesson is dedicated to the `tuple` data type in Python.
It explains the differences between lists, strings, and tuples, focusing on the unique characteristics of tuples.
A tuple is an immutable sequence type that can hold arbitrary data, unlike strings, which are sequences of Unicode characters.
In Python, tuples provide a way to work with collections of items that should not be modified after creation.

## Purpose 🎯

The goal of this lesson is to:

-   Understand what a tuple is and how it differs from other sequence types (such as lists and strings).
-   Learn about the immutability of tuples.
-   Understand common operations on tuples and their use cases.

## Key Topics 🔑

-   **Tuple Definition**: A tuple is a collection of ordered elements, similar to lists, but unlike lists, tuples are immutable (cannot be modified after creation).
-   **Tuple Syntax**: Tuples are defined using parentheses `()` with elements separated by commas.
    ```python
    my_tuple = (1, 2, 3)
    ```
-   **Immutability**: Once a tuple is created, its elements cannot be modified, added, or removed.
-   **Accessing Elements**: Elements of a tuple can be accessed using indexing, similar to lists.
    ```python
    print(my_tuple[1])  # Output: 2
    ```
-   **Nested Tuples**: Tuples can contain other tuples or complex data structures as elements.
    ```python
    nested_tuple = ((1, 2), (3, 4))
    ```
-   **Tuple Methods**: Although tuples are immutable, they provide some built-in methods, such as `.count()` and `.index()`, for querying the tuple.
    ```python
    my_tuple = (1, 2, 3, 2)
    print(my_tuple.count(2))  # Output: 2
    print(my_tuple.index(3))  # Output: 2
    ```

## How It Works 🔍

This lesson is theoretical and covers the concept of tuples in depth. The details are available in the following link:
[Tuple Lesson on Stepik](https://stepik.org/lesson/443989/step/1?unit=434153)

## Conclusion 🚀

By the end of this lesson, I will understand how tuples differ from lists and strings, and how to work with tuples in Python.
Tuples are a powerful tool when I need an immutable collection of items, ensuring data integrity and efficient storage.
