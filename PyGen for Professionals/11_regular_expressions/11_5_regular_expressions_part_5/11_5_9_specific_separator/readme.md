# Regular Expression for Matching Sequences of 8 Digits with Specific Separators

## Description 📝

This **regular expression** matches sequences of **8 digits** that can optionally include separators (`-`, `---`, or `.`), as long as the separators divide the sequence into groups of **2 digits** and the sequence contains only **one type of separator** (if present).

## Purpose 🎯

We need to match sequences of **8 digits**, with the following conditions:

-   **Separators allowed**:
    -   Hyphen (`-`)
    -   Triple hyphen (`---`)
    -   Period (`.`)
-   The sequence must be divided into 4 groups of **2 digits each**, with one of the separators between the groups.
-   Only **one type** of separator can be used in a valid sequence.

## How It Works 🔍

```regex
r'\d{2}((-|---|\.)?)\d{2}\1\d{2}\1\d{2}'
```

**Explanation**:

-   **`\d{2}`** → Matches exactly 2 digits.
-   **`((-|---|\.)?)`** → Optionally matches one of the separators: hyphen (`-`), triple hyphen (`---`), or period (`.`). The `?` means that the separator is optional.
-   **`\1`** → Refers back to the first capturing group (the separator), ensuring that the same separator is used throughout the sequence.
-   **`\d{2}`** → Matches the next 2 digits, repeating the pattern for the 4 groups of 2 digits.

This regular expression matches:

-   8 digits with or without a separator.
-   The separator can only be one type (`-`, `---`, or `.`), used consistently throughout.

---

## Example Usage 📜

```python
import re

regex = r'\d{2}((-|---|\.)?)\d{2}\1\d{2}\1\d{2}'

test_cases = [
    "12-34-56-78",  # ✅ Match (hyphens as separators)
    "12---34---56---78",  # ✅ Match (triple hyphens as separators)
    "12.34.56.78",  # ✅ Match (periods as separators)
    "12-34---56-78",  # ❌ No match (mixed separators)
    "12345678",  # ✅ Match (no separator)
    "12-34.56-78",  # ❌ No match (mixed separators)
]

for case in test_cases:
    if re.search(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"12-34-56-78": ✅ Match
"12---34---56---78": ✅ Match
"12.34.56.78": ✅ Match
"12-34---56-78": ❌ No match
"12345678": ✅ Match
"12-34.56-78": ❌ No match
```

---

## Usage 📦

-   **Text Processing**: To validate numeric sequences where separators might be used in a consistent pattern.
-   **Data Validation**: To ensure that phone numbers, credit card numbers, or other 8-digit numeric identifiers are formatted correctly with consistent separators.

## Conclusion 🚀

This **regular expression** efficiently matches 8-digit sequences with optional separators, ensuring that the separators are consistent throughout the sequence.
