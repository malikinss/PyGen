# Sentence Anagram Checker 📝

## Description 📝

This program determines whether two given sentences are anagrams. An anagram is a sentence formed by rearranging the characters of another sentence, while ignoring case, spaces, and punctuation marks. The program compares the two sentences after cleaning and counting their character frequencies.

## Purpose 🎯

The program is designed to check whether two sentences, when stripped of spaces, punctuation, and case, are anagrams of each other. This could be useful in language processing, cryptography, or word games.

## How It Works 🔍

1. **Input**:
    - The program prompts the user to enter two sentences.
2. **Text Cleaning**:
    - It removes all spaces, punctuation marks, and converts all characters to lowercase.
3. **Character Frequency Calculation**:
    - After cleaning the sentences, the program calculates the frequency of each character in both sentences.
4. **Comparison**:
    - The program compares the character frequencies of both sentences.
    - If the frequencies match, the sentences are anagrams.
5. **Output**:
    - The program outputs "YES" if the sentences are anagrams and "NO" otherwise.

## Output 📜

The program prints:

-   "YES" if the sentences are anagrams.
-   "NO" if they are not.

### Example Input/Output:

**Input**:

```text
Enter the first sentence: The cat
Enter the second sentence: Act the
```

**Output**:

```text
YES
```

**Input**:

```text
Enter the first sentence: Hello world!
Enter the second sentence: Goodbye world
```

**Output**:

```text
NO
```

## Usage 📦

1. Copy the code into a Python file, e.g., `sentence_anagram_checker.py`.
2. Run the program.
3. Enter the two sentences when prompted.

### Example Run:

```python
# Sample run
Enter the first sentence: The cat
Enter the second sentence: Act the
Output: YES
```

## Conclusion 🚀

This program effectively checks for sentence anagrams by eliminating unnecessary characters and focusing on the core characters in each sentence. It can be used for fun, games, or as a utility in text processing tasks.
