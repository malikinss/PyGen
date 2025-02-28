# Password Validator (EAFP Style)

## Description 📝

This program checks if a given password is "good" based on specific criteria:

-   The password must be at least 9 characters long.
-   It must contain both uppercase and lowercase letters.
-   It must contain at least one digit.

The `is_good_password()` function implements the EAFP (Easier to Ask for Forgiveness than Permission) approach, where exceptions are raised if any condition is violated.

## Purpose 🎯

The function `is_good_password()` aims to validate the strength of a password by raising appropriate exceptions when the password doesn't meet the required criteria. This is useful in enforcing strong password rules for security purposes.

## How It Works 🔍

1. The function takes a password string as input.
2. It checks:
    - If the password has at least 9 characters. If not, it raises a `LengthError`.
    - If the password contains both uppercase and lowercase letters. If not, it raises a `LetterError`.
    - If the password contains at least one digit. If not, it raises a `DigitError`.
3. If the password passes all checks, the function returns `True`.
4. If any condition is violated, the respective exception is raised.

## Output 📜

-   Returns `True` if the password meets all criteria.
-   Raises the following exceptions if any criteria are violated:
    -   `LengthError`: If the password is shorter than 9 characters.
    -   `LetterError`: If the password lacks either uppercase or lowercase letters.
    -   `DigitError`: If the password contains no digits.

## Usage 📦

1. Provide a password string to the function `is_good_password()`.
2. The function will return `True` if the password is good, or raise an exception if any conditions are violated.

### Example:

```python
try:
    print(is_good_password("Password123"))  # True
    print(is_good_password("short1"))       # Raises LengthError
    print(is_good_password("alllowercase1"))  # Raises LetterError
    print(is_good_password("ALLUPPERCASE1"))  # Raises LetterError
    print(is_good_password("Password"))  # Raises DigitError
except PasswordError as e:
    print(f"Password validation failed: {e}")
```

## Conclusion 🚀

The `is_good_password()` function is a robust solution for validating password strength.
By using the EAFP style, it handles errors effectively, providing clear messages for what needs to be fixed when a password doesn't meet security standards.
