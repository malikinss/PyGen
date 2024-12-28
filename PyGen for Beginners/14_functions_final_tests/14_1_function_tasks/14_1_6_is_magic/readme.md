# Magic Date Checker 🔮

## Description 📝

This Python script determines whether a given date is "magic."
A magic date is defined as the date when the day multiplied by the month equals the last two digits of the year.
The function `is_magic` takes a string representation of the date in the format "DD.MM.YYYY" and returns `True` if the date is magic, or `False` otherwise.

## Purpose 🎯

The script provides an easy way to check if a given date satisfies the "magic" condition, which can be used in puzzles, fun date calculations, or games.

## How It Works 🔍

1. **Input Format**:
    - The user inputs a date in the format "DD.MM.YYYY" (e.g., "12.06.2024").
2. **Function Logic**:

    - The `is_magic` function splits the input string into the day, month, and year.
    - It then checks if the product of the day and the month equals the last two digits of the year.
    - If the condition is satisfied, it returns `True`, otherwise `False`.

3. **Example**:

    ```
    Enter date in DD.MM.YYYY format: 12.06.2024
    Output: True
    ```

4. **Edge Cases**:
    - Valid dates are assumed (e.g., no need to check for invalid dates like "31.02.2024").
    - Input should always be in the specified format.

## Usage 📦

1. Copy the code into a Python file, e.g., `magic_date.py`.
2. Run the script in the terminal:
    ```bash
    python magic_date.py
    ```
3. Enter a date in the "DD.MM.YYYY" format when prompted.
4. The script will print `True` if the date is magic, or `False` otherwise.

## Conclusion 🚀

This script offers a simple yet fun way to check for "magic" dates based on a mathematical condition involving the day, month, and year.
It is ideal for small projects and applications involving date-related logic.
