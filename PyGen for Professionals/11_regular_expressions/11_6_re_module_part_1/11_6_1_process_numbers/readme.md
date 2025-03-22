# Phone Number Parsing

## Description 📝

This program processes a list of phone numbers and extracts the country code, city code, and number in separate parts.
It handles phone numbers in two formats:

1. `<country code>-<city code>-<number>`
2. `<country code> <city code> <number>`

Where:

-   The country code and city code consist of 1 to 3 digits.
-   The number consists of 4 to 10 digits.
-   The separator between components is either a hyphen (`-`) or a space (` `), but not both in one phone number.

## Purpose 🎯

The purpose of this program is to:

-   Parse phone numbers and output their components in a structured format.
-   Ensure flexibility in handling different separators while maintaining a consistent output format.

## How It Works 🔍

1. **Input**:

    - The program reads multiple phone numbers, each on a separate line.

2. **Parsing**:

    - A **regular expression** is used to match the phone number patterns. The regex extracts:
        - **Country code** (1 to 3 digits).
        - **City code** (1 to 3 digits).
        - **Phone number** (4 to 10 digits).

3. **Output**:
    - For each phone number, the program prints the components (country code, city code, and number) in the following format:
        ```text
        Country code: <country code>, City code: <city code>, Number: <number>
        ```

## Output 📜

### Example Input:

```text
123-456-7890
1 234 567890
789-234-5678
```

### Example Output:

```text
Country code: 123, City code: 456, Number: 7890
Country code: 1, City code: 234, Number: 567890
Country code: 789, City code: 234, Number: 5678
```

## Usage 📦

1. Save the program in a Python file (e.g., `phone_number_parser.py`).
2. Run the script.
3. Input phone numbers as separate lines.
4. The program will process the input and print each phone number's components.

## Conclusion 🚀

This program efficiently parses phone numbers with varying formats and separates them into **country code**, **city code**, and **number** components.
It is versatile in handling different separators and ensures consistent output for easy readability.
