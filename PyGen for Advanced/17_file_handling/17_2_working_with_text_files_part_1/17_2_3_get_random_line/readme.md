# Random Line Picker 📜

## Description 📝

This program reads a file named **"lines.txt"** and prints a **random line** from it.

## Purpose 🎯

Useful for retrieving a random entry from a list of stored phrases, logs, or other textual data.

## How It Works 🔍

1. **File Reading** (`get_data_from_file`):

    - Opens the file in **read mode (`'r'`)** with UTF-8 encoding.
    - Reads all lines and **removes trailing newlines** with `.strip()`.

2. **Random Line Selection** (`get_random_line`):
    - Uses `random.choice(data)` to pick a random line from the list.

## Example Usage:

**File (`lines.txt`):**

```
Hello, world!
Python is awesome.
Coding is fun.
Keep learning new things.
```

**Program Output (random each time):**

```python
>>> Keep learning new things.
```

## Conclusion 🚀

This script efficiently picks and prints a **random line** from a text file, ensuring dynamic and engaging output! 🎲
