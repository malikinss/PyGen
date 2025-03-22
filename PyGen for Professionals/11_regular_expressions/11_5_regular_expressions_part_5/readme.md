# Lesson 11.5: Regular Expressions (Part 5) 💻

## Description 📝

In this lesson, I will delve deeper into **advanced regular expressions**, focusing on the concept of **lookahead** and **lookbehind** assertions.
These assertions allow us to match patterns based on what precedes or follows them without including that text in the match itself.
I'll also explore the differences between **positive** and **negative** lookaheads and lookbehinds, and understand their applications in more complex text matching scenarios.
Mastering these techniques enhances the flexibility of regular expressions for text validation, searching, and manipulation.

## Purpose 🎯

By the end of this lesson, I will:
✅ Understand how to use **lookahead** and **lookbehind** assertions in regular expressions.  
✅ Be able to create patterns that match specific conditions before or after a certain string, without including those conditions in the match itself.  
✅ Learn how to use **positive** and **negative** lookaheads and lookbehinds.  
✅ Apply this knowledge to real-world tasks like validating email addresses, phone numbers, or complex patterns in large datasets.

## How It Works 🔍

This lesson covers the following advanced concepts in regular expressions:

1. **Lookahead Assertions**:  
   Lookahead assertions allow us to match a pattern only if it is followed by another specified pattern, without including the following pattern in the match. The syntax for a lookahead is `X(?=Y)`, where `X` is the pattern to match, and `Y` is the condition that must follow `X` for the match to occur.
2. **Negative Lookahead Assertions**:  
   Negative lookaheads match a pattern only if it is **not** followed by another specified pattern. The syntax for negative lookahead is `X(?!Y)`, where `X` is the pattern to match, and `Y` is the condition that should not follow `X`.

3. **Lookbehind Assertions**:  
   Lookbehind assertions allow us to match a pattern only if it is preceded by a certain pattern. The syntax is `(?<=Y)X`, where `X` is the pattern to match, and `Y` is the condition that must precede `X`.

4. **Negative Lookbehind Assertions**:  
   Negative lookbehinds work similarly to negative lookaheads, matching a pattern only if it is not preceded by a certain pattern. The syntax is `(?<!Y)X`, where `X` is the pattern to match, and `Y` is the condition that should not precede `X`.

## Practical Tasks 🖥️

1. **11_5_1_email_validation**  
   **Goal**: Create a regular expression to match **valid email addresses** using lookaheads and lookbehinds.  
   **Explanation**: This task focuses on using lookahead assertions to ensure that an email address contains an `@` symbol followed by a valid domain, without including the domain in the match.

2. **11_5_2_phone_number_format**  
   **Goal**: Create a regular expression to match **phone numbers** in the format `123-456-7890`, ensuring that the hyphens are correctly placed.  
   **Explanation**: This task demonstrates how to use lookaheads and lookbehinds to validate phone number formatting.

3. **11_5_3_valid_password**  
   **Goal**: Create a regular expression to match **valid passwords** that contain at least one uppercase letter, one lowercase letter, one digit, and one special character.  
   **Explanation**: This task uses lookaheads to check for the presence of different character types without capturing them as part of the match.

4. **11_5_4_exclude_words**  
   **Goal**: Create a regular expression to match words that **do not** contain the substring "bad".  
   **Explanation**: This task focuses on using negative lookaheads to exclude words with specific patterns.

5. **11_5_5_date_format**  
   **Goal**: Create a regular expression to match dates in the format `YYYY-MM-DD`, ensuring that the year is a four-digit number, the month is between 01 and 12, and the day is between 01 and 31.  
   **Explanation**: This task utilizes both lookaheads and lookbehinds to ensure the correct range for month and day values.

6. **11_5_6_match_only_after_word**  
   **Goal**: Create a regular expression to match all occurrences of the word **"test"**, but only when it is preceded by the word **"start"**.  
   **Explanation**: This task demonstrates using lookbehind assertions to match patterns based on their preceding text.

7. **11_5_7_exclude_special_characters**  
   **Goal**: Create a regular expression to match strings that **do not** contain any special characters, but can contain letters and digits.  
   **Explanation**: This task shows how to use negative lookaheads to exclude unwanted characters.

8. **11_5_8_url_validation**  
   **Goal**: Create a regular expression to match **valid URLs** that begin with `http` or `https` and are followed by a valid domain name.  
   **Explanation**: This task helps in validating URLs using lookahead assertions to ensure they match a specific pattern.

9. **11_5_9_case_sensitive_match**  
   **Goal**: Create a regular expression to match the word **"Apple"**, but only if it is written with a capital **A**.  
   **Explanation**: This task demonstrates how to match a word with a specific case using lookaheads.

## Output 📜

By completing this lesson, I will:
✅ Be proficient in using **lookahead** and **lookbehind** assertions to match complex patterns in strings.  
✅ Understand the difference between **positive** and **negative** lookaheads/behind and how to apply them in regular expressions.  
✅ Gain the ability to use regular expressions for advanced text validation tasks, such as email validation, password complexity checks, and phone number formatting.  
✅ Be able to exclude specific patterns from matches using negative lookaheads, enhancing the flexibility of string matching.

## Conclusion 🚀

This lesson expands the power of regular expressions by introducing **lookahead** and **lookbehind** assertions, which allow for more sophisticated string matching conditions.
These assertions enable pattern matching based on context before or after the target string, making them invaluable for tasks that require complex validation and searching.
Mastering these concepts will greatly enhance my ability to work with text-based data in real-world applications.
Regular expressions, with their ability to define intricate patterns, continue to be an indispensable tool in software development.
