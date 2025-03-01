# Recursive Range Sum 📊

## Description 📝

The `range_sum()` function calculates the sum of elements in a list between two given indices using recursion.
This eliminates the need for loops and demonstrates a recursive approach to summing elements in a list.

## Purpose 🎯

This function is useful for:

-   Practicing recursion in list operations.
-   Implementing a sum function that works without explicit iteration.
-   Understanding how to accumulate values recursively.

## How It Works 🔍

1. The function takes a list of integers and two non-negative indices: `start` and `end`.
2. It uses a helper recursive function to:
    - Check if the `current_index` has surpassed `end`. If so, return the accumulated sum.
    - Add the current element to the sum.
    - Call itself recursively, moving to the next index.
3. The recursion continues until all elements within the range are summed.

## Output 📜

For example, if the input is:

```python
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
```

The function will sum the elements from index **3 to 7** (`4 + 5 + 6 + 7 + 8`) and output:

```
30
```

## Usage 📦

1. Call the function `range_sum()` with:
    - A list of integers.
    - A starting index (`start`).
    - An ending index (`end`).
2. Example:
    ```python
    numbers = [10, 20, 30, 40, 50, 60]
    result = range_sum(numbers, 1, 4)  # Output: 20 + 30 + 40 + 50 = 140
    print(result)
    ```
3. The function returns the computed sum.

## Conclusion 🚀

The `range_sum()` function showcases how recursion can replace loops in list operations, making it a useful tool for mastering recursive techniques and understanding functional programming principles.
