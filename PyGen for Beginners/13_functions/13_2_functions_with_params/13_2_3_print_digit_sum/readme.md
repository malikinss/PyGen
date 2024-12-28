# Sum of Digits Calculator Program 🎨

## Description 📝

This Python program calculates and prints the sum of the digits of a given integer.
The program iterates through each digit of the number, adds it to a running total, and then outputs the sum.

## Purpose 🎯

-   To calculate and print the sum of the digits of a given number.
-   Useful for exercises that require digit manipulation in a number.

## How It Works 🔍

1. **Function `print_digit_sum(num)`**:

    - The function takes one input parameter: `num` (an integer).
    - It initializes a variable `digit_sum` to 0, which will store the cumulative sum of the digits.
    - The function uses a `while` loop to iterate through each digit of the number:
        - For each iteration, it adds the last digit (obtained with `num % 10`) to `digit_sum`.
        - The number is then reduced by removing the last digit using integer division (`num //= 10`).
    - The loop continues until all digits are processed (i.e., `num` becomes 0).
    - Finally, the function prints the calculated sum.

2. **Example**:
   For the input `num = 123`, the output will be `6` because `1 + 2 + 3 = 6`.

## Usage 📦

1. Copy the code into a Python file, e.g., `digit_sum.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python digit_sum.py
    ```
5. Input an integer, and the program will print the sum of its digits.

## Conclusion 🚀

This program provides a simple yet efficient way to calculate the sum of digits in a given number.
It can be extended or integrated into larger applications that require number manipulation or digit analysis.
