# Class Name Validator 📝

## Description 📝

This program validates class names for BEEGEEK school.
The class names follow a specific format consisting of:

-   A class number (a digit between 0 and 9).
-   A class letter (a letter between "A" and "P").

The program takes an integer `n` as input, followed by `n` class names, one per line.
For each class name, it outputs "YES" if the class name is valid and "NO" otherwise.

## Purpose 🎯

The purpose of this program is to check whether class names adhere to the correct format as described, ensuring that the class number is a digit from 0 to 9 and the class letter is a letter between 'A' and 'P'.

## How It Works 🔍

1. The program first reads the number `n`, which indicates the number of class names.
2. Then, it reads each class name and checks if it follows the valid format.
3. It prints "YES" if the class name is valid and "NO" if it is invalid.

### Example

```bash
Input: 3 5B 2Z 9P
Output: YES NO YES
```

### Explanation:

-   "5B" is valid: 5 is a valid class number and B is a valid class letter.
-   "2Z" is invalid: Z is not between "A" and "P".
-   "9P" is valid: 9 is a valid class number and P is a valid class letter.

## Usage 📦

1. Copy the program code into a Python script file (e.g., `class_name_validator.py`).
2. Run the script in your terminal or IDE.
3. Enter the number of class names to check.
4. Enter each class name on a new line.
5. The program will output whether each class name is valid ("YES") or invalid ("NO").

## Conclusion 🚀

This program ensures that all class names conform to the expected format, aiding in the validation of class names at BEEGEEK school.
It provides a simple and effective way to check multiple class names at once.
