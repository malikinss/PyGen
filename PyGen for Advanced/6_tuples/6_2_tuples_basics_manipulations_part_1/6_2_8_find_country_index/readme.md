# Find Country Index in Tuple 📍

## Description 📝

This program finds the index of a specified country in a tuple containing a list of country names. It uses the `index()` method, which returns the first occurrence of the specified value in the tuple.

## Purpose 🎯

-   To locate the position of a specific country in a tuple.
-   Demonstrates the use of the `index()` method for tuple element searching.

## How It Works 🔍

1. **Function `find_country_index(countries: Tuple[str, ...], country: str)`**:

    - Takes a tuple `countries` and a string `country` as arguments.
    - Finds the index of the specified `country` in the tuple using `countries.index(country)`.
    - Returns the index of the country.

2. **Tuple `countries`**:

    - Contains a list of country names.

3. **The result**:
    - The index of the specified country in the tuple is calculated and printed.

### Example:

```
Input: ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
Find the index of 'Slovenia'
Output: 5
```

## Output 📜

The output will be:

```
5
```

## Conclusion 🚀

This code successfully finds the index of a specified country in a tuple, demonstrating the use of the `index()` method for retrieving the position of an element.
