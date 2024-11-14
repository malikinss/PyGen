# Same Digits Checker

## Description 📝

This program checks if a given natural number consists of the same digits.
It extracts each digit from the number and compares them to ensure they are identical.
If all digits are the same, the program outputs "YES", otherwise it outputs "NO".

## Purpose 🎯

The purpose of this program is to check whether all digits in a given natural number are the same.
This demonstrates the use of integer division and modulus operations to extract and compare digits in a number.

## How It Works 🔍

1. The program accepts a natural number `n` as input.
2. It retrieves the last digit of the number using the modulus operator (`n % 10`).
3. Then, it iterates through the number, extracting each digit and comparing it to the last digit.
4. If any digit differs from the last digit, it immediately returns "NO".
5. If all digits are the same, it returns "YES".

### Example

```bash
Input: 1111
Output: YES

```

In this example:

-   All digits in `1111` are the same, so the output is `YES`.

```bash
Input: 1234
Output: NO

```

In this case:

-   The digits in `1234` are different, so the output is `NO`.

## Output 📜

The program outputs "YES" if the number consists of the same digits, otherwise "NO".

## Usage 📦

1. Run the script in a Python environment.
2. Enter a natural number `n`.
3. The program will output "YES" or "NO" based on whether all digits are the same.

## Conclusion 🚀

This program demonstrates how to extract and compare digits in a natural number, offering a solution to check if all digits are identical.
