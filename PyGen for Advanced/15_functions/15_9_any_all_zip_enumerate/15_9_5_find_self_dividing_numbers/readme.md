# Self-Dividing Numbers Finder 🔢

## Description 📝

This program identifies all integers in a specified range that are divisible by each of their non-zero digits.
Numbers containing zeros are ignored and not considered.
The program uses the built-in `all()` function to perform the checks.

## Purpose 🎯

The goal is to find and output all self-dividing numbers in a range [a, b].
A self-dividing number is one where each of its digits (that are non-zero) divides the number without leaving a remainder.

## How It Works 🔍

1. **Input**: Two natural numbers `a` and `b` are provided as input, marking the inclusive range [a, b].
2. **Check**: For each number in the range, we check if it is divisible by each of its non-zero digits using the helper function `is_self_dividing()`.
    - This function converts the number to a list of digits, excluding zero.
    - It then checks if the number is divisible by all non-zero digits using `all()`.
3. **Filter**: All numbers that pass the check are collected and returned as a list.
4. **Output**: The self-dividing numbers in the range are printed.

## Output 📜

-   The list of self-dividing numbers in the given range [a, b].

### Example Output:

```
12 24 36 48
```

## Usage 📦

1. Input two natural numbers representing the range [a, b].
2. The program will output all self-dividing numbers within this range that are divisible by each of their non-zero digits.

## Conclusion 🚀

This program efficiently identifies self-dividing numbers in a given range using Python's list comprehensions and built-in functions.
It filters out numbers with zeros and checks divisibility for all non-zero digits.
