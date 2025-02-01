# Sorting Numbers by Sum of Digits and Value

## Description

This program sorts a list of natural numbers in non-decreasing order of the sum of their digits. If two numbers have the same sum of digits, they are then sorted by their value in non-decreasing order.

## Purpose

The program sorts a list of natural numbers by two criteria:

1. The sum of their digits.
2. If two numbers have the same sum of digits, the numbers are sorted by their numerical value.

## How It Works

1. The function `get_sum_of_digits()` calculates the sum of digits for each number and returns a tuple containing the sum of digits and the original number itself.
2. The `sort_numbers_by_digit_sum()` function sorts the list based on the sum of digits. If the sums are the same, it sorts by the value of the numbers.
3. The program uses the `sorted()` function with the custom key function `get_sum_of_digits()`.

## Usage

```python
numbers_as_string_list = input("Enter a string of natural numbers: ").split()
sorted_numbers = sort_numbers_by_digit_sum(numbers_as_string_list)
print(*sorted_numbers)
```

For example:

-   Input: `["12", "21", "11", "10"]`
-   Output: `["10", "11", "12", "21"]`, as:
    -   The sum of digits of `10` is `1`.
    -   The sum of digits of `11` is `2`.
    -   The sum of digits of `12` is `3`.
    -   The sum of digits of `21` is `3`.
    -   Since `12` and `21` have the same sum, they are sorted by their value.

## Output

Example:

```
Enter a string of natural numbers: 12 21 11 10
10 11 12 21
```

## Conclusion

This program effectively sorts numbers based on the sum of their digits and then by their value, making it a versatile sorting tool for various applications.
