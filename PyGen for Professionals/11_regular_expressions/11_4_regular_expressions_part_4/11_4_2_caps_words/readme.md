# Regular Expression for Matching All-Capital Latin Words

## Description 📝

This **regular expression** ensures that words written **entirely in uppercase Latin letters** are matched while avoiding partial matches inside other words.

## Purpose 🎯

We need to match words that:

-   **Contain only uppercase Latin letters (A-Z).**
-   **Are standalone words, not parts of other words.**
-   **Avoid matching numbers, punctuation, or lowercase letters.**

## How It Works 🔍

```regex
r'\b[A-Z]+\b'
```

**Explanation**:

-   **`\b`** → Word boundary (ensures the match is a **standalone word**).
-   **`[A-Z]+`** → Matches **one or more uppercase Latin letters**.
-   **`\b`** → Ensures the match ends at a **word boundary**.

---

## Example Usage 📜

```python
import re

regex = r'\b[A-Z]+\b'

test_cases = [
    "HELLO",     # ✅ Match
    "WORLD",     # ✅ Match
    "hello",     # ❌ No match (lowercase)
    "HelloWorld",# ❌ No match (mixed case)
    "123ABC",    # ❌ No match (contains numbers)
    " ALL ",     # ✅ Match (surrounded by spaces)
    "(TEST)",    # ✅ Match (surrounded by non-word characters)
]

for case in test_cases:
    if re.search(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"HELLO": ✅ Match
"WORLD": ✅ Match
"hello": ❌ No match
"HelloWorld": ❌ No match
"123ABC": ❌ No match
" ALL ": ✅ Match
"(TEST)": ✅ Match
```

## Usage 📦

-   **Text Processing**: Detect uppercase words in documents.
-   **Formatting Validation**: Ensure all-uppercase words follow expected patterns.
-   **Search & Filtering**: Extract uppercase words from text data.

## Conclusion 🚀

This **regular expression** accurately identifies words **written in all capital letters** while avoiding incorrect matches inside mixed-case words or numbers.
