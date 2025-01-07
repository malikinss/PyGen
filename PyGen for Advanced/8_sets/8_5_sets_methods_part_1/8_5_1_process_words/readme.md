# Unique Character Counter Program 🔤

## Description 📝

This program reads multiple words from user input and prints the number of unique characters in each word, ignoring case differences. It leverages Python sets to filter out duplicates, ensuring accurate counting of distinct characters.

## Purpose 🎯

-   Calculate the number of unique letters in each word.
-   Ensure case insensitivity by treating uppercase and lowercase letters as the same.

## How It Works 🔍

1. **Function `count_unique_characters`**:

    - Converts the word to lowercase using `.lower()`.
    - Uses `set()` to collect unique characters.
    - Returns the size of the set.

2. **Function `process_words`**:

    - Accepts an integer `n` representing the number of words.
    - Repeatedly reads `n` words from input.
    - Calls `count_unique_characters` for each word and prints the result.

3. **Main Execution**:
    - The program starts by reading the total number of words `n`.
    - Each word is processed, and the number of unique characters is printed.

### Example:

**Input**:

```
3
Hello
World
Python
```

**Output**:

```
4
5
6
```

-   "Hello" ➝ Unique characters: `h, e, l, o` (4)
-   "World" ➝ Unique characters: `w, o, r, l, d` (5)
-   "Python" ➝ Unique characters: `p, y, t, h, o, n` (6)

## Output 📜

-   The program prints one integer per line, representing the unique character count for each word.

## Usage 📦

1. Run the program.
2. Enter the number of words (`n`).
3. Input each word one by one.
4. The program will print the unique character count for each word.

## Conclusion 🚀

This program provides a quick and efficient way to calculate unique character counts for multiple words, with case insensitivity, using simple Python concepts.
It's a practical example of using sets for character uniqueness.
