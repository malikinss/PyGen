# Extract Short Words Program 📝

## Description 📝

This program processes a sentence to extract unique words that are less than 4 characters long, ignoring punctuation.
It then prints the result in lowercase and sorted alphabetically.

## Purpose 🎯

The goal is to identify and extract short words (less than 4 characters) from a sentence, clean them of punctuation, and output them in sorted order.
The output will contain only unique words.

## How It Works 🔍

1. **Input**:
    - A sentence with words that may contain punctuation marks.
2. **Logic**:
    - Each word is cleaned by removing punctuation and converting it to lowercase.
    - The words that are shorter than 4 characters are selected.
    - The resulting words are stored in a set to ensure uniqueness.
    - The set is sorted alphabetically and printed.
3. **Output**:
    - The program prints the unique short words from the sentence, sorted alphabetically, on a single line with each word separated by a space.

### Example:

**Input**:

```python
"My very photogenic mother died in a freak accident (picnic, lightning) when I was three..."
```

**Output**:

```
a and i in my of on or the
```

## Output 📜

-   A single line containing the unique words that are shorter than 4 characters, sorted alphabetically, space-separated.

## Usage 📦

1. Run the program.
2. The program will process the sentence and output the unique short words sorted alphabetically.

## Conclusion 🚀

This program effectively filters and processes short words from a sentence, providing an efficient and user-friendly output sorted alphabetically.
