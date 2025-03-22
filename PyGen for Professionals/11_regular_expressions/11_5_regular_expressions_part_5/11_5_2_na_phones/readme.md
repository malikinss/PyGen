# Regular Expression for Matching North American Phone Numbers

## Description 📝

This **regular expression** ensures that the phone number follows the North American format, which satisfies the following conditions:

-   **Begins with a three-digit area code** (which may be enclosed in parentheses).
-   **Followed by a separator** (a space or hyphen).
-   **Then followed by a seven-digit number**, which is split into a three-digit prefix and a four-digit line number, separated by a hyphen.
-   **The first digit of the area code and the prefix cannot be 0 or 1**.

## Purpose 🎯

We need to match phone numbers that:

-   Start with a **valid area code** (either in parentheses or not).
-   Are followed by a **valid separator** (space or hyphen).
-   Contain a **valid seven-digit number** (split into prefix and line number), with the **first digits** not being 0 or 1.

## How It Works 🔍

```regex
r'(\([2-9]\d{2}\)|[2-9]\d{2})[- ]?[2-9]\d{2}-\d{4}'
```

**Explanation**:

-   **`(\([2-9]\d{2}\)|[2-9]\d{2})`**:
    -   **`\([2-9]\d{2}\)`** → Matches the area code enclosed in parentheses. The first digit cannot be 0 or 1, hence the `[2-9]` matches digits from 2 to 9, followed by any two digits.
    -   **`[2-9]\d{2}`** → Matches the area code without parentheses. The first digit cannot be 0 or 1, hence `[2-9]` matches digits from 2 to 9, followed by any two digits.
-   **`[- ]?`** → Matches an optional space or hyphen as the separator between the area code and the seven-digit number.
-   **`[2-9]\d{2}-\d{4}`**:
    -   **`[2-9]\d{2}`** → Matches the three-digit prefix of the phone number, where the first digit cannot be 0 or 1 (hence `[2-9]`), followed by any two digits.
    -   **`-\d{4}`** → Matches the four-digit line number, separated by a hyphen.

---

## Example Usage 📜

```python
import re

regex = r'(\([2-9]\d{2}\)|[2-9]\d{2})[- ]?[2-9]\d{2}-\d{4}'

test_cases = [
    "(123) 456-7890",    # ❌ No match (invalid area code)
    "(234) 567-8901",    # ✅ Match
    "234-567-8901",      # ✅ Match
    "234 567-8901",      # ✅ Match
    "123-456-7890",      # ❌ No match (invalid area code and prefix)
    "(234)567-8901",     # ✅ Match
    "(234) 567 8901",    # ❌ No match (incorrect separator)
    "(234) 567-890",     # ❌ No match (line number too short)
    "234-567-89012",     # ❌ No match (line number too long)
]

for case in test_cases:
    if re.fullmatch(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"(123) 456-7890": ❌ No match
"(234) 567-8901": ✅ Match
"234-567-8901": ✅ Match
"234 567-8901": ✅ Match
"123-456-7890": ❌ No match
"(234)567-8901": ✅ Match
"(234) 567 8901": ❌ No match
"(234) 567-890": ❌ No match
"234-567-89012": ❌ No match
```

## Usage 📦

-   **Phone Number Validation**: Validate North American phone numbers.
-   **Form Input Validation**: Ensure proper format in forms requiring phone numbers.
-   **Text Parsing**: Extract phone numbers from text.

## Conclusion 🚀

This **regular expression** validates phone numbers that follow the **North American format**, ensuring they have valid area codes, valid separators, and valid prefixes with line numbers.
