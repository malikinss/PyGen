# Regular Expression for Matching Words with Repeated Letters

## Description 📝

This **regular expression** matches words that contain **repeated letters** at least once.

## Purpose 🎯

We need to match words that contain **two or more identical letters** in them. The regular expression ensures that:

-   The word can have any number of characters, as long as one of them repeats.
-   The repeated letter can occur anywhere in the word.

## How It Works 🔍

```regex
r'\w*(\w)\w*\1\w*'
```

**Explanation**:

-   **`\w*`** → Matches any number of word characters (letters, digits, and underscores) before and after the repeated letter.
-   **`(\w)`** → Captures a single word character (any letter, digit, or underscore).
-   **`\w*`** → Matches any number of word characters after the captured character.
-   **`\1`** → Refers to the first captured character, ensuring that the same letter is repeated somewhere later in the word.
-   **`\w*`** → Matches any number of word characters following the repeated letter.

This regular expression will ensure that the word contains at least one repeated letter, no matter where it occurs in the word.

---

## Example Usage 📜

```python
import re

regex = r'\w*(\w)\w*\1\w*'

test_cases = [
    "apple",  # ✅ Match (repeated 'p')
    "banana",  # ✅ Match (repeated 'a')
    "cat",    # ❌ No match (no repeated letters)
    "hello",  # ✅ Match (repeated 'l')
    "world",  # ❌ No match (no repeated letters)
]

for case in test_cases:
    if re.search(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"apple": ✅ Match
"banana": ✅ Match
"cat": ❌ No match
"hello": ✅ Match
"world": ❌ No match
```

---

## Usage 📦

-   **Text Processing**: Identify words with repeated letters.
-   **Data Validation**: Filter words containing duplicates in string-based systems.
-   **Pattern Matching**: Find words with repeated characters in larger texts.

## Conclusion 🚀

This **regular expression** effectively matches words containing repeated letters, ensuring that at least one letter appears more than once in the word.
