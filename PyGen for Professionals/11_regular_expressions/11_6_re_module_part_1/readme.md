# Lesson 11.6: re module (Part 1) 💻

## Description 📝

This lesson introduces the **re module** in Python, which provides powerful tools to work with regular expressions.
I will explore several key functions such as `search()`, `match()`, `fullmatch()`, and the concept of **Match objects**.
Additionally, I will dive into flags and the `escape()` function to help with escaping special characters.
The primary focus will be on understanding how regular expressions can be used in various practical tasks for text processing.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand the core functions in the **re module** and how to use them.  
✅ Learn the differences between `search()`, `match()`, and `fullmatch()` functions.  
✅ Be able to work with **Match objects** for extracting details from matches.  
✅ Explore various flags and how to use them for advanced pattern matching.  
✅ Learn to escape special characters using the `escape()` function.  
✅ Apply these concepts to solve real-world text processing tasks.

## How It Works 🔍

In this lesson, we will explore the following core concepts and functions in the **re module**:

1. **`search()` function**:  
   The `search()` function scans through a string and returns the first match of the regular expression. It returns a **Match object** that contains details about the match.

2. **`match()` function**:  
   The `match()` function only matches at the beginning of the string. If the pattern is found at the start of the string, it returns a Match object.

3. **`fullmatch()` function**:  
   The `fullmatch()` function ensures that the entire string must match the pattern. If the entire string conforms to the regular expression, a Match object is returned.

4. **Match Object**:  
   A Match object holds information about the match, such as the starting and ending positions of the match, and the actual matched string. You can access various attributes like `group()`, `start()`, and `end()` to extract details.

5. **Flags**:  
   Flags modify how regular expressions are applied. For example, the `re.IGNORECASE` flag allows case-insensitive matching.

6. **`escape()` function**:  
   The `escape()` function ensures that all special characters in a string are escaped, allowing them to be treated as literal characters in a pattern.

## Practical Tasks 🖥️

1. **11_6_1_process_numbers**  
   **Goal**: Create a program that parses phone numbers in two formats (`<country code>-<city code>-<number>` and `<country code> <city code> <number>`). The program should extract the country code, city code, and number separately.  
   **Explanation**: The task focuses on using regular expressions to extract components from phone numbers in different formats.

2. **11_6_2_process_logins**  
   **Goal**: Validate BEEGEEK logins that must start with an underscore (`_`), followed by one or more digits, and optionally end with an underscore. After the digits, there may be zero or more Latin letters (uppercase or lowercase).  
   **Explanation**: This task emphasizes creating a regular expression that matches specific login formats.

3. **11_6_3_process_words**  
   **Goal**: Identify words that consist of two identical parts. A word is valid if it can be split into two identical halves.  
   **Explanation**: This task challenges you to write a regular expression that matches words with repeated structures.

4. **11_6_4_count_bee_and_geek_lines**  
   **Goal**: Count how many lines contain the substring "bee" at least twice and how many contain the word "geek" at least once.  
   **Explanation**: The task focuses on analyzing multiple lines of input to count specific word occurrences.

5. **11_6_5_calculate_popularity_score**  
   **Goal**: Evaluate the popularity of the **BEEGEEK** online school by counting occurrences of the word `"beegeek"` in lowercase in social media posts.  
   **Explanation**: This task helps in calculating the popularity of a brand or term by analyzing its occurrences in text.

6. **11_6_6_is_worthy_email**  
   **Goal**: Check if an email starts with a preferred greeting like "Hello", "Good morning", "Good afternoon", or "Good evening" (case-insensitive).  
   **Explanation**: This task involves pattern matching for greetings at the start of an email.

7. **11_6_7_count_occurances**  
   **Goal**: Count how many lines contain the string "beegeek" (case-insensitive) in any part of the text.  
   **Explanation**: This task focuses on counting case-insensitive occurrences of a specific substring in multiple lines of text.

## Output 📜

By completing this lesson, I will:
✅ Be proficient in using the core functions of the **re module** for regular expression matching.  
✅ Understand how to handle **Match objects** and extract useful information from them.  
✅ Be able to use flags to modify the behavior of regular expressions.  
✅ Gain experience in solving real-world problems using regular expressions in text processing tasks.

## Conclusion 🚀

The **re module** in Python is a powerful tool for working with regular expressions.
By mastering functions like `search()`, `match()`, and `fullmatch()`, as well as understanding **Match objects** and flags, I will be able to tackle a wide range of text processing tasks.
Whether it's validating inputs, counting occurrences, or extracting components from strings, regular expressions provide an efficient way to handle pattern matching in Python.
