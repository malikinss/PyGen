# Lesson 15.2: Functions with Variable Number of Arguments

## Description 📝

This lesson focuses on functions that accept a variable number of arguments.
It covers different types of arguments in Python, including:

-   **args**: Collects arbitrary positional arguments into a tuple.
-   **kwargs**: Collects arbitrary keyword arguments into a dictionary.
-   **Keyword-only arguments**: Parameters that must be specified by keyword when calling the function.

The lesson introduces several practical tasks that demonstrate the use of these argument types in various scenarios.

## Purpose 🎯

Learn how to create functions that can handle an arbitrary number of arguments by using the `*args` and `**kwargs` syntaxes.
These tools provide greater flexibility in defining functions, allowing them to accept varying numbers of inputs without requiring fixed parameters.

This lesson has 6 practical tasks and 8 theoretical questions available on the [Stepik website](https://stepik.org/lesson/503036/step/1?unit=494742).

### Practical Tasks

The practical tasks will help me implement functions with variable numbers of arguments.
Below are the descriptions of the functions I will create:

#### 15_2_1_count_args

The `count_args()` function accepts an arbitrary number of arguments and returns the count of those arguments.
This function is useful when you need to determine how many arguments were provided without requiring them to be passed as a list.

#### 15_2_2_sq_sum

The `sq_sum()` function takes an arbitrary number of numeric arguments and returns the sum of their squares.
This function computes the sum of squares of given numbers by utilizing Python's variable-length argument syntax.

#### 15_2_3_mean

The `mean()` function calculates the arithmetic mean (average) of an arbitrary number of numeric arguments (integers or floats) passed to it, while ignoring non-numeric arguments.
It computes the average of valid numeric inputs, providing a simple solution to calculating the mean of a list of numbers.

#### 15_2_4_greet

The `greet()` function generates a greeting message for one or more names.
It takes at least one mandatory name and can accept additional names, returning a personalized greeting for all.
This function creates a customized greeting message based on the names provided, accommodating an arbitrary number of names.

#### 15_2_5_print_products

The `print_products()` function prints a numbered list of valid product names provided as arguments.
It only considers non-empty strings as products and ignores other types of data.
This function helps in printing a list of product names, where each product is assigned a unique number.
If no valid products are provided, it prints a default message.

#### 15_2_6_info_kwargs

The `info_kwargs()` function takes an arbitrary number of named arguments and prints them in alphabetical order, with the format `<argument name>: <argument value>`.
This function organizes and displays the passed named arguments in ascending alphabetical order based on their names, which makes it easier to analyze or view them in a sorted manner.

## How It Works 🔍

-   **`*args`**: Used to pass a variable number of positional arguments to a function, collected as a tuple.
-   **`**kwargs`\*\*: Used to pass a variable number of keyword arguments to a function, collected as a dictionary.
-   **Keyword-only arguments**: These arguments must be passed by name in the function call (introduced with a `*` in the function signature).

## Conclusion 🚀

Functions with variable numbers of arguments provide great flexibility in Python.
By using `*args` and `**kwargs`, I can design functions that can handle an indefinite number of inputs, making them more versatile.
These tools allow for cleaner, more maintainable code when dealing with dynamic input sizes.
