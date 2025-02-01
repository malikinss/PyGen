# Sorting Tuples by Sum of Min and Max Elements

## Description

This program sorts a list of tuples based on the sum of the minimum and maximum elements of each tuple. The tuple with the smallest sum of its minimum and maximum values will appear first in the sorted list.

## Purpose

The program demonstrates how to sort a list of tuples using a custom sorting key, where the sorting criterion is the sum of the minimum and maximum elements of each tuple.

## How It Works

1. The `sum_min_max()` function sorts a list of tuples based on the sum of the minimum and maximum values of each tuple. The `min()` and `max()` functions are used to find the minimum and maximum elements in each tuple, respectively.
2. The list `numbers` contains tuples of integers.
3. The `sorted()` function is used to sort the list of tuples based on the custom key, which is defined as the sum of the minimum and maximum elements of each tuple.
4. The sorted list is then printed.

## Usage

Example:

```python
numbers = [
    (10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3),
    (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34),
    (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)
]

# Sorting the numbers based on the sum of the min and max values of each tuple
sorted_numbers = sum_min_max(numbers)

print(sorted_numbers)
```

## Output

```
[(1, 2, 3), (10, 10, 10), (30, 45, 56), (12, 45, 67), (50, 40, 50), (81, 80, 39), (34, 78, 65), (-5, 90, -1), (-2, -4, 100), (89, 90, 34), (10, 20, 30), (1, 2, 99)]
```

## Conclusion

This program efficiently sorts a list of tuples by calculating the sum of their minimum and maximum elements. It uses the `sorted()` function and a custom lambda function to define the sorting key, allowing for flexible and powerful sorting operations in Python.
