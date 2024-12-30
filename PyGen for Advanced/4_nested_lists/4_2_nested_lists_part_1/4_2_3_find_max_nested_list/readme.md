# Find Maximum Element in Nested Lists Program 📝

## Description 📝

This program uses a `for` loop and the built-in `max()` function to find the maximum element among all elements in a list of nested lists.
It iterates through each nested list, calculates the maximum value within that list, and keeps track of the overall maximum.

## Purpose 🎯

The program helps in finding the largest element across multiple sublists in a nested list.
It works by determining the maximum value in each sublist and comparing it to the global maximum.

## How It Works 🔍

1. **Initial List**:
   The list `list1` is a list of nested lists, where each sublist contains integer elements:

    ```python
    list1 = [
        [1, 7, 8],
        [9, 7, 102],
        [6, 106, 105],
        [100, 99, 98, 103],
        [1, 2, 3]
    ]
    ```

2. **Looping Through Sublists**:
   The `for` loop iterates over each sublist in `list1`, and the `max()` function is used to find the maximum element of each sublist:

    ```python
    for li in list1:
        current_max = max(li)
        if current_max > maximum:
            maximum = current_max
    ```

3. **Result**:
   The final result, which is the maximum element found across all the sublists, is returned:

    ```python
    return maximum
    ```

    In the example, the maximum element among all sublists is `106`.

4. **Example**:
   **Before**:

    ```python
    list1 = [
        [1, 7, 8],
        [9, 7, 102],
        [6, 106, 105],
        [100, 99, 98, 103],
        [1, 2, 3]
    ]
    ```

    **After running the program**:

    ```python
    print(find_max_nested_list(list1))  # Output: 106
    ```

## Usage 📦

1. Copy the code into a Python file, e.g., `find_max_nested_list.py`.
2. Run the script in the terminal:
    ```bash
    python find_max_nested_list.py
    ```
3. The program will output the maximum element found in the nested lists.

## Conclusion 🚀

This program efficiently finds the largest element in a nested list using a `for` loop and the `max()` function, making it a useful tool for working with lists of lists in Python.
