# Lesson 13.5: Functions with Return Values 🔄

## Description 📝

In this lesson, I will focus on creating functions that return values.
I will learn how to define functions that perform computations and then return results, whether they are numerical, logical, string-based, or other data types.
The lesson will also cover solving practical problems by writing functions that return specific outputs, such as checking for prime numbers, validating passwords, and converting strings.

## Purpose 🎯

-   **Return Value Functions**: Learn how to define functions that return values, including numeric, boolean, and string types.
-   **Practical Problem Solving**: Understand how return value functions can be used to solve real-world problems.
-   **Mathematical and Logical Applications**: Apply the use of return value functions in solving problems involving prime numbers, palindromes, and string manipulations.

## How It Works 🔍

This lesson introduces the concept of functions with return values, meaning that after performing operations within the function, it will return a value to the caller.
The tasks provided require using these return values in various logical and mathematical applications.
I will be solving problems like validating triangles, checking prime numbers, and manipulating strings based on specific rules.

## Tasks 📜

### 13_5_1 Valid Triangle Check

This Python program takes three natural numbers representing the sides of a triangle as input and determines if those sides can form a valid (non-degenerate) triangle.
It uses the triangle inequality theorem to verify the validity.

### 13_5_2 Prime Number Check

This Python program checks whether a given number is prime.
A prime number is a natural number greater than 1 that is divisible only by 1 and itself.

### 13_5_3 Next Prime Number Finder

This Python program finds the next prime number greater than a given natural number.
It calls the `is_prime` function to check for prime numbers and returns the first prime number greater than the input number.

### 13_5_4 Strong Password Validator

This Python program checks whether a password is strong based on these criteria:

-   At least 8 characters long.
-   Contains at least one uppercase letter.
-   Contains at least one lowercase letter.
-   Contains at least one digit.

### 13_5_5 One Character Difference Validator

This Python program checks if two given words differ by exactly one character and are of the same length.
It returns `True` if they meet the criterion; otherwise, it returns `False`.

### 13_5_6 Palindrome Checker

This Python program checks if the given text is a palindrome.
A palindrome is a word, phrase, or sequence that reads the same forward and backward, ignoring spaces and punctuation.

### 13_5_7 BEEGEEK Bank Password Validator

This program validates a BEEGEEK bank password. A valid password follows the format `a:b:c`, where:

-   `a` must be a palindrome.
-   `b` must be a prime number.
-   `c` must be an even number.

### 13_5_8 Correct Bracket Sequence Validator

This Python program checks whether a given string consisting of `(` and `)` forms a correct bracket sequence.
It returns `True` if the sequence is correct, i.e., it has balanced and properly nested brackets, and `False` otherwise.

### 13_5_9 Camel Case to Snake Case Converter

This Python program converts a string written in camel case notation to snake case.
In camel case, each new word starts with a capital letter, while in snake case, words are separated by underscores, and all letters are lowercase.

## Usage 📦

1. Clone the repository or download the files.
2. Navigate to the `13_5_return_value_functions` directory.
3. Run each script individually:
    ```bash
    python 13_5_1_is_valid_triangle.py
    python 13_5_2_is_prime.py
    python 13_5_3_get_next_prime.py
    python 13_5_4_is_password_good.py
    python 13_5_5_is_one_away.py
    python 13_5_6_is_palindrome.py
    python 13_5_7_is_valid_password.py
    python 13_5_8_is_correct_bracket.py
    python 13_5_9_convert_to_python_case.py
    ```
4. Provide the necessary input when prompted or modify the code to pass custom parameters.

## Conclusion 🚀

By the end of this lesson, I should be able to define functions that return values and use them to solve various practical problems.
Understanding the concept of return values is essential for building modular, reusable code that can process input and produce outputs.
Keep practicing by writing functions that return different types of data and solve more complex problems. 🚀✨
