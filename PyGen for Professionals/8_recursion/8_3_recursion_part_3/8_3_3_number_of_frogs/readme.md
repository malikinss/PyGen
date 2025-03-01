# Number of Frogs in a Pond 🐸

## Description 📝

The `number_of_frogs()` function calculates the number of frogs in a pond for a given year using recursion.
The frog population follows a specific pattern where each year:

-   30 frogs are caught and removed.
-   The remaining frogs reproduce, tripling in number.

## Purpose 🎯

This function is useful for modeling population growth under specific conditions and demonstrates how recursion can be used for mathematical sequence calculations.

## How It Works 🔍

1. The pond starts with **77 frogs** in year **1**.
2. Each year, the number of frogs follows the formula:
   \[
   F*k = 3 \times (F*{k-1} - 30)
   \]
   where \( F_k \) is the number of frogs in year \( k \).
3. The function recursively computes the number of frogs for a given year by:
    - Using **year 1 as the base case** with 77 frogs.
    - Recursively calculating the number of frogs for the previous year and applying the given formula.

## Output 📜

For example, if the user inputs:

```
5
```

The function returns:

```
3087
```

(Computed as per the formula)

## Usage 📦

1. Call the function `number_of_frogs()` with a natural number representing the year.
2. Example:
    ```python
    print(number_of_frogs(5))
    ```
3. The function will return the number of frogs in the pond for the specified year.

## Conclusion 🚀

The `number_of_frogs()` function effectively models population changes using recursion, making it useful for ecological simulations, mathematical modeling, and recursive function practice.
