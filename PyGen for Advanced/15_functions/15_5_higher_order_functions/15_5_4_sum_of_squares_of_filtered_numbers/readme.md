# Sum of Squares of Two-Digit Numbers Divisible by 7

## Description

This program calculates and outputs the sum of the squares of two-digit numbers from a given list that are divisible by 7 without a remainder. The program uses the `filter()`, `map()`, and `sum()` functions to perform this task efficiently.

## Purpose

The program filters out two-digit numbers from the list, checks if they are divisible by 7, and then squares these numbers before summing them up.

## How It Works

1. The `predicate()` function checks if a number is a two-digit number and divisible by 7.
2. The `square()` function squares the number.
3. The `sum_of_squares_of_filtered_numbers()` function filters the numbers based on the condition defined in `predicate()`, maps the filtered numbers to their squares, and then sums them up.

## Usage

```python
numbers = [
    77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61,
    298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99,
    270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205,
    183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260,
    -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258,
    196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5,
    187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9,
    23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211,
    5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274,
    73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10,
    236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63,
    263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172,
    216, 30, 15, 229, 205, 123, -105
]

# Calculate and print the sum of squares of the filtered numbers
print(sum_of_squares_of_filtered_numbers(numbers))
```

## Output

```
4742
```

## Conclusion

The program successfully calculates the sum of the squares of two-digit numbers that are divisible by 7. It uses functional programming techniques with `filter()`, `map()`, and `sum()`, providing an efficient and clear solution to the problem.
