# Lesson 11.9: re Module (Part 4) 🔍

## Description 📝

In this lesson, I will continue exploring the **`re` module** in Python with two new functions: **`split()`** and **`compile()`**.
These functions are useful for **splitting strings based on patterns** and **pre-compiling regular expressions** for repeated use.

I will cover how to:  
✅ Use **`re.split()`** to split strings based on patterns.  
✅ Leverage **`re.compile()`** to **compile regular expressions** for efficiency.  
✅ Solve practical programming tasks involving string manipulation, logical expression parsing, and number extraction.

Regular expressions are a powerful tool for **pattern matching** and **text processing**, and mastering these functions will improve my ability to manipulate strings in Python.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand how to **split strings** using **`re.split()`** with custom delimiters.  
✅ Learn to **compile regular expressions** with **`re.compile()`** to improve performance.  
✅ Solve practical problems such as **splitting logical expressions** and **extracting numbers from text**.

## How It Works 🔍

This lesson focuses on two key functions from the **`re` module**:

### 🔹 `re.split(pattern, string)`

-   **Splits** a string by matching a regular expression pattern.
-   Unlike Python's built-in `split()` method, this function supports **complex patterns** and can split based on multiple delimiters at once.

### 🔹 `re.compile(pattern)`

-   Compiles a regular expression pattern into a **regex object**.
-   **Pre-compiling** a pattern is more efficient when the pattern is used multiple times, as it reduces the need for **repeated parsing** of the same regex.

### 🔹 Practical Applications

-   **Custom string splitting** with multiple delimiters.
-   **Logical expression parsing** to extract variables.
-   **Efficient regular expression usage** with pre-compiled regex.
-   **Extracting and summing numbers** from specific parts of a string.

## Practical Tasks 🖥️

1. **11_9_1_custom_split**  
   **Goal**: Split a string based on **periods (.)**, **commas (,)**, and **semicolons (;)**, while removing surrounding spaces.  
   **Explanation**: Helps in **extracting meaningful components** from a string by cleaning up delimiters and spaces.

2. **11_9_2_split_logical_expression**  
   **Goal**: Parse a **logical expression** (containing variables and operators) and split it into its **variables** by removing operators (`and`, `or`, `&`, `|`).  
   **Explanation**: Useful for **parsing and analyzing logical expressions** in programming and mathematical contexts.

3. **11_9_3_multiple_split**  
   **Goal**: Split a string using multiple delimiters from a **list of delimiters**.  
   **Explanation**: This is an extension of the basic `split()` method, offering more **flexibility** when dealing with complex or inconsistent string formats.

4. **11_9_4_sum_numbers_in_range**  
   **Goal**: Extract **natural numbers** from a string within a **specified index range** and return their sum.  
   **Explanation**: This task focuses on **number extraction** from a string, which is useful for **text parsing** and **data analysis** where specific parts of a string contain numerical data.

## Output 📜

By completing this lesson, I will:  
✅ Be proficient in using **`re.split()`** for splitting strings based on patterns.  
✅ Understand how to **compile regular expressions** for efficient reuse.  
✅ Gain practical experience in **splitting complex strings**, **parsing logical expressions**, and **extracting numerical data** from strings.  
✅ Improve my ability to process text data with regular expressions and enhance my overall **Python programming** skills.

## Conclusion 🚀

This lesson deepens my knowledge of Python's **`re` module** by introducing advanced string manipulation techniques like **splitting strings based on patterns** and **pre-compiling regular expressions**.  
Mastering these functions will make me more **efficient** at handling complex text processing tasks, which are common in **data analysis, text parsing**, and **programming**.

By using `re.split()` and `re.compile()`, I can handle more **advanced use cases** and optimize text processing, making me a better Python developer. 💡
