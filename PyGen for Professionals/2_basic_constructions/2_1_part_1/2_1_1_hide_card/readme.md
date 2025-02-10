# Hide Card Number

## Description 📝

This program implements the `hide_card()` function, which takes a string representing a bank card number.
The function hides the first 12 digits of the card number with asterisks (`*`), leaving the last 4 digits visible.
Any space characters between the digits are removed before processing.

## Purpose 🎯

The purpose of this function is to securely hide the first 12 digits of a bank card number while keeping the last 4 digits visible, which is commonly done in many applications for security reasons.

## How It Works 🔍

1. The function removes any space characters from the provided card number.
2. It ensures the card number is exactly 16 digits long.
3. It replaces the first 12 digits with asterisks (`*`) and keeps the last 4 digits visible.
4. If the card number is not exactly 16 digits or contains any non-digit characters, the function raises a `ValueError`.

## Output 📜

-   The card number with the first 12 digits replaced by asterisks and the last 4 digits preserved.
-   If the card number is not valid (not 16 digits or contains non-numeric characters), it raises a `ValueError`.

## Usage 📦

1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Call the `hide_card()` function with a string representing a valid 16-digit bank card number.

Example:

```python
card_number = "1234 5678 9012 3456"
result = hide_card(card_number)
print(result)  # Output: ************3456
```

## Conclusion 🚀

The `hide_card()` function provides a simple and secure way to hide sensitive bank card information while retaining the last 4 digits for identification or verification purposes.
