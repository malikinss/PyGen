# Lesson 10.2: Basic Manipulations with Dictionaries in Python 🔧

## Description 📝

In this lesson, I cover essential operations and manipulations when working with dictionaries in Python.
I explore built-in functions such as `len()`, `sum()`, `min()`, and `max()`, as well as key operations like the `in` operator, dictionary iteration, unpacking, formatted output, comparison, and methods like `keys()`, `values()`, and `items()`.

## Purpose 🎯

The purpose of this lesson is to teach me the fundamental manipulations of dictionaries.
By learning these techniques, I can efficiently work with key-value pairs, perform operations, and manipulate data stored in dictionaries.

## Key Concepts 📚

### Built-in Functions

-   **`len()`**: Returns the number of items (key-value pairs) in a dictionary.
-   **`sum()`**: Sums all the values in a dictionary (if values are numeric).
-   **`min()` / `max()`**: Finds the minimum or maximum key or value (numeric only).

### Membership Operator (`in`)

-   Use the `in` operator to check if a key is present in a dictionary:
    ```python
    if 'key' in my_dict:
        print('Key exists!')
    ```

### Iterating Through Dictionaries

-   You can loop through keys, values, or key-value pairs:
    ```python
    for key, value in my_dict.items():
        print(key, value)
    ```

### Dictionary Unpacking

-   Unpack a dictionary into separate variables:
    ```python
    a, b, c = my_dict
    ```

### Formatted Output

-   Use formatted strings to print dictionary contents:
    ```python
    print(f"{key}: {value}")
    ```

### Dictionary Comparison

-   Compare two dictionaries for equality:
    ```python
    if dict1 == dict2:
        print("Dictionaries are equal!")
    ```

### Methods

-   **`keys()`**: Returns a list of all keys.
-   **`values()`**: Returns a list of all values.
-   **`items()`**: Returns a list of key-value pairs.

## Practical Examples 📝

### 1. Sum of Minimum and Maximum Keys in Dictionary 🔢

This program calculates and prints the sum of the minimum and maximum keys in a given dictionary where the keys are numeric (either integers or floats). It demonstrates how to retrieve and compute with dictionary keys.
The goal of this program is to find the smallest and largest numeric keys in a dictionary and return their sum.

### 2. Users with Phone Ending in 8 Finder 📱8️⃣

This program identifies users whose phone numbers end with the digit '8' from a list of user data. It checks whether the phone number ends with '8' and outputs the names of those users in alphabetical order.
The purpose of this program is to filter out users whose phone numbers end with '8'. It helps in finding specific users based on phone number patterns.

### 3. Users Without Email Finder 📧❌

This program identifies users who do not have email information from a list of dictionaries containing user data. It checks if the 'email' key is either missing or empty and then outputs the names of those users in alphabetical order.  
The purpose of this program is to filter out users without email information and print their names in alphabetical order.

### 4. Number to Words Converter 🔢➡️📝

This program converts a natural number (entered as a string) into a sequence of words representing each digit. For example, the number "123" will be converted to "one two three". It uses a dictionary to map digits to their corresponding word representations.  
The purpose of this program is to transform numeric digits into their word equivalents. It allows users to input a number and receive a string where each digit is replaced by the corresponding word.

### 5. Course Information Finder 🎓

This program retrieves and displays detailed information about a course based on the given course number. The information includes the room number, instructor's name, and class time. The program uses a dictionary to store and retrieve the course details.
The purpose of this program is to provide a simple way to look up the details of a course given its course number. It outputs the room number, instructor, and time for the specified course.

### 6. Mobile Keypad Keystrokes Encoder 📱

This program simulates the process of typing a message on an old push-button mobile phone. It converts each letter of the given message into the corresponding keystrokes on the mobile keypad.
The purpose of this program is to display the sequence of keystrokes required to type a given message on a traditional mobile phone keypad.

### 7. Text to Morse Code Encoder 🔠➡️📡

This program converts a given text message into Morse code. It takes a message, processes it by translating each character into its Morse code equivalent, and outputs the encoded message.
The purpose of this program is to allow users to input a text message and receive the corresponding Morse code translation.

## Conclusion 🚀

By completing this lesson, I'll have a solid understanding of basic manipulations with dictionaries in Python.
I'll be able to efficiently handle key-value data, iterate through dictionaries, and perform essential operations like comparisons, lookups, and more.
