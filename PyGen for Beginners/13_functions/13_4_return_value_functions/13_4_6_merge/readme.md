# Merge Two Sorted Lists Program 🔗

## Description 📝

This Python program takes two ascending-sorted integer lists as input and merges them into one sorted list.
The function efficiently combines the lists by comparing elements and adding them in sorted order.

## Purpose 🎯

-   To merge two sorted integer lists into one sorted list.
-   Useful in scenarios where you need to combine already sorted data or perform efficient list merging.

## How It Works 🔍

1. **Function `merge(list1, list2)`**:

    - Two lists (`list1` and `list2`) are given as input. The function merges them into a new list called `merged`.
    - It compares the smallest elements from both lists and appends the smaller one to the `merged` list.
    - After one of the lists is fully merged, any remaining elements from the other list are appended to `merged`.

2. **Example**:
   For the input:
    ```
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    ```
    The output will be:
    ```
    [1, 2, 3, 4, 5, 6]
    ```

## Usage 📦

1. Copy the code into a Python file, e.g., `merge_sorted_lists.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python merge_sorted_lists.py
    ```
5. Input the two sorted integer lists when prompted. The program will then merge them into one sorted list.

## Conclusion 🚀

This function provides an efficient way to merge two sorted lists without the need for complex sorting operations, making it suitable for scenarios where you already have sorted data and need to combine them.
