# Regular Expression for Matching Specific String Pattern

## Description 📝

This **regular expression** ensures that a string satisfies the following conditions:

-   **Begins with two or more digits (`0-9`).**
-   **Is followed by zero or more lowercase letters (`a-z`).**
-   **Ends with zero or more uppercase letters (`A-Z`).**

## Purpose 🎯

We need to match strings that:

-   **Start with at least two digits** (e.g., `12abcXYZ`).
-   **Optionally contain lowercase letters in the middle** (e.g., `99hello`).
-   **Optionally end with uppercase letters** (e.g., `42GO`).
-   **Do not contain other characters** (e.g., symbols, spaces, special characters).

## How It Works 🔍

```regex
r'^\d{2,}[a-z]*[A-Z]*$'
```

**Explanation**:

-   **`^`** → Ensures the **string starts** here.
-   **`\d{2,}`** → Matches **two or more digits** (`0-9`).
-   **`[a-z]*`** → Matches **zero or more lowercase letters** (`a-z`).
-   **`[A-Z]*`** → Matches **zero or more uppercase letters** (`A-Z`).
-   **`$`** → Ensures the **string ends** here.

---

## Example Usage 📜

```python
import re

regex = r'^\d{2,}[a-z]*[A-Z]*$'

test_cases = [
    "12abcXYZ",    # ✅ Match (starts with "12", has lowercase and uppercase)
    "99hello",     # ✅ Match (starts with "99", followed by lowercase)
    "42GO",        # ✅ Match (starts with "42", ends with uppercase)
    "55",          # ✅ Match (only digits)
    "123abc",      # ✅ Match (digits followed by lowercase)
    "007bondJAMES", # ✅ Match (digits, lowercase, uppercase)
    "8word",       # ❌ No match (starts with a single digit)
    "hello42",     # ❌ No match (does not start with digits)
    "99mix_Match", # ❌ No match (contains `_`)
    "123 TEST",    # ❌ No match (contains space)
]

for case in test_cases:
    if re.fullmatch(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"12abcXYZ": ✅ Match
"99hello": ✅ Match
"42GO": ✅ Match
"55": ✅ Match
"123abc": ✅ Match
"007bondJAMES": ✅ Match
"8word": ❌ No match
"hello42": ❌ No match
"99mix_Match": ❌ No match
"123 TEST": ❌ No match
```

## Usage 📦

-   **Data Validation**: Ensure strings follow a **digit-lowercase-uppercase** pattern.
-   **Sorting & Filtering**: Extract **valid codes** from text data.
-   **Pattern Recognition**: Identify structured **alphanumeric sequences**.

## Conclusion 🚀

This **regular expression** successfully validates strings that begin with **two or more digits**, optionally contain **lowercase letters**, and end with **uppercase letters**, ensuring a strict but flexible format.
