# Lesson 11.7: re module (Part 2) 💻

## Description 📝

This lesson covers the **re module** in Python, which is used for working with regular expressions.
In this part, I will focus on two important functions: `findall()` and `finditer()`.
These functions help to find all occurrences of a pattern in a given text, but they do so in different ways.
Understanding their differences and applications will be crucial for text manipulation and pattern matching tasks.

## Purpose 🎯

By the end of this lesson, I will:
✅ Be proficient in using the `findall()` and `finditer()` functions from the `re` module.  
✅ Understand when to use `findall()` for simple pattern matching and `finditer()` for more complex cases that require additional information like match positions.  
✅ Apply regular expressions to practical programming tasks such as text analysis, hyperlink extraction, and word count analysis.  
✅ Be able to extract data from HTML fragments and process it for web scraping and data analysis.

## How It Works 🔍

In this lesson, we will explore how to use **findall()** and **finditer()** for finding patterns in strings:

1. **findall()**:
   The `findall()` function returns all non-overlapping matches of a pattern in a string as a list. It’s simple to use and returns only the matched strings.

2. **finditer()**:
   The `finditer()` function returns an iterator yielding match objects, which contain information about the match, such as the matched string, its position in the input string, and other details. This function is useful when additional information is needed, such as the position of matches.

### Key Differences:

-   `findall()` returns a list of matched strings, while `finditer()` returns an iterator of match objects.
-   `findall()` is more suitable for simple tasks, while `finditer()` is useful for extracting detailed match data.

## Practical Tasks 🖥️

### 1. **11_7_1_stepik**

**Goal**: Create a program to analyze a multi-line text. It should count:

-   Lines beginning with "Stepik" (case-insensitive).
-   Lines ending with "..." or "!".

**Explanation**: This task involves using regular expressions to match lines based on their beginning and end patterns. It requires a solid understanding of line boundaries and string matching.

### 2. **11_7_2_count_inside**

**Goal**: Create a program that counts how many times a word appears as a **subword** in the text.

**Explanation**: A **subword** is a sequence of characters that is surrounded by word characters (`\w`). This task emphasizes matching partial words within larger ones, using word boundaries for precision.

### 3. **11_7_3_count_word_occurrences**

**Goal**: Create a program that counts how many times a given **word** appears in a text.

**Explanation**: The program should use word boundaries (`\b`) to ensure that only exact matches are counted, excluding partial matches within other words.

### 4. **11_7_4_count_word_variants**

**Goal**: Count occurrences of a word with both its **British** and **American** spellings (e.g., "organize" and "organise").

**Explanation**: This task involves building a regular expression that matches both spellings, utilizing alternation and case-insensitive matching.

### 5. **11_7_5_count_british_american_word_variants**

**Goal**: Count occurrences of words ending in **-our** (British) or **-or** (American), such as "colour" and "color".

**Explanation**: This task focuses on creating a pattern that matches both British and American spellings of words ending in "-our" and "-or".

### 6. **11_7_6_abbreviate**

**Goal**: Create a function `abbreviate()` that generates an abbreviation from a phrase by extracting the first letter of each word that starts with a capital letter.

**Explanation**: This task demonstrates how to create abbreviations by processing capitalized words and extracting their first letters using regular expressions.

### 7. **11_7_7_extract_hyperlinks**

**Goal**: Write a program that extracts all hyperlinks (`<a>` tags) from an HTML fragment, including both the `href` attribute (URL) and the link text.

**Explanation**: This task uses regular expressions to identify and extract all the hyperlinks from a given HTML fragment, which can be useful for web scraping tasks.

### 8. **11_7_8_extract_tags_and_attrs**

**Goal**: Write a program that extracts all HTML tags and their attributes from a given HTML fragment.

**Explanation**: This task involves writing a regular expression that identifies HTML tags and extracts their attributes, which is useful for analyzing HTML content and extracting structured data.

## Output 📜

By completing this lesson, I will:
✅ Be proficient in using the `findall()` and `finditer()` functions for pattern matching.  
✅ Understand how to extract detailed match information with `finditer()`.  
✅ Be able to apply regular expressions to practical tasks, including analyzing structured text, extracting hyperlinks, and processing HTML data.  
✅ Have gained hands-on experience in solving common text processing problems with regular expressions.

## Conclusion 🚀

This lesson expands on the **re module** by introducing **findall()** and **finditer()**, which are crucial functions for text analysis and manipulation.
These tools help extract data from strings efficiently, making them invaluable for tasks such as counting word occurrences, extracting hyperlinks, and parsing HTML content.
Mastering these functions will enhance my ability to process and analyze text in real-world applications, such as web scraping and document processing.
Regular expressions are powerful tools that every developer should be comfortable using for text data manipulation.
