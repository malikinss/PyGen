# Caesar Cipher Decoder 🕵️‍♂️🔓

## Description 📝

This program decodes messages encrypted with the Caesar cipher, a simple substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.
By reversing this process, the program retrieves the original message.

## Purpose 🎯

To demonstrate the decoding of a Caesar cipher and explore modular arithmetic for character manipulation.

## How It Works 🔍

1. **Input:**
    - The **shift** value (number of positions letters were shifted).
    - The **encoded message** (string of lowercase letters).
2. **Decoding:**
    - Each character in the encoded string is processed:
        - The program reverses the shift using the formula:
            ```
            DecodedChar = (EncodedChar - Shift) mod 26
            ```
        - The decoded character is appended to the result.
3. **Output:** The program displays the decoded message.

### Example:

```bash
Input: 3 khoor
Output: hello
```

### Explanation:

-   The cipher shifts each letter forward by 3:
    -   `k -> h`, `h -> e`, `o -> l`, etc.
-   Decoding shifts them backward by 3 to retrieve the original text.

## Output 📜

-   A single string representing the decoded message.

## Usage 📦

1. Run the program in a Python environment.
2. Provide the shift value as an integer.
3. Enter the encoded string of lowercase letters.
4. View the decoded result in plaintext.

### Notes:

-   The program assumes the input contains only lowercase letters.
-   The modular arithmetic ensures the decoding wraps correctly at the alphabet boundaries.

## Conclusion 🚀

This decoder is a great starting point for understanding encryption and decryption techniques and the limitations of the Caesar cipher in secure communication.
