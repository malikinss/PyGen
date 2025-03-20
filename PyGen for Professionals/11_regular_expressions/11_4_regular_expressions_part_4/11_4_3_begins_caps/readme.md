# Regular Expression for Matching Words That Begin with a Capital Letter

## Description 📝

This **regular expression** ensures that words starting **with an uppercase Latin letter** are matched, while avoiding incorrect matches inside other words.

## Purpose 🎯

We need to match words that:

-   **Begin with an uppercase Latin letter (A-Z).**
-   **Can contain lowercase letters, digits, or underscores after the first letter.**
-   **Are standalone words, not parts of other words.**

## How It Works 🔍

```regex
r'\b[A-Z]\w*\b'
```

**Explanation**:

-   **`\b`** → Word boundary (ensures the match is a **standalone word**).
-   **`[A-Z]`** → Matches a **single uppercase letter** at the start of the word.
-   **`\w*`** → Matches **zero or more** word characters (letters, digits, underscores).
-   **`\b`** → Ensures the match ends at a **word boundary**.

---

## Example Usage 📜

```python
import re

regex = r'\b[A-Z]\w*\b'

test_cases = [
    "Hello",     # ✅ Match
    "World",     # ✅ Match
    "hello",     # ❌ No match (lowercase start)
    "HELLO",     # ✅ Match (all caps, still valid)
    "Test123",   # ✅ Match (contains numbers but starts with uppercase)
    "123Test",   # ❌ No match (starts with a digit)
    "_Hidden",   # ❌ No match (starts with an underscore)
    " CamelCase",# ✅ Match (valid PascalCase word)
]

for case in test_cases:
    if re.search(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"Hello": ✅ Match
"World": ✅ Match
"hello": ❌ No match
"HELLO": ✅ Match
"Test123": ✅ Match
"123Test": ❌ No match
"_Hidden": ❌ No match
" CamelCase": ✅ Match
```

## Usage 📦

-   **Text Processing**: Detect proper nouns or capitalized words.
-   **Grammar Checking**: Validate words that should start with a capital letter.
-   **Data Extraction**: Extract titles or formatted names from text.

## Conclusion 🚀

This **regular expression** accurately identifies words **that start with a capital letter**, ensuring proper matches while avoiding incorrect detections.
