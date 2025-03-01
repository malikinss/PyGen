# Sum of Squares of Two-Digit Numbers Divisible by 9 Program

## Description 📝

This Python script calculates the sum of the squares of all two-digit numbers in a given list that are divisible by 9.
The program filters the list to find numbers that meet both criteria: being a two-digit number and divisible by 9 without a remainder.
The square of each valid number is then calculated and summed.

## Purpose 🎯

The goal of this program is to demonstrate how to filter and transform data using `map()` and `filter()` functions in Python.
It also emphasizes understanding conditional checks on numerical properties (like divisibility and range) and applying mathematical operations like squaring numbers.

## How It Works 🔍

1. **get_two_digit_numbers_divisible_by_9()**: Filters the list to include only two-digit numbers divisible by 9.
2. **sum_of_squares_of_filtered_numbers()**: Uses `filter()` to select numbers divisible by 9 and in the two-digit range, then `map()` to square them, and finally sums the results.
3. **map() and filter()**: The `filter()` function is used to narrow down the numbers, and `map()` applies a transformation (squaring) to each valid number.

## Output 📜

When the script is executed with the provided list, the output will be the sum of the squares of all two-digit numbers divisible by 9:

```
25674
```

## Usage 📦

1. Save the code to a file named `sum_of_squares_divisible_by_9.py`.
2. Create a list of integers, `numbers`, as shown in the code.
3. Open a terminal or command prompt.
4. Navigate to the directory where the file is located.
5. Execute the script using the command:
    ```
    python sum_of_squares_divisible_by_9.py
    ```
6. The program will output the sum of squares of the filtered numbers.

## Conclusion 🚀

This program showcases how to use `map()` and `filter()` to manipulate and process a list of numbers.
It highlights the power of functional programming techniques in Python for filtering and transforming data.
