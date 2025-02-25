# Month Name Finder

## Description 📝

This program reads an integer input from the user representing a month number and outputs the corresponding full name of the month in English.
If the input is invalid or out of range, it displays an appropriate error message.

## Purpose 🎯

The purpose of this program is to demonstrate how to handle user input, perform basic integer validation, and return corresponding data from the `calendar` module in Python.

## How It Works 🔍

1. The program prompts the user for a numeric input.
2. It checks if the input is an integer and within the valid range of 1 to 12.
3. If valid, it returns the full name of the month using the `month_name` attribute from the `calendar` module.
4. If the input is not a valid integer, it outputs an error message: `"The entered value is incorrect"`.
5. If the input integer is outside the valid range of 1 to 12, it outputs: `"The entered number is from an invalid range"`.

## Output 📜

The program will print either the corresponding month's full name or an error message:

-   A valid month number (e.g., `5`) will output `"May"`.
-   An invalid number (e.g., `15`) will output `"The entered number is from an invalid range"`.
-   A non-numeric input (e.g., `"abc"`) will output `"The entered value is incorrect"`.

## Usage 📦

1. Run the program.
2. Input a number between 1 and 12, or any other string.
3. Observe the output based on the validation:
    - If a valid month number is entered, the program outputs the month name.
    - If the entered value is out of range, the program informs you of the error.
    - If a non-numeric value is entered, the program handles the error and displays the appropriate message.

Example:

```python
# Input: 5
# Output: May

# Input: 15
# Output: The entered number is from an invalid range

# Input: abc
# Output: The entered value is incorrect
```

```

## Conclusion 🚀

This program efficiently handles user input, validates the input, and provides informative error messages when necessary.
It is a simple demonstration of using `try-except` constructs for input validation and working with Python’s `calendar` module.
```
