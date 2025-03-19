# Regular Expression for Matching Date Formats

## Description 📝

This **regular expression** is designed to match dates in the following formats:

-   `DD.MM.YYYY`
-   `DD/MM/YYYY`
-   `YYYY.MM.DD`
-   `YYYY/MM/DD`

No additional validation of the date is required, meaning it will match any date structure in these formats, regardless of whether the date is valid (e.g., it won't check if a month is between `01` and `12`).

## Purpose 🎯

This regex is intended to:

-   **Extract dates** from a string that follow any of the four specified formats.
-   **Validate** whether the format of a date is correct, without checking if the date values themselves (like the day, month, or year) are valid.

## How It Works 🔍

The regex:

```regex
r'(?:\d{2}\.\d{2}\.\d{4}|' \
    r'\d{2}/\d{2}/\d{4}|' \
    r'\d{4}/\d{2}/\d{2}|' \
    r'\d{4}\.\d{2}\.\d{2})'
```

## Explanation:

-   **`(?: ... )`** → A non-capturing group that allows multiple possible formats.
-   **`\d{2}\.\d{2}\.\d{4}`** → Matches a date in the format `DD.MM.YYYY`, where `\d{2}` represents a two-digit day, month, and `\d{4}` represents a four-digit year.
-   **`\d{2}/\d{2}/\d{4}`** → Matches a date in the format `DD/MM/YYYY`, where `/` separates the day, month, and year.
-   **`\d{4}/\d{2}/\d{2}`** → Matches a date in the format `YYYY/MM/DD`, where the year comes first, followed by month and day.
-   **`\d{4}\.\d{2}\.\d{2}`** → Matches a date in the format `YYYY.MM.DD`, where the year comes first and is separated by periods.

## Output 📜

Example usage:

```python
import re

text = "Here are some dates: 01.12.2021, 02/03/2022, 2023/04/05, 2024.06.07."
regex = r'(?:\d{2}\.\d{2}\.\d{4}|\d{2}/\d{2}/\d{4}|\d{4}/\d{2}/\d{2}|\d{4}\.\d{2}\.\d{2})'

matches = re.findall(regex, text)
print("Matches:", matches)
```

### Output:

```
Matches: ['01.12.2021', '02/03/2022', '2023/04/05', '2024.06.07']
```

## Usage 📦

1. This regex can be used to **extract dates** from text, logs, or user inputs.
2. You can use it to **check** if the date format is correct, but it won't check for date validity (like February 30).
3. It can be useful for **parsing dates** in files, documents, or APIs that use different date formats.

## Conclusion 🚀

This regular expression offers a flexible solution to match dates in various formats, whether the separator is a period or a slash, and whether the year comes first or the day. It's helpful for applications that need to handle different date formats without performing deeper validation.
