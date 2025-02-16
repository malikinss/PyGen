# JSON-like Country Formatter

## Description 📝

This Python script formats a dictionary of country-capital pairs into a structured JSON-like string with specific formatting rules.

## Purpose 🎯

The goal of this program is to:

-   Arrange dictionary elements in lexicographic order based on the country name.
-   Format the output using:
    -   A comma (`,`) without a space as the element separator.
    -   `" - "` (a space-hyphen-space) as the key-value separator.
    -   Three spaces for indentation.

This exercise demonstrates sorting dictionaries, JSON formatting, and customizing string representation.

## How It Works 🔍

1. **format_countries() Function**:

    - Uses `json.dumps()` to format the dictionary.
    - Sorts keys in lexicographic order (`sort_keys=True`).
    - Applies custom separators:
        - `(',', ' - ')` for element and key-value separation.
        - `indent=3` for indentation.

2. **Example Dictionary**:
    - A sample dictionary of country-capital pairs is provided.
    - The function processes and formats it accordingly.

## Output 📜

The program outputs a properly formatted string, starting with:

```
{
   "Angola" - "Luanda",
   "Australia" - "Canberra",
   "Canada" - "Ottawa",
   ...
}
```

## Usage 📦

1. Save the script as `format_countries.py`.
2. Run the script using:
    ```
    python format_countries.py
    ```
3. The formatted country list will be displayed in the terminal.

## Conclusion 🚀

This script provides a structured representation of country-capital data in a JSON-like format with customized spacing.
It showcases Python’s powerful dictionary handling and formatting capabilities.
