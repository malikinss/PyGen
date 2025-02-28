# Lesson 7.4: Exception Handling Part 4 ⚠️

## Description 📝

In this lesson, I dive deeper into **exception handling** by exploring the **exception hierarchy, raising exceptions, and exception chains**.
I also learn how to work with the raised exception object itself.

## Purpose 🎯

By the end of this lesson, I will be able to:

-   Understand the **exception hierarchy** and how Python categorizes exceptions.
-   Work with raised exception objects to extract meaningful error information.
-   **Raise custom exceptions** to handle specific cases.
-   Use **exception chaining** to track errors across multiple layers of execution.

## Study Material 🔍

1. **Exception Hierarchy** 🏗️

    - Python exceptions follow a hierarchy, starting from `BaseException`.
    - Understanding this structure helps in catching **specific** or **general** exceptions effectively.

2. **Working with Raised Exceptions** 🔍

    - I can retrieve information about an exception using its attributes, such as `.args` and `.message`.
    - This allows for better logging and debugging.

3. **Raising Exceptions** 🚀

    - The `raise` statement lets me trigger exceptions intentionally.
    - Useful for enforcing **business rules** or handling edge cases manually.

4. **Exception Chains** 🔗
    - Using `raise from` allows me to **preserve the original cause** of an exception when handling errors at multiple levels.
    - This is crucial for debugging and understanding how errors propagate.

## Tasks and Code Snippets 🔍

1. **7_4_1_get_weekday** - Weekday Name Retriever 📅  
   The `get_weekday()` function returns the full name of a **weekday in Russian** based on an integer input (1 to 7).
   It includes error handling for invalid inputs.

    **Goal:**

    - Demonstrate exception handling for **out-of-range** and **non-integer** inputs.
    - Ensure that invalid values are gracefully rejected.

2. **7_4_2_get_id** - Student ID Generator 🎓  
   The `get_id()` function assigns a **unique student ID** to a new student enrolling in the BEEGEEK online school.
   It includes validation rules for names and raises exceptions for invalid inputs.

    **Goal:**

    - Validate **user input** to ensure only proper names are accepted.
    - Use **custom exceptions** where necessary.
    - Ensure IDs are correctly assigned.

3. **7_4_3_load_json_file** - JSON File Reader 📜  
   The `load_json_file()` function reads a JSON file, deserializes its content, and handles errors gracefully.

    **Goal:**

    - Safely read and parse a **JSON file**.
    - Handle **file-related exceptions** such as `FileNotFoundError`.
    - Catch **invalid JSON format** errors using `json.JSONDecodeError`.

## Conclusion 🚀

This lesson equips me with the skills to **handle, raise, and chain exceptions** effectively.
By mastering these techniques, I will be able to write **robust and error-resistant** Python programs that can manage unexpected situations gracefully.
