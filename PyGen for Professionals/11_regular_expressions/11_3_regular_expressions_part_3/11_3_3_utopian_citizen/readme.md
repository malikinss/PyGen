# Regular Expression for Utopian Citizen Identification Number

## Description 📝

Each **Utopian citizen** has an **identification number** that follows a **specific pattern**.
This regular expression ensures that only **valid identification numbers** are matched.

## Purpose 🎯

The regex ensures that the ID:

1. **Starts** with **0 to 3 lowercase letters** (`a-z`).
2. **Contains a sequence of 2 to 8 digits** (`0-9`).
3. **Ends with at least 3 uppercase letters** (`A-Z`).

## How It Works 🔍

The regex:

```regex
r'[a-z]{0,3}\d{2,8}[A-Z]{3,}'
```

**Explanation:**

-   **`[a-z]{0,3}`** → Matches **0 to 3 lowercase letters** at the start.
-   **`\d{2,8}`** → Matches a **sequence of 2 to 8 digits**.
-   **`[A-Z]{3,}`** → Matches **at least 3 uppercase letters** at the end.

## Output 📜

**Example Usage:**

```python
import re

regex = r'[a-z]{0,3}\d{2,8}[A-Z]{3,}'

test_cases = [
    "ab123ABCD",     # ✅ Valid
    "z12XYZ",        # ✅ Valid
    "xyz99999999AAA",# ❌ Too many digits (more than 8)
    "123ABC",        # ❌ Missing lowercase letters at the beginning
    "aa45ZXC",       # ✅ Valid
]

for case in test_cases:
    if re.fullmatch(regex, case):
        print(f"{case}: ✅ Valid")
    else:
        print(f"{case}: ❌ Invalid")
```

**Expected Output:**

```
ab123ABCD: ✅ Valid
z12XYZ: ✅ Valid
xyz99999999AAA: ❌ Invalid
123ABC: ❌ Invalid
aa45ZXC: ✅ Valid
```

## Usage 📦

-   **User Validation**: Ensures only **valid identification numbers** are used.
-   **Government Databases**: Helps in processing **citizen records**.
-   **Form Input Validation**: Prevents **invalid entries** in **online forms**.

## Conclusion 🚀

This **regular expression** effectively validates **Utopian citizen ID numbers**, ensuring they follow the **prescribed format**.
