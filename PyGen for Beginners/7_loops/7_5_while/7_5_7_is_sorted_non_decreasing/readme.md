# Non-Decreasing Digit Sequence Checker

## Description 📝

This program checks whether the sequence of digits in a given natural number, when viewed from right to left, is sorted in non-decreasing order.
The program outputs "YES" if the digits form a non-decreasing sequence when reversed, and "NO" otherwise.

## Purpose 🎯

The purpose of this program is to determine if the digits of a given natural number are sorted in non-decreasing order when read from right to left. It demonstrates the use of modulus and division operations to extract and compare digits of a number.

## How It Works 🔍

1. The program accepts a natural number `n` as input.
2. It starts by extracting the last digit of the number.
3. Then, it iterates through the number from right to left, comparing each digit to the one before it.
4. If any digit is greater than the digit to its right, it returns "NO".
5. If all digits are in non-decreasing order, it returns "YES".

### Example

```bash
Input: 1234
Output: YES

```

In this example:

-   The digits in `1234` are in non-decreasing order when viewed from right to left, so the output is `YES`.

```bash
Input: 4321
Output: NO

```

In this case:

-   The digits in `4321` are not in non-decreasing order when viewed from right to left, so the output is `NO`.

## Output 📜

The program outputs "YES" if the digits, when viewed from right to left, are sorted in non-decreasing order. Otherwise, it outputs "NO".

## Usage 📦

1. Run the script in a Python environment.
2. Enter a natural number `n`.
3. The program will output "YES" or "NO" based on whether the digits are sorted in non-decreasing order when viewed from right to left.

## Conclusion 🚀

This program demonstrates how to check if a number's digits, when read from right to left, form a non-decreasing sequence.
It is useful for analyzing number properties and practicing basic number manipulation techniques.
