# British-American Spelling Counter

## Description 📝

This program counts the occurrences of a word in a text, considering both its **British** and **American** spellings.
For example, it handles cases where the word ends in **-ze** (American English) or **-se** (British English).

The program is case-insensitive and will count both variations of the word in any case (e.g., "organize" and "organise").

## Purpose 🎯

This script is useful for counting words in a text that might be spelled differently in **British** and **American** English, especially for **linguistic studies**, **text analysis**, or **document comparison**.

## How It Works 🔍

1. **Reads input**:
    - First line: the word in either its **British** or **American** spelling.
    - Second line: the text to search in.
2. **Uses a regex pattern**: It looks for words that match both British and American variants of the entered word.
    - It adjusts the word ending to account for **-ze** and **-se** spellings.
3. **Counts occurrences**:
    - The program counts both variations (`-ze` and `-se`).
    - It ignores case sensitivity.

## Output 📜

### Example Input:

```text
organize
The company will organize the event, while the British will organise the meeting.
```

### Example Output:

```text
2
```

Explanation: Both "organize" (American) and "organise" (British) are counted.

## Usage 📦

1. Save the script as `british_american_spelling_counter.py`.
2. Run the script and enter:
    - A **word** in either its **British** or **American** spelling (e.g., "organize" or "organise").
    - The **text** to search in.
3. The output will be the number of occurrences of the word in both variants.

## Conclusion 🚀

This program is helpful for efficiently counting occurrences of words with different spellings in British and American English.
It's ideal for **language studies**, **linguistic research**, and **international text analysis**.
