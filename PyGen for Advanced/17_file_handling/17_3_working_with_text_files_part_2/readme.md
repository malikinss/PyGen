# Lesson 17.3: Working with Text Files (Part 2)

## Description 📝

In this lesson, I continue exploring file handling in Python, specifically focusing on **file position** and **context managers**.
I will learn how to use methods like `seek()` and `tell()` to manage the position of the file cursor.
dditionally, I will study how to work with context managers to ensure proper file handling and resource management.

## Purpose 🎯

The goals of this lesson are:

-   Learn how to manage the **position (cursor)** within a file using the `seek()` and `tell()` methods.
-   Understand how to use **context managers** for efficient and clean file handling.
-   Solve practical problems related to text file manipulation.

## Practical Tasks 🚀

### 1️⃣ Reverse Line from File 🌀📄

**Task:** Read a single line of text from a file named **"text.txt"** and display the line in **reverse order**.

-   The text is read, reversed, and printed.
-   Useful for quickly reversing a line's content from a text file.

---

### 2️⃣ Reverse Lines from File 🔄📄

**Task:** Read all lines from a file named **"data.txt"** and print them in **reverse order**.

-   This program prints the last line first, then the penultimate line, and so on.
-   Useful for reversing the order of lines in a text file.

---

### 3️⃣ Get Longest Strings from File 📜🔝

**Task:** Read a file named **"lines.txt"** and output all the **longest strings** from the file while maintaining their original order.

-   Helps identify and print the longest strings without altering their order.

---

### 4️⃣ Calculate Sum of Numbers in Each Row 📊🔢

**Task:** Read a file named **"numbers.txt"** where each line contains one or more integers separated by spaces.

-   This program calculates the sum of numbers in each row and displays the results.
-   Useful for summing up numbers row by row in a text file.

---

### 5️⃣ Extract Numbers from Text 📝💰

**Task:** Read a file named **"nums.txt"** that contains non-negative integers mixed with other text.

-   The program extracts all numbers from the file and calculates their sum.
-   Useful for extracting numbers from unstructured text and performing calculations.

---

### 6️⃣ Count Letters, Words, and Lines in a Text File 📝🔢

**Task:** Read a file named **"file.txt"** and output the count of:

-   **Latin letters** (both uppercase and lowercase)
-   **Words** (sequences of characters separated by spaces)
-   **Lines** in the file

---

### 7️⃣ Generate Random Name Pairs 🎲👤

**Task:** Read two files, **"first_names.txt"** and **"last_names.txt"**, and generate 3 random pairs of first and last names.

-   Outputs each random name pair on a separate line.
-   Useful for generating random name combinations from separate lists.

---

### 8️⃣ Filter Countries Based on Population and Name Starting with 'G' 🌍

**Task:** Read a file **"population.txt"** containing country names and populations, separated by a tab character.

-   Filters countries whose names start with 'G' and whose populations exceed 500,000.
-   Prints the filtered countries in the same order as in the file.

---

### 9️⃣ Read and Parse CSV Data 📊

**Task:** Read a CSV file named **"data.csv"** and convert its contents into a list of dictionaries.

-   Each dictionary represents a row with column names as keys and corresponding row values.
-   Useful for parsing and processing CSV files into a more structured format.

---

## Conclusion 🎯

This lesson deepens my understanding of working with text files, introducing advanced concepts like **file position management** and **context managers**.
By mastering these techniques, I will be able to handle file data efficiently and implement robust file processing solutions in Python.
