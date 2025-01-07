# Unique Character Count Program 🔤

## Description 📝

This program takes a string of text as input and calculates the number of unique characters in that string.
It utilizes Python's `set` data structure to eliminate duplicates, allowing for easy counting of distinct characters.

## Purpose 🎯

-   To determine the number of unique characters in a string.
-   To demonstrate the power of Python sets for solving problems involving uniqueness and counting.

## How It Works 🔍

1. **Function `count_unique_chars`**:

    - Accepts a string `text` as input.
    - Converts the string into a set, which automatically removes duplicates, leaving only unique characters.
    - Returns the length of the set, representing the number of unique characters in the string.

2. **Input**:

    - A string is taken as input from the user.

3. **Output**:
    - The program outputs the number of unique characters in the provided string.

### Example:

```python
text = "programming"
print(count_unique_chars(text))
```

**Output**:

```
8
```

## Output 📜

-   If the input string is `"programming"`, the output will be `8` because the unique characters in `"programming"` are: `'p', 'r', 'o', 'g', 'a', 'm', 'i', 'n'`.

## Conclusion 🚀

This program illustrates a simple yet efficient way to count unique characters in a string by leveraging Python's set data structure.
It highlights the importance of understanding data structures like sets to solve common problems efficiently.
