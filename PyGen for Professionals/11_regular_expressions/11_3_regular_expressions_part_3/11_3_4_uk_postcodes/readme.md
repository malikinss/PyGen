# Regular Expression for UK Postcodes

## Description 📝

This **regular expression** ensures that a **UK postcode** follows the correct format as per official postal guidelines.

## Purpose 🎯

UK postcodes have a **structured format**, where:

1. **Starts with 1 or 2 uppercase letters** (`A-Z`).
2. **Followed by 1 digit** (`0-9`).
3. **An optional character** (either a **digit** or an **uppercase letter**).
4. **A mandatory space**.
5. **Followed by 1 digit** (`0-9`).
6. **Ends with 2 uppercase letters**, **excluding** `C, I, K, M, O, V`.

## How It Works 🔍

The regex:

```regex
r'[A-Z]{1,2}\d[A-Z0-9]? \d[ABDEFGHJLNPQRSTUWXYZ]{2}'
```

**Explanation:**

-   **`[A-Z]{1,2}`** → Matches **1 or 2 uppercase letters** at the start.
-   **`\d`** → Matches **a single digit** (`0-9`).
-   **`[A-Z0-9]?`** → Matches **an optional character**, which can be **a digit or an uppercase letter**.
-   **` ` (space)** → Ensures a **mandatory space** in the postcode.
-   **`\d`** → Matches **another digit** (`0-9`).
-   **`[ABDEFGHJLNPQRSTUWXYZ]{2}`** → Matches **exactly 2 uppercase letters**, excluding `C, I, K, M, O, V`.

## Output 📜

**Example Usage:**

```python
import re

regex = r'[A-Z]{1,2}\d[A-Z0-9]? \d[ABDEFGHJLNPQRSTUWXYZ]{2}'

test_cases = [
    "W1A 1AA",   # ✅ Valid
    "EC1A 1BB",  # ✅ Valid
    "B33 8TH",   # ✅ Valid
    "DN55 1PT",  # ✅ Valid
    "M1 1AB",    # ✅ Valid
    "L1 8IJ",    # ❌ Invalid (contains I)
    "AA123 BB",  # ❌ Invalid (extra digit)
]

for case in test_cases:
    if re.fullmatch(regex, case):
        print(f"{case}: ✅ Valid")
    else:
        print(f"{case}: ❌ Invalid")
```

**Expected Output:**

```
W1A 1AA: ✅ Valid
EC1A 1BB: ✅ Valid
B33 8TH: ✅ Valid
DN55 1PT: ✅ Valid
M1 1AB: ✅ Valid
L1 8IJ: ❌ Invalid
AA123 BB: ❌ Invalid
```

## Usage 📦

-   **Address Validation**: Ensures **UK postcodes** follow the correct format.
-   **E-commerce**: Helps in **shipping address validation**.
-   **Government & Postal Services**: Used for **sorting and verifying addresses**.

## Conclusion 🚀

This **regular expression** effectively validates **UK postcodes**, ensuring they conform to the **official format** while excluding **invalid characters**.
