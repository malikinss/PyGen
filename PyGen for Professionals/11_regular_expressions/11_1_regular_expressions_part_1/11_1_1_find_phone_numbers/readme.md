# Phone Number Finder

## Description 📝

The `find_phone_numbers()` function extracts phone numbers from a given text that match specific formats. The supported formats are:

-   `7-ddd-ddd-dd-dd`
-   `8-ddd-dddd-dddd`
-   `+7-ddd-ddd-dd-dd` (converted to `7-ddd-ddd-dd-dd`)

where `d` represents a digit from 0 to 9.

## Purpose 🎯

This function helps identify and extract phone numbers from any text input.
It can be useful for data validation, text processing, and contact information extraction.

## How It Works 🔍

-   **Regular Expressions (`re` module)**: A regex pattern is used to find phone numbers that match the specified formats.
-   **Pattern Matching**: The function looks for:
    -   Numbers starting with `7-` or `+7-` followed by three groups of digits in the format `7-ddd-ddd-dd-dd`.
    -   Numbers starting with `8-` followed by three groups of digits in the format `8-ddd-dddd-dddd`.
-   **Processing Matches**: The `findall()` method extracts all matching numbers, and if a number starts with `+7-`, the `+` sign is removed before printing.

## Output 📜

Example usage:

```python
text = "Call me at 7-123-456-78-90 or 8-987-6543-2109. Also, try +7-555-666-77-88."
find_phone_numbers(text)
```

Output:

```
7-123-456-78-90
8-987-6543-2109
7-555-666-77-88
```

## Usage 📦

1. Save the function in a Python file, e.g., `find_phone_numbers.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run Python and test the function:
    ```python
    from find_phone_numbers import find_phone_numbers
    text = "Some numbers: 7-123-456-78-90, 8-987-6543-2109, +7-555-666-77-88."
    find_phone_numbers(text)
    ```
4. The extracted phone numbers will be printed, one per line.

## Conclusion 🚀

The `find_phone_numbers()` function is an efficient way to extract phone numbers from text using regular expressions.
It ensures proper formatting and handles different variations, making it useful for text analysis and data processing.
