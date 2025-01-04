# Get Elements Except First Three and Last Two from a Tuple 🔄

## Description 📝

This program demonstrates how to extract all elements from a tuple except for the first three and the last two using Python's slicing feature.
The function `get_elements_except_first_three_and_last_two` returns a tuple containing all the elements except the first three and the last two.

## Purpose 🎯

-   To retrieve all elements from a tuple except for the first three and the last two using slicing.
-   Showcase how to use Python slicing to exclude specific elements from the beginning and end of a tuple.

## How It Works 🔍

1. **Function `get_elements_except_first_three_and_last_two(tup: Tuple[str, ...])`**:

    - Takes a tuple `tup` as an argument.
    - Uses slicing (`tup[3:-2]`) to get all elements starting from the fourth element (index 3) and excluding the last two elements.
    - Returns the sliced tuple containing the elements except the first three and last two.

2. **Tuple `countries`**:

    - Contains a sequence of country names.

3. **The result**:
    - The function is called to retrieve all countries excluding the first three and last two, which is then printed.

### Example:

```
Input: Tuple of country names
Output: All countries except the first three and last two
```

## Output 📜

The output will be:

```
('Canada', 'Slovenia', 'Italy', 'Spain')
```

## Conclusion 🚀

This code demonstrates how to use Python slicing to exclude the first three and last two elements of a tuple and return the rest.
This technique is efficient and concise for manipulating tuples.
