# Chunking a List into Sublists 📝

## Description 📝

This program takes a string of characters and a number `n` as input, splits the string into a list of characters, and then groups the characters into chunks of size `n`.

## Purpose 🎯

The purpose of this program is to split a list of characters into smaller sublists of a specified size.
This can be useful when working with large datasets that need to be processed in smaller chunks.

## How It Works 🔍

1. **Input**:
    - The first line contains characters separated by spaces.
    - The second line contains an integer `n` which determines the size of each chunk.
2. **Logic**:
    - The program splits the first input line into a list of characters.
    - It then uses the `chunked()` function to divide the list into sublists, where each sublist contains `n` elements, except possibly the last sublist if there are fewer elements left.
3. **Output**:
    - The program returns a list of sublists, each containing up to `n` characters.

### Example:

For the input:

```plaintext
a b c d e f g h i j
3
```

The output will be:

```plaintext
[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j']]
```

This means the list has been split into chunks of size 3, with the last chunk containing only 1 element.

## Usage 📦

1. Copy the code into a Python file, e.g., `chunk_list.py`.
2. Run the script in the terminal:
    ```bash
    python chunk_list.py
    ```
3. Enter the characters as space-separated values in the first line.
4. Enter the chunk size `n` on the second line.
5. The program will output the chunked list.

## Conclusion 🚀

This program efficiently breaks down a list into smaller chunks, which can be helpful for processing large amounts of data in manageable portions.
