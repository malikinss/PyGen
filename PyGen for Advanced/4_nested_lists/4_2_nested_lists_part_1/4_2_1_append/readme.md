# List Manipulation Program 📝

## Description 📝

This program demonstrates how to manipulate nested lists in Python using the `append()` method.
The goal is to modify a nested list by appending a value to an innermost sublist.

## Purpose 🎯

The purpose of this program is to update a deeply nested list by appending a value to the innermost sublist.
Specifically, it adds `7000` to the innermost list `[5000, 6000]`.

## How It Works 🔍

1. **Input List**:
   The initial list is defined as:
    ```python
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    ```
2. **Target Modification**:
   Using `list1[2][2].append(7000)`, the program navigates to the innermost list `[5000, 6000]` and appends the value `7000` to it.

3. **Output**:
   After the `append()` method is called, the list is updated to:
    ```python
    [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
    ```
4. **Example**:
   **Before**:
    ```python
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    ```
    **After**:
    ```python
    list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
    ```

## Usage 📦

1. Copy the code into a Python file, e.g., `list_manipulation.py`.
2. Run the script in the terminal:
    ```bash
    python list_manipulation.py
    ```
3. The program will modify the list as specified and output the result.

## Conclusion 🚀

This program demonstrates how to append values to specific positions within nested lists, which is a useful technique when working with complex data structures.
