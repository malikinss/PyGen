# Tribonacci Sequence Calculator 🚀

## Description 📝

This Python function calculates the n-th term of the Tribonacci sequence using recursion and memoization.
The Tribonacci sequence is a sequence of natural numbers where each subsequent number is the sum of the three previous ones.
The first few terms of the sequence are: 1, 1, 1, 3, 5, 9, 17, 31, 57, 105, ...

## Purpose 🎯

The purpose of this function is to compute any term in the Tribonacci sequence efficiently using recursion with memoization to reduce repeated calculations.

## How It Works 🔍

1. The function starts by checking if `n` is a valid natural number greater than 0.
2. A memoization dictionary (`memo`) is initialized with the first three terms of the sequence: `{1: 1, 2: 1, 3: 1}`.
3. The helper function `_tribonacci_recursive()` is called recursively to compute the Tribonacci numbers. If a number has already been computed, it is fetched from `memo` to avoid redundant calculations.
4. The n-th term of the Tribonacci sequence is returned.

## Output 📜

-   The output will be an integer representing the n-th term of the Tribonacci sequence.

## Usage 📦

1. Copy the code into your Python script.
2. Call the `tribonacci(n)` function, passing a positive integer `n` as an argument.
3. The function will return the n-th term of the Tribonacci sequence.

### Example Usage:

```python
print(tribonacci(1))  # Output: 1
print(tribonacci(7))  # Output: 17
print(tribonacci(4))  # Output: 3
```

## Conclusion 🚀

This implementation efficiently computes the n-th term of the Tribonacci sequence, leveraging recursion and memoization to ensure performance even for larger values of `n`.
