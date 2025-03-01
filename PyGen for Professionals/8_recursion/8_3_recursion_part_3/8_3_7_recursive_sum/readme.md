# Recursive Sum Function 🔢

## Description 📝

The `recursive_sum()` function calculates the sum of two non-negative integers using recursion.
The function avoids using loops and limits arithmetic operations to only `+1` and `-1` operations.

## Purpose 🎯

The purpose of this function is:

-   To calculate the sum of two non-negative integers.
-   To demonstrate how recursion can be used to perform basic arithmetic operations without the use of loops or advanced arithmetic operations.

## How It Works 🔍

1. The function takes two arguments:
    - `a`: A non-negative integer.
    - `b`: A non-negative integer.
2. If `a == 0`, the function returns `b` (base case).
3. If `b == 0`, the function returns `a` (base case).
4. Otherwise, the function recursively decreases `a` by 1 and increases `b` by 1 until the base case is reached.

## Output 📜

For example:

```python
print(recursive_sum(5, 3))
```

The function computes:

\[
5 + 3 = 8
\]

**Output:**

```
8
```

## Usage 📦

1. Call the function `recursive_sum()` with:
    - Two non-negative integers (`a` and `b`).
2. Example:
    ```python
    result = recursive_sum(7, 2)  # Output: 9
    print(result)
    ```
3. The function returns the computed sum.

## Conclusion 🚀

The `recursive_sum()` function shows how basic arithmetic operations like addition can be done using recursion, all while adhering to constraints such as not using loops or advanced arithmetic operations like `+` or `-` in their typical form.
