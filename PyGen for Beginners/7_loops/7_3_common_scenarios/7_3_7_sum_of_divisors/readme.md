# Sum of Divisors

## Description 📝

This program calculates the sum of all divisors of a given natural number `n`.
The program efficiently computes the sum of divisors by iterating up to the square root of `n` and considering both divisors in each pair.
This is useful for finding divisors in a time-efficient manner.

## Purpose 🎯

The purpose of this program is to compute the sum of divisors for any natural number `n`.
This is a common operation in number theory, often used for understanding the properties of numbers and their factorization.

## How It Works 🔍

1. The user enters a natural number `n`.
2. The program iterates from 1 to the square root of `n` to find divisors.
3. For each divisor `i`, both `i` and `n // i` are added to the sum of divisors.
4. The program avoids adding the square root twice if `n` is a perfect square.
5. The final result is printed.

## Output 📜

-   The program outputs the sum of all divisors of the given number `n`.

For example:

```bash
Input: 12

Output: 28
```

Explanation: The divisors of 12 are 1, 2, 3, 4, 6, and 12, and their sum is 28.

## Usage 📦

1. Run the script in a Python environment.
2. Enter a natural number when prompted.
3. The program will calculate and print the sum of divisors of the number.

## Conclusion 🚀

This program efficiently calculates the sum of divisors of a natural number by leveraging the square root method.
It is an optimized approach for finding divisors and summing them, which can be useful in mathematical applications.
