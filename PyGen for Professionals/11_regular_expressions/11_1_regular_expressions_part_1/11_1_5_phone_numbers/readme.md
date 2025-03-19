# Regular Expression for Matching Phone Numbers

## Description 📝

This code defines a **regular expression** that matches **phone numbers** in the format `xxx-xxx-xxxx`, where `x` is any digit (`0-9`).
The pattern ensures that the input strictly follows this format.

## Purpose 🎯

This regular expression can be used for:

-   **Validating phone numbers** in forms or user input.
-   **Extracting phone numbers** from text data.
-   **Formatting and filtering** structured data.

## How It Works 🔍

-   **`\d{3}`**: Matches exactly **three digits** (area code).
-   **`-`**: Matches the first hyphen separator.
-   **`\d{3}`**: Matches exactly **three digits** (central office code).
-   **`-`**: Matches the second hyphen separator.
-   **`\d{4}`**: Matches exactly **four digits** (line number).

This pattern ensures that only numbers in the format **`xxx-xxx-xxxx`** are matched.

## Output 📜

Example usage:

```python
import re

text = "Call me at 123-456-7890 or 987-654-3210. Invalid: 1234567890, (123)-456-7890."
regex = r'\d{3}-\d{3}-\d{4}'

matches = re.findall(regex, text)
print("Matches:", matches)
```

Output:

```
Matches: ['123-456-7890', '987-654-3210']
```

## Usage 📦

1. Save the regex in a Python script, e.g., `phone_number_regex.py`.
2. Use it in a Python program with the `re` module.
3. Run the script with different text inputs to extract valid phone numbers.

## Conclusion 🚀

The regular expression `r'\d{3}-\d{3}-\d{4}'` is a simple and effective way to **validate and extract** phone numbers in the format `xxx-xxx-xxxx`.
It ensures consistency and accuracy when working with structured numerical data.
