# Is Power Function 🧮

## Description 📝

The `is_power()` function determines if a given number is a power of 2 using recursion.
The function returns `True` if the number is a power of 2, and `False` otherwise.

## Purpose 🎯

The purpose of this function is:

-   To check if a given number is a power of 2.
-   To implement a recursive solution for determining if a number can be expressed as 2 raised to some integer power.

## How It Works 🔍

1. The function takes a single argument:
    - `number`: A natural number to be checked.
2. The function follows the steps:
    - If the number is less than or equal to 0, return `False` because negative numbers and 0 cannot be powers of 2.
    - If the number is 1, return `True` because 2^0 = 1, which is a power of 2.
    - If the number is divisible by 2, the function recursively checks if the result is a power of 2.
    - If the number is not divisible by 2, return `False` because the number is not a power of 2.

## Output 📜

For example:

```python
print(is_power(16))  # Output: True
print(is_power(18))  # Output: False
print(is_power(1))   # Output: True
print(is_power(0))   # Output: False
print(is_power(-8))  # Output: False
```

**Output:**

```
True
False
True
False
False
```

## Usage 📦

1. Call the function `is_power()` with:
    - A non-negative integer `number`.
2. Example:
    ```python
    result = is_power(32)  # Output: True (2^5 = 32)
    print(result)
    ```
3. The function returns `True` if the number is a power of 2 and `False` otherwise.

## Conclusion 🚀

The `is_power()` function offers a simple recursive way to check if a number is a power of 2, handling both positive and negative numbers, as well as edge cases like 0.
