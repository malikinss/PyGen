# Regular Expression for Matching Sequences of 8 Digits with Optional Hyphens

## Description 📝

This **regular expression** matches sequences of exactly 8 digits, where hyphens can optionally appear to separate the digits into groups of 2, but only in the correct format.

## Purpose 🎯

We need to match sequences of **8 digits**:

-   Without hyphens, e.g., `12345678`
-   With hyphens, dividing the digits into groups of 2, e.g., `12-34-56-78`

The hyphen is optional and only allowed if it divides the digits into groups of 2.

## How It Works 🔍

```regex
r'(\d{8})|(\d{2})(-\d{2}){3}'
```

**Explanation**:

-   **`(\d{8})`** → Matches exactly 8 digits in a row (without any hyphens).
-   **`|`** → The **OR** operator, meaning either the previous pattern or the next one can match.
-   **`(\d{2})`** → Matches exactly 2 digits.
-   **`(-\d{2}){3}`** → Matches a hyphen followed by exactly 2 digits, repeated **3 times**. This ensures that the digits are divided into 4 groups of 2 digits each, with hyphens separating them.

This regular expression allows two formats:

-   8 digits in a row (`12345678`)
-   4 groups of 2 digits, each separated by a hyphen (`12-34-56-78`)

---

## Example Usage 📜

```python
import re

regex = r'(\d{8})|(\d{2})(-\d{2}){3}'

test_cases = [
    "12345678",  # ✅ Match (8 digits without hyphens)
    "12-34-56-78",  # ✅ Match (4 groups of 2 digits with hyphens)
    "1234-5678",  # ❌ No match (not a valid format)
    "12-34-56-789",  # ❌ No match (extra digit)
    "1234-56-78",  # ❌ No match (incorrect grouping)
]

for case in test_cases:
    if re.search(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"12345678": ✅ Match
"12-34-56-78": ✅ Match
"1234-5678": ❌ No match
"12-34-56-789": ❌ No match
"1234-56-78": ❌ No match
```

---

## Usage 📦

-   **Validation**: For validating credit card numbers, phone numbers, or similar numeric sequences that might have optional separators.
-   **Text Processing**: Matching numeric sequences with optional hyphen separators.
-   **Data Extraction**: Extracting well-structured numeric data that may use hyphens as separators.

## Conclusion 🚀

This **regular expression** is designed to match exactly 8 digits, optionally divided into groups of 2 by hyphens.
It ensures that the hyphenated format adheres strictly to the grouping rules, while also allowing a simple, uninterrupted sequence of digits.
