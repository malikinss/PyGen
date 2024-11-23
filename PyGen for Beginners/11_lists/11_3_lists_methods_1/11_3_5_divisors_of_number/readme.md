# Divisors of a Number 📝

## Description 📝

This Python program takes a natural number `n` as input and returns a list of divisors of that number. A divisor is any number that divides `n` without leaving a remainder.

## Purpose 🎯

The program demonstrates how to find all divisors of a given number by using a list comprehension in Python to check for divisibility.

## How It Works 🔍

1. The function `divisors_of_number()` takes a single integer `n` as input.
2. It uses a list comprehension to generate a list of all integers from `1` to `n` that divide `n` evenly (i.e., where `n % i == 0`).
3. The function returns a list containing all divisors of `n`.

## Output 📜

```bash
Example Input:
12
Example Output:
[1, 2, 3, 4, 6, 12]
```

## Usage 📦

1. Save the script as `divisors_of_number.py`.
2. Run the script in a Python environment.
3. Input a natural number n.
4. The program will output a list of divisors of the given number.

## Conclusion 🚀

This program illustrates how to find all divisors of a number, showcasing the use of list comprehension for filtering based on a condition.
