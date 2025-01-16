# Correct Identifiers 📝

## Description 📝

This program corrects a string of identifier names by ensuring that no duplicate identifiers remain. If an identifier appears more than once, it appends a postfix `_n` to the duplicate, where `n` is the number of times the identifier has already been encountered. The resulting string contains all the corrected identifiers, with no duplicates.

## Purpose 🎯

The purpose of this program is to process a string of identifier names, making sure there are no duplicates by modifying the repeating identifiers. It can be useful for automatically fixing naming conflicts in datasets or code, ensuring that all identifiers are unique while retaining their original form.

## How It Works 🔍

1. **Input**:
    - A space-separated string of identifiers.
2. **Processing**:
    - The program splits the input string into individual identifiers.
    - It keeps track of how many times each identifier has appeared.
    - For each repeating identifier, it appends a suffix `_n` to it, where `n` is the count of its previous occurrences.
3. **Output**:
    - A string containing the corrected identifiers with no duplicates.

## Output 📜

The program outputs a space-separated string of corrected identifiers, where duplicates have been resolved by adding a postfix to the repeating identifiers.

### Example:

**Input**:

```text
apple banana apple grape apple orange banana apple
```

**Output**:

```text
apple banana apple_1 grape apple_2 orange banana_1 apple_3
```

### Another Example:

**Input**:

```text
dog cat dog cat dog
```

**Output**:

```text
dog cat dog_1 cat_1 dog_2
```

## Usage 📦

1. Copy the code into a Python file, e.g., `correct_identifiers.py`.
2. Provide a string of identifiers as input when prompted.
3. The program will output the corrected identifiers string.

### Example Run:

```python
Enter identifier strings: apple banana apple grape apple orange banana apple
Output: apple banana apple_1 grape apple_2 orange banana_1 apple_3
```

## Conclusion 🚀

This program efficiently ensures that no identifier appears more than once in a given string by appending a postfix to the repeated identifiers. It can be useful in various scenarios where uniqueness of identifiers is crucial, such as in code refactoring or data handling.
