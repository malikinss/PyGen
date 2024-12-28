# Youth Jargon Converter Program

## Description 📝

This Python program converts each word of the input text into "youth jargon." The conversion follows a simple rule where:

-   The first letter of each word is removed and placed at the end of the word.
-   The syllable "ki" is added to the end of the word.

## Purpose 🎯

-   To demonstrate string manipulation in Python.
-   To apply list expressions for transforming each word in the text.
-   To showcase how text can be manipulated and transformed to match a given pattern.

## How It Works 🔍

1. **Function `convert_to_youth_jargon`**:

    - The function splits the input string into a list of words.
    - It processes each word by:
        - Removing the first letter.
        - Moving the first letter to the end of the word.
        - Appending the syllable "ki" to the end of the word.
    - The function returns a list of words transformed into youth jargon.

2. **Processing**:

    - The input string is split into words.
    - Each word is manipulated according to the specified rules.
    - The transformed words are returned as a list.

3. **Output**:
    - The program prints the transformed string with each word in youth jargon.

## Output 📜

The program outputs each word from the input text converted into youth jargon, with the words separated by spaces.

**Example 1**:

```
Input:
Hello world

Output:
elloHki orldwki
```

**Example 2**:

```
Input:
Python is great

Output:
ythonPki si kireatgki
```

## Usage 📦

1. Copy the code into a Python file, e.g., `youth_jargon_converter.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python youth_jargon_converter.py
    ```
5. Enter a string of text when prompted.
6. View the output: the program will print the text in youth jargon.

## Conclusion 🚀

This program is a fun example of string manipulation and list expressions.
It takes a standard string and transforms it into a unique "youth jargon" format, showcasing Python's flexibility in text processing. 🎉
