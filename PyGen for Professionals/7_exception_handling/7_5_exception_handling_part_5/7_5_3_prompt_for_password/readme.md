# Password Validator (Prompt Until Success)

## Description 📝

This program repeatedly prompts the user for a password until a valid one is entered.
A valid password must meet the following criteria:

-   At least 9 characters long.
-   Contains both uppercase and lowercase letters.
-   Contains at least one digit.

The program outputs error messages based on the type of failure:

-   **LengthError** if the password is shorter than 9 characters.
-   **LetterError** if the password contains no letters or all letters have the same case.
-   **DigitError** if the password does not contain any digits.
-   **Success!** if the password meets all the criteria.

## Purpose 🎯

The purpose of this program is to ensure that the user enters a password that meets the required security standards by validating its length, letter case, and the presence of digits.
It will continuously request a password until the user provides a valid one.

## How It Works 🔍

1. The program enters a loop and requests the user to input a password.
2. The password is checked against the following criteria:
    - Length: At least 9 characters.
    - Case: Both uppercase and lowercase letters are required.
    - Digit: At least one digit is required.
3. If the password fails any check, the corresponding error message is displayed.
4. The program stops prompting once a valid password is entered and prints "Success!".
5. The program exits, and no further passwords are requested.

## Output 📜

-   For an invalid password:
    -   **LengthError**: If the password is too short.
    -   **LetterError**: If the password does not contain both uppercase and lowercase letters.
    -   **DigitError**: If the password lacks digits.
-   **Success!**: When a valid password is entered.

## Usage 📦

1. Run the program.
2. Enter a password when prompted.
3. If the password is invalid, the program will display the appropriate error message.
4. Once a valid password is entered, the program will print "Success!" and stop.

### Example:

```bash
Enter password: abc123
LengthError

Enter password: ABCdefg
LetterError

Enter password: Abcdefgh
DigitError

Enter password: Abcdefgh1
Success!
```

## Conclusion 🚀

The program ensures that users set a strong password by validating it according to security requirements.
By prompting the user until a valid password is entered, it guarantees that a secure password is eventually chosen.
