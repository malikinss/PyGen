# List Manipulation Program with `extend()` Method 📝

## Description 📝

This program demonstrates the use of the `extend()` method in list comprehension to add multiple elements to a specific sublist in a deeply nested list.
The task is to extend an innermost list with new elements.

## Purpose 🎯

The purpose of this program is to update a deeply nested list by extending the innermost list with additional elements.
Specifically, it adds the elements `['h', 'i', 'j']` to the list `['f', 'g']`.

## How It Works 🔍

1. **Initial List**:
   The starting list is:

    ```python
    list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
    ```

2. **Target Modification**:
   Using `list1[2][1][2].extend(['h', 'i', 'j'])`, the program navigates to the innermost list `['f', 'g']` and extends it with the elements `['h', 'i', 'j']`.

3. **Updated List**:
   After the `extend()` method is applied, the list becomes:

    ```python
    ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
    ```

4. **Example**:
   **Before**:
    ```python
    list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
    ```
    **After**:
    ```python
    list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
    ```

## Usage 📦

1. Copy the code into a Python file, e.g., `list_extend.py`.
2. Run the script in the terminal:
    ```bash
    python list_extend.py
    ```
3. The program will modify the list as specified and output the result.

## Conclusion 🚀

This program demonstrates how to extend a list in a deeply nested structure, which is helpful when you need to add multiple elements to a sublist at a specific depth.
