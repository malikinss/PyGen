# Rounding Numbers to 2 Decimal Places Using `map()`

## Description

This program rounds all elements of a list of numbers to 2 decimal places using the `map()` function and prints each result on a separate line.

## Purpose

The program rounds a list of floating-point numbers to 2 decimal places and outputs each rounded number on a new line.

## How It Works

1. The `round_numbers()` function applies the `map()` function to round each number in the list using the `round_until_to_decimal_simbols()` helper function.
2. The helper function `round_until_to_decimal_simbols()` rounds a single number to 2 decimal places using Python's built-in `round()` function.
3. The results are printed, each number on a separate line.

## Usage

```python
numbers = [
    3.56773, 5.57668, 4.00914,
    56.24241, 9.01344, 32.12013,
    23.22222, 90.09873, 45.45,
    314.1528, 2.71828, 1.41546
]

rounded_numbers = round_numbers(numbers)
print(*rounded_numbers, sep='\n')
```

## Output

For the example list of numbers:

```
3.57
5.58
4.01
56.24
9.01
32.12
23.22
90.1
45.45
314.15
2.72
1.42
```

## Conclusion

This program efficiently rounds numbers to 2 decimal places using the `map()` function, and the results are printed in a clear and readable format.
