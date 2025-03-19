# Lesson 11.2: Regular Expressions (Part 2) 🔍

## Description 📝

This lesson explores **regular expressions** in more depth, focusing on advanced pattern matching techniques.  
It covers how to match **specific character sets**, **ranges**, **excluded characters**, and even **multiple expressions** at once.

The lesson includes **9 practical programming tasks** and **12 theoretical questions** available on [Stepik](https://stepik.org/lesson/683127/step/1?unit=681950).

## Purpose 🎯

By the end of this lesson, I will:  
✅ Learn how to match **one of multiple characters** using square brackets `[]`.  
✅ Understand how to define **character ranges** and **excluded characters** in regex.  
✅ Be able to construct **regular expressions that match multiple conditions**.  
✅ Gain hands-on experience with **real-world regex applications**, including validating phone numbers, dates, and times.

## How It Works 🔍

This lesson focuses on **advanced regular expression techniques**, including:

1. **Matching One of Multiple Characters**

    - Using character sets like `[abc]` to match `"a"`, `"b"`, or `"c"`.
    - Helps simplify pattern creation when looking for multiple possible matches.

2. **Using a Range of Character Sets**

    - Defining ranges using `A-Z`, `a-z`, or `0-9` to match specific groups of characters.
    - Efficiently targets a wide range of input values.

3. **Matching Anything Except Certain Characters**

    - Using `[^xyz]` to match anything **except** `"x"`, `"y"`, or `"z"`.
    - Useful when filtering out unwanted characters.

4. **Matching One of Multiple Regular Expressions**
    - Using the **alternation operator (`|`)** to match multiple patterns.
    - For example, `cat|dog|fish` matches `"cat"`, `"dog"`, or `"fish"`.

## Practical Tasks 🖥️

1. **11_2_1_cartb** – Match `"car"`, `"cat"`, and `"cab"` using a character set.
2. **11_2_2_hex_digits** – Identify hexadecimal digits from `0-9` and `A-F`.
3. **11_2_3_sequence** – Match sequences of an uppercase letter followed by four digits.
4. **11_2_4_sequence** – Match sequences of a lowercase letter, digit, lowercase letter, and two uppercase letters.
5. **11_2_5_multiple_conditions** – Create a regex for sequences meeting six complex conditions.
6. **11_2_6_multiple_conditions** – Define another set of strict character-based conditions.
7. **11_2_7_phone_numbers** – Validate different Russian phone number formats.
8. **11_2_8_dates** – Match dates in `DD.MM.YYYY`, `DD/MM/YYYY`, `YYYY.MM.DD`, and `YYYY/MM/DD` formats.
9. **11_2_9_time** – Validate times in `HH:MM` format, ensuring correct hour and minute ranges.

## Output 📜

By completing this lesson, I will:  
✅ Be proficient in **advanced regex techniques**, including **character sets and alternations**.  
✅ Understand how to **validate complex formats**, such as **dates, times, and phone numbers**.  
✅ Gain confidence in using **regular expressions for filtering and searching data**.

## Conclusion 🚀

This lesson is a crucial step in mastering **regular expressions** for real-world applications.  
By learning how to match **specific characters, exclude patterns, and define conditions**, I can build powerful search and validation tools.  
These skills are essential for **data processing, text parsing, and input validation** in software development.
