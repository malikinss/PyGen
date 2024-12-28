# Merge Multiple Sorted Lists Program 🔗

## Description 📝

This Python program merges multiple sorted lists into one sorted list.
The program reads a number `n` (the number of lists) and then `n` lines of sorted integers.
It uses the `quick_merge()` function to merge these lists and outputs the final merged list in ascending order.

## Purpose 🎯

-   To merge multiple sorted integer lists into one sorted list.
-   Efficiently handles merging by using the `quick_merge()` function to combine each input list with the growing merged list.

## How It Works 🔍

1. **Function `quick_merge(list1, list2)`**:

    - This function takes two sorted lists and merges them into a single sorted list. It does this by comparing the elements from both lists, adding the smaller element to the result, and continuing until all elements are merged.
    - If there are remaining elements in either list after one is exhausted, they are appended to the result.

2. **Merging Multiple Lists**:
    - The program starts with an empty `total_list` and repeatedly merges each new input list with it using `quick_merge()`.
3. **Example**:
   For the input:
    ```
    3
    1 3 5
    2 4 6
    0 7 8
    ```
    The output will be:
    ```
    0 1 2 3 4 5 6 7 8
    ```

## Usage 📦

1. Copy the code into a Python file, e.g., `merge_multiple_sorted_lists.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python merge_multiple_sorted_lists.py
    ```
5. Input the number of lists followed by the lists themselves when prompted. The program will merge them into one sorted list and display the result.

## Conclusion 🚀

This program efficiently merges multiple sorted lists into a single sorted list using the `quick_merge()` function, making it useful for scenarios where you need to merge already sorted data.
