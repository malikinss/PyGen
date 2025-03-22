# Regular Expression for Matching U.S. ZIP Codes

## Description 📝

This **regular expression** ensures that the string matches **U.S. ZIP Codes**, including both **five-digit** and **ZIP+4 formats**.

## Purpose 🎯

We need to match **ZIP Codes** that follow these rules:

-   A **standard ZIP Code** consists of **exactly five digits** (e.g., `12345`).
-   A **ZIP+4 Code** consists of **five digits**, followed by a **hyphen** and **four more digits** (e.g., `12345-6789`).
-   The **four-digit portion** after the hyphen is **optional**.

## How It Works 🔍

```regex
r'^\d{5}(-\d{4})?$'
```

**Explanation**:

-   **`^`** → Ensures the match starts at the **beginning of the string**.
-   **`\d{5}`** → Matches exactly **five digits** (the core ZIP Code).
-   **`(-\d{4})?`** → Matches an **optional** group:
    -   **`-`** → A literal hyphen.
    -   **`\d{4}`** → Exactly **four digits**.
    -   **`?`** → Makes the **hyphen and four digits optional** (for standard five-digit ZIP Codes).
-   **`$`** → Ensures the match ends at the **end of the string**.

---

## Example Usage 📜

```python
import re

regex = r'^\d{5}(-\d{4})?$'

test_cases = [
    "12345",        # ✅ Match (Standard ZIP Code)
    "98765",        # ✅ Match (Standard ZIP Code)
    "12345-6789",   # ✅ Match (ZIP+4 Code)
    "54321-4321",   # ✅ Match (ZIP+4 Code)
    "1234",         # ❌ No match (less than 5 digits)
    "123456",       # ❌ No match (more than 5 digits without hyphen)
    "12345-678",    # ❌ No match (ZIP+4 but missing a digit)
    "ABCDE",        # ❌ No match (non-numeric characters)
    "12345-67890",  # ❌ No match (ZIP+4 but too many digits)
    "12345-",       # ❌ No match (ZIP+4 but missing the four digits)
]

for case in test_cases:
    if re.fullmatch(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"12345": ✅ Match
"98765": ✅ Match
"12345-6789": ✅ Match
"54321-4321": ✅ Match
"1234": ❌ No match
"123456": ❌ No match
"12345-678": ❌ No match
"ABCDE": ❌ No match
"12345-67890": ❌ No match
"12345-": ❌ No match
```

## Usage 📦

-   **Address Validation**: Ensure ZIP Codes are entered in the correct format in forms.
-   **Data Cleaning**: Extract valid ZIP Codes from text datasets.
-   **Location-Based Services**: Validate ZIP Codes for geographical lookup and processing.

## Conclusion 🚀

This **regular expression** correctly identifies **valid U.S. ZIP Codes**, supporting both **five-digit** and **ZIP+4 formats**, while avoiding incorrect or incomplete matches.
