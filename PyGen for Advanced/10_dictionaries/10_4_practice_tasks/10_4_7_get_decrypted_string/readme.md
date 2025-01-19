# Frequency Analysis Decryption 🔐

## Description 📝

This program decrypts a secret word using frequency analysis. The encrypted string is processed, and the program maps the frequency of characters in the encrypted string to a predefined frequency distribution. The goal is to identify the correct letter substitutions based on the frequency of letters.

## Purpose 🎯

The purpose of this program is to demonstrate a basic method of cryptanalysis using frequency analysis. By using known frequencies of letters in the language, the program decrypts a message.

## How It Works 🔍

1. **Input**:
    - The user is prompted to enter the encrypted string.
    - The user provides a frequency distribution of letters, where each letter is paired with its repetition rate.
2. **Frequency Mapping**:
    - The program reads the frequency of letters and stores them in a dictionary.
3. **Flipping Dictionary**:
    - The dictionary is flipped, turning the frequency count into keys and letters into values.
4. **Decryption**:
    - The program counts the occurrence of each character in the encrypted string and maps that to the correct letter using the flipped dictionary.
5. **Output**:
    - The decrypted string is printed by substituting characters based on their frequencies.

## Output 📜

The program prints:

-   The decrypted version of the encrypted string based on frequency analysis.

### Example Input/Output:

**Input**:

```text
Enter the encrypted string: ABBA
Enter the number of letters: 2
Enter letter and repetition rate (e.g., A: 3): A: 1
Enter letter and repetition rate (e.g., A: 3): B: 2
```

**Output**:

```text
Decrypted string: DCBD
```

## Usage 📦

1. Copy the code into a Python file, e.g., `decrypt.py`.
2. Run the program.
3. Enter the encrypted string when prompted.
4. Provide the number of letter-repetition pairs.
5. Input the letter and repetition rate pairs.
6. The program will output the decrypted string.

### Example Run:

```python
# Sample run
Enter the encrypted string: ABBA
Enter the number of letters: 2
Enter letter and repetition rate (e.g., A: 3): A: 1
Enter letter and repetition rate (e.g., A: 3): B: 2
Output:
Decrypted string: DCBD
```

## Conclusion 🚀

This program offers a straightforward implementation of decryption using frequency analysis. While the approach is basic, it serves as an introduction to cryptography and cryptanalysis techniques.
