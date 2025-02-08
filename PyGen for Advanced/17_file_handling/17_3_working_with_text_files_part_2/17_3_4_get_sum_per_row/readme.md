# Program to Calculate Sum of Numbers in Each Row 📊🔢

## Description 📝

This program reads a file **"numbers.txt"**, where each line contains one or more integers separated by spaces. It calculates the sum of the numbers in each row and displays the results.

## Purpose 🎯

To compute and display the sum of numbers in each row of a file, handling multiple numbers per row.

## How It Works 🔍

1. **Reading File (`get_data_from_file`)**:

    - The file **"numbers.txt"** is opened and each line is read into a list.
    - Each line is stripped of trailing newline characters to ensure proper formatting.

2. **Calculating Sum per Row (`get_sum_per_row`)**:

    - For each row in the list:
        - The row is split into individual numbers using `split()`, which automatically handles multiple spaces.
        - Each number is converted into an integer using `map(int, ...)`, and the sum of these integers is calculated using `sum()`.
    - A list of sums is created, each corresponding to a row.

3. **Outputting Results**:
    - The sum of the numbers in each row is printed, one sum per line using `print(*data, sep='\n')` for easy formatting.

## Example Usage:

**File (`numbers.txt`):**

```
1 2 3
4 5 6
7 8 9 10
```

**Program Output:**

```python
>>> 6
>>> 15
>>> 34
```

## Conclusion 🚀

This program efficiently computes the sum of integers in each row of a file. It handles rows with multiple numbers and spaces, ensuring correct results in all cases.
