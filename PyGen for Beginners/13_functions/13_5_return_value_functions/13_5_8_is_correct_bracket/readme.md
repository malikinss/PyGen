# Correct Bracket Sequence Validator 🎯

## Description 📝

This program checks whether a given string consisting of the characters `(` and `)` forms a correct bracket sequence.
A valid sequence must have matching opening and closing brackets, and each opening bracket must appear before its corresponding closing bracket.

## Purpose 🎯

The function `is_correct_bracket()` is designed to validate a bracket sequence.
It returns `True` if the sequence is correct, i.e., it has balanced and properly nested brackets, and `False` otherwise.

## How It Works 🔍

1. **Function `is_correct_bracket(text)`**:
    - Initializes a `balance` variable to track the count of unmatched opening brackets.
    - Iterates over each character in the string:
        - Increases `balance` for each opening bracket `(`.
        - Decreases `balance` for each closing bracket `)`.
    - If `balance` ever becomes negative, it means there is a closing bracket without a matching opening bracket, and the function immediately returns `False`.
    - After checking all characters, if `balance` equals 0, the sequence is correct, meaning every opening bracket has a matching closing bracket.

## Usage 📦

1. Copy the code into a Python file, e.g., `bracket_sequence_validator.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python bracket_sequence_validator.py
    ```
5. Enter a string of brackets to check if the sequence is correct.

    - Example 1: `()()` will return `True` because the sequence has matching brackets.
    - Example 2: `())(` will return `False` because the sequence has an unmatched closing bracket.

## Conclusion 🚀

This program ensures that only valid bracket sequences are accepted, making it useful for validating input in scenarios involving structured data or balanced expressions.
