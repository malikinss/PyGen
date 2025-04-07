# PhoneNumber Class Contact Formatter

## Description 📝

The `PhoneNumber` class represents a ten-digit phone number, accepting it as a string in either 'dddddddddd' or 'ddd ddd dddd' format.
It normalizes the input by removing spaces and provides a formal string representation via `__repr__` as `PhoneNumber('<dddddddddd>')` and an informal one via `__str__` as `(ddd) ddd-dddd`.

## Purpose 🎯

This class is designed for managing phone number data, suitable for contact management systems, educational examples of string formatting, or applications needing standardized phone number displays.

## How It Works 🔍

-   **Initialization**: The `__init__` method takes a `phone_number` string, removes any spaces, and stores it as `self.phone_number`.
-   ****repr**() Method**: Returns the formal string `PhoneNumber('<dddddddddd>')` using the stored number.
-   ****str**() Method**: Formats the number into `(ddd) ddd-dddd` by splitting it into region (first 3 digits), first three (next 3), and last four (final 4), then joining with appropriate separators.

## Usage 📦

1. Save the class in a Python file, e.g., `phone_number.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the class:

```python
from phone_number import PhoneNumber
phone1 = PhoneNumber("1234567890")
phone2 = PhoneNumber("123 456 7890")
print(phone1)
print(repr(phone2))
```

## Conclusion 🚀

The `PhoneNumber` class offers a simple and effective way to handle ten-digit phone numbers in Python, with distinct formal and informal string outputs.
Its design is flexible and can be extended with features like validation or alternative formats for more complex telephony applications.
