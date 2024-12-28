# Reverse Last Five Digits Program 🔄

## Description 📝

This program takes a five-digit or six-digit natural number as input and reverses the order of its last five digits.
The number can either have five or six digits, and the program will modify the last five digits accordingly.

## Purpose 🎯

The program is designed to manipulate numbers by reversing the last five digits.
This can be useful in various situations where such transformations are required, such as in coding challenges or cryptography.

## How It Works 🔍

1. **Input Format**:

    - The user is prompted to enter a five-digit or six-digit number.

2. **Logic**:
    - The program first converts the input number into a string for easy manipulation.
    - It checks the length of the number:
        - If the number has six digits, it reverses the last five digits and keeps the rest of the number unchanged.
        - If the number has five digits, it simply reverses the entire number.
3. **Example**:

    - **Input**: `123456`
    - **Output**: `123654`
    - **Explanation**: The last five digits (`23456`) are reversed to `65432`, resulting in `123654`.

4. **Edge Cases**:
    - The program handles both five-digit and six-digit numbers properly.

## Usage 📦

1. Copy the code into a Python file, e.g., `reverse_last_five.py`.
2. Run the script in the terminal:
    ```bash
    python reverse_last_five.py
    ```
3. Enter a five-digit or six-digit number when prompted.
4. The program will output the number with its last five digits reversed.

## Conclusion 🚀

This program provides a simple yet effective way to reverse the last five digits of a given natural number, making it useful for specific number manipulations in coding challenges or practical applications.
