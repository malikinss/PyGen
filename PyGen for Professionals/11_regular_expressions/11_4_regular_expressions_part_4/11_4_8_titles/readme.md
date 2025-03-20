# Regular Expression for Matching Titles and Uppercase Letters

## Description 📝

This **regular expression** ensures that the string meets the following conditions:

-   **The string begins** with one of the specified titles: **Mr.**, **Mrs.**, **Ms.**, **Dr.**, or **Er.**.
-   **The rest of the string** consists of one or more **uppercase Latin letters**.

## Purpose 🎯

We need to match strings that:

-   Start with one of the **specified titles**: **"Mr."**, **"Mrs."**, **"Ms."**, **"Dr."**, or **"Er."**.
-   Have **one or more uppercase Latin letters** after the title.

## How It Works 🔍

```regex
r'^(Mr|Mrs|Ms|Dr|Er)\.[A-Z]+$'
```

**Explanation**:

-   **`^`** → Ensures the **string starts** with the following pattern.
-   **`(Mr|Mrs|Ms|Dr|Er)`** → Matches one of the **specified titles**: **"Mr."**, **"Mrs."**, **"Ms."**, **"Dr."**, or **"Er."**.
-   **`\.`** → Matches the literal **dot** character (`.`) following the title.
-   **`[A-Z]+`** → Matches one or more **uppercase Latin letters**.
-   **`$`** → Ensures the **string ends** here (i.e., no characters after the uppercase letters).

---

## Example Usage 📜

```python
import re

regex = r'^(Mr|Mrs|Ms|Dr|Er)\.[A-Z]+$'

test_cases = [
    "Mr.ABC",     # ✅ Match
    "Mrs.XYZ",    # ✅ Match
    "Ms.ABCD",    # ✅ Match
    "Dr.JOHN",    # ✅ Match
    "Er.SMITH",   # ✅ Match
    "Mr.Abc",     # ❌ No match (contains lowercase letter)
    "Dr.123",     # ❌ No match (contains digits)
    "Ms.ABC123",  # ❌ No match (contains digits)
    "Mx.JOHN",    # ❌ No match (invalid title "Mx.")
    "MrABC",      # ❌ No match (missing dot after title)
]

for case in test_cases:
    if re.fullmatch(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"Mr.ABC": ✅ Match
"Mrs.XYZ": ✅ Match
"Ms.ABCD": ✅ Match
"Dr.JOHN": ✅ Match
"Er.SMITH": ✅ Match
"Mr.Abc": ❌ No match
"Dr.123": ❌ No match
"Ms.ABC123": ❌ No match
"Mx.JOHN": ❌ No match
"MrABC": ❌ No match
```

## Usage 📦

-   **Title Validation**: Ensure correct formatting of titles and names.
-   **User Input Filtering**: Filter user-provided titles and names based on a defined pattern.
-   **String Parsing**: Extract or match titles in **formal name formats**.

## Conclusion 🚀

This **regular expression** validates strings that start with specific titles followed by one or more uppercase Latin letters, ensuring correct formatting and structure.
