# Regular Expression for Matching Specific Words

## Description 📝

This **regular expression** ensures that the words **"a", "A", "an", and "An"** are matched **as whole words**, avoiding partial matches within other words.

## Purpose 🎯

We need to match the **exact words**:

-   **"a"**
-   **"A"**
-   **"an"**
-   **"An"**

This means:

-   **Case-sensitive variations** (`A`, `a`, `An`, `an`) must be included.
-   **The word must not be part of a larger word** (e.g., "another" should not match).

## How It Works 🔍

```regex
r'\b[Aa](n)?\b'
```

**Explanation**:

-   **`\b`** → Word boundary (ensures the match is a **standalone word**).
-   **`[Aa]`** → Matches either **"A"** or **"a"**.
-   **`(n)?`** → Matches an **optional "n"**, allowing both `"a"` and `"an"`.
-   **`\b`** → Ensures the match ends at a **word boundary**.

---

## Example Usage 📜

```python
import re

regex = r'\b[Aa](n)?\b'

test_cases = [
    "a",     # ✅ Match
    "A",     # ✅ Match
    "an",    # ✅ Match
    "An",    # ✅ Match
    "Another",   # ❌ No match (part of a word)
    "Banana",    # ❌ No match
    " an ",  # ✅ Match (surrounded by spaces)
    "(An)",  # ✅ Match (surrounded by non-word characters)
]

for case in test_cases:
    if re.search(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"a": ✅ Match
"A": ✅ Match
"an": ✅ Match
"An": ✅ Match
"Another": ❌ No match
"Banana": ❌ No match
" an ": ✅ Match
"(An)": ✅ Match
```

## Usage 📦

-   **Text Processing**: Identify and replace standalone words.
-   **Linguistic Analysis**: Detect articles in **natural language processing (NLP)**.
-   **Search & Validation**: Filter specific words in texts.

## **Conclusion 🚀**

This **regular expression** ensures precise detection of the words **"a", "A", "an", and "An"** while avoiding incorrect matches in larger words.
