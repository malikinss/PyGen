# Lesson 9.7: Decorators (part 1) 📝

## Description 📝

In this lesson, I delve into **decorators** in Python, a powerful and flexible tool for modifying the behavior of functions or methods.
A decorator is a function that takes another function as an argument, wraps it with additional functionality, and returns it.
I will explore various types of decorators, including those that add behavior before and after a function call, change the function’s arguments, and handle exceptions.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand the concept and syntax of **decorators** in Python.  
✅ Learn how to define and apply decorators to modify the behavior of functions.  
✅ Explore how to use multiple decorators on a single function.  
✅ Work with decorators that take arguments and return values.  
✅ Learn how to handle exceptions using decorators and validate input before function execution.

## How It Works 🔍

This lesson covers the following key topics:

1. **Defining a Decorator**: The basic structure of a decorator, how it accepts a function as an argument and returns a modified version of it.
2. **Special Syntax for Using Decorators**: The use of the `@decorator` syntax to apply decorators to functions.
3. **Changing Function Behavior**: Modifying a function’s behavior before and after its execution.
4. **Using Multiple Decorators**: Applying more than one decorator to a function and understanding the order of execution.
5. **Decorating Functions that Take Arguments**: Handling functions that accept parameters and modifying them using decorators.
6. **Returning Values from a Decorated Function**: Ensuring the decorated function returns appropriate values after modification.

The lesson includes 6 practical tasks that demonstrate the use of decorators:

1.  **9_7_1_sandwich**

**Goal**: Implement a `sandwich` decorator that adds "bread slices" before and after the decorated function.

-   This task teaches how to decorate functions and add behavior before and after their execution without altering their return value.

2.  **9_7_2_upper_print**

**Goal**: Create a `upper_print` decorator that modifies the behavior of the `print()` function to print all text in uppercase.

-   This task shows how to override built-in functions using decorators and modify their behavior while keeping the original function's signature.

3.  **9_7_3_do_twice**

**Goal**: Write a `do_twice` decorator that calls the decorated function twice.

-   This teaches how to repeat function calls without changing the function's return value or parameters.

4.  **9_7_4_reverse_args**

**Goal**: Define a `reverse_args` decorator that reverses the order of positional arguments passed to a function.

-   This task demonstrates how to modify the arguments of a function before passing them, allowing me to change the order of input.

5.  **9_7_5_exception_decorator**

**Goal**: Implement an `exception_decorator` that handles exceptions gracefully and returns a message indicating success or failure.

-   This teaches how to wrap functions with a decorator that handles errors and returns appropriate status messages.

6.  **9_7_6_takes_positive**

**Goal**: Create a `takes_positive` decorator that validates whether all arguments passed to a function are positive integers.

-   This task shows how to validate inputs before executing the function, ensuring only valid data is processed.

## Output 📜

After completing this lesson, I will:  
✅ Understand how decorators work and how to define them.  
✅ Be able to apply decorators to functions to modify their behavior, handle exceptions, and validate inputs.  
✅ Learn how to use multiple decorators and understand how they interact.  
✅ Have a deeper understanding of **function wrapping** and how decorators can enhance code readability and functionality.

## Conclusion 🚀

Decorators are a powerful feature in Python that allow me to modify the behavior of functions in a clean and reusable way.
This lesson provides a solid foundation in understanding decorators, from basic usage to handling more complex scenarios such as error handling and input validation.
By mastering decorators, I will be able to write more modular, maintainable, and flexible code.
