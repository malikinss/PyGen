# Normalize Whitespace 🧹

## Description 📝

This program normalizes the whitespace in a string by replacing all sequences of multiple spaces, tabs, or newlines with a single space.
It also removes leading and trailing whitespace.

## Purpose 🎯

The function ensures that any arbitrary string has consistent, single spaces between words and no extra spaces at the beginning or end of the string.

## How It Works 🔍

1. **Takes Input**:

    - Accepts a string that may contain multiple spaces, tabs, or newlines.

2. **Normalizes Whitespace**:

    - Replaces all sequences of whitespace characters (spaces, tabs, and newlines) with a single space using a regular expression.

3. **Strips Leading and Trailing Whitespace**:

    - The `strip()` method is used to remove any leading or trailing spaces after normalization.

4. **Returns Normalized String**:
    - Outputs the string with normalized whitespace.

## Output 📜

### Example Input:

```python
string = "   Hello   world!   This  is    a test.  "
```

### Example Output:

```python
"Hello world! This is a test."
```

## Usage 📦

1. Call the function with the string:

    ```python
    normalized_string = normalize_whitespace("   Hello   world!   This  is    a test.  ")
    print(normalized_string)  # Output: "Hello world! This is a test."
    ```

2. The program will return the string with normalized whitespace and no leading or trailing spaces.

## Conclusion 🚀

This function ensures consistency by reducing excessive whitespace in strings, making the text easier to process and display.
