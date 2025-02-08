# Writing Text to a File

## Description 📝

This Python program reads a line of text from the user and writes it to a file named `output.txt` in the same folder as the executable. The function `write_data_to_file(file_name, data)` is responsible for writing the input data to the specified file.

## Purpose 🎯

The purpose of this program is to demonstrate how to handle file operations in Python. Specifically, it shows how to write user input to a text file in the same directory as the executable program.

## How It Works 🔍

1. **Input**:
    - The user is prompted to enter a line of text.
2. **Processing**:
    - The program calls the `write_data_to_file(file_name, data)` function to write the input text to the file `output.txt`.
3. **Output**:
    - The program creates (or overwrites if it already exists) the `output.txt` file and writes the user's input into it.

## Output 📜

The program writes the user-provided text to a file named `output.txt`. If the file does not exist, it is created. If it already exists, it is overwritten with the new content.

### Example:

For the input:

```
Enter some text: Hello, world!
```

The output will be a file named `output.txt` containing:

```
Hello, world!
```

## Usage 📦

1. Save the code in a file, e.g., `write_to_file.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python write_to_file.py`
5. The program will prompt you to enter text, and it will save the text to the `output.txt` file.

## Conclusion 🚀

This program demonstrates how to handle basic file input/output in Python. It shows how to write user input to a file and manage text file creation.
