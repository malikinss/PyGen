# Prime Number Checker

## Description 📝

This script defines the `is_prime()` function, which determines whether a given natural number is prime.
The implementation efficiently checks divisibility using a generator expression with the `all()` function.

## Purpose 🎯

The function aims to efficiently verify if a number is prime by reducing the number of division operations required.
It leverages mathematical properties to minimize iterations, checking only up to the square root of the number.

## How It Works 🔍

1. **Initial Check**: If the number is less than 2, it is not prime.
2. **Generator Expression**: Iterates through numbers from `2` to `√number` and checks if `number` is divisible by any of them.
3. **`all()` Function**: If all conditions (`number % i != 0`) hold true, the number is prime; otherwise, it is composite.

## Output 📜

Example usage:

```python
print(is_prime(7))   # True
print(is_prime(10))  # False
```

## Usage 📦

1. Save the code in a Python file, e.g., `is_prime.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the function:
    ```python
    from is_prime import is_prime
    print(is_prime(17))  # True
    print(is_prime(20))  # False
    ```
4. The function can be used in loops, list comprehensions, or filtering operations.

## Conclusion 🚀

This function provides an optimized approach to prime number checking using generator expressions.
It efficiently eliminates non-prime candidates while maintaining readability and performance. 🚀
