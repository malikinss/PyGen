# Find the Least Frequent Word 📉

## Description 📝

This program finds the word that occurs the least frequently in the provided input text, ignoring case and punctuation. If multiple words occur with the same frequency, it returns the lexicographically smallest one. The program works by cleaning the text, counting the occurrences of each word, and then selecting the least frequent word based on the specified conditions.

## Purpose 🎯

The purpose of this program is to identify the least frequent word in a string of text, ignoring case and punctuation. This can be useful for analyzing text to find uncommon words, which may help in various text processing tasks such as content analysis, keyword extraction, or data cleansing.

## How It Works 🔍

1. **Input**:
    - A string of text that may include words, spaces, and punctuation marks.
2. **Processing**:
    - The program normalizes the text by converting it to lowercase and removing punctuation marks.
    - It then counts the occurrences of each word and finds the word(s) with the minimum frequency.
    - If there are multiple such words, the program returns the lexicographically smallest one.
3. **Output**:
    - The least frequent word (case-insensitive and punctuation-removed) is returned.

## Output 📜

The program outputs the word that occurs least frequently in the text, after processing it according to the specified conditions.

### Example:

**Input**:

```text
apple apple banana apple! Orange, orange apple?
```

**Output**:

```text
banana
```

### Another Example:

**Input**:

```text
This is a test, test. This is just a test.
```

**Output**:

```text
just
```

## Usage 📦

1. Copy the code into a Python file, e.g., `find_least_frequent_word.py`.
2. Provide input text when prompted.
3. The program will return the least frequent word in the text.

### Example Run:

```python
Enter text: apple apple banana apple! Orange, orange apple?
Output: banana
```

## Conclusion 🚀

This program helps to find the least frequent word in a given text, regardless of case or punctuation. It can be helpful in processing and analyzing text data for tasks like keyword extraction, content analysis, or data cleaning.
