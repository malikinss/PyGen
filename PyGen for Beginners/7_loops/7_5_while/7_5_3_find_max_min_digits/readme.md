# Find Maximum and Minimum Digits

## Description 📝

This program takes a natural number `n` (where n ≥ 10) as input and determines its maximum and minimum digits.
It processes each digit of the number by extracting and comparing them to find the largest and smallest digits in the number.

## Purpose 🎯

The purpose of this program is to demonstrate how to extract and evaluate the digits of a natural number to find the maximum and minimum digits within the number.
This process is done using mathematical operations like modulo and integer division.

## How It Works 🔍

1. The program accepts a natural number `n` as input.
2. It initializes `max_digit` to 0 and `min_digit` to 9, as the possible digit range is from 0 to 9.
3. A while loop is used to extract each digit of the number by applying the modulo operation (`n % 10`) and integer division (`n //= 10`).
4. After extracting each digit, the program updates `max_digit` and `min_digit` accordingly.
5. The loop continues until all digits are processed.
6. Finally, it returns the maximum and minimum digits found.

### Example

```bash
Input: 2857
Output: Maximum digit is 8 Minimum digit is 2

```

In this example:

-   The program takes the number 2857 and determines that the maximum digit is 8 and the minimum digit is 2.

## Output 📜

The program outputs the maximum and minimum digits from the given number.

## Usage 📦

1. Run the script in a Python environment.
2. Enter a natural number `n ≥ 10`.
3. The program will output the maximum and minimum digits of the number.

## Conclusion 🚀

This program demonstrates how to work with the digits of a number in Python, efficiently extracting and comparing them to determine the maximum and minimum digits.
