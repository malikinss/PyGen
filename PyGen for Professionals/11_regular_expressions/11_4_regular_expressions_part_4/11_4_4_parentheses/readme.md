# Regular Expression for Matching Lines Containing Parentheses

## Description 📝

This **regular expression** ensures that a line **contains an opening parenthesis `(` followed by a closing parenthesis `)` at some point**.

## Purpose 🎯

We need to match **any line** that:

-   **Contains at least one `(` somewhere.**
-   **Has a corresponding `)` later in the same line.**
-   **May contain anything before, between, or after the parentheses.**

## How It Works 🔍

```regex
r'.*\(.*\).*'
```

**Explanation**:

-   **`.*`** → Matches **any characters (including none)** at the start of the line.
-   **`\(`** → Matches an **opening parenthesis `(`**.
-   **`.*`** → Matches **any characters (including none)** between the parentheses.
-   **`\)`** → Matches a **closing parenthesis `)`**.
-   **`.*`** → Matches **any characters (including none)** after the parentheses.

---

## Example Usage 📜

```python
import re

regex = r'.*\(.*\).*'

test_cases = [
    "This is a test (example).",   # ✅ Match (contains "(example)")
    "(Start)",                     # ✅ Match (contains "()")
    "No parentheses here.",        # ❌ No match (no "(" or ")")
    "A single ( bracket",          # ❌ No match (missing ")")
    "Random ) text (order)",       # ✅ Match (contains both "(" and ")")
    "Empty () brackets",           # ✅ Match (contains "()")
    "Nested (inside (more))",      # ✅ Match (has at least one pair of "()")
]

for case in test_cases:
    if re.search(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"This is a test (example).": ✅ Match
"(Start)": ✅ Match
"No parentheses here.": ❌ No match
"A single ( bracket": ❌ No match
"Random ) text (order)": ✅ Match
"Empty () brackets": ✅ Match
"Nested (inside (more))": ✅ Match
```

## Usage 📦

-   **Text Parsing**: Identify lines containing **parentheses**.
-   **Syntax Highlighting**: Detect **function calls or grouped expressions**.
-   **Log Analysis**: Extract **specific data enclosed in parentheses**.

## Conclusion 🚀

This **regular expression** correctly finds lines **that contain an opening and closing parenthesis**, making it useful for text processing and pattern recognition.
