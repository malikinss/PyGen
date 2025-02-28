# Lesson 7.5: Exception Handling Part 5 🛡️

## Description 📝

In this lesson, I explore more advanced topics in exception handling, including **custom exceptions**, **LBYL (Look Before You Leap)** vs **EAFP (Easier to Ask for Forgiveness than Permission)** methodologies, and the use of the **assert operator**.

## Purpose 🎯

By the end of this lesson, I will be able to:

-   Create and raise **custom exceptions** for better error handling.
-   Understand and apply the **LBYL** and **EAFP** methodologies to handle potential issues in different ways.
-   Use the `assert` operator to verify conditions during program execution.

## Study Material 🔍

1. **Custom Exceptions** 🚀

    - Custom exceptions allow me to create specific error types, making it easier to identify and handle issues in my program.
    - I will define these exceptions by subclassing the built-in `Exception` class.

2. **LBYL vs EAFP** 🔄

    - **LBYL (Look Before You Leap):** I check conditions before executing actions to prevent errors.
    - **EAFP (Easier to Ask for Forgiveness than Permission):** I try to perform actions and handle errors if they occur.
    - I will see how each methodology can be applied in different scenarios for more **robust code**.

3. **The `assert` Operator** 🛠️
    - The `assert` operator is used to check conditions that should always be true during program execution.
    - It throws an `AssertionError` if the condition evaluates to `False`.
    - I will use this tool to enforce certain conditions in my code and catch potential issues early.

## Tasks and Code Snippets 🔍

1. **7_5_1_is_good_password_lbyl** - Password Validator (LBYL) 🔐  
   The `is_good_password()` function checks if a given password is "good" by evaluating the following criteria:

    - The password is at least 9 characters long.
    - It contains both uppercase and lowercase letters.
    - It contains at least one digit.  
      This version uses **LBYL** methodology by checking the conditions before performing further operations.

    **Goal:**

    - Implement the **Look Before You Leap** methodology to validate passwords.

2. **7_5_2_is_good_password_eafp** - Password Validator (EAFP Style) 🔑  
   This program checks if the password meets the same criteria as the previous one, but it uses the **Easier to Ask for Forgiveness than Permission** (EAFP) methodology. If any condition is violated, an exception is raised.

    **Goal:**

    - Use **EAFP** methodology to handle invalid passwords by raising exceptions.

3. **7_5_3_prompt_for_password** - Password Validator (Prompt Until Success) 🔒  
   This program repeatedly prompts the user for a password until one that meets all criteria is entered. If the password doesn't meet the requirements, an appropriate **custom exception** (such as `LengthError`, `LetterError`, or `DigitError`) is raised.

    **Goal:**

    - Continuously request the user to enter a valid password.
    - Raise **custom exceptions** for specific validation errors.
    - Ensure the program outputs **error messages** for different failure scenarios.

## Conclusion 🚀

This lesson teaches me how to **define custom exceptions** and choose between **LBYL** and **EAFP** approaches for handling errors.
By learning to validate conditions before acting or handling errors post-action, I can create **more reliable and user-friendly programs**.
The use of **assertions** helps catch bugs early in the process, ensuring that my code works as intended.
