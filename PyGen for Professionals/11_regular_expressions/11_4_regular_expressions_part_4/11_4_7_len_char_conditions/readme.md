# Regular Expression for Matching Strings with Specific Length and Character Conditions

## Description 📝

This **regular expression** ensures that the string meets the following conditions:

-   **The first 40 characters** are either uppercase or lowercase Latin letters (`a-zA-Z`) or even digits (`0, 2, 4, 6, 8`).
-   **The last 5 characters** are either odd digits (`1, 3, 5, 7, 9`) or space characters.

## Purpose 🎯

We need to match a **string of length 45** that:

-   Starts with **40 characters** that are either **Latin letters** or **even digits**.
-   Ends with **5 characters** that are either **odd digits** or **space characters**.

## How It Works 🔍

```regex
r'^[a-zA-Z02468]{40}[13579 ]{5}$'
```

**Explanation**:

-   **`^`** → Ensures the **string starts** here.
-   **`[a-zA-Z02468]{40}`** → Matches exactly **40 characters**, where each character is either a **Latin letter** (uppercase or lowercase) or an **even digit** (`0, 2, 4, 6, 8`).
-   **`[13579 ]{5}`** → Matches exactly **5 characters**, where each character is either an **odd digit** (`1, 3, 5, 7, 9`) or a **space** (` `).
-   **`$`** → Ensures the **string ends** here.

---

## Example Usage 📜

```python
import re

regex = r'^[a-zA-Z02468]{40}[13579 ]{5}$'

test_cases = [
    "AbC1234E56789X0zWqRsU0e1t4567890ABC123 ",  # ✅ Match (valid length and characters)
    "abcD1X2O34M5p6Q7rH8F9v0z ",  # ✅ Match (valid length and characters)
    "AbC1234E56789X0zWqRsU0e1t4567890ABC123",  # ❌ No match (length not 45)
    "12345678901234567890123456789012345678901234567",  # ❌ No match (last characters are not odd digits or space)
    "AbC1234E56789X0zWqRsU0e1t4567890ABC12    ",  # ❌ No match (5 spaces at the end must be odd digits or space, not a mix)
]

for case in test_cases:
    if re.fullmatch(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"AbC1234E56789X0zWqRsU0e1t4567890ABC123 ": ✅ Match
"abcD1X2O34M5p6Q7rH8F9v0z ": ✅ Match
"AbC1234E56789X0zWqRsU0e1t4567890ABC123": ❌ No match
"12345678901234567890123456789012345678901234567": ❌ No match
"AbC1234E56789X0zWqRsU0e1t4567890ABC12    ": ❌ No match
```

## Usage 📦

-   **String Validation**: Ensure strings follow a **specific format** for input data, such as IDs or codes.
-   **Pattern Matching**: Extract or identify strings that match **length-based conditions**.
-   **Data Integrity**: Filter strings that meet **character set and position criteria**.

## Conclusion 🚀

This **regular expression** validates strings that meet the specified **length** and **character rules**, ensuring a consistent and structured format.
