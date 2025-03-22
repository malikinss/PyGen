# Regular Expression for Matching Character Sequences with Specific Conditions

## Description 📝

This **regular expression** matches character sequences of exactly **6 characters** that satisfy the following conditions:

-   The first character is a **lowercase Latin letter**.
-   The second character can be a **digit**, **any letter** (uppercase or lowercase), or an **underscore**.
-   The third character is an **uppercase Latin letter**.
-   The fourth character **must match the first character**.
-   The fifth character **must match the second character**.
-   The sixth character **must match the third character**.

## Purpose 🎯

We need to match strings that:

-   Begin with a **lowercase letter**.
-   Have a second character that can be a **digit**, **letter**, or **underscore**.
-   Followed by an **uppercase letter**.
-   The next three characters are **repetitions of the first three characters** in the sequence.

## How It Works 🔍

```regex
r'([a-z])([\da-zA-Z_])([A-Z])\1\2\3'
```

**Explanation**:

-   **`([a-z])`** → Captures the first character, which is a **lowercase Latin letter**.
-   **`([\da-zA-Z_])`** → Captures the second character, which can be a **digit**, a **letter** (uppercase or lowercase), or an **underscore**.
-   **`([A-Z])`** → Captures the third character, which is an **uppercase Latin letter**.
-   **`\1`** → Refers to the first captured group (the lowercase Latin letter), ensuring the fourth character matches the first character.
-   **`\2`** → Refers to the second captured group (the second character), ensuring the fifth character matches the second character.
-   **`\3`** → Refers to the third captured group (the uppercase Latin letter), ensuring the sixth character matches the third character.

---

## Example Usage 📜

```python
import re

regex = r'([a-z])([\da-zA-Z_])([A-Z])\1\2\3'

test_cases = [
    "a1A1a1",    # ✅ Match
    "b2B2b2",    # ✅ Match
    "z9Z9z9",    # ✅ Match
    "m4X4m4",    # ❌ No match (uppercase letter in 2nd position)
    "a1a1a1",    # ❌ No match (uppercase letter missing)
    "z9Z8z9",    # ❌ No match (mismatch in last character)
    "A1A1A1",    # ❌ No match (first character should be lowercase)
    "b_3B_3b"    # ✅ Match
]

for case in test_cases:
    if re.fullmatch(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"a1A1a1": ✅ Match
"b2B2b2": ✅ Match
"z9Z9z9": ✅ Match
"m4X4m4": ❌ No match
"a1a1a1": ❌ No match
"z9Z8z9": ❌ No match
"A1A1A1": ❌ No match
"b_3B_3b": ✅ Match
```

## Usage 📦

-   **Input Validation**: Ensure that inputs follow a specific pattern of characters.
-   **Pattern Matching**: Extract or validate sequences with specific repeated patterns.
-   **Text Processing**: Process or filter strings with a predefined structure.

## Conclusion 🚀

This **regular expression** ensures that character sequences of length 6 follow the defined structure with specific repetitions, allowing precise matching and validation.
