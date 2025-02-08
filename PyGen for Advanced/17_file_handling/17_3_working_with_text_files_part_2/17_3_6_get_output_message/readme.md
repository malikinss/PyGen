# Program to Count Letters, Words, and Lines in a Text File 📝🔢

## Description 📝

This program reads a file **"file.txt"** and outputs the number of Latin alphabet letters, words, and lines in the file.

## Purpose 🎯

To analyze a file and count:

-   The total number of Latin letters (both uppercase and lowercase).
-   The number of words (sequences of characters separated by spaces).
-   The number of lines in the file.

## How It Works 🔍

1. **Reading File (`get_data_from_file`)**:

    - The program reads the file **"file.txt"** line by line and stores the content in a list of strings.

2. **Counting Letters (`get_letters_number`)**:

    - The program counts the Latin alphabet letters (both uppercase and lowercase) using `ascii_letters` from the `string` module. Each character in each line is checked, and the count of valid letters is calculated.

3. **Counting Words (`get_words_number`)**:

    - Words are identified by splitting each line into words using the `split()` method. The number of words in each line is counted and summed up to get the total number of words.

4. **Counting Lines (`get_lines_number`)**:

    - The number of lines is simply the length of the list of lines read from the file.

5. **Output**:
    - The counts of letters, words, and lines are printed in a formatted message.

## Example Usage:

**File (`file.txt`):**

```
This is a test.
Another test here.
```

**Program Output:**

```python
Input file contains:
22 letters
5 words
2 lines
```

## Conclusion 🚀

This program provides a simple and effective way to analyze a text file, counting the letters, words, and lines, and then outputs the result in a clear, formatted manner.
