# get_avg() and min-max Arithmetic Mean Program

## Description

The program contains a function `get_avg()` that calculates the arithmetic mean of a tuple, and then uses the built-in `min()` and `max()` functions to find and print the tuples with the minimum and maximum arithmetic means from a list of tuples.

## Purpose

The program demonstrates how to use the `min()` and `max()` functions with the `key` argument to find the tuples with the smallest and largest average values in a list of numeric tuples.

## How It Works

1. The `get_avg()` function calculates the arithmetic mean of the numbers in a tuple by summing the elements and dividing by the number of elements.
2. The `min()` function is used to find the tuple with the smallest mean.
3. The `max()` function is used to find the tuple with the largest mean.
4. Both results are printed on separate lines.

## Usage

Example:

```python
numbers = [
    (10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100),
    (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65),
    (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)
]

# Prints the tuple with the minimum arithmetic mean
print(min(numbers, key=get_avg))

# Prints the tuple with the maximum arithmetic mean
print(max(numbers, key=get_avg))
```

## Output

```
(10, 10, 10)  # Tuple with the minimum mean
(1, 2, 3, 4, 5, 6)  # Tuple with the maximum mean
```

## Conclusion

This program effectively identifies and prints the tuples with the minimum and maximum arithmetic means from a given list of numeric tuples, utilizing Python's built-in `min()` and `max()` functions with the `key` argument.
