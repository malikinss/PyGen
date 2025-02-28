# Lesson 7.1: Exception Handling Part 1 ⚠️

## Description 📝

This lesson focuses on **exception handling**, exploring different **error types**, and how to **work with return codes**.
I'll learn to identify errors in my code, understand various error types, and handle them effectively to prevent my program from crashing.

## Purpose 🎯

The lesson will teach me how to:

-   Understand and categorize different types of errors.
-   Work with return codes to handle errors in my program gracefully.
-   Correct faulty code by using exception handling mechanisms.

## Study Material 🔍

1. **Error Types** 🚨  
   I'll learn about common types of errors, such as syntax errors, runtime errors, and logical errors, and how to handle them using **try** and **except** blocks.

2. **Working with Return Codes** 📝  
   Return codes help indicate the success or failure of a function. Handling return codes effectively allows for better control over the flow of my program and the handling of errors.

3. **Practical Tasks** 💻  
   The lesson presents 4 tasks where I will fix errors in different programs by applying exception handling techniques.

## Tasks and Code Snippets 🔍

1. **7_1_1_review_code** - Line Counter 📝  
   The program counts the number of lines in a given text file and prints the result.
   My task is to correct a faulty program that failed to properly read and count the lines in the file.

    **Goal:** Fix the program to handle errors that might occur during file reading, such as `FileNotFoundError`.

2. **7_1_2_swapcase_vowels** - Vowel Case Converter 📝  
   The program converts all lowercase Latin vowels in a given string to uppercase while keeping the rest of the characters unchanged.
   I need to correct a function that was supposed to replace all vowels with uppercase.

    **Goal:** Correct the implementation to handle edge cases like an empty string or a string without vowels.

3. **7_1_3_divisible_by_7** - Divisible by 7 Finder 📝  
   The program takes two integers as input and returns a list of all integers between them (inclusive) that are divisible by 7.
   My task is to fix an incorrect implementation and provide a correct version that finds numbers divisible by 7.

    **Goal:** Handle possible errors like invalid input types (e.g., non-integer values) or incorrect bounds.

4. **7_1_4_get_max_index** - Find the Maximum Index 📝  
   This program implements a function `get_max_index()` that returns the index of the largest integer in a list of distinct integers.
   I need to identify and correct mistakes in the original code to ensure the function correctly returns the index of the largest number in the list.

    **Goal:** Handle scenarios where the list might be empty or contain invalid elements.

## Conclusion 🚀

By the end of this lesson, I'll be equipped with the knowledge to handle errors in my programs using exception handling techniques.
I’ll also learn how to work with return codes to control my program flow more efficiently.
These skills are crucial for debugging and ensuring my programs run smoothly even in the face of unexpected errors.
