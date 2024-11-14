# Print Digits in Reverse Order

## Description 📝

This program takes a natural number as input and prints each of its digits in reverse order, with each digit displayed on a new line.
The program continuously extracts the last digit of the number until there are no more digits left to print.

## Purpose 🎯

The program demonstrates how to extract and manipulate the digits of a number by using simple mathematical operations.
It helps to understand the process of number digit manipulation through division and modulo operations.

## How It Works 🔍

1. The program accepts a natural number `n` as input.
2. It uses a while loop to repeatedly extract the last digit of the number using modulo (`n % 10`).
3. The number is reduced by removing the last digit through integer division (`n // 10`).
4. The last digit is printed on a new line until the number becomes zero.

### Example

```bash
Input: 12345
Output: 5 4 3 2 1

```

In this example:

-   The program extracts and prints the digits of 12345 starting from the last digit (5), working its way backward to 1.

## Output 📜

The output consists of the digits of the given number printed in reverse order, one per line.

## Usage 📦

1. Run the script in a Python environment.
2. Enter a natural number.
3. The program will output each digit of the number in reverse order.

## Conclusion 🚀

This program is a simple demonstration of basic mathematical operations in Python to manipulate and reverse the order of digits of a given natural number.
