# Print All Lowercase Latin Letters 🅰️

## Description 📝

The program outputs all lowercase Latin letters from 'a' to 'z', each printed on a separate line.
It demonstrates different approaches to achieve this:

1. Using the `ord()` and `chr()` functions to convert between Unicode code points and characters.
2. Using the `ascii_lowercase` constant from the `string` module.
3. Using unpacking with a newline separator to print the letters in a single call.

## Purpose 🎯

This program is designed to:

-   Demonstrate different ways to iterate through lowercase Latin letters.
-   Utilize built-in functions and modules in Python such as `ord()`, `chr()`, and `ascii_lowercase`.
-   Show how to print each letter on a new line, utilizing multiple methods.

## How It Works 🔍

### 1. **Using `ord()` and `chr()`**:

-   The `ord()` function is used to get the Unicode code point of the letter 'a', and similarly for 'z'.
-   The `chr()` function is then used to convert these Unicode code points back into characters.
-   A loop iterates from the Unicode code point of 'a' to 'z', printing each corresponding character.

### 2. **Using `ascii_lowercase`**:

-   The `ascii_lowercase` constant, which contains all lowercase Latin letters, is imported from the `string` module.
-   A simple loop is used to iterate over this constant and print each letter on a new line.

### 3. **Using Unpacking with Newline Separator**:

-   The unpacking operator `*` is used to unpack the `ascii_lowercase` string.
-   The `sep='\n'` argument ensures that each letter is printed on a new line.

## Usage 📦

1. **Call the function `print_lowercase_letters()`**.
    - No arguments are needed.
2. Example usage:

    ```python
    print_lowercase_letters()
    ```

3. The function will print all lowercase Latin letters, one per line, using three different methods.

## Conclusion 🚀

This program demonstrates the versatility of Python’s built-in functions and modules for handling common tasks such as printing characters.
It shows how to use `ord()`/`chr()` conversion, predefined constants like `ascii_lowercase`, and basic unpacking techniques to efficiently solve the problem of printing all lowercase Latin letters.
