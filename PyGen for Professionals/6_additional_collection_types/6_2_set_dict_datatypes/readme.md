# Lesson 6.2: Set and Dict Datatypes 📋🔠

## Description 📝

This lesson continues the **review of built-in collection types** by exploring **sets** and **dictionaries**.
It includes **18 theoretical questions** and **1 programming task** to reinforce my understanding.

## Purpose 🎯

By the end of this lesson, I will:

-   Understand how **sets** differ from other collections.
-   Learn how **dictionaries** store and retrieve key-value pairs efficiently.
-   Apply knowledge through a **practical task**.

## How It Works 🔍

Key topics covered in this lesson:

-   **Sets (`set`)** 🔥

    -   **Unordered**, **mutable**, and **unique elements only**.
    -   Useful for **removing duplicates** and **set operations** (union, intersection, difference).
    -   Example:
        ```python
        numbers = {1, 2, 3, 4, 4, 5}  # {1, 2, 3, 4, 5}
        numbers.add(6)  # {1, 2, 3, 4, 5, 6}
        ```

-   **Dictionaries (`dict`)** 📖
    -   **Key-value pairs**, **mutable**, and **fast lookup**.
    -   Useful for **mapping relationships** and **storing structured data**.
    -   Example:
        ```python
        user = {"name": "Alice", "age": 25}
        print(user["name"])  # Alice
        user["age"] = 26  # Updating value
        ```

## Practical Task: **Custom Alphabet Translator** 🔡

📌 **Task:** Create a program that translates text using a **user-defined alphabet mapping**.  
📌 **Details:**

-   The **custom alphabet** is a string where each character corresponds to **Latin letters (`a-z`)**.
-   The program should **maintain case sensitivity** (uppercase letters should be mapped correctly).
-   Example usage:
    ```python
    custom_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    text = "hello"
    translated = translate_text(text, custom_alphabet)
    print(translated)  # Outputs: "svool"
    ```

## Output 📜

After completing this lesson, I will be able to:  
✅ Use **sets** for unique data storage and operations.  
✅ Work with **dictionaries** to store and retrieve information efficiently.  
✅ Implement a **custom encoding system** using dictionaries.

## Conclusion 🚀

Sets and dictionaries are **powerful tools** in Python.
This lesson strengthens my grasp on these structures and introduces a **hands-on challenge** to apply what I've learned!
