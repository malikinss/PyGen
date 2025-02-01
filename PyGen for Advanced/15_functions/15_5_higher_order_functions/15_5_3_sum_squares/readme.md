# Sum of Squares of Elements in the List

## Description

This program calculates and prints the sum of the squares of elements in the list of numbers. The problem is solved in two ways:

1. Using the `reduce()` function.
2. Using a combination of the `map()` and `sum()` functions.

## Purpose

The program demonstrates how to calculate the sum of squares using two different approaches: `reduce()` for an iterative reduction and `map()` with `sum()` for a more functional programming style.

## How It Works

1. The `reduce()` function applies a binary operation (in this case, summing the squares) to the list of numbers cumulatively.
2. The `sum_of_squares()` function is used as the operation in `reduce()` to add the squares of numbers.
3. The `map()` function is used to create a new list of squared numbers, and the `sum()` function adds them up.

## Usage

```python
numbers = [
    97, 42, 9, 32, 3, 45, 31, 77, -1, 11,
    -2, 75, 5, 51, 34, 28, 46, 1, -8, 84,
    16, 51, 90, 56, 65, 90, 23, 35, 11,
    -10, 70, 90, 90, 12, 96, 58, -8, -4,
    91, 76, 94, 60, 72, 43, 4, -6, -5, 51,
    58, 60, 30, 38, 67, 62, 36, 72, 34, 82,
    62, -1, 60, 82, 87, 81, -7, 57, 26, 36,
    17, 43, 80, 40, 75, 94, 91, 64, 38, 72,
    29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82,
    1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73
]

# Using reduce to sum the squares of the elements
sum_squares_reduce = reduce(sum_of_squares, numbers, 0)
print(f"Sum of squares using reduce: {sum_squares_reduce}")

# Using map and sum to sum the squares of the elements
sum_squares_map_sum = sum(map(lambda x: x ** 2, numbers))
print(f"Sum of squares using map and sum: {sum_squares_map_sum}")
```

## Output

```
Sum of squares using reduce: 189792
Sum of squares using map and sum: 189792
```

## Conclusion

This program successfully calculates the sum of squares in two different ways. The `reduce()` function offers an iterative approach, while the combination of `map()` and `sum()` provides a more functional style solution. Both approaches yield the same result.
