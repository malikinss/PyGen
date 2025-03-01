# Lesson 9.2: Built-in Functions part 2 🔧

## Description 📝

This lesson focuses on **useful built-in functions** in Python, specifically functions like `callable()`, `hasattr()`, `help()`, `repr()`, `hash()`, `eval()`, and `exec()`.
These functions are key tools for checking attributes, evaluating expressions, debugging, and interacting with Python objects and the runtime environment.

## Purpose 🎯

By the end of this lesson, I will:

-   Understand how to use **`callable()`** and **`hasattr()`** to interact with functions and objects.
-   Learn how to utilize **`help()`** and **`repr()`** for debugging and providing better object representations.
-   Be able to apply **`hash()`** to manage hashable objects in data structures.
-   Use **`eval()`** and **`exec()`** to dynamically evaluate expressions and execute Python code.

## How It Works 🔍

This lesson covers the following functions:

1. **`callable()`**: Checks if an object appears callable (i.e., can be used as a function).
2. **`hasattr()`**: Checks if an object has a specific attribute.
3. **`help()`**: Provides documentation for any Python object, useful for learning and debugging.
4. **`repr()`**: Returns a string that represents an object and can ideally be used to recreate the object.
5. **`hash()`**: Returns a hash value for an object, essential for using objects as dictionary keys.
6. **`eval()`**: Evaluates a string expression as Python code.
7. **`exec()`**: Executes dynamically created Python code, useful for more complex, runtime code generation.

This lesson includes 4 programming tasks:

## 1. 9_2_1_hash_as_key

**Goal**: Demonstrate how to use hash values as dictionary keys to store objects or group objects with the same hash value.

-   This task highlights the use of **`hash()`** to handle hashable objects in Python.

## 2. 9_2_2_process_input

**Goal**: Process a string representation of a list, tuple, or set and perform different operations based on the type of input.

-   Demonstrates the use of **`eval()`** to convert a string into its corresponding Python object and perform type-specific operations.

## 3. 9_2_3_find_max_expression_result

**Goal**: Read multiple mathematical expressions from the user, evaluate them using **`eval()`**, and output the largest result.

-   This task showcases the power of **`eval()`** to evaluate dynamic Python expressions.

## 4. 9_2_4_find_and_print_min_max_values

**Goal**: Find the minimum and maximum values of a mathematical function over a user-defined segment [a, b].

-   It uses Python’s built-in capabilities for mathematical evaluations and ensures correct evaluations of a function over a range of integer values.

## Output 📜

After completing this lesson, I will be able to:  
✅ Use **`callable()`**, **`hasattr()`**, **`repr()`**, and **`help()`** for effective debugging and introspection.  
✅ Use **`hash()`** to handle hashable objects in collections.  
✅ Apply **`eval()`** and **`exec()`** to evaluate and execute dynamic expressions and code.

## Conclusion 🚀

Mastering these built-in functions will greatly enhance my ability to handle Python objects dynamically, perform runtime evaluations, and simplify complex tasks like debugging and managing collections.
Understanding how to use these functions correctly can significantly improve the flexibility and functionality of my Python code.
