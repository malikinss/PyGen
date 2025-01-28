# Sum of Smallest and Largest Digits in a Decimal Number

## Description 📝

This Python script calculates the sum of the smallest and largest digits in a given decimal number.
It uses Python's `Decimal` class to handle the input number and extracts all unique digits, including handling special cases for numbers between -1 and 1.
The program then computes the sum of the smallest and largest digits and prints the result.

## Purpose 🎯

The goal of this program is to demonstrate:

1. How to extract digits from a `Decimal` number.
2. How to handle edge cases, such as numbers between -1 and 1, ensuring the digit `0` is included.
3. How to find the smallest and largest digits in a set and compute their sum.

This exercise is useful for understanding the `Decimal` class, set operations, and basic arithmetic in Python.

## How It Works 🔍

1. **Input**: The program prompts the user to input a decimal number.
2. **Digit Extraction**: The `get_digits_set()` function extracts all unique digits from the number.
    - The number is converted to its tuple representation using `as_tuple()`.
    - The digits are extracted and stored in a set.
    - If the number is between -1 and 1, the digit `0` is explicitly added to the set.
3. **Sum Calculation**: The smallest and largest digits in the set are identified using `min()` and `max()`, and their sum is calculated.
4. **Output**: The program prints the sum of the smallest and largest digits.

## Output 📜

When the script is executed and the user inputs a decimal number, the output will be:

```
The sum of the smallest and largest digits is: <result>
```

For example, if the user inputs `123.456`, the output will be:

```
The sum of the smallest and largest digits is: 7
```

(Explanation: The smallest digit is `1`, and the largest is `6`. Their sum is `7`.)

## Usage 📦

1. Save the code to a file named `sum_digits_decimal.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
    ```bash
    python sum_digits_decimal.py
    ```
5. Enter a decimal number when prompted.
6. The program will calculate and print the sum of the smallest and largest digits in the number.

## Conclusion 🚀

This program is a practical example of working with the `Decimal` class and set operations in Python.
It reinforces concepts like digit extraction, handling edge cases, and basic arithmetic. Happy coding! 😊
