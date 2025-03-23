# Subword Counter

## Description 📝

This program takes a **text string** and a **word** as input and determines how many times the word appears as a **subword** in the given text.

A **subword** is a sequence of characters that:

-   Matches `\w` (word character).
-   Is **surrounded by other word characters** (`\w` on both sides).

For example:

-   `"is"` is a subword of `"optimist"`, but **not** of `"this is a test"`.
-   `"age"` is **not** a subword of `"ageless"`, because it is not surrounded by `\w` on both sides.

The program is **case-sensitive**, meaning `"Python"` and `"python"` are treated as different words.

## Purpose 🎯

This script is useful for analyzing words **inside** other words without considering standalone words. It can be applied in **linguistic analysis, text processing, and pattern recognition** tasks.

## How It Works 🔍

1. **Reads input**:
    - First line: the full text.
    - Second line: the word to search.
2. **Uses a regex pattern**: `(?<=\w)word(?=\w)`
    - Ensures the word is **inside** another word.
    - Does **not** count standalone occurrences.
3. **Prints the number of matches**.

## Output 📜

### Example Input:

```text
optimist and realism have similar endings
is
```

### Example Output:

```text
1
```

Explanation: `"is"` appears **inside** `"optimist"`, but not elsewhere.

## Usage 📦

1. Save the script as `subword_counter.py`.
2. Run the script and enter:
    - A **text string** (first input).
    - A **word** (second input).
3. The output will be the number of times the word appears **as a subword**.

## Conclusion 🚀

This program helps identify **subwords** in a text efficiently using **regular expressions**.
It is useful for text analysis tasks where subword occurrences matter, such as **morphological studies, linguistic research, and pattern detection**.
