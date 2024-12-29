# Swap Adjacent Elements Program 🔄

## Description 📝

This program takes a string of natural numbers as input, splits it into a list, and swaps the adjacent elements of the list.
If the list contains an odd number of elements, the last element remains in its place.

## Purpose 🎯

The goal of the program is to rearrange a list of numbers by swapping adjacent elements.
This is a common operation in algorithms and can be useful for tasks like sorting, reordering, and data manipulation.

## How It Works 🔍

1. **Input Format**:

    - The program reads a string of natural numbers, where the numbers are separated by spaces.
    - The input string is split into a list of strings.

2. **Logic**:

    - The program iterates through the list, stepping by 2 indices each time.
    - It swaps each pair of adjacent elements: the element at index `i` is swapped with the element at index `i + 1`.
    - If the list has an odd number of elements, the last element remains unchanged because there is no adjacent element to swap with it.

3. **Example**:

    - **Input**:
        ```
        1 2 3 4 5
        ```
    - **Output**:
        ```
        2 1 4 3 5
        ```
    - **Explanation**:
        - `1` and `2` are swapped.
        - `3` and `4` are swapped.
        - `5` remains in its place as it has no adjacent element to swap with.

4. **Edge Cases**:
    - If the list contains a single element, it remains unchanged because there are no adjacent elements.
    - If the list contains an even number of elements, all adjacent pairs are swapped.

## Usage 📦

1. Copy the code into a Python file, e.g., `swap_adjacent_elements.py`.
2. Run the script in the terminal:
    ```bash
    python swap_adjacent_elements.py
    ```
3. Enter a sequence of natural numbers, separated by spaces.
4. The program will print the list with adjacent elements swapped.

## Conclusion 🚀

This program efficiently swaps adjacent elements in a list, making it a useful tool for rearranging or manipulating data sequences.
It handles both even and odd-length lists with ease, leaving the last element unchanged in odd-length cases.
