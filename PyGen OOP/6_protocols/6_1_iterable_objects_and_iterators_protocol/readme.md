# Lesson 6.1: Iterable Objects and Iterators Protocol 🔄

## Description 📝

This lesson covers:

-   Iterables and iterators in Python
-   Iterables protocol with the **`__iter__()`**8 magic method
-   Iterators protocol with the **`__next__()`** magic method
-   Practical implementation of custom iterables and iterators

This lesson includes a detailed theoretical explanation, 7 programming practical tasks, and 12 theoretical questions available on the Stepik platform.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand the difference between iterables and iterators  
✅ Implement custom iterables using **`__iter__()`**  
✅ Create iterators with **`__next__()`** for controlled element access  
✅ Apply iteration protocols to diverse scenarios like 3D points and random looping

## Concepts & Theory 🔍

### 🔹 Iterables

-   **Purpose**: Objects that can return an iterator, enabling looping (e.g., via `for` loops).
-   **When Used**: To define objects that can be iterated over, like lists or custom classes.

### 🔹 Iterators

-   **Purpose**: Objects that produce elements one at a time, tracking their state.
-   **When Used**: To control the sequence and logic of element generation.

### 🔹 **`__iter__()`** Magic Method

-   **Purpose**: Returns an iterator for an iterable object.
-   **When Used**: Invoked by `iter()` to initiate iteration.

### 🔹 **`__next__()`** Magic Method

-   **Purpose**: Returns the next element in an iterator or raises `StopIteration`.
-   **When Used**: Invoked by `next()` to fetch elements sequentially.

## Practical Task 🧪

### 1️⃣ **Custom Iterables and Iterators**

The lesson includes 7 practical tasks, each implementing iterable or iterator behavior:

1. **`Point` Class**: Represents a 3D point.

    - `__repr__`: `Point(x, y, z)`
    - Iterable: Yields `x`, `y`, `z`.

2. **`DevelopmentTeam` Class**: Manages junior/senior developers.

    - Iterable: Yields `(name, 'junior')` then `(name, 'senior')`.

3. **`AttrsIterator` Class**: Iterates over an object’s attributes.

    - Yields `(name, value)` tuples from `obj.__dict__`.

4. **`SkipIterator` Class**: Yields every `(n+1)`-th element.

    - Initialized with `iterable` and skip count `n`.

5. **`RandomLooper` Class**: Randomly yields elements from multiple iterables.

    - Shuffles elements across inputs.

6. **`Peekable` Class**: Iterator with lookahead.

    - `peek()` previews next element, supports default value.

7. **`LoopTracker` Class**: Tracks iteration statistics.
    - Properties: `accesses`, `empty_accesses`, `first`, `last`
    - Method: `is_empty()`.

💡 These tasks showcase creative ways to control iteration flow and state.

## Benefits ✅

-   **`__iter__()`** enables custom objects to act like built-in sequences.
-   **`__next__()`** provides fine-grained control over element generation.
-   Iterables and iterators simplify complex looping logic.
-   Custom iteration enhances flexibility in data processing.

## Output 📜

After completing this lesson, I now:  
✅ Create iterable objects and custom iterators  
✅ Implement iteration protocols for diverse use cases  
✅ Apply iteration to practical examples like attribute traversal and random looping

## Conclusion 🚀

Mastering iterables and iterators with **`__iter__()`** and **`__next__()`** unlocks powerful ways to handle sequences in Python.  
From 3D coordinates to random element shuffling, these tools make code more flexible, intuitive, and efficient for complex data tasks. 🧑‍💻✨
