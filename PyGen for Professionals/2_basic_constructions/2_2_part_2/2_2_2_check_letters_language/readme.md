# Check Letters Language Function

## Description 📝

The `check_letters_language()` function determines whether three given letters are from the Russian alphabet, the English alphabet, or if they are a mixture of both.
The function checks against predefined sets of letters that look similar in both languages.

## Purpose 🎯

This function is helpful for:

-   Identifying the language of mixed letter inputs.
-   Checking if three characters are from either Russian or English alphabets based on visually similar letters.

## How It Works 🔍

1. The function takes a string `letters` containing exactly three characters from a predefined list of Russian and English letters.
2. It compares each character against two predefined sets:
    - Russian letters: "АаВСсЕеНКМОоРрТХху"
    - English letters: "AaBCcEeHKMOoPpTXxy"
3. Based on the comparison, the function outputs:
    - 'ru' if all three letters are Russian.
    - 'en' if all three letters are English.
    - 'mix' if there is a mix of Russian and English letters.

## Output 📜

Example usage and expected outputs:

```python
check_letters_language("ААА")
# Returns: 'ru', because all letters are Russian.

check_letters_language("ABC")
# Returns: 'en', because all letters are English.

check_letters_language("АBC")
# Returns: 'mix', because the input contains both Russian and English letters.
```

## Usage 📦

1. Clone this repository.
2. Navigate to the project directory.
3. Use the function in your script or interactive Python shell.

Example:

```python
from letter_language_checker import check_letters_language

print(check_letters_language("ABC"))  # Output: en
```

## Conclusion 🚀

The `check_letters_language()` function is a simple tool to classify groups of visually similar Russian and English letters, determining whether they belong to one language or a mix of both.
