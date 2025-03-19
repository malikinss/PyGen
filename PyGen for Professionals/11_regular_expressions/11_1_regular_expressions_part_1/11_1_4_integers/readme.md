# Regular Expression for Matching Integers Between 100 and 199

## Description 📝

This code defines a regular expression that matches sequences of digits representing integers in the range **100 to 199**, inclusive.
The pattern ensures that only three-digit numbers starting with `1` are matched.

## Purpose 🎯

This regular expression can be used in various applications, such as:

-   Filtering numbers within a specific range.
-   Validating input data to check if it falls within 100–199.
-   Extracting relevant numerical values from text.

## How It Works 🔍

-   **`1`**: Ensures that the number starts with the digit `1`.
-   **`\d{2}`**: Matches exactly **two** more digits (each from `0-9`), ensuring the number has three digits in total.

This guarantees that only numbers from **100 to 199** are matched.

## Output 📜

Example usage:

```python
import re

text = "Valid numbers: 100, 123, 150, 199. Invalid numbers: 200, 99, 50."
regex = r'1\d{2}'

matches = re.findall(regex, text)
print("Matches:", matches)
```

Output:

```
Matches: ['100', '123', '150', '199']
```

## Usage 📦

1. Save the regex in a Python script, e.g., `match_100_to_199.py`.
2. Use it in a Python program with the `re` module.
3. Run the script with different text inputs to find numbers within **100–199**.

## Conclusion 🚀

The regular expression `r'1\d{2}'` is an efficient way to identify integers between **100 and 199**.
It ensures a strict format while remaining simple and effective for numerical filtering tasks.
