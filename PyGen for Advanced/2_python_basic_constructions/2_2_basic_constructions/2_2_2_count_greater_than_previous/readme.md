# Count Numbers Greater Than Previous Program 🔢

## Description 📝

This program takes a string of natural numbers as input, splits it into a list, and counts how many numbers are greater than the number that precedes them in the list.

## Purpose 🎯

The goal of the program is to analyze a sequence of numbers and determine how many of them are greater than the one that comes before them.
This type of problem is useful in various contexts, such as data analysis, trend detection, and processing sequences of numerical data.

## How It Works 🔍

1. **Input Format**:

    - The program reads a string of natural numbers, where the numbers are separated by spaces.
    - The input string is split into a list of integers.

2. **Logic**:
    - The program iterates over the list starting from the second element.
    - For each element, it checks if the current number is greater than the one preceding it.
    - If this condition is true, it increments a counter.
3. **Example**:

    - **Input**:
        ```
        1 3 2 4 5
        ```
    - **Output**:
        ```
        3
        ```
    - **Explanation**:
        - `3` is greater than `1`.
        - `4` is greater than `2`.
        - `5` is greater than `4`.
          Therefore, the result is `3`.

4. **Edge Cases**:
    - If the list has only one number, the output will be `0`, as there are no numbers to compare.
    - If the numbers are in a strictly decreasing order, the output will be `0` because no number will be greater than its predecessor.

## Usage 📦

1. Copy the code into a Python file, e.g., `greater_than_previous.py`.
2. Run the script in the terminal:
    ```bash
    python greater_than_previous.py
    ```
3. Enter a sequence of natural numbers, separated by spaces.
4. The program will print the count of numbers that are greater than the one before them.

## Conclusion 🚀

This program efficiently counts how many numbers in a list are greater than the number that precedes them.
It's a simple yet powerful tool for analyzing sequences of data in many applications.
