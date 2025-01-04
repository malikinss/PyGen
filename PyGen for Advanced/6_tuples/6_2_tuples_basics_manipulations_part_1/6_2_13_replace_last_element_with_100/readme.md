# Replace Last Element of Tuples with 100 📜

## Description 📝

This program takes a list of tuples, modifies each tuple by replacing its last element with the numeric value `100`, and returns the new list of modified tuples.

## Purpose 🎯

-   To demonstrate how to modify the last element of each tuple in a list.
-   To showcase how to convert a tuple to a list for modification and then convert it back to a tuple.

## How It Works 🔍

1. **Function `replace_last_element_with_100(tuples: List[Tuple[int, ...]])`**:

    - Takes a list of tuples as input.
    - Iterates through each tuple in the list.
    - Converts the tuple to a list to allow modification.
    - Replaces the last element with `100`.
    - Converts the list back into a tuple and appends it to the result list.

2. **List `tuples`**:

    - Contains multiple tuples with integer elements.

3. **The result**:
    - A new list of tuples where each tuple has its last element replaced with `100`.

### Example:

```
Input: [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100), (10, 100), (1, 2, 3, 100), (5, 6, 10, 2, 1, 100)]
```

## Output 📜

The output will be:

```
[(10, 20, 100), (40, 50, 100), (70, 80, 100), (10, 100), (1, 2, 3, 100), (5, 6, 10, 2, 1, 100)]
```

## Conclusion 🚀

This code successfully replaces the last element of each tuple with `100`, demonstrating tuple modification using list conversion.
It is a practical example of handling tuples in a list while making specific changes to their contents.
