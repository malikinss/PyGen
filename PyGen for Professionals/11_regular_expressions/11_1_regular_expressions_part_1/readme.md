Lesson 11.1: Regular Expressions (part 1)

Lesson Topic: Regular Expressions
Regular Expressions
Raw Strings and Character Escaping
Searching for a Specified Text
Searching for Any Character
Searching for a Dot Character.
Searching for Numbers
Searching for Space Characters
Searching for Alphanumeric Characters
Abstract: The lesson is devoted to studying regular expressions.

This lesson has good theory explonation, 5 practical programming tasks and 16 thoretical questions presented on the website

https://stepik.org/lesson/640164/step/1?unit=636683

1. 11_1_1_find_phone_numbers

```
# Phone Number Finder
The `find_phone_numbers()` function extracts phone numbers from a given text that match specific formats.
The supported formats are:
-   `7-ddd-ddd-dd-dd`
-   `8-ddd-dddd-dddd`
-   `+7-ddd-ddd-dd-dd` (converted to `7-ddd-ddd-dd-dd`)
where `d` represents a digit from 0 to 9.
This function helps identify and extract phone numbers from any text input.
It can be useful for data validation, text processing, and contact information extraction.
```

2. 11_1_2_beegeek

```
# Regular Expression Matching
The code snippet provides a regular expression that matches the string `beegeek`.
This simple regex is designed to directly match the exact sequence of characters "beegeek" in any input string.
This regular expression can be used for text searching, validation, or extraction when the target string is exactly "beegeek".
It's ideal for use cases where you need to confirm the presence of this specific word in a larger text.
```

3.

```
# Regular Expression for Matching Sequences
The code snippet demonstrates how to write a regular expression to match sequences in the format `xxx.xxx`, where each `x` represents any character.
The provided regular expression should match three characters, followed by a dot (`.`), and then three more characters.
This regular expression can be used to validate or search for patterns such as IP addresses (without strict digit validation), version numbers, or any text with similar structure, where the format consists of three characters, a dot, and three more characters.
```
