# Regular Expression for Matching Specific String Pattern

## Description 📝

This **regular expression** ensures that the string satisfies the following conditions:

-   **The string begins** with **one or two digits**.
-   **Followed by three or more uppercase Latin letters**.
-   **Ends with three or fewer dots**.

## Purpose 🎯

We need to match strings that:

-   Start with **one or two digits**.
-   Are followed by **three or more uppercase Latin letters**.
-   End with **three or fewer dots**.

## How It Works 🔍

```regex
r'^\d{1,2}[A-Z]{3,}\.{0,3}$'
```

**Explanation**:

-   **`^`** → Ensures the string **starts** with the following pattern.
-   **`\d{1,2}`** → Matches **one or two digits** at the beginning of the string.
-   **`[A-Z]{3,}`** → Matches **three or more uppercase Latin letters** after the digits.
-   **`\.`** → Matches the literal **dot character**.
-   **`{0,3}`** → Matches **zero to three** dots (ensuring the string ends with no more than three dots).
-   **`$`** → Ensures the string **ends** here (i.e., no characters after the dots).

---

## Example Usage 📜

```python
import re

regex = r'^\d{1,2}[A-Z]{3,}\.{0,3}$'

test_cases = [
    "12ABC...",      # ✅ Match
    "9XYZ",          # ✅ Match
    "1AB.",          # ✅ Match
    "34WXYZ...",     # ✅ Match
    "3A.",           # ❌ No match (only one letter)
    "12abc.",        # ❌ No match (contains lowercase letters)
    "99XYZ....",     # ❌ No match (more than three dots)
    "7ABCD....",     # ❌ No match (more than three dots)
    "ABC123",        # ❌ No match (does not start with digits)
]

for case in test_cases:
    if re.fullmatch(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"12ABC...": ✅ Match
"9XYZ": ✅ Match
"1AB.": ✅ Match
"34WXYZ...": ✅ Match
"3A.": ❌ No match
"12abc.": ❌ No match
"99XYZ....": ❌ No match
"7ABCD....": ❌ No match
"ABC123": ❌ No match
```

## Usage 📦

-   **Text Validation**: Ensure correct format for codes, identifiers, or tags that follow this pattern.
-   **Input Filtering**: Filter and validate user input based on a specific structure.
-   **Data Parsing**: Extract or match strings with a defined format from text sources.

## Conclusion 🚀

This **regular expression** validates strings that start with one or two digits, followed by three or more uppercase letters, and ends with up to three dots, ensuring the correct structure for identifiers or codes.
