# Remove Elements at Odd Indices 📝

## Description 📝

This Python program takes a natural number `n` and a list of `n` integers as input. It creates a list by removing all elements that are positioned at odd indices (1, 3, 5, etc.) from the original list and prints the resulting list.

## Purpose 🎯

The program demonstrates how to modify a list by removing elements at specific indices and prints the modified list.

## How It Works 🔍

1. The function `remove_odd_indices()` takes two parameters: `n` (the number of integers) and `numbers` (the list of integers).
2. The function uses list slicing to select only the elements at even indices (0, 2, 4, etc.), effectively removing elements at odd indices.
3. The result is returned as a list of the remaining elements.

## Output 📜

```bash
Example Input:
5
1
2
3
4
5
Example Output:
[1, 3, 5]
```

## Usage 📦

1. Save the script as `remove_odd_indices.py`.
2. Run the script in a Python environment.
3. Input the number `n`.
4. Input `n` integers.
5. The program will output the list with elements at odd indices removed.

## Conclusion 🚀

This program shows how to manipulate a list by removing elements at specific indices, and is a useful demonstration of Python's list slicing feature.
