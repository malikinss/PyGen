# Cyrillic to Latin Transliteration

## Description 📝

This Python program reads a text file (`cyrillic.txt`) containing Cyrillic text and transliterates it to Latin characters based on a predefined mapping.
The result is saved in a new file (`transliteration.txt`). Characters not found in the transliteration dictionary are left unchanged.

## Purpose 🎯

The purpose of this script is to convert Cyrillic script to its Latin transliteration equivalent for better accessibility and use in systems that require Latin characters.

## How It Works 🔍

1. **Transliteration Dictionary**:

    - A predefined dictionary is used to map each Cyrillic character to its Latin equivalent (e.g., 'а' → 'a', 'б' → 'b', etc.).
    - The script handles both lowercase and uppercase letters.

2. **Reading the Input File**:

    - The program opens the input file (`cyrillic.txt`), reads its content character by character, and looks up the corresponding Latin character in the dictionary.

3. **Processing and Writing the Output**:

    - Each character is transliterated or left unchanged (for non-Cyrillic characters).
    - The transliterated text is then written to the output file (`transliteration.txt`).

4. **Character Case Handling**:
    - Cyrillic uppercase letters are transliterated to their Latin uppercase equivalents, preserving the case of the input text.

## Output 📜

### Example

#### **Input (`cyrillic.txt`)**

```
Привет мир! Как дела?
```

#### **Output (`transliteration.txt`)**

```
Privet mir! Kak dela?
```

## Usage 📦

1. Save the script as `transliteration.py`.
2. Create a file named `cyrillic.txt` with Cyrillic text.
3. Ensure the script and text files are in the same directory.
4. Run the script using:
    ```bash
    python transliteration.py
    ```
5. The transliterated text will be written to `transliteration.txt`.

## Conclusion 🚀

This script efficiently converts Cyrillic text into its Latin transliteration based on a predefined dictionary.
It preserves the original character case and ignores non-Cyrillic characters, making it suitable for a variety of use cases.
