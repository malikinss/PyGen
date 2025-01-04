# Average Calculation for Nested Tuples 📊

## Description 📝

This program calculates the average of the numbers in each nested tuple in a tuple of tuples.
The function takes a tuple of tuples, computes the average for each nested tuple, and returns a list of averages.

## Purpose 🎯

-   To compute the average of the numbers in each nested tuple.
-   To show how to handle tuple of tuples and perform calculations on the inner elements.

## How It Works 🔍

1. **Function `calculate_averages(numbers: Tuple[Tuple[int, ...], ...])`**:
    - Takes a tuple of tuples as input, where each nested tuple contains integer values.
    - For each nested tuple, calculates the average by summing the elements and dividing by the length of the tuple.
    - Returns a list containing the average of each nested tuple.

### Example:

```
Input: (
    (10, 10, 10, 12),
    (30, 45, 56, 45),
    (81, 80, 39, 32),
    (1, 2, 3, 4),
    (90, 10)
)

Output: [10.5, 44.0, 57.0, 2.5, 50.0]
```

## Output 📜

The output will be:

```
[10.5, 44.0, 57.0, 2.5, 50.0]
```

## Conclusion 🚀

The code successfully computes the average of numbers in each nested tuple within the tuple of tuples and returns a list of the computed averages.
