# Sum and Largest Numbers Calculator

## Description 📝

This Python script processes a string of space-separated decimal numbers.
It calculates the sum of all the numbers and identifies the five largest numbers in the list.
The results are displayed on two lines:

-   the first line shows the total sum
-   the second line lists the five largest numbers in descending order.

## Purpose 🎯

The goal of this program is to demonstrate:

1. How to parse a string of decimal numbers into a list of `Decimal` objects.
2. How to calculate the sum of all numbers in a list.
3. How to extract and sort the largest numbers from a list.

This exercise is useful for understanding string manipulation, list operations, sorting, and working with the `Decimal` class in Python.

## How It Works 🔍

1. **Input String**: The program starts with a string of decimal numbers separated by spaces.
2. **String to List Conversion**: The string is split into individual elements, which are then converted into a list of `Decimal` objects.
3. **Sum Calculation**: The `calculate_sum()` function computes the sum of all numbers in the list.
4. **Largest Numbers Extraction**: The `get_largest_numbers()` function sorts the list in descending order and extracts the top five numbers.
5. **Output**: The program prints the total sum on the first line and the five largest numbers on the second line.

## Output 📜

When the script is executed, it produces the following output:

```
Sum of all numbers: 111.25
Five largest numbers: 9.85 9.74 9.73 9.60 9.36
```

## Usage 📦

1. Save the code to a file named `sum_and_largest_numbers.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
    ```bash
    python sum_and_largest_numbers.py
    ```
5. The program will calculate and print the sum of all numbers and the five largest numbers in descending order.

## Conclusion 🚀

This program is a practical example of working with decimal numbers in Python, emphasizing precision, list operations, and sorting.
It reinforces concepts like string parsing, list manipulation, and arithmetic operations with the `Decimal` class.
