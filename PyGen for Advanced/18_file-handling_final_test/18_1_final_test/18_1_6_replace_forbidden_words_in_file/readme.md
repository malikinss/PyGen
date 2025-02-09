# Forbidden Words Filter

## Description 📝

This Python program reads a text file and replaces all forbidden words with asterisks (\*), where the number of asterisks matches the length of the forbidden word.
The forbidden words are listed in a separate file (`forbidden_words.txt`).

## Purpose 🎯

The program is designed to censor specified words in a given text file, ensuring that they are masked regardless of their case or position within other words.

## How It Works 🔍

1. **Load Forbidden Words**:

    - Reads a list of forbidden words from `forbidden_words.txt`.
    - All forbidden words are assumed to be in lowercase.

2. **Process the Text File**:

    - The user inputs the name of the file to be processed.
    - The program reads the file line by line.

3. **Word Replacement**:

    - Uses regular expressions to find and replace forbidden words.
    - Matches words regardless of case (e.g., `exam`, `Exam`, `EXAM` → `****`).
    - Even partial matches inside other words are replaced (e.g., `example` → `****ple`).

4. **Display the Censored Text**:
    - The modified text is printed to the console.

## Output 📜

### Example

#### **Input (`forbidden_words.txt`)**

```
exam test
```

#### **Input (`input.txt`)**

```
The final Exam is tough.
This is a test case.
The textbook contains examples.
```

#### **Output**

```
The final **** is tough.
This is a **** case.
The textbook contains ****ples.
```

## Usage 📦

1. Save the script as `forbidden_words_filter.py`.
2. Create a file named `forbidden_words.txt` and list the forbidden words.
3. Place the target text file in the same directory.
4. Open a terminal or command prompt.
5. Navigate to the script's directory.
6. Run the script using:
    ```bash
    python forbidden_words_filter.py
    ```
7. Enter the name of the file to be processed when prompted.

## Conclusion 🚀

This script provides an efficient way to filter and censor words in a text file.
It ensures case-insensitive matching and replaces words with the correct number of asterisks.
