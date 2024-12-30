# Calculate Average of Nested Lists Program 📝

## Description 📝

This program calculates the average of all elements in a nested list.
It iterates through each sublist, sums the elements in that sublist, and keeps track of the total count of numbers.
After processing all the sublists, it divides the total sum by the total count of numbers to find the average.

## Purpose 🎯

The goal of this program is to compute the average of all numbers present in a list of nested lists, making it useful for calculating the mean of numbers across multiple groups.

## How It Works 🔍

1. **Initial List**:
   The list `list1` is a list of nested lists, where each sublist contains integers:

    ```python
    list1 = [
        [1, 7, 8],
        [9, 7, 102],
        [102, 106, 105],
        [100, 99, 98, 103],
        [1, 2, 3]
    ]
    ```

2. **Looping Through Sublists**:
   The program uses a `for` loop to iterate through each sublist (`li`), summing the elements of each sublist and updating the total count of numbers (`counter`):

    ```python
    total += sum(li)
    counter += len(li)
    ```

3. **Calculating the Average**:
   After iterating through all sublists, the program calculates the average by dividing the total sum of elements by the total count of numbers:

    ```python
    return total / counter if counter != 0 else 0.0
    ```

4. **Example**:
   **Before**:

    ```python
    list1 = [
        [1, 7, 8],
        [9, 7, 102],
        [102, 106, 105],
        [100, 99, 98, 103],
        [1, 2, 3]
    ]
    ```

    **After running the program**:

    ```python
    print(calculate_average(list1))  # Output: 48.6
    ```

    This output is the average of all numbers across the sublists in `list1`.

## Usage 📦

1. Copy the code into a Python file, e.g., `calculate_average.py`.
2. Run the script in the terminal:
    ```bash
    python calculate_average.py
    ```
3. The program will output the average value of all numbers in the nested lists.

## Conclusion 🚀

This program efficiently computes the average of all integers in a list of nested lists.
It's a useful tool for calculating the mean across grouped data in Python.
