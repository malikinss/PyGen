# Total Unique Characters Counter Program 🔠

## Description 📝

This program calculates and prints the total number of unique characters across multiple words, ignoring case differences.
It combines all input words, normalizes them to lowercase, and uses a set to extract and count unique characters.

## Purpose 🎯

-   Aggregate unique characters from all words provided by the user.
-   Ensure case insensitivity by treating uppercase and lowercase as the same character.

## How It Works 🔍

1. **Function `count_unique_characters_in_all_words`**:

    - Takes an integer `n` as input (number of words).
    - Iterates `n` times to read `n` words from the user.
    - Concatenates all words into a single string, converting each to lowercase.
    - Creates a set of the combined string to filter out duplicate characters.
    - Returns the size of the set, representing the number of unique characters.

2. **Main Execution**:
    - Reads the number of words `n`.
    - Calls the function and prints the result.

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
10
```

-   Combined string: `helloworldpython`
-   Unique characters: `h, e, l, o, w, r, d, p, y, n` (10)

## Output 📜

-   A single integer representing the total number of unique characters across all words.

## Usage 📦

1. Run the program.
2. Enter the number of words (`n`).
3. Input each word.
4. The program will print the total count of unique characters.

## Conclusion 🚀

This program efficiently counts unique characters from multiple words, ensuring case insensitivity, by utilizing Python sets.
It's a simple yet powerful example of character aggregation and processing.
