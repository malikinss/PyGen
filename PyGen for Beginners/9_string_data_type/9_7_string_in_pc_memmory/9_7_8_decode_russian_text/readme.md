# Russian Text Decoder 📝

## Description 📝

This program is designed to decode Russian text that has been corrupted due to a system crash.
After the crash, all letters in the Russian alphabet are displayed in the following format: `[u-<symbol number in Unicode>]`.
This decoder restores the original Russian letters by replacing these encoded sequences with their corresponding Unicode characters.

## Purpose 🎯

The purpose of this program is to take a string of text with corrupted Russian characters and output the correctly decoded version.
The program specifically decodes characters encoded in the format `[u-<symbol number in Unicode>]`, and replaces them with the corresponding Russian letter.
The letter `'Ё'` is excluded from the Russian alphabet in this program for simplicity.

## How It Works 🔍

1. The input string is examined for patterns that match the format `[u-<number>]`, where `<number>` is a Unicode value.
2. The program extracts each number, converts it to its corresponding Russian letter, and rebuilds the string.
3. Non-encoded characters are appended to the result unchanged.

## Output 📜

The program outputs a decoded string with the original Russian text.

### Example

```bash
Input: [u-1076][u-1080][u-1072][u-1074][u-1083][u-1074]
Output: привет
```

## Usage 📦

1. Copy the program code into a Python script file (e.g., `decode_russian.py`).
2. Run the script in your terminal or an IDE.
3. When prompted, enter the corrupted Russian text in the format `[u-<number>]`.
4. The program will output the correctly decoded text.

## Conclusion 🚀

This program is a simple but effective way to restore corrupted Russian text.
By converting encoded Unicode values back into readable characters, it helps you retrieve the original information that was lost due to the system crash.
