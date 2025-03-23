# British-American Spelling Counter (Our/Or)

## Description 📝

This program counts the occurrences of a word in a text, considering both its **British** and **American** spellings.
Specifically, it handles cases where the word ends in **-our** (British English) or **-or** (American English), as in the words **"colour"** (British) and **"color"** (American).

The program is case-insensitive and will count both variations of the word in any case (e.g., "color" and "colour").

## Purpose 🎯

This script is useful for counting words in a text that might be spelled differently in **British** and **American** English, particularly when it comes to words that use the letter **"u"** (British) versus those that don't (American).

## How It Works 🔍

1. **Reads input**:
    - First line: the word in the **British** spelling (with "our" in it).
    - Second line: the text to search in.
2. **Uses a regex pattern**: It looks for words that match both British and American variants of the entered word.
    - It adjusts the word ending to account for **-our** (British) and **-or** (American) spellings.
3. **Counts occurrences**:
    - The program counts both variations (`-our` and `-or`).
    - It ignores case sensitivity.

## Output 📜

### Example Input:

```text
colour
The room was painted in both colour and color, a true blend of British and American styles.
```

### Example Output:

```text
2
```

Explanation: Both "colour" (British) and "color" (American) are counted.

## Usage 📦

1. Save the script as `british_american_spelling_counter_our_or.py`.
2. Run the script and enter:
    - A **word** in its **British** spelling (e.g., "colour").
    - The **text** to search in.
3. The output will be the number of occurrences of the word in both variants.

## Conclusion 🚀

This program is helpful for efficiently counting occurrences of words with different spellings in British and American English, especially when the word contains the **"our"** vs **"or"** difference.
It's ideal for **language studies**, **linguistic research**, and **international text analysis**.
