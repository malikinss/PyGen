# Lesson 11.3: Regular Expressions (Part 3) 🔍

## Description 📝

This lesson continues the deep dive into **regular expressions (regex)**, focusing on pattern matching techniques.  
It covers how to match **repeating patterns**, including **one or more characters**, **zero or more characters**, and **optional characters**.  
Additionally, the lesson explores **interval-based matching**, as well as the concepts of **greedy and lazy quantifiers**.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand how to use **quantifiers** like `+`, `*`, and `?` for flexible pattern matching.  
✅ Learn how to specify **character repetition intervals** using `{n,m}`.  
✅ Differentiate between **greedy** and **lazy matching** in regex.  
✅ Be able to apply regex to real-world problems like **PAN validation**, **HTML comment extraction**, **ID validation**, and **postcode verification**.

## How It Works 🔍

This lesson covers fundamental regex techniques:

1. **Repeating Matches** 🔄

    - The `+` quantifier: Matches **one or more** occurrences of a character or pattern.
    - The `*` quantifier: Matches **zero or more** occurrences.
    - The `?` quantifier: Matches **zero or one** occurrence.

2. **Using Intervals `{n,m}`** 📏

    - `{n}` ensures **exactly** `n` occurrences.
    - `{n,}` ensures **at least** `n` occurrences.
    - `{n,m}` matches between `n` and `m` occurrences.

3. **Greedy vs. Lazy Matching** ⏳
    - By default, quantifiers are **greedy**, meaning they match **as much as possible**.
    - Adding `?` after a quantifier makes it **lazy**, meaning it matches **as little as possible**.

## Practical Tasks 🖥️

1. **11_3_1_pan**

    **Goal**: Validate an **Indian PAN (Permanent Account Number)** using regex.

    - **Explanation**:
        - A PAN consists of **10 characters**.
        - The first **5 characters** must be **uppercase letters**.
        - The next **4 characters** must be **digits**.
        - The last **character** must be an **uppercase letter**.
    - This task demonstrates how regex enforces **strict format validation** for identity numbers.

2. **11_3_2_html**

    **Goal**: Extract **HTML comments** using regex.

    - **Explanation**:
        - HTML comments are enclosed within `<!-- ... -->`.
        - The regex must capture **everything inside** the comment tags.
        - This task helps understand **pattern extraction** using **start and end delimiters**.

3. **11_3_3_utopian_citizen**

    **Goal**: Validate **Utopian Citizen Identification Numbers** using regex.

    - **Explanation**:
        - The ID starts with **0 to 3 lowercase letters**.
        - Followed by **2 to 8 digits**.
        - Ends with **at least 3 uppercase letters**.
    - This exercise demonstrates the use of **interval-based matching `{n,m}`**.

4. **11_3_4_uk_postcodes**

    **Goal**: Validate **UK postcodes** using regex.

    - **Explanation**:
        - UK postcodes follow a structured format:
            - Starts with **1 or 2 uppercase letters**.
            - Followed by **a digit** and an optional **letter or digit**.
            - Contains a **mandatory space**.
            - Ends with **a digit followed by 2 uppercase letters**, excluding certain letters.
    - This exercise demonstrates **complex pattern validation** with **character exclusions**.

## Output 📜

By completing this lesson, I will:  
✅ Master **quantifiers** (`+`, `*`, `?`) and **interval-based matching** (`{n,m}`).  
✅ Understand **greedy vs. lazy matching** and when to use them.  
✅ Be able to extract **specific patterns** like **comments, IDs, and postcodes**.  
✅ Apply regex to **real-world data validation** scenarios.

## Conclusion 🚀

Regular expressions are a **powerful tool** for text processing and pattern matching.  
This lesson enhances my ability to construct **efficient** and **precise** regex patterns.  
By mastering **quantifiers, intervals, and matching techniques**, I can solve a wide range of **data validation** and **extraction** problems.  
Regex is an essential skill for developers, and this lesson takes my **pattern recognition** abilities to the next level! 🎯
