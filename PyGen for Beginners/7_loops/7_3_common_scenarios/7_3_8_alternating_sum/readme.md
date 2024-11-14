# Alternating Sum

## Description 📝

This program calculates the alternating sum of a sequence of natural numbers from 1 to `n`, where the sum alternates between addition and subtraction, starting with addition.
Specifically, the sum follows the pattern: `1 - 2 + 3 - 4 + 5 - 6 + ... + (-1)^(n+1) * n`.

## Purpose 🎯

The purpose of this program is to compute the alternating sum of numbers from 1 to a given natural number `n`.
This type of sum is often used in mathematical sequences and series.

## How It Works 🔍

1. The user enters a natural number `n`.
2. The program iterates through the numbers from 1 to `n`.
3. For each number:
    - Odd-indexed numbers (1, 3, 5, etc.) are added to the sum.
    - Even-indexed numbers (2, 4, 6, etc.) are subtracted from the sum.
4. The final alternating sum is printed.

## Output 📜

-   The program outputs the alternating sum for the sequence from 1 to `n`.

For example:

```bash
Input: 5

Output: 3
```

Explanation: The alternating sum for 1 - 2 + 3 - 4 + 5 is 3.

## Usage 📦

1. Run the script in a Python environment.
2. Enter a natural number when prompted.
3. The program will calculate and print the alternating sum for the sequence from 1 to `n`.

## Conclusion 🚀

This program calculates the alternating sum for any natural number `n` using a simple loop and alternating addition and subtraction.
It's useful for understanding alternating series in mathematics.
