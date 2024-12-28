# Phone Number Validation Program

## Description 📝

This Python program checks if an input string is a valid phone number.
The program determines whether the phone number follows one of the two valid formats:

-   `abc-def-hijk`
-   `7-abc-def-hijk`

Where each character (`a`, `b`, `c`, `d`, `e`, `f`, `h`, `i`, `j`, `k`) is a digit from `0` to `9`.

## Purpose 🎯

-   To validate phone numbers based on specific format rules.
-   To demonstrate the use of string manipulation and conditional statements in Python.

## How It Works 🔍

1. **Function `is_valid_phone_number`**:

    - The function takes a string `phone` as input and splits it by the hyphen (`-`) into a sequence of parts.
    - It checks if the parts conform to the valid format by verifying their lengths and ensuring that all characters are digits.
    - The function returns `"YES"` if the phone number is valid, and `"NO"` otherwise.

2. **Phone Number Format Check**:
    - The program checks two formats:
        - Format `abc-def-hijk`, where there are three parts: 3 digits, 3 digits, and 4 digits.
        - Format `7-abc-def-hijk`, where the first part must be `7`, followed by 3 digits, 3 digits, and 4 digits.
3. **Validation**:
    - The function checks the lengths of the parts and verifies if all characters are digits using `isdigit()`.
4. **Output**:
    - If the number matches one of the valid formats, the program prints `"YES"`. Otherwise, it prints `"NO"`.

## Output 📜

The program prints `"YES"` if the phone number is valid, and `"NO"` if it is not.

**Example 1**:

```
Input:
123-456-7890

Output:
YES
```

**Example 2**:

```
Input:
7-123-456-7890

Output:
YES
```

**Example 3**:

```
Input:
123-45-6789

Output:
NO
```

## Usage 📦

1. Copy the code into a Python file, e.g., `phone_number_validation.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script by executing:
    ```bash
    python phone_number_validation.py
    ```
5. Enter a phone number string.
6. View the result: the program will print `"YES"` for a valid phone number and `"NO"` for an invalid one.

## Conclusion 🚀

This program efficiently checks the validity of phone numbers according to specific format rules.
It is a great way to practice string manipulation and condition checking in Python. 🎉
