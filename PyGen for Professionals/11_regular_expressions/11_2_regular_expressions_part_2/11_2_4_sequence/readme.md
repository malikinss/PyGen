# Regular Expression for Matching Specific Character Sequences

## Description 📝

This **regular expression** is designed to match sequences of exactly **5 characters** that satisfy the following conditions:

-   The **first character** is a **lowercase Latin letter** (a–z).
-   The **second character** is an **arbitrary digit** (0–9).
-   The **third character** is a **lowercase Latin letter** (a–z).
-   The **fourth character** is an **uppercase Latin letter** (A–Z).
-   The **fifth character** is also an **uppercase Latin letter** (A–Z).

## Purpose 🎯

This regex can be used for:

-   **Validating strings** with a specific pattern of letters and digits.
-   **Extracting matching patterns** from a text where specific conditions apply.
-   **Enforcing input formats** for user-provided strings that need to follow this exact structure.

## How It Works 🔍

The regex:

```regex
r'[a-z]\d[a-z][A-Z]{2}'
```

### Explanation:

-   **`[a-z]`** → Matches any **lowercase Latin letter** (a to z).
-   **`\d`** → Matches any **digit** (0 to 9).
-   **`[a-z]`** → Matches any **lowercase Latin letter** (a to z).
-   **`[A-Z]{2}`** → Matches exactly **two uppercase Latin letters** (A to Z), ensuring the last two characters are uppercase.

This regex ensures that the sequence starts with a lowercase letter, followed by a digit, another lowercase letter, and ends with two uppercase letters.

## Output 📜

Example usage:

```python
import re

text = "Valid codes are a1bXY, c9dAB, and e2zZZ. Invalid codes are A1bXY and a1BxZ."
regex = r'[a-z]\d[a-z][A-Z]{2}'

matches = re.findall(regex, text)
print("Matches:", matches)
```

### Output:

```
Matches: ['a1bXY', 'c9dAB', 'e2zZZ']
```

## Usage 📦

1. Save the regex in a Python script.
2. Use Python's `re` module to apply the regex to a string.
3. Run the script and check for valid matches.

## Conclusion 🚀

The regex `r'[a-z]\d[a-z][A-Z]{2}'` efficiently matches sequences of 5 characters with the exact pattern of lowercase and uppercase Latin letters and digits, making it a useful tool for validating and extracting structured strings.
