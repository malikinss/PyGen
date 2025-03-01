# Linearize a Nested List 🧳

## Description 📝

The `linear()` function recursively transforms a nested list of integers into a flattened list, containing all the integers without any nesting.
This process is known as **linearization**.
It works with lists that may contain integers or other nested lists, with any level of nesting.

## Purpose 🎯

The function demonstrates:

-   The concept of recursion to flatten nested structures.
-   How to process and extract elements from deeply nested lists.
-   A method for transforming arbitrary nested lists into a linear list.

## How It Works 🔍

1. **Input Parameters**:

    - `nested_lists`: A list containing integers or other nested lists. Nesting can be arbitrary.

2. **Recursive Flow**:

    - The function checks each element:
        - If the element is an integer, it is added to the result list.
        - If the element is a list, the function recursively flattens the nested list by calling `linear()` on the element and adding the result to the list.

3. **Base Case**:

    - If an integer is encountered, the function returns it inside a list.

4. **Return Value**:
    - The function returns a new list with all the integers in a flattened, linear form.

For example, given the input:

```python
[1, [2, 3], [4, [5, 6, [7, 8, 9]]]]
```

The function will return:

```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Output 📜

For example:

```python
linear([3, [4], [5, [6, [7, 8]]]])
```

The function computes:

```
[3, 4, 5, 6, 7, 8]
```

**Output:**

```
[3, 4, 5, 6, 7, 8]
```

## Usage 📦

1. Call the function `linear()` with:
    - A list that may contain integers or nested lists.
2. Example:
    ```python
    linear([1, [2, 3], [4, [5, 6, [7, 8, 9]]]])  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```
3. The function returns a new list containing all the integers in a flat, linear form.

## Conclusion 🚀

The `linear()` function is a practical example of using recursion to flatten deeply nested data structures.
It demonstrates how recursion can be applied to process hierarchical data and transform it into a simpler, linear structure.
