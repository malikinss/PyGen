Chapter 11: Regular Expressions

Chapter Topic: Regular Expressions and re module
Abstract: This chapter is about learning regular expressions and the re module, which allows you to work with regular expressions in Python.

Its divided for 9 lessons wwhich have good theory explonation, 63 practical programming tasks and 95 theoretical questions.

11_regular_expressions
├───11_1_regular_expressions_part_1
├───11_2_regular_expressions_part_2
├───11_3_regular_expressions_part_3
├───11_4_regular_expressions_part_4
├───11_5_regular_expressions_part_5
├───11_6_re_module_part_1
├───11_7_re_module_part_2
├───11_8_re_module_part_3
└───11_9_re_module_part_4

1. 11_1_regular_expressions_part_1

```
# Lesson 11.1: Regular Expressions (Part 1) 🔍
This lesson introduces **regular expressions** and their application in Python.
Regular expressions (regex) provide a powerful way to search, match, and manipulate text using patterns.
I will learn about raw strings, character escaping, and different regex patterns for identifying numbers, spaces, alphanumeric characters, and specific text sequences.
By the end of this lesson, I will:
✅ Understand **how regular expressions work** in Python.
✅ Learn to use regex for **searching and matching patterns** in text.
✅ Apply **various regex patterns** to find phone numbers, specific words, and sequences.
✅ Get comfortable with **special characters**, such as `.` for any character and `\d` for digits.
```

2. 11_2_regular_expressions_part_2

```
# Lesson 11.2: Regular Expressions (Part 2) 🔍
This lesson explores **regular expressions** in more depth, focusing on advanced pattern matching techniques.
It covers how to match **specific character sets**, **ranges**, **excluded characters**, and even **multiple expressions** at once.
The lesson includes **9 practical programming tasks** and **12 theoretical questions** available on [Stepik](https://stepik.org/lesson/683127/step/1?unit=681950).
By the end of this lesson, I will:
✅ Learn how to match **one of multiple characters** using square brackets `[]`.
✅ Understand how to define **character ranges** and **excluded characters** in regex.
✅ Be able to construct **regular expressions that match multiple conditions**.
✅ Gain hands-on experience with **real-world regex applications**, including validating phone numbers, dates, and times.
```

3. 11_3_regular_expressions_part_3

```
# Lesson 11.3: Regular Expressions (Part 3) 🔍
This lesson continues the deep dive into **regular expressions (regex)**, focusing on pattern matching techniques.
It covers how to match **repeating patterns**, including **one or more characters**, **zero or more characters**, and **optional characters**.
Additionally, the lesson explores **interval-based matching**, as well as the concepts of **greedy and lazy quantifiers**.
By the end of this lesson, I will:
✅ Understand how to use **quantifiers** like `+`, `*`, and `?` for flexible pattern matching.
✅ Learn how to specify **character repetition intervals** using `{n,m}`.
✅ Differentiate between **greedy** and **lazy matching** in regex.
✅ Be able to apply regex to real-world problems like **PAN validation**, **HTML comment extraction**, **ID validation**, and **postcode verification**.
```

4. 11_4_regular_expressions_part_4

```
# Lesson 11.4: Regular Expressions (Part 4) 💻
This lesson covers advanced topics in **regular expressions**, specifically focusing on using **boundaries** in patterns.
I will explore **word boundaries**, **line boundaries**, and various other practical applications of regular expressions to match specific patterns in text.
Regular expressions are an essential tool for string matching, making them invaluable for text processing, validation, and searching.
By the end of this lesson, I will:
✅ Understand how to use **word boundaries** and **line boundaries** in regular expressions.
✅ Be proficient in creating patterns to match specific string conditions.
✅ Learn how to handle cases like capitalized words, specific characters, and titles.
✅ Apply the knowledge gained in real-world tasks, such as validating and searching strings.
```

5. 11_5_regular_expressions_part_5

