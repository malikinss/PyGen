# Custom Alphabet Translator 📝

## Description 📝

This program translates an input text using a user-defined custom alphabet.
The custom alphabet is provided as a string, where each character corresponds to a letter in the Latin alphabet (`a-z`).
Uppercase letters are also mapped accordingly.

## Purpose 🎯

The goal of this program is to allow translation of a text based on a user-specified mapping of the Latin alphabet.
It can be useful for simple ciphers, custom encoding, or language experiments.

## How It Works 🔍

1. The program first reads a string defining the custom alphabet mapping.
    - The first character corresponds to `a`, the second to `b`, ..., the 26th to `z`.
2. It then reads the text that needs to be translated.
3. The program builds a dictionary mapping Latin letters (`a-z`) to the user-defined characters.
4. It translates the input text:
    - If a letter is uppercase, its mapped character is also converted to uppercase.
    - Non-Latin characters remain unchanged.
5. The translated text is printed.

## Output 📜

The output is the transformed text where Latin letters are replaced according to the user-provided mapping.

### Example:

**Input:**

```text
αβγδεζηθικλμνξοπρστυφχψω
Hello, World!
```

**Output:**

```text
Ηελλο, Ωορλδ!
```

## Usage 📦

1. The user provides a mapping string (26 characters, one per letter in the Latin alphabet).
2. The user inputs the text to be translated.
3. The program outputs the translated text.

## Conclusion 🚀

This program efficiently maps Latin letters to a custom alphabet while preserving non-Latin characters, making it useful for encoding and custom linguistic experiments.
