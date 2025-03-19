# Regular Expression for Matching Sequences in Format Xxxxx

## Description 📝

This **regular expression** is designed to match character sequences of the format **Xxxxx**, where:

-   **X** is any uppercase Latin letter (A–Z),
-   **x** is any digit (0–9).

## Purpose 🎯

This regex can be used for:

-   **Validating alphanumeric strings** where the first character is an uppercase letter followed by four digits.
-   **Extracting specific patterns** from a dataset.
-   **Checking user input** that follows this format.

## How It Works 🔍

The regex:

```regex
r'[A-Z]\d{4}'
```

### Explanation:

-   **`[A-Z]`** → Matches any **uppercase Latin letter** from `A` to `Z`.
-   **`\d{4}`** → Matches exactly **four digits** (0–9), ensuring the sequence ends with a digit pattern.

This pattern ensures the sequence starts with an uppercase letter, followed by exactly four digits.

## Output 📜

Example usage:

```python
import re

text = "Valid codes are A1234, B5678, and C9012. Invalid codes are a1234 and 12345."
regex = r'[A-Z]\d{4}'

matches = re.findall(regex, text)
print("Matches:", matches)
```

### Output:

```
Matches: ['A1234', 'B5678', 'C9012']
```

## Usage 📦

1. Save the regex in a Python script.
2. Use Python's `re` module to apply the regex to a string.
3. Run the script and check for valid matches.

## Conclusion 🚀

This regex `r'[A-Z]\d{4}'` is an efficient and concise solution for matching sequences that consist of one uppercase letter followed by exactly four digits.
It’s great for pattern matching and input validation.
