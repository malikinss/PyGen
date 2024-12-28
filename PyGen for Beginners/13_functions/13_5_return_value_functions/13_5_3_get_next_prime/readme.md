# Next Prime Number Finder Program 🔢

## Description 📝

This Python program finds the next prime number greater than a given natural number.
It uses the `is_prime` function to check for prime numbers and then returns the first prime number that is greater than the input number.

## Purpose 🎯

-   To find the next prime number greater than a given number.
-   Useful in mathematical tasks, algorithms, or situations where you need to find consecutive prime numbers.

## How It Works 🔍

1. **Function `is_prime(num)`**:
    - This function checks if a number is prime by iterating through all possible divisors up to the square root of the number. If the number is divisible by any of these divisors, it is not prime.
2. **Function `get_next_prime(num)`**:
    - This function starts searching from the number greater than the input (`num + 1`), and keeps checking each number using `is_prime` until it finds a prime number.
3. **Example**:
    - For the input `num = 5`, the next prime number would be `7`.
    - For the input `num = 10`, the next prime number would be `11`.

## Usage 📦

1. Copy the code into a Python file, e.g., `next_prime.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python next_prime.py
    ```
5. Input a natural number when prompted. The program will then print the first prime number greater than the input number.

## Conclusion 🚀

This function allows you to easily find the next prime number after any given input, making it an essential tool for prime number generation or related calculations.
