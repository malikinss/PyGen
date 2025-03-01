# Sum of Powers of Digits Program

## Description 📝

This Python script defines a function `sum_of_powers_of_digits()` that computes the sum of the digits of a number, where each digit is raised to the power of its position in the number.
It demonstrates the use of `enumerate()` and `sum()` for concise calculations.

## Purpose 🎯

The goal of this program is to practice working with digits of a number, iterating through them while keeping track of their positions, and applying exponentiation.
It reinforces concepts like string manipulation, enumeration, and list comprehensions in Python.

## How It Works 🔍

1. **TODO Comment**: Describes the function’s purpose—calculating the sum of digits raised to their ordinal powers.
2. **Input Validation**: Ensures the number is non-negative, raising a `ValueError` otherwise.
3. **Conversion to String**: The number is converted to a string for easy digit extraction.
4. **enumerate() Function**: Used to assign an ordinal position (starting from 1) to each digit.
5. **List Comprehension with sum()**: Computes the sum of each digit raised to its respective power.

## Output 📜

For an input of `139`, the function computes:

```
1^1 + 3^2 + 9^3 = 739
```

Expected output:

```
739
```

## Usage 📦

1. Save the code to a file named `sum_of_powers.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
    ```
    python sum_of_powers.py
    ```
5. The program will print the calculated sum for a given number.

## Conclusion 🚀

This program is an excellent example of leveraging Python’s built-in functions like `enumerate()` and `sum()` for elegant and efficient computations.
It strengthens understanding of number manipulation and list comprehensions.
