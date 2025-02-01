# sq_sum() Function

## Description

The `sq_sum()` function takes an arbitrary number of numeric arguments and returns the sum of their squares.

## Purpose

This function efficiently computes the sum of squares of given numbers by utilizing Python's variable-length argument syntax.

## How It Works

-   Accepts any number of numeric arguments (integers or floats) using `*args`.
-   Iterates over each argument, squares it, and accumulates the result.
-   Returns the total sum of the squared values.

## Usage

Example calls:

```python
print(sq_sum(1, 2, 3))        # Output: 14 (i.e., 1^2 + 2^2 + 3^2)
print(sq_sum(4.5, 3.2))         # Output: 4.5^2 + 3.2^2
```

## Conclusion

The `sq_sum()` function provides a concise and efficient way to calculate the sum of squares for a set of numbers.
