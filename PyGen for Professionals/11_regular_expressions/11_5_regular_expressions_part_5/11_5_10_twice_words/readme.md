# Regular Expression for Matching Words Written Twice in a Row

## Description 📝

This **regular expression** matches sequences where a word is written twice in a row.
The words can be separated by one or more spaces.

## Purpose 🎯

We need to match:

-   A **word** (a sequence of characters that match `\w` surrounded by word boundaries `\b`).
-   The word should be **repeated twice**, separated by one or more spaces.

## How It Works 🔍

```regex
r'(\b\w+\b)\s+\1'
```

**Explanation**:

-   **`\b`** → Word boundary (ensures the match starts at the beginning of a word).
-   **`\w+`** → Matches one or more word characters (letters, digits, or underscores).
-   **`\b`** → Word boundary (ensures the match ends at the end of the word).
-   **`\s+`** → Matches one or more space characters.
-   **`\1`** → Refers back to the first capturing group, ensuring that the same word is repeated after the space(s).

This regular expression will match words that are written twice in a row, separated by any amount of space.

---

## Example Usage 📜

```python
import re

regex = r'(\b\w+\b)\s+\1'

test_cases = [
    "hello hello",  # ✅ Match (word repeated)
    "hello   hello",  # ✅ Match (word repeated with multiple spaces)
    "world world",  # ✅ Match (word repeated)
    "hello world",  # ❌ No match (words are different)
    "this is a test test",  # ❌ No match (only one pair of repeated words)
    "hello 123 hello",  # ✅ Match (word repeated with numbers)
    "word_word word_word",  # ❌ No match (special characters are part of the word)
]

for case in test_cases:
    if re.search(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"hello hello": ✅ Match
"hello   hello": ✅ Match
"world world": ✅ Match
"hello world": ❌ No match
"this is a test test": ❌ No match
"hello 123 hello": ✅ Match
"word_word word_word": ❌ No match
```

---

## Usage 📦

-   **Text Processing**: To detect repeated words in text.
-   **Data Cleaning**: To remove accidental duplicates or repeated words in datasets.
-   **Search & Validation**: To identify patterns of redundancy in documents.

## Conclusion 🚀

This **regular expression** matches instances where a word is written twice in a row, separated by spaces, ensuring precise word duplication detection.
