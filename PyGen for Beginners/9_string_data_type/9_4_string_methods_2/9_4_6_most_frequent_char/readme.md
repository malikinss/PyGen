# Most Frequent Character Finder 🔍

## Description 📝

This program identifies the character that appears most frequently in a given string of text. In case of a tie, the program outputs the last character in the order of their appearance.

## Purpose 🎯

The purpose of this program is to find the most frequent character in a string, distinguishing between uppercase and lowercase letters, as well as letters from different alphabets such as Russian and English.

## How It Works 🔍

1. The program takes a string as input.
2. It counts the frequency of each character in the string.
3. It returns the most frequent character, with a preference for the last character in case of ties.

### Example:

```bash
Input: "abCccde"
Output: c

Input: "aabbcc"
Output: c

Input: "AaBbCc"
Output: C
```

## Output 📜

The program will output the most frequent character in the input string, taking into account case sensitivity and resolving ties by the last character encountered.

## Conclusion 🚀

This program serves as a simple character analysis tool, useful for applications such as text analysis and frequency-based encoding or debugging.
