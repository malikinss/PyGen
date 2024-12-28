# Strong Password Validator Program 🔐

## Description 📝

This Python program checks whether a password is strong based on the following criteria:

-   The password must be at least 8 characters long.
-   It must contain at least one uppercase letter.
-   It must contain at least one lowercase letter.
-   It must contain at least one digit.

## Purpose 🎯

The goal of this program is to validate if a password meets the security standards necessary for being considered strong. It can be used in applications where password strength is a concern, such as in user account creation or authentication processes.

## How It Works 🔍

1. **Function `is_password_good(password)`**:

    - It first checks if the length of the password is at least 8 characters.
    - Then, it iterates through the password string and checks if it contains at least one uppercase letter, one lowercase letter, and one digit.
    - If all the criteria are met, the function returns `True`. Otherwise, it returns `False`.

2. **Example**:
    - For the input `Password123`, the function returns `True`.
    - For the input `password`, the function returns `False` because it does not contain an uppercase letter or a digit.
    - For the input `Pass123`, the function returns `True` as it meets all the conditions.

## Usage 📦

1. Copy the code into a Python file, e.g., `password_validator.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python password_validator.py
    ```
5. Enter a password when prompted. The program will check if the password is strong and display the result.

## Conclusion 🚀

This password validation function helps ensure that users create strong passwords by enforcing the most common security rules.
It can be easily integrated into any system requiring password strength validation.
