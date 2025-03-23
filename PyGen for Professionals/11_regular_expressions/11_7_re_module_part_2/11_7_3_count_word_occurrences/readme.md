# Word Occurrence Counter

## Description 📝

This program takes a **text string** and a **word** as input and counts how many times the **exact word** appears in the given text.

A word is considered a standalone entity, meaning it must be surrounded by **non-word characters** (like spaces or punctuation).

For example:

-   `"hello"` in `"hello world"` will be counted.
-   `"is"` in `"this is a test"` will be counted, but not as part of `"thisis"`.

The program uses **word boundaries** (`\b`) to ensure that the word is matched exactly.

## Purpose 🎯

This script is useful for counting **exact occurrences** of a word in a text, such as for **text analysis, document search, or keyword frequency analysis**.

## How It Works 🔍

1. **Reads input**:
    - First line: the text to search in.
    - Second line: the word to search for.
2. **Uses a regex pattern**: `\bword\b`
    - The word is matched exactly, considering boundaries.
3. **Prints the number of occurrences** of the word.

## Output 📜

### Example Input:

```text
hello world, this is a hello world test.
hello
```

### Example Output:

```text
2
```

Explanation: `"hello"` appears twice in the text, both times as a standalone word.

## Usage 📦

1. Save the script as `word_occurrence_counter.py`.
2. Run the script and enter:
    - A **text string** (first input).
    - A **word** (second input).
3. The output will be the number of occurrences of the word.

## Conclusion 🚀

This program helps efficiently count the **exact occurrences** of a word in a given text.
It is particularly useful for **keyword search, word frequency analysis, and linguistic studies** where exact word matches are needed.
