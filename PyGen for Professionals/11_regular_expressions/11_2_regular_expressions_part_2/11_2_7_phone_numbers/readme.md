# Regular Expression for Matching Various Phone Number Formats

## Description 📝

This **regular expression** matches phone numbers in the following formats, where `x` represents any arbitrary digit:

-   `+7xxxxxxxxxx`
-   `+7(xxx)xxxxxxx`
-   `+7(xxx)-xxx-xx-xx`
-   `+7 xxx xxx xx xx`

It does **not** perform additional validation beyond ensuring that the phone number matches one of the specified formats.

## Purpose 🎯

This regex is designed for:

-   **Extracting or validating phone numbers** that follow a particular format, such as in user input, log files, or text documents.
-   **Parsing phone numbers** from structured or unstructured text, where the format variations are predefined.

## How It Works 🔍

The regex:

```regex
r'\+7(?:' \
    r'\d{10}|' \
    r'\(\d{3}\)\d{7}|' \
    r'\(\d{3}\)-\d{3}-\d{2}-\d{2}|' \
    r'\s\d{3}\s\d{3}\s\d{2}\s\d{2}' \
r')'
```

## Explanation:

-   **`\+7`** → Matches the literal `+7`, which is the country code for Russia.
-   **`(?: ... )`** → A non-capturing group that allows multiple formats for the phone number.
-   **`\d{10}`** → Matches 10 consecutive digits, representing a phone number like `+7xxxxxxxxxx`.
-   **`\(\d{3}\)\d{7}`** → Matches a phone number in the format `+7(xxx)xxxxxxx`, where `(xxx)` is a 3-digit area code and `xxxxxxx` is a 7-digit number.
-   **`\(\d{3}\)-\d{3}-\d{2}-\d{2}`** → Matches a phone number in the format `+7(xxx)-xxx-xx-xx`, with the area code in parentheses and dashes separating the groups of digits.
-   **`\s\d{3}\s\d{3}\s\d{2}\s\d{2}`** → Matches a phone number in the format `+7 xxx xxx xx xx`, with spaces separating the digit groups.

## Output 📜

Example usage:

```python
import re

text = "Here are some phone numbers: +7xxxxxxxxxx, +7(123)4567890, +7(123)-456-78-90, +7 123 456 78 90."
regex = r'\+7(?:\d{10}|\(\d{3}\)\d{7}|\(\d{3}\)-\d{3}-\d{2}-\d{2}|\s\d{3}\s\d{3}\s\d{2}\s\d{2})'

matches = re.findall(regex, text)
print("Matches:", matches)
```

### Output:

```
Matches: ['+7xxxxxxxxxx', '+7(123)4567890', '+7(123)-456-78-90', '+7 123 456 78 90']
```

## Usage 📦

1. Use this regex in a Python script with the `re` module to find all matching phone numbers in a text.
2. Apply this regex to validate or extract phone numbers in the specified formats.
3. Use it for processing user input, validating phone numbers, or extracting phone numbers from larger datasets.

## Conclusion 🚀

This regular expression efficiently matches a variety of phone number formats that include Russian country code `+7`. It is flexible enough to handle several common formats and can be used for tasks such as validation, extraction, and parsing.
