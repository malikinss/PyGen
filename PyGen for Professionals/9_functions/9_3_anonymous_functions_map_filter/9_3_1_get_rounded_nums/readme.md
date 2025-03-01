# Filter and Round Numbers Program

## Description 📝

This Python script processes a list of arbitrary objects and filters out only the integers and floats.
It then discards the fractional part of the float numbers and prints each number on a separate line.
The program demonstrates how to work with filtering and mapping data in Python.

## Purpose 🎯

The goal of this program is to filter a list to extract only the numbers (integers and floats) and round down the floats to their integer form.
The result is then printed with each number on a new line, preserving the original order.
This exercise helps with understanding filtering and type-checking in Python.

## How It Works 🔍

1. **filter_numbers()**: Filters out all non-integer and non-float objects from the list using the `filter()` function.
2. **get_rounded_nums()**: Processes the filtered numbers by converting floats to integers (removing the fractional part) using list comprehension.
3. **map() and filter()**: These functions are utilized to transform and filter the data in a clean, functional style.

## Output 📜

When the script is executed, it will output the list of numbers with their fractional parts discarded, each on a separate line:

```
-16
-202
883
-765
-105
976
458
479
-87
-71
112
-621
-715
-974
882
-894
323
-224
431
170
-343
104
-353
-113
288
-708
```

## Usage 📦

1. Save the code to a file named `filter_and_round_numbers.py`.
2. Create the `data` list with arbitrary objects, as shown in the code.
3. Open a terminal or command prompt.
4. Navigate to the directory where the file is located.
5. Execute the script using the command:
    ```
    python filter_and_round_numbers.py
    ```
6. The program will display the filtered and rounded numbers.

## Conclusion 🚀

This program demonstrates how to filter, process, and print specific data types from a list.
It teaches filtering with `filter()` and transforming data with list comprehension.
It's a useful exercise for working with lists of arbitrary objects.
