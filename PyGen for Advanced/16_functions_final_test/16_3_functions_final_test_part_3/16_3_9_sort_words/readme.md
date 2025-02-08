# Sorting Words Ignoring Case 🎯

## Description 📝

The `sort_words()` function takes a string of space-separated words, sorts them in lexicographic order regardless of their case, and prints the words in their original case as they appeared in the input string.

## Purpose 🎯

This function helps sort a list of words in a user-friendly way, preserving the original casing of each word while ignoring case differences during the sorting process.

## How It Works 🔍

1. **Splitting the String**: The function first splits the input string into individual words using `split()`.
2. **Sorting Words Ignoring Case**: It sorts the list of words using `sorted()`, where the `key` parameter is set to `str.lower` to ensure case-insensitive sorting.
3. **Printing Sorted Words**: Finally, the function prints the sorted words, keeping the original casing intact.

## Example Usage:

```python
>>> input_string = "banana Apple cherry Orange apple Banana"
>>> sort_words(input_string)
Apple Banana apple banana cherry Orange
```

## Conclusion 🚀

The `sort_words()` function makes it easy to sort words while disregarding case sensitivity. It ensures that the case of the words remains as it was initially entered, which can be particularly useful for displaying words in a user-friendly format.
