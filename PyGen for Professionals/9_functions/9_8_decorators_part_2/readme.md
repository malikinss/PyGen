# Lesson 9.8: Decorators (part 2) 📝

## Description 📝

In this lesson, I explore more advanced aspects of **decorators** in Python.
I will cover how to use the `functools.wraps` decorator to preserve the name and docstring of a decorated function, how to create general-purpose decorators, and various practical use cases.
These include decorators for measuring execution time, tracking function calls, modifying return values, and handling exceptions.
I will also learn how to create decorators that accept arguments, providing more flexibility for customizing function behavior.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Learn to use **`functools.wraps`** to preserve function metadata.  
✅ Understand how to create general-purpose decorators.  
✅ Create a decorator that measures function execution time.  
✅ Track the number of times a function is called using a decorator.  
✅ Implement a decorator that intentionally slows down a function’s execution.  
✅ Work with decorators that accept arguments for more control over function behavior.  
✅ Explore advanced decorators for handling exceptions and retrying failed executions.

## How It Works 🔍

This lesson covers the following advanced decorator topics:

1. **Preserving Function Metadata**: Using `functools.wraps` to maintain a decorated function’s original name, docstring, and other metadata.
2. **General-Purpose Decorators**: How to write decorators that can be used across different functions for tasks like timing execution, counting function calls, etc.
3. **Measuring Function Execution Time**: Creating a decorator that tracks how long a function takes to execute, which can be useful for performance profiling.
4. **Tracking Function Calls**: A decorator that counts how many times a function is called, providing insight into its usage.
5. **Slowing Down Function Execution**: A decorator that deliberately delays a function’s execution, useful for testing or simulating slow environments.
6. **Decorators with Arguments**: How to pass arguments to decorators to provide additional flexibility and customization.
7. **Exception Handling and Retrying**: Implementing decorators that catch exceptions and retry failed function executions a specified number of times.

The lesson includes 12 practical tasks to reinforce these concepts:

1.  **9_8_1_square**

**Goal**: Implement a `square` decorator that squares the return value of the function.

-   Use `functools.wraps` to preserve the original function's name and docstring.

2.  **9_8_2_returns_string**

**Goal**: Implement a `returns_string` decorator that ensures the function’s return value is always a string, raising an exception if it is not.

3.  **9_8_3_trace**

**Goal**: Create a `trace` decorator that prints the function’s name, arguments, and return value for debugging purposes.

4.  **9_8_4_prefix**

**Goal**: Implement a `prefix` decorator that adds a prefix to the return value of the function.

5.  **9_8_5_make_html**

**Goal**: Write a `make_html()` decorator that wraps the return value of a function in an HTML tag.

6.  **9_8_6_repeat**

**Goal**: Create a `repeat()` decorator that repeats the function’s execution a specified number of times.

7.  **9_8_7_strip_range**

**Goal**: Implement a `strip_range()` decorator that replaces a specific range of characters in the return string with a specified character.

8.  **9_8_8_returns**

**Goal**: Create a `returns()` decorator that checks the function’s return type, raising a `TypeError` if the type does not match the expected one.

9.  **9_8_9_takes**

**Goal**: Write a `takes()` decorator that ensures the function’s arguments are of the correct types, raising a `TypeError` for invalid argument types.

10. **9_8_10_add_attrs**

**Goal**: Implement an `add_attrs` decorator that adds arbitrary named attributes to the function.

11. **9_8_11_ignore_exception**

**Goal**: Create an `ignore_exception` decorator that handles specific exceptions and continues function execution without interruption.

12. **9_8_12_retry**

**Goal**: Write a `retry` decorator that retries the function execution up to a specified number of times if an exception occurs.

## Output 📜

After completing this lesson, I will:  
✅ Be proficient in creating general-purpose decorators that handle a wide range of scenarios, including performance tracking, type checking, and retry logic.  
✅ Understand how to use `functools.wraps` to preserve the metadata of the decorated functions.  
✅ Be able to create custom decorators with arguments for more flexible behavior.  
✅ Gain experience in advanced decorator use cases such as exception handling and timing function execution.

## Conclusion 🚀

This lesson provides an in-depth exploration of decorators and how they can be used to enhance function behavior in Python.
By mastering these concepts, I will be able to write more flexible, maintainable, and powerful code that can be reused across multiple projects.
Decorators are a key tool in Python that allow me to keep my code clean while adding useful functionality such as logging, performance monitoring, and error handling.
