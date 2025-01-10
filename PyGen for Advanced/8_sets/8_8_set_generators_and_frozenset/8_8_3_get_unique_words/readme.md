# Extract Unique Words Program 📝

## Description 📝

This program processes a sentence to extract unique words in lowercase, ignoring punctuation marks.
The unique words are then printed in alphabetical order, space-separated.

## Purpose 🎯

The program is designed to clean and extract unique words from a sentence, convert them to lowercase, and display them in alphabetical order.
It also handles punctuation removal to ensure that only words are considered.

## How It Works 🔍

1. **Input**:
    - A sentence with words that may include punctuation marks.
2. **Logic**:
    - Each word is cleaned to remove punctuation and converted to lowercase.
    - The cleaned words are then stored in a set, which automatically ensures uniqueness.
    - Finally, the words are sorted alphabetically and printed.
3. **Output**:
    - The program prints the unique words from the sentence, sorted alphabetically, on a single line with each word separated by a space.

### Example:

**Input**:

```python
"My very photogenic mother died in a freak accident (picnic, lightning) when I was three..."
```

**Output**:

```
a accident died freak in lightning mother picnic photogenic three very was when
```

## Output 📜

-   A single line containing the unique words, sorted alphabetically, space-separated.

## Usage 📦

1. Run the program.
2. The program will process the sentence and output the unique words sorted alphabetically.

## Conclusion 🚀

This program efficiently processes a sentence to extract unique words, cleans them of punctuation, and prints them in a sorted and user-friendly format.
