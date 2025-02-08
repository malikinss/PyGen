# Password Strength Checker 🔐

## Description 📝

This program checks if the entered password meets specific criteria for being considered "strong." The password must have a minimum length of 7 characters and contain at least one uppercase letter, one lowercase letter, and one digit. It uses the built-in `any()` function to efficiently check these conditions.

## Purpose 🎯

The purpose of this program is to validate the strength of a password by ensuring it adheres to commonly accepted security standards, including length and character variety.

## How It Works 🔍

1. **Input**: The user enters a password string.
2. **Check**: The `is_password_strong()` function checks:
    - The password's length is at least 7 characters.
    - The password contains at least one uppercase letter, one lowercase letter, and one digit.
    - The `any()` function is used for each of the conditions to verify if the password contains the required character types.
3. **Output**: If the password meets all the criteria, the program prints `"YES"`, otherwise it prints `"NO"`.

## Output 📜

-   **YES** if the password is strong according to the criteria.
-   **NO** if the password does not meet the strength requirements.

### Example Output:

```
YES
```

## Usage 📦

1. Enter a password when prompted.
2. The program will output whether the password is strong enough based on the defined criteria.

## Conclusion 🚀

This program effectively determines the strength of a password by verifying its length and the presence of required character types using Python's built-in `any()` function. This makes it an efficient and simple solution for checking password strength.
