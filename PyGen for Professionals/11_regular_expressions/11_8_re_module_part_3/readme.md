# Lesson 11.8: re Module (Part 3) 🔍

## Description 📝

This lesson continues exploring Python’s **`re` module**, focusing on the powerful **`sub()`** and **`subn()`** functions for **string substitution** using regular expressions.
These functions allow me to find and replace text patterns efficiently.

I will learn how to:  
✅ Use **`re.sub()`** to replace occurrences of patterns in a string.  
✅ Use **`re.subn()`** to replace patterns while also counting replacements.  
✅ Apply these functions in real-world tasks like text normalization, keyword replacement, and comment removal.

Regular expressions are a core tool for text processing, allowing me to **modify and clean** textual data effectively.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Master **`sub()`** and **`subn()`** for **text replacement**.  
✅ Learn how to **normalize, transform, and clean** text using regular expressions.  
✅ Solve practical tasks such as **formatting file extensions, handling whitespace, removing duplicates, and more**.  
✅ Understand how to apply **pattern-based transformations** in various real-world applications.

## How It Works 🔍

This lesson focuses on **substitution techniques** using the `re` module in Python.

### 🔹 `re.sub(pattern, replacement, string)`

-   **Replaces** occurrences of a pattern in a string with the specified replacement.
-   Can use **capture groups** to reference parts of the matched text.

### 🔹 `re.subn(pattern, replacement, string)`

-   Works like `re.sub()` but **returns a tuple**: `(new_string, num_replacements)`.
-   Useful when I need to know **how many replacements** were made.

### 🔹 Practical Applications

-   **Text normalization** (e.g., standardizing file extensions).
-   **Cleaning up text** (e.g., removing duplicate words).
-   **Syntax processing** (e.g., replacing Python keywords).
-   **Expanding encoded text patterns** (e.g., `3(abc) → abcabcabc`).
-   **Code cleanup** (e.g., stripping comments from Python code).

## Practical Tasks 🖥️

1. **11_8_1_normalize_jpeg**  
   **Goal**: Convert `.jpeg` and `.JPG` file extensions to `.jpg`.  
   **Explanation**: Ensures consistency in **image file naming** by normalizing variations of the JPEG format.

2. **11_8_2_normalize_whitespace**  
   **Goal**: Replace multiple spaces, tabs, and newlines with a single space.  
   **Explanation**: Helps in **text formatting** by ensuring consistent spacing between words.

3. **11_8_3_replace_all_keywords**  
   **Goal**: Replace all **Python keywords** in a string with `<kw>`.  
   **Explanation**: Useful for **syntax highlighting** or preventing keyword conflicts in variable names.

4. **11_8_4_swap_first_two_letters_in_words**  
   **Goal**: Swap the first two letters of every word with **2+ characters**.  
   **Explanation**: Demonstrates **text transformation** while preserving spacing and punctuation.

5. **11_8_5_expand_multiplications**  
   **Goal**: Expand expressions like `3(abc)` into `abcabcabc`.  
   **Explanation**: Handles encoded **repetitive text patterns**, useful in text preprocessing.

6. **11_8_6_remove_adjacent_duplicates**  
   **Goal**: Remove **consecutive duplicate words** in a string.  
   **Explanation**: Cleans up text by eliminating **redundant words** while preserving order.

7. **11_8_7_remove_comments**  
   **Goal**: Remove all **Python comments** (`#`, `""" """`).  
   **Explanation**: Useful for **cleaning code** by stripping unnecessary comments while keeping the logic intact.

## Output 📜

By completing this lesson, I will:  
✅ Be proficient in using **`re.sub()` and `re.subn()`** for text processing.  
✅ Understand how to **modify and clean text** efficiently with **regular expressions**.  
✅ Gain experience solving **real-world problems** with text manipulation.  
✅ Improve my ability to **normalize, replace, and clean** text data effectively.

## Conclusion 🚀

This lesson builds on my **regular expressions** knowledge by introducing **powerful substitution functions** in Python.  
With `re.sub()` and `re.subn()`, I can **transform, clean, and format** text efficiently, making them essential for **text preprocessing, data cleaning, and automation**.  
Mastering these techniques will **enhance my ability** to work with **structured and unstructured text**, improving my overall skills in **Python programming and data processing**. 💡
