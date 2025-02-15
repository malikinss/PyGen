# Reverse Characters in Input Lines

## Description 📝

This Python program reads multiple lines of text from the user, reverses the characters in each line, and outputs them in the same order as they were entered.
It helps in manipulating text input by reversing each line, maintaining the original input order.

## Purpose 🎯

The program takes user input, processes each line by reversing the characters, and prints the reversed lines in the order they were provided.
This is useful for text manipulation tasks where the reversal of individual characters is required.

## How It Works 🔍

1. **Function `reversed_words_in_input()`**:

    - It reads all lines of input using `sys.stdin`.
    - Strips unnecessary whitespace from the input.
    - Reverses each line and outputs it in the same order as it was entered.

2. **Key Operations**:
    - The function reads all input lines and stores them in a list.
    - It then reverses each line by slicing the string in reverse order `row[-1::-1]`.
    - Each reversed line is printed to the standard output.

### Example:

For input:

```
hello
world
```

The output will be:

```
olleh
dlrow
```

If no input is given, the program outputs nothing.

## Output 📜

The program prints each line of text with the characters reversed.

Example output:

```
olleh
dlrow
```

## Usage 📦

1. Save the code in a file named `reverse_input.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script.

### Example usage:

```bash
$ python reverse_input.py
hello
world
```

## Conclusion 🚀

This program is a simple yet effective tool for reversing characters in each line of input.
It maintains the order of lines, but the characters within each line are reversed.
Perfect for text manipulation tasks or learning basic string operations in Python.
