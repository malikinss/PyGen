# Convert Words to ASCII Codes 📖

## Description 📝

This program takes a list of words and returns a dictionary where each word is associated with a list of ASCII codes corresponding to the characters of that word.

## Purpose 🎯

The purpose of this program is to provide a simple way to convert words into their ASCII code representations. This can be useful in encoding, encryption, or various text processing tasks.

## How It Works 🔍

1. **Input**:
    - A list of words.
2. **Processing**:
    - For each word in the list, the program iterates over each character and retrieves its corresponding ASCII value using the `ord()` function.
3. **Output**:
    - The program outputs a dictionary where the keys are the words, and the values are lists containing the ASCII codes of the characters in those words.

## Output 📜

The program outputs a dictionary where each word from the input list is a key, and the corresponding value is a list of ASCII codes for each character in that word.

### Example Input/Output:

**Input**:

```python
words = ['yes', 'hello']
```

**Output**:

```python
{
    'yes': [121, 101, 115],
    'hello': [104, 101, 108, 108, 111]
}
```

## Usage 📦

1. Copy the code into a Python file (e.g., `ascii_codes.py`).
2. Call the `get_ascii_codes()` function, passing a list of words as an argument.
3. The function will return a dictionary with each word as the key and the corresponding list of ASCII codes for that word.

### Example Run:

```python
# Sample run
words = ['hello', 'python', 'world']
result = get_ascii_codes(words)
print(result)
```

**Output**:

```python
{
    'hello': [104, 101, 108, 108, 111],
    'python': [112, 121, 116, 104, 111, 110],
    'world': [119, 111, 114, 108, 100]
}
```

## Conclusion 🚀

This program efficiently converts words into their ASCII codes, which can be useful for text analysis, cryptography, or even for understanding how computers represent characters.
