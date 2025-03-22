# BEEGEEK Login Validation

## Description 📝

This program checks whether each input string represents a valid login for the BEEGEEK online school. A valid login must adhere to the following format:

1. The login starts with an underscore (`_`).
2. It is followed by one or more digits.
3. After the digits, there may be zero or more Latin letters (uppercase or lowercase).
4. The login may optionally end with an underscore (`_`).

## Purpose 🎯

The purpose of this program is to validate a list of strings to determine if they represent valid logins for the BEEGEEK online school, ensuring that only correctly formatted logins are accepted.

## How It Works 🔍

1. **Input**:

    - The program receives multiple login attempts, each on a separate line.

2. **Validation**:

    - A **regular expression** is used to match the login format:
        - Starts with an underscore (`_`).
        - Contains one or more digits (`\d+`).
        - Optionally followed by Latin letters (`a-zA-Z*`).
        - Optionally ends with an underscore (`_?`).

3. **Output**:
    - For each login attempt, the program prints `True` if the login is valid, or `False` if it does not match the expected format.

## Output 📜

### Example Input:

```text
_123abc_
_123_
_abc123
_45_X_
```

### Example Output:

```text
True
True
False
False
```

## Usage 📦

1. Save the program in a Python file (e.g., `login_validator.py`).
2. Run the script.
3. Enter login attempts, one per line.
4. The program will output `True` for valid logins and `False` for invalid ones.

## Conclusion 🚀

This program ensures that all login attempts conform to the BEEGEEK online school's format, making it easier to validate logins for users.
The regular expression provides a robust way to handle various login formats while maintaining simplicity.
