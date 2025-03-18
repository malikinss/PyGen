# `print_unique_permutations()` - Generate Unique String Permutations

## Description 📝

The `print_unique_permutations()` function generates all unique permutations of a given string and prints them in lexicographical order, each on a new line.

## Purpose 🎯

✔ **Generates all permutations** of the input string.  
✔ **Removes duplicate permutations** using `set()`.  
✔ **Sorts results lexicographically** for ordered output.  
✔ **Handles strings up to 10 characters long** efficiently.

## How It Works 🔍

1. **Generates all permutations** of the string using `permutations()`.
2. **Converts each permutation tuple** into a string using `''.join(p)`.
3. **Eliminates duplicates** by storing permutations in a `set`.
4. **Sorts the unique permutations** lexicographically.
5. **Prints each permutation** on a separate line.

## Usage 📦

```python
print_unique_permutations("abc")
```

**Output:**

```plaintext
abc
acb
bac
bca
cab
cba
```

## Conclusion 🚀

This function efficiently generates all unique permutations of a string while ensuring they are printed in a sorted order.
It is optimized for small strings, making it ideal for use cases where performance matters.
