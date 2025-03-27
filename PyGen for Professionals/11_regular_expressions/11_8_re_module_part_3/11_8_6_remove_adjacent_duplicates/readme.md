# Remove Adjacent Duplicate Words ✂️

## Description 📝

This program removes repeated adjacent words from a given string.
If the same word appears consecutively, only the first occurrence is kept.

## Purpose 🎯

To clean up text by eliminating redundant adjacent words while preserving word order.
The program is case-sensitive, meaning `python` and `Python` are treated as different words.

## How It Works 🔍

1. **Regular Expression Matching**:

    - The pattern `r'\b(\w+)(?:\W+\1\b)+'` captures repeated adjacent words.
    - `(\w+)` captures a word.
    - `(?:\W+\1\b)+` matches one or more occurrences of the same word with non-word characters (spaces, punctuation) in between.

2. **Replacement**:
    - A lambda function replaces each duplicate sequence with a single occurrence of the word.

## Output 📜

### Example Input:

```python
text = "hello hello world world"
```

### Example Output:

```python
"hello world"
```

### Example Cases:

| Input                      | Output              |
| -------------------------- | ------------------- |
| `"Python Python is great"` | `"Python is great"` |
| `"repeat repeat repeat"`   | `"repeat"`          |
| `"this is is a test test"` | `"this is a test"`  |

## Usage 📦

1. Run the function with an input string:
    ```python
    result = remove_adjacent_duplicates("hello hello world")
    print(result)
    ```
2. Expected Output:
    ```python
    "hello world"
    ```

## Conclusion 🚀

This program efficiently removes repeated adjacent words, making text cleaner and easier to read. The case-sensitive approach ensures accuracy in distinguishing between similar-looking words.
