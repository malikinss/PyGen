# Unique Words Counter Program 📝

## Description 📝

This program determines the total number of different words in a line of text.
It ignores punctuation marks (.,;:-?!) and considers words case-insensitively.
Words are defined as sequences of non-space characters, and the program handles cases where multiple spaces separate words.

## Purpose 🎯

-   Clean and count unique words in a given text.
-   Remove punctuation and ensure case-insensitivity when counting words.

## How It Works 🔍

1. **Function `count_different_words`**:
    - Takes a line of text as input.
    - Converts the text to lowercase and splits it into words based on spaces.
    - Strips punctuation marks from each word.
    - Uses a set to find the unique words (since sets automatically remove duplicates).
    - Returns the number of unique words.

### Example:

**Input**:

```
Hello, world! Hello again; world?
```

**Output**:

```
3
```

-   After cleaning: `hello`, `world`, `again`
-   Unique words: 3

## Output 📜

-   A single integer representing the number of different unique words in the text.

## Usage 📦

1. Run the program.
2. Enter a line of text containing words.
3. The program will print the total number of different words.

## Conclusion 🚀

This program efficiently counts the number of unique words in a string of text, ignoring punctuation and ensuring case-insensitivity.
It uses Python’s string handling and set features to clean and count words, making it a straightforward solution to word counting problems.
