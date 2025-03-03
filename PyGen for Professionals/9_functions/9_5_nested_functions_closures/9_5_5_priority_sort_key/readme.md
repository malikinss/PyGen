# Sort Priority

## Description 📝

This Python script defines the `sort_priority()` function, which sorts a list of numbers by placing the numbers that belong to a specified group at the beginning.
The remaining numbers are sorted in non-decreasing order after the prioritized group.

## Purpose 🎯

The purpose of this program is to demonstrate how to prioritize specific numbers in a list while sorting.
The function allows users to specify a group of numbers that should appear first in the sorted list, followed by the other numbers in non-decreasing order.

## How It Works 🔍

1. **Arguments**: The function takes two arguments:
    - `values`: A list of numbers that needs to be sorted.
    - `group`: A list, tuple, or set of numbers that should appear at the beginning of the sorted list.
2. **Input Validation**: The function checks if `values` is a list and `group` is a valid iterable (list, tuple, or set).
3. **Priority Sorting**: The function uses a custom sorting key (`priority_sort_key`), which gives higher priority (priority 0) to numbers in the `group` and lower priority (priority 1) to others.
4. **Sorting**: The list is sorted using the custom key, ensuring that the numbers in `group` come first, followed by the rest of the numbers sorted in non-decreasing order.

## Output 📜

The function sorts the `values` list in place.
It does not return anything but modifies the original list directly.  
For example, if the input is:

```python
values = [7, 2, 5, 3, 8]
group = [5, 2]
sort_priority(values, group)
```

The output will be:

```python
[2, 5, 3, 7, 8]
```

## Usage 📦

1. Save the code to a file named `sort_priority.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
    ```python
    python sort_priority.py
    ```
5. Call the function `sort_priority()` with a list of numbers and a group to prioritize.
   Example:
    ```python
    values = [7, 2, 5, 3, 8]
    group = [5, 2]
    sort_priority(values, group)
    print(values)  # Output: [2, 5, 3, 7, 8]
    ```

## Conclusion 🚀

This function provides an efficient way to sort a list while giving priority to specific elements.
It demonstrates the power of custom sorting in Python using sorting keys and showcases how to use sets for faster lookup.
