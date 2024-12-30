# Reverse Nested Lists Program 📝

## Description 📝

This program takes a list of nested lists and reverses each individual sublist within it.
The `reverse()` method is used to reverse the elements of each sublist in-place.

## Purpose 🎯

The purpose of the program is to reverse the elements of each sublist in a list of lists, effectively changing the order of the elements within each nested list.

## How It Works 🔍

1. **Initial List**:
   The input list `list1` is a list of nested lists:

    ```python
    list1 = [
        [1, 7, 8],
        [9, 7, 102],
        [102, 106, 105],
        [100, 99, 98, 103],
        [1, 2, 3]
    ]
    ```

2. **Reversing Each Sublists**:
   The function `reverse_nested_lists()` uses a `for` loop to iterate through each sublist in `list1` and reverses it using the `reverse()` method:

    ```python
    for li in list1:
        li.reverse()
    ```

3. **Returning the Reversed List**:
   After reversing all sublists, the modified list is returned:

    ```python
    return list1
    ```

    For example, the sublist `[1, 7, 8]` becomes `[8, 7, 1]`.

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
    print(reverse_nested_lists(list1))  # Output: [
        [8, 7, 1],
        [102, 7, 9],
        [105, 106, 102],
        [103, 98, 99, 100],
        [3, 2, 1]
    ]
    ```

## Usage 📦

1. Copy the code into a Python file, e.g., `reverse_nested_lists.py`.
2. Run the script in the terminal:
    ```bash
    python reverse_nested_lists.py
    ```
3. The program will output the modified list with each nested list reversed.

## Conclusion 🚀

This program provides an easy way to reverse each sublist within a list of lists.
It uses the `reverse()` method to alter the order of elements in place, making it a straightforward solution for this problem.
