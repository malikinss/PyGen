# Password Verification

## Description 📝

This Python script defines the `verification()` function, which checks whether the provided password meets specific criteria.
The function verifies if the password contains at least one uppercase Latin letter, one lowercase Latin letter, and one digit.
Depending on the validation outcome, it calls either the success or failure function.

## Purpose 🎯

The purpose of this program is to demonstrate how to validate user passwords against defined rules.
It showcases the use of string operations and conditional checks to ensure the password meets specific security requirements.

## How It Works 🔍

1. **Arguments**: The function takes four arguments:
    - `login`: The user's login (a string).
    - `password`: The user's password (a string).
    - `success`: A function that is called if the password is correct.
    - `failure`: A function that is called if the password does not meet the criteria.
2. **Password Checks**: The function performs a series of checks to ensure:
    - The password contains at least one Latin letter (uppercase or lowercase).
    - The password contains at least one uppercase Latin letter.
    - The password contains at least one lowercase Latin letter.
    - The password contains at least one digit.
3. **Error Messages**: If any condition is not met, the failure function is called with an appropriate error message. The error message priorities are:
    - "The password does not contain any letters"
    - "The password does not contain any uppercase letters"
    - "The password does not contain any lowercase letters"
    - "The password does not contain any digits"
4. **Success**: If all conditions are satisfied, the success function is called with the login.

## Output 📜

The function does not return anything but calls either the `success()` or `failure()` function:

-   If the password is correct, the `success()` function is called with the login.
-   If the password is incorrect, the `failure()` function is called with the login and an error message.

Example:

```
failure(login, 'в пароле нет ни одной заглавной буквы')
```

## Usage 📦

1. Save the code to a file named `password_verification.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Call the `verification()` function with the required arguments:
    ```python
    verification(
        login="user123",
        password="Password1",
        success=lambda login: print(f"Welcome, {login}!"),
        failure=lambda login, error_message: print(f"Error for {login}: {error_message}")
    )
    ```

## Conclusion 🚀

This program provides a simple and effective way to validate user passwords against common security rules.
It can be easily extended or integrated into larger authentication systems to improve password security.
