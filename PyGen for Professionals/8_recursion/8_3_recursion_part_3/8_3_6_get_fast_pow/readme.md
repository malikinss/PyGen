# Fast Exponentiation Function ⚡

## Description 📝

The `get_fast_pow()` function computes the power of a number efficiently using fast exponentiation (also known as exponentiation by squaring).
It uses the following recurrence relations:

-   For even exponents: \(a^n = (a \times a)^{\frac{n}{2}}\)
-   For odd exponents: \(a^n = a \times a^{n-1}\)

This method drastically reduces the number of multiplications required to compute the power.

## Purpose 🎯

The purpose of this function is:

-   To perform exponentiation more efficiently than with repeated multiplications.
-   To demonstrate the use of the divide-and-conquer technique in recursion.
-   To compute exponents without using the `**` operator.

## How It Works 🔍

1. The function takes two arguments:
    - `a`: The base (a positive integer).
    - `n`: The exponent (a non-negative integer).
2. If `n == 0`, the function returns `1` (base case).
3. If `n` is even, it calculates the power by squaring the result of the half exponent: \((a^n) = (a \times a)^{\frac{n}{2}}\).
4. If `n` is odd, it reduces the exponent by 1 and then multiplies the base by the result: \(a^n = a \times a^{n-1}\).

## Output 📜

For example:

```python
print(get_fast_pow(5, 3))
```

The function computes:

\[
5^3 = 5 \times 5^2 = 5 \times (5 \times 5) = 125
\]

**Output:**

```
125
```

## Usage 📦

1. Call the function `get_fast_pow()` with:
    - A base (`a`).
    - An exponent (`n`).
2. Example:
    ```python
    result = get_fast_pow(2, 10)  # Output: 1024
    print(result)
    ```
3. The function returns the computed power.

## Conclusion 🚀

The `get_fast_pow()` function provides an efficient way to calculate exponents using fast exponentiation, reducing the number of multiplications and making the process much faster, especially for large exponents.
