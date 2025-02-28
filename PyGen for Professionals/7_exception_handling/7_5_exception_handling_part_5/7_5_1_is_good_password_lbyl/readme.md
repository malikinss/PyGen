# Password Validator

## Description 📝

This program checks whether a given password is "good" based on specific criteria.
A good password must:

-   Be at least 9 characters long
-   Contain both uppercase and lowercase letters
-   Contain at least one digit

The function `is_good_password()` evaluates a password string and returns `True` if it satisfies all conditions, otherwise it returns `False`.

## Purpose 🎯

The `is_good_password()` function aims to validate the strength of a password by ensuring it meets basic security requirements.

## How It Works 🔍

1. The function takes a password as input.
2. It checks:
    - If the password is at least 9 characters long.
    - If it contains both uppercase and lowercase letters.
    - If it contains at least one digit.
3. If any of the conditions are not met, the function returns `False`.
4. If all conditions are satisfied, it returns `True`.

## Output 📜

-   Returns `True` if the password meets the required criteria.
-   Returns `False` if any of the criteria are not met.

## Usage 📦

1. Provide a password string as input to the function `is_good_password()`.
2. The function will return `True` or `False` based on the password validity.

### Example:

```python
print(is_good_password("Password123"))  # True
print(is_good_password("short1"))       # False
print(is_good_password("alllowercase1"))  # False
print(is_good_password("ALLUPPERCASE1"))  # False
```

## Conclusion 🚀

This function helps validate password strength, ensuring it meets essential security requirements such as length, character case, and the inclusion of digits.
