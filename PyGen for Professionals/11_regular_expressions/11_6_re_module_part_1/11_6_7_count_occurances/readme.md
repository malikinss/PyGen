# BeeGeek Mentions Counter

## Description 📝

This program counts how many lines (representing Twitter publications) contain the string "beegeek", regardless of case.
The string can appear in any part of the publication, and the program counts each mention in each line.

## Purpose 🎯

The purpose of this program is to analyze a list of publications and determine how many of them mention the string "beegeek" in any case, allowing it to capture variations like "BEEGEEK", "BeeGeek", or "beeGeek".

## How It Works 🔍

1. **Input**:
    - The program reads multiple lines of text (each representing a publication).
2. **Regex Matching**:
    - For each line, the program checks if the string "beegeek" appears in any case using a case-insensitive regular expression (`re.I`).
3. **Count Occurrences**:

    - The program counts how many lines contain the string "beegeek" and returns the total count.

4. **Output**:
    - The program outputs the total number of lines containing "beegeek".

## Output 📜

### Example Input:

```text
I love BEEGEEK courses!
When is the OOP course? @timur_guev
BEEGEEK, thanks for the courses, you are the best! #python #BeeGeek
```

### Example Output:

```text
2
```

## Usage 📦

1. Save the program in a Python file (e.g., `beegeek_mentions_counter.py`).
2. Run the script.
3. Enter or pipe in the publications (lines of text).
4. The program will output the count of lines containing the string "beegeek" in any case.

## Conclusion 🚀

This program provides a simple way to analyze Twitter-like publications and determine how many times the string "beegeek" appears, helping to track mentions or measure the popularity of "beegeek" in various posts.
