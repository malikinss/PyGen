# Full Name Initials Printer Program 🎨

## Description 📝

This Python program takes a person's full name, which includes their first name (`name`), surname (`surname`), and patronymic (`patronymic`), and prints out the initials of the full name in uppercase letters. The initials are derived from the first letter of each component.

## Purpose 🎯

-   To print the initials of a person's full name in uppercase.
-   The program ensures that each initial is capitalized, regardless of the case of the input.

## How It Works 🔍

1. **Function `print_fio(name, surname, patronymic)`**:

    - Takes three input parameters:

        - `name` (str): The first name of the person.
        - `surname` (str): The surname of the person.
        - `patronymic` (str): The patronymic of the person.

    - The function then:
        - Extracts the first letter from each parameter (`name`, `surname`, and `patronymic`).
        - Converts the letters to uppercase using the `.upper()` method.
        - Prints the concatenated initials as a single string.

2. **Example**:
   For the inputs:
    ```
    name = "ivan"
    surname = "petrov"
    patronymic = "ivanovich"
    ```
    The output will be:
    `"IPI"`

## Usage 📦

1. Copy the code into a Python file, e.g., `print_initials.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python print_initials.py
    ```
5. Input the first name, surname, and patronymic when prompted, and the initials will be printed in uppercase.

## Conclusion 🚀

This program effectively demonstrates the use of string manipulation to print initials in uppercase, making it a simple yet powerful utility for handling full names.
It can be further extended to handle more complex formatting or name structures.
