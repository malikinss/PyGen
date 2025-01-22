# Count Word Occurrences 📝

## Description 📝

This program counts the number of occurrences of each word in a given line of text.
It returns a list where each entry corresponds to the number of times a word has appeared in the text up to that point.

## Purpose 🎯

The purpose of this program is to count the occurrences of each word in a string of text and to display a sequence of counts where each count corresponds to the number of times the respective word has appeared so far.

## How It Works 🔍

1. **Input**:
    - A string `text` containing words separated by spaces.
2. **Processing**:
    - The program splits the text into words by spaces.
    - It then iterates through the list of words, counting their occurrences as it goes.
3. **Output**:
    - The program generates a list of integers representing the occurrence count of each word in the order they appear in the input text.

## Output 📜

The output is a space-separated list of integers. Each integer represents the count of the corresponding word as it appears in the input text.

### Example Input/Output:

**Input**:

```
Enter a line of text: яблоки груши яблоки апельсины груши
```

**Output**:

```
1 1 2 1 2
```

### Explanation:

-   The word "яблоки" appears twice: 1st and 3rd.
-   The word "груши" appears twice: 2nd and 5th.
-   The word "апельсины" appears once: 4th.

## Usage 📦

1. Copy the code into a Python file (e.g., `count_word_occurrences.py`).
2. Run the program and input a line of text when prompted.
3. The program will return a list of integers representing the count of occurrences for each word.

### Example Run:

```python
# Sample run
given_text = "яблоки груши яблоки апельсины груши"
occurrences = count_word_occurrences(given_text)
print(*occurrences)
```

**Output**:

```python
1 1 2 1 2
```

## Conclusion 🚀

This program is useful for analyzing the frequency of words in a text while maintaining the order of their occurrences.
It works efficiently even with repeated words, and it can be modified to handle various text formats.
