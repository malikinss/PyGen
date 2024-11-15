# Smallest Divisor Finder

## Description 📝

This program calculates the smallest divisor of a given number \( n > 1 \), other than 1.
It iteratively checks each integer starting from 2 to find the smallest number that divides \( n \) without a remainder.

## Purpose 🎯

To determine the smallest divisor of a number greater than 1, excluding 1.
This program demonstrates basic concepts of divisors and loops.

## How It Works 🔍

1. The program accepts an integer \( n > 1 \) as input.
2. It starts checking divisors from 2 upwards.
3. For each divisor, it checks if \( n \) modulo the divisor equals 0.
4. When it finds the smallest divisor, it breaks the loop and outputs it.

### Example

```bash
Input: 15
Output: 3

```

In this case:

-   The smallest divisor of 15, other than 1, is 3.

```bash
Input: 29
Output: 29

```

Here:

-   Since 29 is a prime number, the smallest divisor other than 1 is itself.

## Output 📜

The program outputs the smallest divisor of the given number \( n \) (excluding 1).

## Usage 📦

1. Run the script in a Python environment.
2. Enter a number greater than 1 when prompted.
3. The program will output the smallest divisor of the number other than 1.

### Example Usage

1. Run the script.
2. Input: `n = 42`.
3. Output: `2`.

## Conclusion 🚀

This program effectively determines the smallest divisor of a number \( n > 1 \), making it a simple yet powerful example of number theory and modular arithmetic in Python.