```
# Lesson 11.5: Regular Expressions (Part 5) 💻
In this lesson, I will delve deeper into **advanced regular expressions**, focusing on the concept of **lookahead** and **lookbehind** assertions.
These assertions allow us to match patterns based on what precedes or follows them without including that text in the match itself.
I'll also explore the differences between **positive** and **negative** lookaheads and lookbehinds, and understand their applications in more complex text matching scenarios.
Mastering these techniques enhances the flexibility of regular expressions for text validation, searching, and manipulation.
By the end of this lesson, I will:
✅ Understand how to use **lookahead** and **lookbehind** assertions in regular expressions.
✅ Be able to create patterns that match specific conditions before or after a certain string, without including those conditions in the match itself.
✅ Learn how to use **positive** and **negative** lookaheads and lookbehinds.
✅ Apply this knowledge to real-world tasks like validating email addresses, phone numbers, or complex patterns in large datasets.
```

6. 11_6_re_module_part_1

```
# Lesson 11.6: re module (Part 1) 💻
This lesson introduces the **re module** in Python, which provides powerful tools to work with regular expressions.
I will explore several key functions such as `search()`, `match()`, `fullmatch()`, and the concept of **Match objects**.
Additionally, I will dive into flags and the `escape()` function to help with escaping special characters.
The primary focus will be on understanding how regular expressions can be used in various practical tasks for text processing.
By the end of this lesson, I will:
✅ Understand the core functions in the **re module** and how to use them.
✅ Learn the differences between `search()`, `match()`, and `fullmatch()` functions.
✅ Be able to work with **Match objects** for extracting details from matches.
✅ Explore various flags and how to use them for advanced pattern matching.
✅ Learn to escape special characters using the `escape()` function.
✅ Apply these concepts to solve real-world text processing tasks.
```

7. 11_7_re_module_part_2

```
# Lesson 11.7: re module (Part 2) 💻
This lesson covers the **re module** in Python, which is used for working with regular expressions.
In this part, I will focus on two important functions: `findall()` and `finditer()`.
These functions help to find all occurrences of a pattern in a given text, but they do so in different ways.
Understanding their differences and applications will be crucial for text manipulation and pattern matching tasks.
By the end of this lesson, I will:
✅ Be proficient in using the `findall()` and `finditer()` functions from the `re` module.
✅ Understand when to use `findall()` for simple pattern matching and `finditer()` for more complex cases that require additional information like match positions.
✅ Apply regular expressions to practical programming tasks such as text analysis, hyperlink extraction, and word count analysis.
✅ Be able to extract data from HTML fragments and process it for web scraping and data analysis.
```

8. 11_8_re_module_part_3

```
# Lesson 11.8: re Module (Part 3) 🔍
This lesson continues exploring Python’s **`re` module**, focusing on the powerful **`sub()`** and **`subn()`** functions for **string substitution** using regular expressions.
These functions allow me to find and replace text patterns efficiently.
I will learn how to:
✅ Use **`re.sub()`** to replace occurrences of patterns in a string.
✅ Use **`re.subn()`** to replace patterns while also counting replacements.
✅ Apply these functions in real-world tasks like text normalization, keyword replacement, and comment removal.
Regular expressions are a core tool for text processing, allowing me to **modify and clean** textual data effectively.
By the end of this lesson, I will:
✅ Master **`sub()`** and **`subn()`** for **text replacement**.
✅ Learn how to **normalize, transform, and clean** text using regular expressions.
✅ Solve practical tasks such as **formatting file extensions, handling whitespace, removing duplicates, and more**.
✅ Understand how to apply **pattern-based transformations** in various real-world applications.
```

9. 11_9_re_module_part_4

```
# Lesson 11.9: re Module (Part 4) 🔍
In this lesson, I will continue exploring the **`re` module** in Python with two new functions: **`split()`** and **`compile()`**.
These functions are useful for **splitting strings based on patterns** and **pre-compiling regular expressions** for repeated use.
I will cover how to:
✅ Use **`re.split()`** to split strings based on patterns.
✅ Leverage **`re.compile()`** to **compile regular expressions** for efficiency.
✅ Solve practical programming tasks involving string manipulation, logical expression parsing, and number extraction.
Regular expressions are a powerful tool for **pattern matching** and **text processing**, and mastering these functions will improve my ability to manipulate strings in Python.
By the end of this lesson, I will:
✅ Understand how to **split strings** using **`re.split()`** with custom delimiters.
✅ Learn to **compile regular expressions** with **`re.compile()`** to improve performance.
✅ Solve practical problems such as **splitting logical expressions** and **extracting numbers from text**.
```
