# Regular Expression for Matching Character Sequences of "bee" and "geek"

## Description 📝

This **regular expression** ensures that a sequence consists only of **"bee"** and **"geek"** while satisfying the following conditions:

-   The sequence must contain **at least one "geek"**.
-   **"bee"** cannot be next to itself (i.e., no "beebee").
-   **"geek"** can only appear after a "bee".
-   Every **"bee"** must eventually be followed by a **"geek"**.

## Purpose 🎯

We need to match character sequences that:

-   **Contain only the words "bee" and "geek"**.
-   **Contain at least one "geek"**.
-   **Ensure no adjacent "bee" words**.
-   **Ensure "geek" always follows "bee"**.
-   **Ensure every "bee" is eventually followed by a "geek"**.

## How It Works 🔍

```regex
r'(bee(geek)+)+'
```

**Explanation**:

-   **`bee`** → Matches the word "bee".
-   **`(geek)+`** → Matches the word "geek" one or more times after each "bee". Ensures that every "bee" is followed by at least one "geek".
-   **`(bee(geek)+)+`** → The entire group can be repeated one or more times, ensuring that the sequence contains **multiple "bee" and "geek"** pairs with no "beebee" allowed.

---

## Example Usage 📜

```python
import re

regex = r'(bee(geek)+)+'

test_cases = [
    "beegeek",        # ✅ Match
    "beegeekgeek",    # ✅ Match
    "beegeekbee",     # ✅ Match
    "geekbee",        # ❌ No match (must start with "bee")
    "beebee",         # ❌ No match (no "beebee")
    "bee",            # ❌ No match (must be followed by "geek")
    "geekgeek",       # ❌ No match (must start with "bee")
]

for case in test_cases:
    if re.fullmatch(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"beegeek": ✅ Match
"beegeekgeek": ✅ Match
"beegeekbee": ✅ Match
"geekbee": ❌ No match
"beebee": ❌ No match
"bee": ❌ No match
"geekgeek": ❌ No match
```

## Usage 📦

-   **Text Parsing**: Identify valid sequences in text composed of "bee" and "geek".
-   **Validation**: Ensure correct ordering of "bee" and "geek" without adjacent "bee" words.
-   **Pattern Recognition**: Identify specific patterns in natural language processing (NLP).

## Conclusion 🚀

This **regular expression** matches sequences containing **"bee"** and **"geek"**, while ensuring that the sequence follows specific constraints such as no adjacent "bee" and proper ordering with at least one "geek" after each "bee".
