# Reverse Number Digits

## Description 📝

This program takes a natural number as input and reverses the order of its digits.
The program processes each digit by extracting the last digit and building the reversed number one digit at a time.

## Purpose 🎯

The program demonstrates how to manipulate the digits of a number by using mathematical operations like modulo and integer division to reverse the digits of the input number.

## How It Works 🔍

1. The program accepts a natural number `n` as input.
2. A while loop is used to extract the last digit of `n` using the modulo operation (`n % 10`).
3. The last digit is then added to a new number `reversed_num`, and the original number `n` is reduced by dividing it by 10 (`n //= 10`).
4. The process repeats until the original number becomes zero, effectively reversing the order of the digits.

### Example

```bash
Input: 12345
Output: 54321

```

In this example:

-   The program takes the number 12345 and reverses the order of its digits, printing the result as 54321.

## Output 📜

The program outputs the reversed number, with the digits in the opposite order.

## Usage 📦

1. Run the script in a Python environment.
2. Enter a natural number.
3. The program will output the reversed number.

## Conclusion 🚀

This program demonstrates basic number manipulation in Python, specifically reversing the digits of a given natural number using arithmetic operations.
