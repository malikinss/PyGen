# Regular Expression for PAN (Permanent Account Number) Validation

## Description 📝

The **Permanent Account Number (PAN)** is a **10-character unique identifier** assigned to taxpayers in **India**. The **format** follows strict rules:

-   **First 5 characters** → **Uppercase Latin letters** (`A-Z`).
-   **Next 4 characters** → **Digits** (`0-9`).
-   **Last character** → **Uppercase Latin letter** (`A-Z`).

## Purpose 🎯

This **regular expression** ensures that:

1. The PAN **always consists of 10 characters**.
2. The **first five** characters are **uppercase English letters**.
3. The **next four** characters are **digits (0-9)**.
4. The **last character** is an **uppercase English letter**.

## How It Works 🔍

The regex:

```regex
r'[A-Z]{5}\d{4}[A-Z]'
```

## Explanation:

-   **`[A-Z]{5}`** → Matches **exactly 5 uppercase Latin letters**.
-   **`\d{4}`** → Matches **exactly 4 digits**.
-   **`[A-Z]`** → Matches **exactly 1 uppercase Latin letter**.

## Output 📜

**Example Usage:**

```python
import re

regex = r'[A-Z]{5}\d{4}[A-Z]'

test_cases = [
    "ABCDE1234F",  # ✅ Valid
    "abcde1234f",  # ❌ Invalid (lowercase letters)
    "ABCD12345F",  # ❌ Invalid (only 4 letters at the start)
    "ABCDE12345",  # ❌ Invalid (last character should be a letter)
    "ABCDE12F34",  # ❌ Invalid (wrong digit-letter placement)
]

for pan in test_cases:
    if re.fullmatch(regex, pan):
        print(f"{pan} ✅ Valid PAN")
    else:
        print(f"{pan} ❌ Invalid PAN")
```

**Expected Output:**

```
ABCDE1234F ✅ Valid PAN
abcde1234f ❌ Invalid PAN
ABCD12345F ❌ Invalid PAN
ABCDE12345 ❌ Invalid PAN
ABCDE12F34 ❌ Invalid PAN
```

## Usage 📦

-   **Tax Filing Systems**: Ensure valid **PAN** numbers are used in official documents.
-   **Banking & Finance**: PAN validation for **KYC (Know Your Customer)**.
-   **Government Portals**: Verify PAN format before allowing **registrations**.
-   **Data Validation**: Ensure **correct PAN structure** before storage or processing.

## Conclusion 🚀

This **regular expression** is a simple yet powerful way to validate **PAN numbers** in India, ensuring they follow the correct **10-character structure**.
