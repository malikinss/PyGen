# CaesarCipher Class Implementation

## Description 📝

The provided code implements the `CaesarCipher` class, which encrypts and decrypts text using the Caesar cipher with a specified shift.
The class supports encryption via the `encode()` method (shifting letters to the right) and decryption via the `decode()` method (shifting letters to the left).
It preserves the case of letters, only processes Latin letters (a-z, A-Z), and leaves non-letter characters unchanged.
The implementation uses a helper method `_code` to handle the core transformation logic for both encryption and decryption.

## Purpose 🎯

Intended for applications requiring simple text encryption/decryption, such as educational exercises, basic security demonstrations, or puzzles involving the Caesar cipher.

## How It Works 🔍

-   **Class Definition**:
    -   `CaesarCipher` is a class with methods for encryption and decryption.
    -   Uses type hints for clarity (`int`, `str`).
-   **Initialization (`__init__`)**:
    -   Takes a `shift` parameter (integer from 1 to 26).
    -   Stores `shift` as `self.shift`.
-   **Helper Method (`_code`)**:
    -   Takes `text` (string to process) and `shift` (positive for encoding, negative for decoding).
    -   Iterates over each character in `text`:
        -   If the character is a Latin letter (`c.isalpha() and c.isascii()`):
            -   Determines the ASCII base (`65` for uppercase, `97` for lowercase).
            -   Applies the Caesar shift: `(ord(c) - base + shift) % 26 + base`.
            -   Converts the result back to a character with `chr`.
        -   Otherwise, appends the character unchanged.
    -   Joins processed characters into a string and returns it.
-   **encode Method**:
    -   Calls `_code` with `self.shift` to shift letters to the right.
    -   Example: `CaesarCipher(5).encode('Beegeek')` → `'Gjjljjp'`.
-   **decode Method**:
    -   Calls `_code` with `-self.shift` to shift letters to the left.
    -   Example: `CaesarCipher(5).decode('Gjjljjp')` → `'Beegeek'`.
-   **Behavior**:
    -   Preserves letter case (e.g., `B` → `G`, `e` → `j` with shift 5).
    -   Only transforms Latin letters; non-letters (e.g., digits, Cyrillic) remain unchanged.
    -   Handles shifts in the range [1, 26] as guaranteed.
    -   Uses modulo 26 to wrap around the alphabet (e.g., `z` + 1 → `a`).

## Verification ✅

Implementation satisfies requirements:

-   **Initialization**:
    -   Accepts a `shift` value (1 to 26).
    -   Example: `CaesarCipher(5)` initializes correctly.
-   **encode Method**:
    -   Encrypts by shifting Latin letters to the right by `shift`.
    -   Preserves case and non-letters.
    -   Example: `CaesarCipher(5).encode('Beegeek')` → `'Gjjljjp'`.
    -   Example with non-letters: `CaesarCipher(5).encode('Биgeek123')` → `'Биljjp123'`.
-   **decode Method**:
    -   Decrypts by shifting Latin letters to the left by `shift`.
    -   Preserves case and non-letters.
    -   Example: `CaesarCipher(5).decode('Gjjljjp')` → `'Beegeek'`.
    -   Example with non-letters: `CaesarCipher(5).decode('Биljjp123')` → `'Биgeek123'`.
-   **Correctness**:
    -   `_code` handles both encoding and decoding with a single logic path.
    -   Case preservation: Uses separate bases (65 for A-Z, 97 for a-z).
    -   Non-letters: Left unchanged via `isalpha() and isascii()` check.
    -   Modulo 26 ensures alphabet wrap-around.
    -   No validation needed, as shift is guaranteed in [1, 26] and inputs are valid.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `isalpha() and isascii()` ensures only Latin letters (a-z, A-Z) are processed, correctly handling non-Latin (e.g., Cyrillic) and non-letter characters.
    -   `(ord(c) - base + shift) % 26 + base` correctly implements the Caesar shift, preserving case and wrapping around the alphabet.
    -   Using `shift` for encoding and `-shift` for decoding ensures inverse operations.
    -   The implementation is symmetric: decoding an encoded string returns the original.
-   **Performance**:
    -   Initialization: O(1) for storing `shift`.
    -   `_code`: O(n) for processing n characters in the input string.
    -   `encode` and `decode`: O(n) via `_code`.
    -   Efficient for typical string lengths.
-   **Design**:
    -   Single `_code` method reduces code duplication by handling both encoding and decoding.
    -   Type hints (`int`, `str`) clarify method signatures.
    -   Simple list-based character processing is clear and maintainable.
    -   No external dependencies, relying only on standard library.
-   **Alternatives**:
    -   String translation table (`str.maketrans`): Possible but less readable for case handling.
    -   Precomputed alphabet mapping: Faster for repeated calls but unnecessary for this task.
    -   Separate encode/decode logic: More verbose, less DRY.
-   **Extensibility**:
    -   Easily extended to support custom alphabets or additional transformations.
    -   Could add validation (e.g., shift range) if needed.
-   **Edge Cases**:
    -   Empty string: Returns `''`.
    -   Non-Latin letters (e.g., Cyrillic): Left unchanged (e.g., `Б` remains `Б`).
    -   Special characters (e.g., `123`, `@`): Left unchanged.
    -   Maximum shift (26): Effectively no shift, but handled correctly via modulo.
    -   Case preservation: Uppercase and lowercase letters shift within their respective alphabets.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Create cipher instance
cipher = CaesarCipher(5)

# Test encoding
print(cipher.encode('Beegeek'))  # Gjjljjp
print(cipher.encode('Биgeek123'))  # Биljjp123
print(cipher.encode('ABC'))  # FGH (uppercase preserved)
print(cipher.encode('xyz'))  # cde (wrap-around)

# Test decoding
print(cipher.decode('Gjjljjp'))  # Beegeek
print(cipher.decode('Биljjp123'))  # Биgeek123
print(cipher.decode('FGH'))  # ABC
print(cipher.decode('cde'))  # xyz

# Test with different shift
cipher2 = CaesarCipher(1)
print(cipher2.encode('abc'))  # bcd
print(cipher2.decode('bcd'))  # abc

# Test empty string and special characters
print(cipher.encode(''))  # ''
print(cipher.encode('123!@#'))  # 123!@#
```

## Conclusion 🚀

The `CaesarCipher` class implementation is precise, correctly implementing encryption and decryption with a specified shift while preserving letter case and leaving non-Latin and non-letter characters unchanged. The shared `_code` method ensures DRY code, and the implementation is efficient and extensible.
It is ideal for cryptographic exercises or teaching Caesar cipher concepts, fully compliant with the task’s requirements.
