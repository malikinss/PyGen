# Filter Non-Empty Tuples from List 📜

## Description 📝

This program filters out empty tuples from a list of tuples, returning a new list containing only the non-empty tuples while preserving the original order.

## Purpose 🎯

-   To remove all empty tuples from a list of tuples.
-   This demonstrates how to filter elements in a list based on a condition, in this case, checking for non-empty tuples.

## How It Works 🔍

1. **Function `filter_non_empty_tuples(tuples: List[Tuple])`**:

    - Takes a list `tuples` as input.
    - Uses a list comprehension to iterate through each tuple in the list, keeping only those that are not empty.
    - Returns the list of non-empty tuples.

2. **List `tuples`**:

    - Contains a combination of empty and non-empty tuples.

3. **The result**:
    - The function returns a list of tuples that excludes any empty tuples, keeping the original order intact.

### Example:

```
Input: [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
Output: [('a', 'b'), ('a', 'b', 'c'), (1,), ('d',)]
```

## Output 📜

The output will be:

```
[('a', 'b'), ('a', 'b', 'c'), (1,), ('d',)]
```

## Conclusion 🚀

This code successfully filters out empty tuples from the list, preserving the order of the non-empty tuples.
It demonstrates how to apply list comprehension to filter elements based on a condition.
