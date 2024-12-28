# Month Name Finder 🌍

## Description 📝

This Python script returns the name of a month in either Russian (`ru`) or English (`eng`) based on user input.
The function `get_month` takes two arguments: the desired language and the month number (1 to 12).

## Purpose 🎯

The script simplifies the process of retrieving month names in different languages, making it useful for localization, educational tools, or language learning applications.

## How It Works 🔍

1. **Month Lists**:

    - `month_ru` – Contains month names in Russian.
    - `month_eng` – Contains month names in English.

2. **Function Logic**:

    - The user specifies the language (`ru` or `eng`) and the month number.
    - The function selects the appropriate month from the corresponding list.
    - The selected month is printed as output.

3. **Example**:

    ```
    Enter language (ru or eng): ru
    Enter month number (1-12): 3
    Output: март
    ```

4. **Edge Cases**:
    - If the user enters an invalid month number (less than 1 or greater than 12), the program will raise an `IndexError`.
    - No input validation is currently implemented.

## Usage 📦

1. Copy the code into a Python file, e.g., `get_month.py`.
2. Run the script in the terminal:
    ```bash
    python get_month.py
    ```
3. Enter the language (`ru` or `eng`) and month number when prompted.
4. The name of the corresponding month is displayed.

## Conclusion 🚀

This script offers a simple and effective way to retrieve month names in different languages.
It leverages lists and basic conditionals to deliver accurate results quickly, making it a practical addition to any multilingual application.
