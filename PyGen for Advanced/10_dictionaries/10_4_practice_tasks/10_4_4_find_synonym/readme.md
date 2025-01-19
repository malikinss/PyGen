# Synonym Finder 📝

## Description 📝

This program determines a synonym for a given word based on a dictionary of word pairs. The dictionary is constructed from pairs of synonymous words inputted by the user. The program then retrieves the synonym for a given word, ensuring that each word in the dictionary has a valid synonym.

## Purpose 🎯

The purpose of this program is to provide an easy way to look up synonyms for words from a pre-defined dictionary. This could be useful in language tools, vocabulary enhancement, or any application requiring synonym lookup.

## How It Works 🔍

1. **Input**:
    - The program prompts the user to input a certain number of synonym pairs.
    - Each pair consists of a word and its synonym.
2. **Dictionary Construction**:
    - The pairs are stored in a dictionary, allowing the program to quickly retrieve the synonym for any given word.
3. **Synonym Lookup**:
    - The program asks for a word and returns its corresponding synonym from the dictionary.
4. **Output**:
    - The synonym for the provided word is printed.

## Output 📜

The program prints:

-   The synonym of the given word.

### Example Input/Output:

**Input**:

```text
Enter the number of synonym pairs: 2
Enter a word and its synonym: Happy Joyful
Enter a word and its synonym: Sad Unhappy
Enter a word to find its synonym: Happy
```

**Output**:

```text
Joyful
```

**Input**:

```text
Enter the number of synonym pairs: 2
Enter a word and its synonym: Beautiful Lovely
Enter a word and its synonym: Smart Intelligent
Enter a word to find its synonym: Intelligent
```

**Output**:

```text
Smart
```

## Usage 📦

1. Copy the code into a Python file, e.g., `synonym_finder.py`.
2. Run the program.
3. Enter the number of synonym pairs when prompted.
4. Input each synonym pair.
5. Enter the word for which you want to find a synonym.

### Example Run:

```python
# Sample run
Enter the number of synonym pairs: 3
Enter a word and its synonym: Brave Courageous
Enter a word and its synonym: Happy Cheerful
Enter a word and its synonym: Intelligent Bright
Enter a word to find its synonym: Brave
Output: Courageous
```

## Conclusion 🚀

This program helps users find synonyms of words from a predefined set of pairs, making it a great tool for vocabulary building, word games, or text processing tasks.
