# Bee and Geek Occurrence Counter

## Description 📝

This program processes multiple lines of input and counts:

-   The number of lines where the substring "bee" occurs at least twice.
-   The number of lines where the word "geek" occurs at least once.

## Purpose 🎯

The purpose of this program is to analyze a given set of lines and determine how many contain:

-   "bee" as a substring at least twice.
-   "geek" as a standalone word at least once.

This helps in analyzing patterns and specific word occurrences in text.

## How It Works 🔍

1. **Input**:

    - The program accepts an arbitrary number of input lines, each containing a mix of characters.

2. **Regex Matching**:
    - The program uses regular expressions:
        - `r'(bee).*?\1'` to find if "bee" appears at least twice in the line (non-overlapping).
        - `r'\bgeek\b'` to find "geek" as a whole word (bound by word boundaries).
3. **Counting**:

    - The program counts how many lines satisfy each of the conditions and outputs these counts separately.

4. **Output**:
    - The program outputs two numbers:
        - The first is the number of lines where "bee" occurs at least twice.
        - The second is the number of lines where "geek" occurs at least once.

## Output 📜

### Example Input:

```text
bee bee geek
hello geek bee
geek and bee geek
geek bee bee
bee bee bee
```

### Example Output:

```text
3
4
```

## Usage 📦

1. Save the program in a Python file (e.g., `bee_geek_counter.py`).
2. Run the script.
3. Enter lines, each on a separate line.
4. The program will output two numbers:
    - The first represents lines with "bee" at least twice.
    - The second represents lines with "geek" at least once.

## Conclusion 🚀

This program is useful for analyzing text and detecting specific patterns in lines.
It can help identify the frequency of certain substrings or words in larger datasets.
The use of regular expressions makes it both efficient and easy to extend for similar tasks.
