# BEEGEEK Bank Password Validator 🏦

## Description 📝

This program validates a BEEGEEK bank password. A valid password follows the format `a:b:c`, where:

-   `a` must be a palindrome.
-   `b` must be a prime number.
-   `c` must be an even number.

## Purpose 🎯

The goal of this program is to verify whether a given password is valid for the BEEGEEK bank system. The password format is strictly defined and involves checking for mathematical properties of the numbers.

## How It Works 🔍

1. **Function `is_palindrome(text)`**:
    - Removes unwanted symbols like spaces, punctuation, and converts the text to lowercase.
    - Checks if the cleaned text is the same forward and backward.
2. **Function `is_even(num)`**:
    - Checks if the number is divisible by 2 to determine if it's even.
3. **Function `is_prime(num)`**:

    - Checks if a number is prime by dividing it by all numbers from 2 up to the square root of the number.

4. **Function `is_valid_password(password)`**:
    - Splits the password into three parts (`a`, `b`, `c`) based on the colon (`:`) separator.
    - Verifies that:
        - `a` is a palindrome.
        - `b` is a prime number.
        - `c` is an even number.
    - Returns `True` if all conditions are satisfied, `False` otherwise.

## Usage 📦

1. Copy the code into a Python file, e.g., `beegeek_password_validator.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python beegeek_password_validator.py
    ```
5. Enter a password in the format `a:b:c` when prompted.

    - Example 1: `121:5:8` will return `True` because `121` is a palindrome, `5` is a prime number, and `8` is even.
    - Example 2: `121:4:6` will return `False` because `4` is not prime.

## Conclusion 🚀

This program ensures that BEEGEEK bank passwords adhere to a strict format, making the password validation process secure and reliable.
