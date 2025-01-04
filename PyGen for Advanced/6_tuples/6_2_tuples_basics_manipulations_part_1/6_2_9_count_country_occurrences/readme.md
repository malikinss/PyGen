# Count Country Occurrences in Tuple 📊

## Description 📝

This program counts the number of occurrences of a specified country in a tuple containing a list of country names.
It uses the `count()` method, which returns the number of times a specified value appears in the tuple.

## Purpose 🎯

-   To count how many times a specific country appears in a tuple.
-   Demonstrates the use of the `count()` method to calculate element frequency in a tuple.

## How It Works 🔍

1. **Function `count_country_occurrences(countries: Tuple[str, ...], country: str)`**:

    - Takes a tuple `countries` and a string `country` as arguments.
    - Uses the `count()` method to count how many times the specified `country` appears in the tuple.
    - Returns the count of the specified country.

2. **Tuple `countries`**:

    - Contains a list of country names, including duplicate entries.

3. **The result**:
    - The number of occurrences of the specified country (`'Spain'` in this case) in the tuple is calculated and printed.

### Example:

```
Input: ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Spain', 'Cameroon')
Count occurrences of 'Spain'
Output: 3
```

## Output 📜

The output will be:

```
3
```

## Conclusion 🚀

This code successfully counts the number of occurrences of a specified country in a tuple, demonstrating the usage of the `count()` method to count element occurrences in a tuple.
