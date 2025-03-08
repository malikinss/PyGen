# `primes` Generator

## Description 📝

The `primes` function is a generator that produces a sequence of prime numbers within a given range `[left, right]` (inclusive).
A prime number is a natural number greater than 1 that has no divisors other than 1 and itself.

## Purpose 🎯

This generator is designed to efficiently generate prime numbers within a specified range, making it useful for mathematical problems, prime factorization, or prime number-related algorithms without generating unnecessary numbers outside the specified range.

## How It Works 🔍

1. **`is_prime` Function**:

    - This function checks whether a given number is prime by testing divisibility from `2` to the square root of the number. If a divisor is found, the number is not prime.

2. **Prime Number Generation (`primes` Generator)**:
    - The generator iterates over all numbers in the specified range `[left, right]`, checking each number for primality using the `is_prime` function.
    - If the number is prime, it is yielded to the caller.
    - The iteration stops when all numbers in the range have been processed.

## Usage 📦

1. **Create the generator**:
    ```python
    gen = primes(10, 30)
    ```
2. **Retrieve values using `next()` or iterate with a loop**:
    ```python
    for prime in primes(10, 30):
        print(prime)
    ```

## Conclusion 🚀

The `primes` generator is an efficient way to generate prime numbers within a specified range.
It optimizes the primality test by checking only up to the square root of each number, and it allows for flexible and memory-efficient prime number generation through iteration.
