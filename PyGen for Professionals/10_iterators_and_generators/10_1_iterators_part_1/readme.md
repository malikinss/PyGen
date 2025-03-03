# Lesson 10.1: Iterators (Part 1) 📝

## Description 📝

In this lesson, I explore **iterators** and **iterable objects** in Python.
I learn the difference between **iterables** (objects that can be looped over) and **iterators** (objects that produce values one at a time).
I also get familiar with built-in functions like `iter()` and `next()` and understand how they work under the hood to traverse sequences efficiently.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand what **iterable objects** are and how they differ from **iterators**.  
✅ Learn how to manually retrieve elements from an iterable using `iter()` and `next()`.  
✅ Be able to work with **collections and sequences** in an iterator-based approach.  
✅ Solve problems using iterators instead of direct indexing, enhancing my Python skills.

## How It Works 🔍

This lesson covers the following key topics:

1. **Iterable Objects**: These are objects that can be looped over using `for` loops (e.g., lists, tuples, strings, dictionaries).
2. **Collections and Sequences**: I will see how iterators can be applied to common Python collections.
3. **Iterators**: An iterator is an object that implements the `__iter__()` and `__next__()` methods, allowing me to traverse a sequence one element at a time.
4. **iter() function**: This function converts an iterable object into an iterator.
5. **next() function**: This function retrieves the next item from an iterator. If there are no more elements, it raises a `StopIteration` exception.

This lesson includes 2 practical tasks that demonstrate how to use iterators:

1.  **10_1_1_iter**

**Goal**: Retrieve the **N-th element** of a list using `iter()` and `next()`, without using direct indexing.

-   Instead of `numbers[3]`, I will iterate through the list step by step until I reach the desired element.
-   This task teaches me how to use iterators to access specific elements in an iterable.

2.  **10_1_2_print_last_element**

**Goal**: Retrieve and print the **last element** of a list using `iter()` and `next()` instead of direct indexing (`numbers[-1]`).

-   I will learn how to traverse an iterable object efficiently using iterator functions.
-   This task also emphasizes **handling edge cases**, such as an empty list, to prevent runtime errors.

## Output 📜

After completing this lesson, I will:  
✅ Understand how **iterators** work and how they differ from **iterables**.  
✅ Be able to use `iter()` and `next()` to retrieve specific elements from a sequence.  
✅ Solve problems using iterators instead of direct indexing.  
✅ Know how to handle **edge cases** when working with iterators, such as empty lists.

## Conclusion 🚀

Iterators are a fundamental concept in Python that enable me to traverse sequences efficiently. By mastering `iter()` and `next()`, I can work with iterable objects in a more flexible way, avoiding direct indexing when needed.
This knowledge is essential for working with **generators**, **lazy evaluation**, and **custom iterators** in future lessons.
