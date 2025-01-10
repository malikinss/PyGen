# Unique Values from Items List Program 📝

## Description 📝

This program takes a list of items, which includes both numbers and strings, and produces a set containing the unique values by treating string representations of numbers as integers.
It then outputs these unique values in sorted order, separated by spaces.

## Purpose 🎯

The goal of this program is to process a list with mixed data types (numbers and strings representing numbers), convert all elements to integers, remove duplicates, and print the resulting unique integers in sorted order.

## How It Works 🔍

1. **Input**:
    - A list of items (`items`), where some elements are numbers and some are string representations of numbers.
2. **Logic**:
    - The program uses a set generator to convert all items to integers, ensuring uniqueness by using a set data structure.
    - After creating the set, the elements are printed in sorted order using the `print_sorted_set` function.
3. **Output**:
    - The program prints the unique integers from the list, sorted in ascending order and separated by a space.

### Example:

**Input**:

```python
[10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
```

**Output**:

```
1 5 6 10 12 23 30 34 45 56 67 89 90
```

## Output 📜

-   A single line containing the sorted unique values from the input list, separated by spaces.

## Usage 📦

1. Run the program.
2. The program will automatically process the list and output the unique sorted values.

## Conclusion 🚀

This program provides an efficient way to handle a list of mixed data types (numbers and string representations) and outputs the unique integers in a clean, sorted format.
