# Sorting Numbers by Sum of Digits

## Description

This program sorts a list of numbers based on the sum of their digits in non-decreasing order. If two numbers have the same sum of digits, their relative positions in the original list are preserved.

## Purpose

The program allows sorting of numbers by the sum of their digits while maintaining the original order of numbers with the same sum of digits. This is useful in scenarios where the relative order needs to be preserved even when the sorting criterion is the sum of digits.

## How It Works

1. The function `get_sum_of_digits()` calculates the sum of digits of a given number (represented as a string).
2. The function `sort_numbers_by_digit_sum()` sorts the list of numbers based on the sum of their digits.
3. The program uses the `sorted()` function with a custom sorting key (`get_sum_of_digits()`) to ensure that the list is sorted correctly.

## Usage

```python
numbers_as_string_list = input("Enter the list of numbers: ").split()
sorted_numbers = sort_numbers_by_digit_sum(numbers_as_string_list)
print(*sorted_numbers)
```

For example:

-   If the user inputs `["12", "21", "11", "10"]`, the output will be `["10", "11", "12", "21"]`, as the sum of digits of `10` is `1`, the sum of `11` is `2`, the sum of `12` is `3`, and the sum of `21` is `3`.

## Output

Example:

```
Enter the list of numbers: 12 21 11 10
10 11 12 21
```

## Conclusion

This program demonstrates how to sort numbers by the sum of their digits while maintaining their relative order when the sums are equal. It provides an efficient way to organize numbers based on a custom criterion (sum of digits).
