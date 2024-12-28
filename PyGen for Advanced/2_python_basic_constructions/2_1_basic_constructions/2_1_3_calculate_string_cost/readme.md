# String Cost Calculator 💰

## Description 📝

This Python program calculates the cost of a given string, where each character (including spaces) costs 50 cents.
The program computes the total cost and presents it in dollars and cents.

## Purpose 🎯

The program allows users to estimate the cost of a string based on the number of characters, making it useful for applications where text length has a pricing structure, such as SMS or printing services.

## How It Works 🔍

1. **Input Format**:
    - The user is asked to input a line of text.
2. **Function Logic**:

    - Each character, including spaces, is charged 50 cents.
    - The total cost is calculated by multiplying the number of characters in the string by 50.
    - The result is then converted into dollars and cents.

3. **Example**:
    ```
    Enter the text: Hello, world!
    Output:
    1 dollars 50 cents
    ```
4. **Edge Cases**:
    - The program works for any length of string, including empty strings.
    - Handles spaces as valid characters.

## Usage 📦

1. Copy the code into a Python file, e.g., `string_cost_calculator.py`.
2. Run the script in the terminal:
    ```bash
    python string_cost_calculator.py
    ```
3. Enter your string when prompted.
4. The program will output the cost of the string in dollars and cents.

## Conclusion 🚀

This simple calculator helps estimate the financial cost of a string based on its length, with each character incurring a fixed cost.
It's a useful tool for various pricing scenarios involving text.
