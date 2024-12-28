# Arithmetic Operations Program ➕➖✖️➗

## Description 📝

This Python script performs a series of arithmetic operations on two integers provided by the user.
It calculates the sum, difference, product, quotient, integer division, remainder, and the square root of the sum of their 10th powers.

## Purpose 🎯

The program allows users to perform basic and advanced arithmetic operations, which can be useful for mathematical exercises, testing, or problem-solving.

## How It Works 🔍

1. **Input Format**:
    - The user inputs two integers `a` and `b`.
2. **Function Logic**:

    - The program calculates:
        1. Sum of `a` and `b`
        2. Difference between `a` and `b`
        3. Product of `a` and `b`
        4. Quotient of `a` divided by `b`
        5. Integer division of `a` by `b`
        6. Remainder of `a` divided by `b`
        7. Square root of the sum of `a^10` and `b^10`
    - The results are printed to the console line by line.

3. **Example**:

    ```
    Enter the first integer: 5
    Enter the second integer: 2
    Output:
    7
    3
    10
    2.5
    2
    1
    45.0
    ```

4. **Edge Cases**:
    - If `b` is `0`, division and modulo operations will raise a `ZeroDivisionError`.
    - Ensure the input integers are positive if calculating large powers to avoid overflow.

## Usage 📦

1. Copy the code into a Python file, e.g., `arithmetic_operations.py`.
2. Run the script in the terminal:
    ```bash
    python arithmetic_operations.py
    ```
3. Enter two integers when prompted.
4. The script will display the results of all calculations in sequence.

## Conclusion 🚀

This program provides a quick way to perform essential and advanced arithmetic operations on two numbers, making it a handy tool for mathematical analysis and learning exercises.
