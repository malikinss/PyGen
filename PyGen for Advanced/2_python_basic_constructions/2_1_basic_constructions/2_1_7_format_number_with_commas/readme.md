# Format Number with Commas Program 💰

## Description 📝

This program takes a natural number as input and formats it by inserting commas at appropriate places according to the standard American convention for large numbers.
This makes it easier to read large numbers, following the common format of separating every three digits by commas.

## Purpose 🎯

The program is designed to improve the readability of large natural numbers by inserting commas in the appropriate places, making the numbers easier to comprehend, especially when dealing with financial figures, population counts, or other large data.

## How It Works 🔍

1. **Input Format**:

    - The user is prompted to enter a natural number.

2. **Logic**:

    - The program converts the number into a string and processes it from the end, adding commas after every three digits.
    - It handles the remainder of the number that is less than three digits separately and then joins the formatted parts with commas.

3. **Example**:

    - **Input**: `123456789`
    - **Output**: `123,456,789`
    - **Explanation**: The program inserts commas into the number every three digits, starting from the right, to follow the American convention for large numbers.

4. **Edge Cases**:
    - The program correctly handles numbers with less than or equal to three digits by returning the number as is without any commas.
    - The program works for very large numbers as well, efficiently processing them in chunks of three digits.

## Usage 📦

1. Copy the code into a Python file, e.g., `format_number.py`.
2. Run the script in the terminal:
    ```bash
    python format_number.py
    ```
3. Enter the natural number when prompted.
4. The program will output the number formatted with commas.

## Conclusion 🚀

This program is a simple and efficient way to format large natural numbers with commas, making them more readable in various contexts such as finance, population statistics, and large data management.
