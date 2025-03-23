# Abbreviation Generator

## Description 📝

This program defines a function `abbreviate()`, which takes an input phrase and generates an abbreviation by extracting the initial letters of each word and subword that starts with a capital letter.
The abbreviation is then returned in uppercase.

## Purpose 🎯

The function is useful for creating abbreviations from phrases, particularly for phrases that consist of multiple words or compound words with capital letters.
It handles both standard words and capitalized subwords, making it suitable for abbreviating terms like "JavaScript Object Notation" into "JSON".

## How It Works 🔍

1. **The `abbreviate()` function** takes a string `phrase` as input.
2. **Regular Expression**: It uses a regular expression to identify the first letter of each word or capitalized subword.
    - The regular expression `\b[a-zA-Z]|[A-Z]` matches the first letter of each word or subword that begins with a capital letter.
3. **Output**: The function returns the generated abbreviation in uppercase.

## Output 📜

### Example Input:

```python
abbreviate("JavaScript Object Notation")
```

### Example Output:

```text
"JSON"
```

## Usage 📦

1. Define the `abbreviate()` function in your code.
2. Pass a phrase as the argument to the function.
3. The function will return the abbreviation formed from the capital letters of the phrase.

### Example Usage:

```python
print(abbreviate("HyperText Markup Language"))  # Output: "HTML"
```

## Conclusion 🚀

The `abbreviate()` function is a simple yet powerful tool for generating abbreviations from a given phrase, particularly useful for handling compound words or technical terms like programming languages or protocols.
