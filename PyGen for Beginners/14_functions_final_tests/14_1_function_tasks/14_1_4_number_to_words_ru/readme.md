# Number to Words (Russian) Converter 🇷🇺

## Description 📝

This Python script converts a natural number between 1 and 99 into its verbal description in Russian.
For example, the number `42` will be converted to "сорок два".

## Purpose 🎯

The `number_to_words_ru` function simplifies the process of translating numbers into Russian words, which can be useful for educational purposes, speech synthesis, or localization of software.

## How It Works 🔍

1. **Lists of Words**:

    - `ed` – Words for single digits (0-9).
    - `od` – Words for numbers 11-19.
    - `ds` – Words for multiples of 10 (10-90).

2. **Logic**:

    - For numbers between 1 and 9, the function returns the corresponding word from `ed`.
    - For numbers between 11 and 19, the function selects from `od`.
    - For multiples of 10 (10, 20, 30, etc.), the function selects from `ds`.
    - For numbers between 21 and 99, the function combines the tens (from `ds`) and the units (from `ed`).

3. **Example**:

    ```
    Enter a number between 1 and 99: 37
    Output: тридцать семь
    ```

4. **Edge Cases**:
    - `1` returns "один".
    - `10` returns "десять".
    - `99` returns "девяносто девять".

## Usage 📦

1. Copy the code into a Python file, e.g., `number_to_words_ru.py`.
2. Run the script in the terminal:
    ```bash
    python number_to_words_ru.py
    ```
3. Enter a number between 1 and 99.
4. The verbal description of the number in Russian will be printed.

## Conclusion 🚀

This script provides a simple yet effective way to convert numbers to their Russian verbal equivalent.
It leverages basic Python control structures and lists to achieve accurate results, making it a practical tool for small projects involving number-to-text conversion.
