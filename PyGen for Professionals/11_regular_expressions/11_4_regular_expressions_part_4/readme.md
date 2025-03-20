# Lesson 11.4: Regular Expressions (Part 4) 💻

## Description 📝

This lesson covers advanced topics in **regular expressions**, specifically focusing on using **boundaries** in patterns.
I will explore **word boundaries**, **line boundaries**, and various other practical applications of regular expressions to match specific patterns in text.
Regular expressions are an essential tool for string matching, making them invaluable for text processing, validation, and searching.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand how to use **word boundaries** and **line boundaries** in regular expressions.  
✅ Be proficient in creating patterns to match specific string conditions.  
✅ Learn how to handle cases like capitalized words, specific characters, and titles.  
✅ Apply the knowledge gained in real-world tasks, such as validating and searching strings.

## How It Works 🔍

In this lesson, we will dive into various **regular expressions** to match specific patterns:

1. **Word Boundaries**:  
   Word boundaries allow us to ensure that a word is matched exactly, not as a part of a larger word. This lesson introduces how to use the `\b` and `\B` metacharacters to specify word boundaries in regular expressions.
2. **Line Boundaries**:  
   The use of `^` (beginning of line) and `$` (end of line) in regular expressions ensures that patterns match only at the start or end of a line.

3. **Practical Tasks**:  
   Various tasks will demonstrate how to write regular expressions for specific use cases, such as matching all-capital words, titles, and strings that satisfy complex conditions.

## Practical Tasks 🖥️

1. **11_4_1_specific_words**  
   **Goal**: Create a regular expression to match the words **"a"**, **"A"**, **"an"**, and **"An"** as whole words.  
   **Explanation**: This task focuses on matching specific words, ensuring no partial matches occur (e.g., "another" should not match "an").

2. **11_4_2_caps_words**  
   **Goal**: Create a regular expression to match words that are **entirely in uppercase Latin letters**.  
   **Explanation**: This task helps to match all-uppercase words, ensuring that they are not part of larger words.

3. **11_4_3_begins_caps**  
   **Goal**: Create a regular expression to match words that begin with a **capital letter**.  
   **Explanation**: This task will focus on ensuring that only words starting with a capital letter are matched, followed by lowercase letters or other valid characters.

4. **11_4_4_parentheses**  
   **Goal**: Create a regular expression to match lines that contain **parentheses**.  
   **Explanation**: This task ensures that parentheses `()` are present in a line, allowing for flexibility in what can appear before or after them.

5. **11_4_5_specific_string**  
   **Goal**: Create a regular expression to match strings that:

    - Start with two or more digits.
    - Followed by lowercase letters.
    - End with uppercase letters.  
      **Explanation**: This task teaches how to match strings based on specific starting, middle, and ending conditions.

6. **11_4_6_end_s**  
   **Goal**: Create a regular expression to match strings that end with the letter **"s"**.  
   **Explanation**: This task demonstrates how to match strings that end with specific characters, particularly lowercase 's', ensuring they consist only of Latin letters.

7. **11_4_7_len_char_conditions**  
   **Goal**: Create a regular expression to match strings that:

    - The first 40 characters are Latin letters or even digits.
    - The last 5 characters are odd digits or spaces.  
      **Explanation**: This task focuses on matching strings with specific character-length conditions.

8. **11_4_8_titles**  
   **Goal**: Create a regular expression to match titles like **Mr.**, **Mrs.**, **Ms.**, **Dr.**, or **Er.** followed by uppercase Latin letters.  
   **Explanation**: This task teaches how to match titles followed by a name, ensuring the rest of the string contains uppercase letters.

9. **11_4_9_specific_string**  
   **Goal**: Create a regular expression to match strings that:
    - Start with one or two digits.
    - Followed by three or more uppercase Latin letters.
    - End with three or fewer dots.  
      **Explanation**: This task demonstrates how to match strings with a specific pattern and ending, useful for file extensions or version numbers.

## Output 📜

By completing this lesson, I will:
✅ Be proficient in using **word and line boundaries** in regular expressions.  
✅ Understand how to match patterns that contain specific conditions, like capitalization and punctuation.  
✅ Be able to construct regular expressions to match strings that follow complex conditions, such as specific character lengths and title formats.  
✅ Gain the ability to apply regular expressions effectively in text processing tasks.

## Conclusion 🚀

This lesson builds on previous knowledge of regular expressions by introducing the use of **boundaries** for more precise string matching.
The ability to match specific words, conditions, and patterns in strings opens up powerful possibilities for text processing, validation, and searching.
By mastering these techniques, I can efficiently manipulate and analyze text data in real-world applications.
Regular expressions remain an indispensable tool for any developer working with string-based data.
