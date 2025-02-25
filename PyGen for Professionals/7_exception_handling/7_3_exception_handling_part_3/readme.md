# Lesson 7.3: Exception Handling Part 3 ⚠️

## Description 📝

In this lesson, I will explore advanced exception handling techniques, including the **optional else** and **finally** blocks.
I'll also learn about the **general try-except pattern** for handling multiple exceptions more effectively.

## Purpose 🎯

The lesson will teach me how to:

-   Use the **else** block to handle code that should run when no exception occurs.
-   Implement the **finally** block to execute code that runs no matter what.
-   Understand the **general try-except pattern** for catching multiple exception types.

## Study Material 🔍

1. **Optional else block** 🔄

    - The `else` block allows me to define code that only runs **if no exceptions** occur in the `try` block.
    - Useful for situations where I want to handle successful execution separately from error handling.

2. **Optional finally block** 🔑

    - The `finally` block is executed **no matter what**, whether an exception is raised or not.
    - Ideal for clean-up actions such as closing files, releasing resources, or logging.

3. **General try-except pattern** 📝
    - The general pattern involves using multiple `except` blocks to handle different types of exceptions.
    - This allows more fine-grained error handling and **prevents unhandled exceptions** from terminating my program.

## Tasks and Code Snippets 🔍

1. **7_3_1_print_month_name** - Month Name Finder 📝  
   The program reads an integer input from the user representing a month number and outputs the corresponding full name of the month in English.
   If the input is invalid or out of range, it displays an appropriate error message.

    **Goal:** Demonstrate how to handle user input, validate integers, and return corresponding data from the `calendar` module. The use of exception handling ensures smooth execution even with invalid input.

2. **7_3_2_add_to_list_in_dict** - add_to_list_in_dict Function 📝  
   The function modifies a dictionary of lists by adding an element to the list at the specified key. If the key is not present, a new key is created with an empty list, and the element is added.

    **Goal:** Simplify adding elements to lists within a dictionary while ensuring proper handling of missing keys. Use exception handling to maintain the dictionary structure even when a key is absent.

3. **7_3_3_read_file** - File Reader Program 📝  
   The function attempts to read the contents of a specified text file. If the file exists, its contents are displayed. If not, an error message is printed.

    **Goal:** Use exception handling to manage file reading operations safely. The program ensures that it provides feedback if the file is not found, preventing crashes when the file is missing.

## Conclusion 🚀

By the end of this lesson, I'll be familiar with advanced techniques for handling exceptions in Python.
I'll be able to use the **else** and **finally** blocks to manage execution flow more effectively and implement a **general try-except pattern** for robust error handling in my programs.
These skills will help me write more **reliable** and **clean** code.
