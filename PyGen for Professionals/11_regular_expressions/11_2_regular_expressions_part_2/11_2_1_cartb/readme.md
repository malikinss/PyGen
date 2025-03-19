# Regular Expression for Matching "car", "cat", and "cab"

## Description 📝

This **regular expression** is designed to match **three specific words**: `"car"`, `"cat"`, and `"cab"`.
It uses a **character set** to simplify the pattern.

## Purpose 🎯

The regex can be used for:

-   **Filtering specific words** in a text.
-   **Validating predefined inputs** containing "car", "cat", or "cab".
-   **Extracting relevant words** from larger text datasets.

## How It Works 🔍

The regex:

```regex
r'ca[rtb]'
```

### Explanation:

-   **`ca`** → Matches the common prefix `"ca"` in all three words.
-   **`[rtb]`** → Matches exactly **one** of the characters **`r`**, **`t`**, or **`b`**, completing the words:
    -   `"car"` (matches because `r` is in the set)
    -   `"cat"` (matches because `t` is in the set)
    -   `"cab"` (matches because `b` is in the set)

## Output 📜

Example usage:

```python
import re

text = "I saw a cat, a car, and a cab, but not a cap or cam."
regex = r'ca[rtb]'

matches = re.findall(regex, text)
print("Matches:", matches)
```

### Output:

```
Matches: ['cat', 'car', 'cab']
```

## Usage 📦

1. Store the regex in a Python script.
2. Use Python's `re` module to apply the regex.
3. Run the script with different text inputs to verify matches.

## Conclusion 🚀

By using a **character set (`[rtb]`)**, we avoid writing multiple explicit alternatives (e.g., `car|cat|cab`), making the regex **shorter, more readable, and efficient**.
