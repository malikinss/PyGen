# Cyclic Right Shift Program 🔄➡️

## Description 📝

This program takes a string of natural numbers as input, splits it into a list, and performs a cyclic right shift.
The last element of the list becomes the first element, and the rest of the elements move one position forward.

## Purpose 🎯

The purpose of this program is to demonstrate the operation of cyclically shifting a list of numbers to the right.
This is a common operation in algorithms, data manipulation, and array rotations.

## How It Works 🔍

1. **Input Format**:

    - The program reads a string of natural numbers, where the numbers are separated by spaces.
    - The input string is split into a list of strings.

2. **Logic**:

    - If the list is empty, the function returns the empty list as is.
    - Otherwise, the function shifts the last element to the front, and the rest of the elements move one position forward.

3. **Example**:

    - **Input**:
        ```
        1 2 3 4 5
        ```
    - **Output**:
        ```
        5 1 2 3 4
        ```
    - **Explanation**:
        - The last element `5` is moved to the front.
        - All other elements are shifted one position to the right.

4. **Edge Cases**:
    - If the list is empty, the program returns an empty list.
    - If the list contains only one element, the result will be the same list since the shift doesn’t change the order.

## Usage 📦

1. Copy the code into a Python file, e.g., `cyclic_shift_right.py`.
2. Run the script in the terminal:
    ```bash
    python cyclic_shift_right.py
    ```
3. Enter a sequence of natural numbers, separated by spaces.
4. The program will print the list with the cyclic right shift applied.

## Conclusion 🚀

This program effectively demonstrates the concept of cyclically shifting a list of elements to the right.
It works for lists of any size and handles edge cases like empty or single-element lists seamlessly.
