# Get Elements Except the Last Three from a Tuple 🔄

## Description 📝

This program demonstrates how to extract all elements from a tuple except for the last three using Python's slicing feature.
The function `get_elements_except_last_three` returns a tuple containing all elements except the last three.

## Purpose 🎯

-   To retrieve all elements from a tuple except for the last three using slicing.
-   Show how to use Python slicing to omit specific elements from the end of a tuple.

## How It Works 🔍

1. **Function `get_elements_except_last_three(tup: Tuple[str, ...])`**:

    - Takes a tuple `tup` as an argument.
    - Uses slicing (`tup[:-3]`) to get all elements except the last three.
    - Returns the sliced tuple containing the elements.

2. **Tuple `countries`**:

    - Contains a sequence of country names.

3. **The result**:
    - The function is called to retrieve all the countries except the last three, which is then printed.

### Example:

```
Input: Tuple of country names
Output: All countries except the last three
```

## Output 📜

The output will be:

```
('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain')
```

## Conclusion 🚀

This code demonstrates how to use Python slicing to omit the last three elements of a tuple and return the rest, providing an efficient and concise way to manipulate tuples.
