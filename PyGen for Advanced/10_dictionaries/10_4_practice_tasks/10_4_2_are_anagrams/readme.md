# Anagram Checker 📝

## Description 📝

This program determines whether two given words are anagrams. An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all original letters exactly once. For example, the words "evil" and "live" are anagrams.

## Purpose 🎯

The program is designed to verify if two words are anagrams, helping users identify relationships between words or phrases in various linguistic and cryptographic contexts.

## How It Works 🔍

1. **Input**:
    - The program prompts the user to enter two words.
2. **Character Frequency Calculation**:
    - Each word is processed to count the frequency of its characters.
    - A helper function `count_character_frequencies` creates a dictionary for each word, where keys are characters and values are their counts.
3. **Comparison**:
    - The program compares the frequency dictionaries of the two words.
    - If they match, the words are anagrams.
4. **Output**:
    - The program outputs "YES" if the words are anagrams and "NO" otherwise.

## Output 📜

The program prints:

-   "YES" if the words are anagrams.
-   "NO" if they are not.

### Example Input/Output:

**Input**:

```text
Enter the first word: evil
Enter the second word: live
```

**Output**:

```text
YES
```

**Input**:

```text
Enter the first word: hello
Enter the second word: world
```

**Output**:

```text
NO
```

## Usage 📦

1. Copy the code into a Python file, e.g., `anagram_checker.py`.
2. Run the program.
3. Enter the two words when prompted.

### Example Run:

```python
# Sample run
Enter the first word: evil
Enter the second word: live
Output: YES
```

## Conclusion 🚀

This program is a simple yet effective tool for checking anagrams. It highlights the importance of character arrangement and serves as a useful utility in language processing and word games.
