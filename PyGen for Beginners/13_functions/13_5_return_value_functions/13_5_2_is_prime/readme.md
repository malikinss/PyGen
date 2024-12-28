# Prime Number Check Program 🔢

## Description 📝

This Python program checks whether a given number is prime. A prime number is a natural number greater than 1 that is divisible only by 1 and itself.

## Purpose 🎯

-   To determine if a given number is prime.
-   This function can be used in mathematical applications where identifying prime numbers is needed.

## How It Works 🔍

1. **Function `is_prime(num)`**:

    - The function checks if the number `num` has exactly two divisors: 1 and itself.
    - If it does, the number is prime, and the function returns `True`.
    - If it has more than two divisors, the function returns `False`.

2. **Example**:
   For the input `num = 5`, the output will be `True`, since 5 is a prime number.
   For the input `num = 10`, the output will be `False`, since 10 has more than two divisors (1, 2, 5, 10).

## Usage 📦

1. Copy the code into a Python file, e.g., `prime_check.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python prime_check.py
    ```
5. Input a natural number when prompted. The program will then check if it is prime and print the result.

## Conclusion 🚀

The function provides a simple and efficient way to check for primality of a given number, making it useful in mathematical and algorithmic contexts.
