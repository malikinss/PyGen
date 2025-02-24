# Vowel Case Converter 📝

## Description 📝

The program converts all lowercase Latin vowels in a given string to uppercase while keeping the rest of the characters unchanged.

## Purpose 🎯

To correct a faulty implementation of a function that was meant to replace all Latin vowels with uppercase letters.

## How It Works 🔍

1. The function `swapcase_vowels2(string)`:
    - Takes a string as input.
    - Defines a string `vowels` containing lowercase Latin vowels.
    - Uses a generator expression inside `''.join()` to iterate over each character in the string:
        - If the character is a vowel, it is converted to uppercase.
        - If the character is not a vowel, it remains unchanged.
2. The function returns the modified string.

## Output 📜

**Example Input:**

```python
"hello world"
```

**Example Output:**

```python
"hEllO wOrld"
```

## Usage 📦

1. Call the function `swapcase_vowels2()` and pass the string you want to modify.
2. The returned string will have all vowels in uppercase.

## Conclusion 🚀

The function is now fixed and works as expected, efficiently converting vowels to uppercase in a given string.
