# Sum of Numbers from a File 📄➕

## Description 📝

This program reads a file named **"nums.txt"**, which contains **two integers separated by spaces or new lines**, and prints their **sum**.

## Purpose 🎯

It demonstrates how to **read, process, and compute** numbers from a file with flexible formatting.

## How It Works 🔍

1. **File Reading (`get_all_data_from_file`)**:

    - Opens the file in **read mode (`'r'`)** with UTF-8 encoding.
    - Reads the entire content and **splits it** using whitespace (`split()`), handling both **spaces and newlines**.

2. **Summation (`get_sum_of_data`)**:
    - Converts the extracted **string numbers** into integers.
    - Uses Python’s built-in `sum()` function to compute the total.

## Example Usage:

**File (`nums.txt`):**

```
42
58
```

or

```
42 58
```

or

```
42
58
```

**Program Output:**

```python
>>> 100
```

## Conclusion 🚀

This script efficiently extracts numbers from a text file, **regardless of formatting**, and calculates their **sum**, making it a great **file-handling** example in Python! 🔢📂
