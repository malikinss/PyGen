# Multiple Splitter 🧩

## Description 📝

This program provides a function to **split a string** using multiple delimiters provided in a list. It is similar to Python's `split()` method but supports multiple delimiters at once.

## Purpose 🎯

The script is designed to handle the splitting of strings by **multiple delimiters**, enabling greater flexibility when dealing with complex string formats.

## How It Works 🔍

1. **Reads Input**:

    - The function `multiple_split()` accepts a string and a list of delimiters.

2. **Escapes Delimiters**:

    - Each delimiter in the list is **escaped** to ensure it works correctly with regular expressions (for special characters like `.` or `*`).

3. **Splits the String**:
    - The string is then split at all positions where any of the delimiters appear, and the result is returned as a list of substrings.

## Output 📜

### Example Input:

```sh
apple, orange; banana and grape
```

### Example Output:

```sh
['apple', 'orange', 'banana', 'grape']
```

## Usage 📦

1. Run the script:
    ```sh
    python multiple_splitter.py
    ```
2. Input a string and delimiters list:
    ```
    "apple, orange; banana and grape", [", ", "; ", " and "]
    ```
3. The output will be:
    ```
    ['apple', 'orange', 'banana', 'grape']
    ```

## Conclusion 🚀

This function makes it easy to **split strings using multiple delimiters**, saving time and providing flexibility for complex string processing tasks.
