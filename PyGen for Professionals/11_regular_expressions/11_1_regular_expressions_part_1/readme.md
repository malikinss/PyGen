# Lesson 11.1: Regular Expressions (Part 1) 🔍

## Description 📝

This lesson introduces **regular expressions** and their application in Python.
Regular expressions (regex) provide a powerful way to search, match, and manipulate text using patterns.
I will learn about raw strings, character escaping, and different regex patterns for identifying numbers, spaces, alphanumeric characters, and specific text sequences.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand **how regular expressions work** in Python.  
✅ Learn to use regex for **searching and matching patterns** in text.  
✅ Apply **various regex patterns** to find phone numbers, specific words, and sequences.  
✅ Get comfortable with **special characters**, such as `.` for any character and `\d` for digits.

## How It Works 🔍

The lesson covers the following key topics:

-   **Raw strings and escaping characters**: Understanding how `r"pattern"` works to avoid conflicts with Python string syntax.
-   **Searching for specified text**: Finding exact matches using regex.
-   **Using metacharacters (`.` and `\d`)**: Matching any character and digits.
-   **Finding space and alphanumeric characters**: Using `\s` and `\w` for text search.

This lesson includes **5 programming tasks** to practice regex:

1.  **11_1_1_find_phone_numbers**  
    **Goal**: Extract phone numbers from a given text that match specific formats.

-   **Supported formats**:
    -   `7-ddd-ddd-dd-dd`
    -   `8-ddd-dddd-dddd`
    -   `+7-ddd-ddd-dd-dd` (converted to `7-ddd-ddd-dd-dd`)
-   **Key Concepts**: Regular expressions for extracting and validating structured text.

2.  **11_1_2_beegeek**  
    **Goal**: Create a regex pattern to match the exact string **"beegeek"** in any input.

-   **Key Concepts**: Simple string matching using regex, useful for text validation and keyword detection.

3.  **11_1_3_sequence**  
    **Goal**: Match text sequences in the format **`xxx.xxx`**, where each `x` represents any character.

-   **Example Matches**: `abc.123`, `xyz.abc`
-   **Key Concepts**: Using the `.` metacharacter for flexible pattern matching.

4.  **11_1_4_integers**  
    **Goal**: Match **integers in the range 100-199** using regex.

-   **Key Concepts**: Number validation using regex patterns.
-   **Use Cases**: Filtering numbers in a dataset, validating input values.

5.  **11_1_5_phone_numbers**  
    **Goal**: Match phone numbers in the **xxx-xxx-xxxx** format.

-   **Example Matches**: `123-456-7890`, `987-654-3210`
-   **Key Concepts**: Regex for structured numeric data validation.
-   **Use Cases**: Input validation for forms, data extraction.

## Output 📜

After completing this lesson, I will be able to:  
✅ Use **regular expressions** to search and extract patterns in text.  
✅ Understand **raw strings (`r""`)** and their importance in regex.  
✅ Apply **regex metacharacters (`.`, `\d`, `\w`, `\s`)** for different search patterns.  
✅ Validate and extract **structured data** such as phone numbers and numeric ranges.

## Conclusion 🚀

Regular expressions are a crucial tool for **text processing**, **data validation**, and **pattern matching** in Python.
By mastering regex, I will enhance my ability to work with strings efficiently, making tasks like data extraction and text validation much easier.
