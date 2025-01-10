# Extract Unique PNG Files Program 📝

## Description 📝

This program processes a list of file names and extracts unique files with the `.png` extension, regardless of case.
It outputs the file names in lowercase, sorted alphabetically, and separated by a space.

## Purpose 🎯

The goal is to identify and extract `.png` files from a list, making sure to handle case insensitivity and return the unique file names in sorted order.

## How It Works 🔍

1. **Input**:
    - A list of file names (with different file extensions, including `.png`).
2. **Logic**:
    - Each file name is checked for the `.png` extension, regardless of case.
    - The selected file names are converted to lowercase.
    - The unique file names are stored in a set.
    - The set of file names is sorted alphabetically.
3. **Output**:
    - The program prints the file names with the `.png` extension, all in lowercase, sorted alphabetically, space-separated.

### Example:

**Input**:

```python
['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt']
```

**Output**:

```
python.png stepik.png
```

## Output 📜

-   A single line containing the unique `.png` file names, sorted alphabetically, and separated by spaces.

## Usage 📦

1. Run the program.
2. The program will process the list and output the `.png` files in lowercase, sorted alphabetically.

## Conclusion 🚀

This program effectively filters, processes, and outputs the `.png` file names from a list, ensuring case insensitivity and uniqueness in the result.
