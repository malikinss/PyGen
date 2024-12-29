# Divisibility Checker Program 🔢

## Description 📝

This program defines a function that checks whether one natural number is evenly divisible by another.
If the first number is divisible by the second, it prints "divided"; otherwise, it prints "not divided".

## Purpose 🎯

The purpose of this program is to determine if one number (num1) is divisible by another number (num2) without a remainder.

## How It Works 🔍

1. **Input Format**:
    - The program takes two natural numbers as input: `num1` and `num2`.
2. **Processing**:

    - The function `is_divisible` checks if `num1` is divisible by `num2` using the modulus operator (`%`).
      If the remainder of `num1 % num2` is zero, it returns `True`; otherwise, it returns `False`.

3. **Example**:

    - **Input**:
        ```
        10
        2
        ```
    - **Output**:
        ```
        divided
        ```
    - **Input**:
        ```
        10
        3
        ```
    - **Output**:
        ```
        not divided
        ```

4. **Edge Cases**:
    - If `num2` is 1, the result will always be "divided" because any number is divisible by 1.
    - If `num1` is smaller than `num2`, the result will typically be "not divided", unless `num1` is zero.

## Usage 📦

1. Copy the code into a Python file, e.g., `divisibility_checker.py`.
2. Run the script in the terminal:
    ```bash
    python divisibility_checker.py
    ```
3. Enter the two numbers when prompted.
4. The program will print either "divided" or "not divided" based on the divisibility check.

## Conclusion 🚀

This simple program provides an easy way to check if one number is divisible by another and outputs the result in a clear format.
