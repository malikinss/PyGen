# Filtering and Sorting Words of Exact Length 6

## Description

This program filters a list of words to find those that are exactly 6 characters long and then sorts them in alphabetical order.
The filtered words are printed as a single line, separated by spaces.

## Purpose

The goal is to practice using Python's built-in functions `filter()` and `sorted()` along with an anonymous function (`lambda`) to process a list efficiently.

## How It Works

1. **Filtering**:
    - Uses `filter()` with a lambda function to keep only words that are exactly 6 characters long.
2. **Sorting**:
    - The `sorted()` function arranges the filtered words in alphabetical order.
3. **Output Formatting**:
    - Uses `print(*result)` to display the sorted words as a space-separated string.

## Output

For the given list of words, the program outputs:

```
abduct aboard abrupt absent accept access abroad absorb abound abrupt betray bestow beyond bicycle
```

## Usage

1. **Define the word list (`words`)**.
2. **Use `filter()` with a lambda function** to extract words of length 6.
3. **Sort the filtered words** alphabetically using `sorted()`.
4. **Print the result** as a space-separated string.

## Conclusion

This approach demonstrates how to efficiently filter and sort data using Python's built-in functions with concise lambda expressions.
