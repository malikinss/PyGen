# Longest Words Finder

## Description 📝

This Python program reads a text file containing words separated by spaces and finds the longest words without changing their order.

## Purpose 🎯

The program helps identify the longest words in a given file, making it useful for text analysis or word length evaluation.

## How It Works 🔍

1. **Reading the File**:
    - The program reads the contents of `words.txt` as a single line.
2. **Splitting Words**:
    - The line is split into individual words based on spaces.
3. **Finding the Longest Words**:
    - The program determines the length of the longest word(s).
    - It collects and prints all words that match this length while preserving their original order.

## Output 📜

The program outputs the longest words, each on a new line.

### Example:

If `words.txt` contains:

```
apple banana watermelon kiwi grape strawberry
```

The program will output:

```
watermelon
strawberry
```

(Since these are the longest words in the file.)

## Usage 📦

1. Save the script as `longest_words_finder.py`.
2. Ensure `words.txt` is in the same directory.
3. Open a terminal or command prompt.
4. Navigate to the script's directory.
5. Run the script using:
    ```
    python longest_words_finder.py
    ```
6. The program will print the longest words.

## Conclusion 🚀

This script efficiently extracts and prints the longest words from a text file while preserving their original order.
