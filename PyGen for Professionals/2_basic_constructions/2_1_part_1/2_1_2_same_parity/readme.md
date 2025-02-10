# Same Parity Filter

## Description 📝

This program implements the `same_parity()` function, which filters and returns a list of integers from the input list that share the same parity (even or odd) as the first element in the list.
The order of elements is preserved in the returned list.

## Purpose 🎯

The purpose of this function is to allow filtering of a list of integers based on their parity, i.e., whether they are even or odd.
It ensures that all elements in the result share the same parity as the first element of the input list.

## How It Works 🔍

1. The function takes a list of integers as input.
2. It checks the parity of the first element in the list (even or odd).
3. It filters out the elements from the list that have the same parity as the first element.
4. The filtered list is returned, preserving the original order of elements.

## Output 📜

-   A new list containing the elements from the input list that share the same parity as the first element.
-   If the input list is empty, the function returns an empty list.

## Usage 📦

1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Call the `same_parity()` function with a list of integers.

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]
result = same_parity(numbers)
print(result)  # Output: [1, 3, 5]
```

## Conclusion 🚀

The `same_parity()` function provides an efficient way to filter a list of integers based on their parity, helping with tasks where only numbers of a certain parity are required.
