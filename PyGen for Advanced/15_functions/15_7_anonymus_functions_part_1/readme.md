# Lesson 15.7: Anonymous Functions (Part 1)

## Description 📝

This lesson introduces **anonymous functions** (also known as lambda functions) in Python, which are functions that do not require a name.
They are typically used for short, throwaway operations, especially in functional programming.

### Topics covered:

-   **Defining Anonymous Functions**: Learn how to define lambda functions and how they differ from regular functions.
-   **Conditional Operator in the Body of an Anonymous Function**: Using conditional expressions within lambda functions.
-   **Passing Arguments to an Anonymous Function**: How to pass arguments to lambda functions.
-   **Limitations of Anonymous Functions**: Understanding the constraints and limitations of lambda functions.

The lesson consists of **2 practical tasks** and **13 theoretical questions** provided on the course website.

## Purpose 🎯

The goal of this lesson is to provide an understanding of when and how to use anonymous functions (lambdas) in Python.
By the end of the lesson, I should be able to:

-   Use lambda functions to simplify short operations.
-   Apply conditional logic within lambda functions.
-   Understand the limitations and appropriate use cases for lambda functions.

## Practical Tasks 🔍

1. **15_7_1_process_data**:

    - **Objective**: Process three lists of data to perform specific transformations.
    - **Operations**:
        - Square and round floating-point numbers.
        - Filter words to leave palindromes longer than 4 characters.
        - Calculate the product of integers in a list.
    - This task demonstrates the use of **map()**, **filter()**, and **reduce()** with lambda functions.

2. **15_7_2_process_cities**:
    - **Objective**: Process a list of cities to identify primary cities with populations over 10 million.
    - **Operations**:
        - Filter cities based on type and population.
        - Map and sort the cities.
        - Reduce the list into a formatted string.
    - This task showcases the application of **filter()**, **map()**, **sorted()**, and **reduce()** using lambda functions.

## Limitations of Anonymous Functions 🚧

While lambda functions are convenient for simple operations, they come with limitations:

-   **Single Expression**: Lambda functions can only contain one expression.
-   **No Statements**: You cannot use statements (such as loops or assignments) inside lambda functions.
-   **Readability**: Overuse of lambda functions can reduce code readability, especially for complex operations.

## Conclusion 🚀

Anonymous functions are a powerful feature in Python for writing concise and efficient code for one-off operations.
However, they should be used judiciously, as they can make code harder to understand if overused.
In this lesson, I have learned how to use `lambda` functions for basic data processing tasks, as well as the benefits and drawbacks of using them.
