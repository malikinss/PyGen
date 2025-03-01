# Recursive Power Function 🔢

## Description 📝

The `get_pow()` function computes the power of a number using recursion, following the recurrence relation:

\[
a^n = a \times a^{(n-1)}
\]

## Purpose 🎯

This function is designed to:

-   Demonstrate recursion in mathematical operations.
-   Compute exponents without using the `**` operator.
-   Reinforce the concept of breaking problems into smaller subproblems.

## How It Works 🔍

1. The function takes two arguments:
    - `a`: The base (a positive integer).
    - `n`: The exponent (a non-negative integer).
2. If `n == 0`, the function returns `1` (base case).
3. Otherwise, it returns `a * get_pow(a, n - 1)`, recursively reducing `n` until it reaches `0`.

## Output 📜

For example:

```python
print(get_pow(5, 2))
```

The function computes:

\[
5^2 = 5 \times 5^1 = 5 \times (5 \times 5^0) = 5 \times (5 \times 1) = 25
\]

**Output:**

```
25
```

## Usage 📦

1. Call the function `get_pow()` with:
    - A base (`a`).
    - An exponent (`n`).
2. Example:
    ```python
    result = get_pow(3, 4)  # Output: 3 * 3 * 3 * 3 = 81
    print(result)
    ```
3. The function returns the computed power.

## Conclusion 🚀

The `get_pow()` function efficiently calculates exponents using recursion, reinforcing fundamental recursion concepts and eliminating the need for built-in exponentiation operators.
