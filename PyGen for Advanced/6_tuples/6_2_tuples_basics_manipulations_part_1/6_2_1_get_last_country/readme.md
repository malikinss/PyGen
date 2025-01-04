# Get the Last Country from a Tuple 🌍

## Description 📝

This program demonstrates how to access the last element of a tuple using indexing. The function `get_last_country` is used to return the last country from a tuple containing a list of country names.

## Purpose 🎯

-   To retrieve the last element from a tuple of country names.
-   Show the usage of negative indexing in tuples to access elements from the end.

## How It Works 🔍

1. **Function `get_last_country(countries: Tuple[str, ...])`**:

    - Takes a tuple `countries` containing country names as strings.
    - Returns the last country in the tuple using negative indexing (`countries[-1]`).

2. **Tuple `countries`**:
    - Contains a list of country names.
3. **The result**:
    - The function is called to retrieve the last element of the tuple, which is then printed.

### Example:

```
Input: Tuple of countries
Output: The last country name in the tuple
```

## Output 📜

For the given tuple `countries`, the program will output the last country in the list, which is `Italy`.

Example output:

```
Italy
```

## Conclusion 🚀

This code showcases how to retrieve the last element from a tuple using negative indexing, a feature that makes it easy to access elements from the end of a sequence without knowing the exact length of the tuple.
