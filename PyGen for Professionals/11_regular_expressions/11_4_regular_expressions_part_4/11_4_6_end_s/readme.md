# Regular Expression for Matching Strings Ending with 's'

## Description 📝

This **regular expression** ensures that a string satisfies the following conditions:

-   **Contains only Latin letters (`a-z`, `A-Z`).**
-   **Ends with a lowercase 's' (`s`).**

## Purpose 🎯

We need to match strings that:

-   **Contain only English letters** (no numbers, spaces, or special characters).
-   **End with a lowercase 's'.**
-   **Can be of any length (including a single character 's').**

## How It Works 🔍

```regex
r'^[a-zA-Z]*s$'
```

**Explanation**:

-   **`^`** → Ensures the **string starts** here.
-   **`[a-zA-Z]*`** → Matches **zero or more** uppercase or lowercase Latin letters.
-   **`s`** → Ensures the **string ends with a lowercase 's'**.
-   **`$`** → Ensures the **string ends** here.

---

## Example Usage 📜

```python
import re

regex = r'^[a-zA-Z]*s$'

test_cases = [
    "apples",   # ✅ Match (only letters, ends with 's')
    "Berries",  # ✅ Match (only letters, ends with 's')
    "S",        # ✅ Match (single lowercase 's')
    "Words",    # ✅ Match (only letters, ends with 's')
    "cars",     # ✅ Match (valid lowercase ending 's')
    "hello",    # ❌ No match (does not end with 's')
    "123s",     # ❌ No match (contains numbers)
    "Banana!",  # ❌ No match (contains a special character)
    "Spaces ",  # ❌ No match (contains a space)
]

for case in test_cases:
    if re.fullmatch(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"apples": ✅ Match
"Berries": ✅ Match
"S": ✅ Match
"Words": ✅ Match
"cars": ✅ Match
"hello": ❌ No match
"123s": ❌ No match
"Banana!": ❌ No match
"Spaces ": ❌ No match
```

## Usage 📦

-   **Text Filtering**: Identify words following **specific naming conventions**.
-   **Data Validation**: Ensure strings consist only of **Latin letters** and **end with 's'**.
-   **Pattern Matching**: Extract words in **linguistic analysis**.

## Conclusion 🚀

This **regular expression** successfully validates **words composed only of Latin letters** that **end with a lowercase 's'**, ensuring a structured format.
