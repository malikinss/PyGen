# Word Splitter: Identical Parts Checker

## Description 📝

This program identifies words that consist of two identical parts.
A word is considered valid if it can be split into two equal halves where both halves are identical.
The program reads a list of words and prints those that match this condition.

## Purpose 🎯

The purpose of this program is to process a list of words and output only those that are made up of two identical syllables (or parts).
This helps in identifying words that have a specific repeated structure.

## How It Works 🔍

1. **Input**:

    - The program accepts an arbitrary number of words, each on a separate line.

2. **Validation**:

    - A **regular expression** is used to check whether the word can be split into two identical parts. The regular expression `r'^(\w+)\1$'` matches any word where:
        - The word can be split into two identical parts (`\w+` matches a word and `\1` checks if the second part is identical to the first part).
        - The word's length must be even for it to be split evenly.

3. **Output**:
    - For each word, the program checks if it satisfies the condition and outputs those that do. Each matching word is printed on a new line, maintaining the original order of input.

## Output 📜

### Example Input:

```text
hello
abcabc
aaaa
abcabcabc
```

### Example Output:

```text
abcabc
aaaa
```

## Usage 📦

1. Save the program in a Python file (e.g., `word_splitter.py`).
2. Run the script.
3. Enter words, each on a separate line.
4. The program will output words consisting of two identical parts.

## Conclusion 🚀

This program efficiently identifies words that follow a specific structure, making it easy to find and process words with repeated patterns.
The use of regular expressions ensures that the matching process is both fast and reliable.
