# Display Words in a Column

## Description 📝

This Python program takes a line of text containing words, splits the text into individual words, and prints each word on a separate line.
The words are displayed in a column format.

## Purpose 🎯

-   To practice splitting a string into individual words.
-   To demonstrate how to handle user input and display the output in a specific format.
-   To work with **string manipulation** and **iterating over collections** in Python.

## How It Works 🔍

1. **Function `print_words_in_column`**:

    - Accepts the input text (`text`) which is a string.
    - Splits the string into a list of words using the `split()` method.
    - Prints each word on a new line using the `print(*words, sep='\n')` statement. The `*` operator unpacks the list of words, and the `sep='\n'` argument makes sure each word appears on a separate line.

2. **Function `main`**:
    - Prompts the user to input a line of text using `input()`.
    - Calls the `print_words_in_column` function to process the input and print each word on a new line.

## Output 📜

The words from the input string are printed in a column format, one word per line.

**Example**:

```
Enter a line of text: Hello world, this is Python
Hello
world,
this
is
Python
```

## Usage 📦

1. Copy the code into a Python file, e.g., `words_in_column.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python words_in_column.py
    ```
5. Enter a line of text when prompted.
6. View the words printed in a column.

## Conclusion 🚀

This simple program demonstrates how to manipulate text and print its components in a readable format.
It’s an excellent exercise for beginners to learn about string manipulation, list handling, and formatted output in Python. 🎉
