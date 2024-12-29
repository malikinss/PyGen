# Count Unique Elements Program 🔢

## Description 📝

This program takes a string of natural numbers arranged in non-decreasing order as input.
It splits the string into a list of numbers and then counts how many unique elements are present in the list.

## Purpose 🎯

The purpose of this program is to count how many different (unique) numbers are present in a list of numbers that are arranged in non-decreasing order.

## How It Works 🔍

1. **Input Format**:

    - The program reads a string of numbers separated by spaces, where the numbers are in non-decreasing order.
    - The input string is split into a list of numbers.

2. **Logic**:

    - If the list is empty, the program returns `0` because there are no elements to count.
    - The function then iterates through the list, comparing each number with the next one. Every time a new (different) number is encountered, it increments a counter.

3. **Example**:

    - **Input**:
        ```
        1 1 2 2 3 3 3 4
        ```
    - **Output**:
        ```
        4
        ```
    - **Explanation**:
        - The unique numbers in the list are `1`, `2`, `3`, and `4`.
        - Thus, the result is `4`.

4. **Edge Cases**:
    - If the list is empty, the program returns `0`.
    - If all numbers are the same, the program returns `1`.

## Usage 📦

1. Copy the code into a Python file, e.g., `count_unique_elements.py`.
2. Run the script in the terminal:
    ```bash
    python count_unique_elements.py
    ```
3. Enter a sequence of non-decreasing numbers, separated by spaces.
4. The program will print the number of unique elements in the list.

## Conclusion 🚀

This program efficiently counts the number of unique elements in a non-decreasing list of numbers.
It handles edge cases like empty lists or lists where all numbers are the same, making it robust and easy to use.
