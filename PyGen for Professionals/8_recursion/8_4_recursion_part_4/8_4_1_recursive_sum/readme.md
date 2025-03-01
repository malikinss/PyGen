# Recursive Sum of Nested Lists 🧮

## Description 📝

The `recursive_sum()` function calculates the sum of all integers in a nested list, where the list may contain integers or other nested lists (with arbitrary depth).
The function uses recursion to traverse through all the levels of the nested lists and computes the total sum of all integer values.

## Purpose 🎯

The function demonstrates:

-   How to handle nested lists and calculate sums through recursion.
-   The concept of recursion to process lists with arbitrary depth.
-   How to traverse nested structures and perform calculations.

## How It Works 🔍

1. **Input Parameters**:

    - `nested_list`: A list that contains either integers or other lists. The nesting can be arbitrary.

2. **Recursive Flow**:

    - The function iterates through each element in the list.
    - If the element is an integer, it is added to the total sum.
    - If the element is a nested list, the function recursively calls itself to process the nested list and adds its result to the total.

3. **Base Case**:

    - The recursion stops when an empty list is encountered, returning a sum of 0.

4. **Return Value**:
    - The function returns the total sum of all integers found in the nested structure.

For example, if the input is:

```python
[[1, 2, [3, 4]], [5, 6], 7]
```

The function computes:

```
1 + 2 + (3 + 4) + 5 + 6 + 7 = 28
```

## Output 📜

For example:

```python
recursive_sum([[1, 2, [3, 4]], [5, 6], 7])
```

The function computes:

```
28
```

**Output:**

```
28
```

## Usage 📦

1. Call the function `recursive_sum()` with:
    - A nested list containing integers or other nested lists.
2. Example:
    ```python
    recursive_sum([[1, 2, [3, 4]], [5, 6], 7])  # Output: 28
    ```
3. The function returns the sum of all integers in the nested list.

## Conclusion 🚀

The `recursive_sum()` function showcases a recursive approach to summing values in a nested list structure, making it a useful tool for handling complex, arbitrarily nested data structures.
This approach demonstrates the power of recursion for traversing hierarchical data and performing calculations.
