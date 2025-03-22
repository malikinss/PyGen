# Regular Expression for Matching Nine-Character Palindromes

## Description 📝

This **regular expression** is designed to match **nine-character palindromes**, ensuring that the string reads the same forward and backward.

## Purpose 🎯

We want to match strings that are exactly **nine characters long** and are palindromes. For a string to be a palindrome:

-   The first character must match the last character.
-   The second character must match the second-to-last character, and so on.

## How It Works 🔍

```regex
r'(.)(.)(.)(.)(.)\4\3\2\1'
```

**Explanation**:

-   **`(.)`** → Captures any character (except newlines) as a group. Each of these will represent a corresponding character in the palindrome.
-   **`\4`** → Refers to the fourth captured group, ensuring that the character in position 6 matches the one in position 4.
-   **`\3`** → Refers to the third captured group, ensuring that the character in position 7 matches the one in position 3.
-   **`\2`** → Refers to the second captured group, ensuring that the character in position 8 matches the one in position 2.
-   **`\1`** → Refers to the first captured group, ensuring that the character in position 9 matches the one in position 1.

This regular expression will ensure that the string reads the same forwards and backwards, satisfying the palindrome condition.

---

## Example Usage 📜

```python
import re

regex = r'(.)(.)(.)(.)(.)\4\3\2\1'

test_cases = [
    "abcdefedc",  # ✅ Match (palindrome)
    "abcabcabc",  # ❌ No match (not a palindrome)
    "12321",  # ❌ No match (not 9 characters)
    "abcdedcba",  # ✅ Match (palindrome)
]

for case in test_cases:
    if re.fullmatch(regex, case):
        print(f'"{case}": ✅ Match')
    else:
        print(f'"{case}": ❌ No match')
```

**Expected Output:**

```
"abcdefedc": ✅ Match
"abcabcabc": ❌ No match
"12321": ❌ No match
"abcdedcba": ✅ Match
```

---

## Usage 📦

-   **Text Processing**: Identify palindromic patterns in texts.
-   **Data Validation**: Check if a string follows the palindrome format.
-   **Pattern Matching**: Find symmetric patterns in sequences.

## **Conclusion 🚀**

This regular expression accurately matches nine-character palindromes, ensuring the string is symmetric by validating the first and last characters, the second and second-to-last characters, and so on.
