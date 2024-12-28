# Word Count Program 📚

## Description 📝

This Python program counts the number of words in a given string.
Words are separated by spaces, and the program correctly handles multiple spaces between words.

## Purpose 🎯

The program is designed to count how many words are present in a string, making it useful for text analysis or situations where you need to evaluate the length of a sentence.

## How It Works 🔍

1. **Input Format**:
    - The user is prompted to input a line of text.
2. **Function Logic**:

    - The program splits the string by spaces using the `split()` method. This method automatically removes extra spaces and handles any leading or trailing spaces.
    - The program then counts the number of elements in the list returned by `split()`, which corresponds to the number of words in the string.

3. **Example**:

    ```
    Enter the text: Hello   world   program
    Output:
    3
    ```

    Even though there are multiple spaces between the words, the program correctly counts them as three words.

4. **Edge Cases**:
    - If the string contains only spaces, the program will return `0` as there are no words.
    - Leading and trailing spaces are ignored.

## Usage 📦

1. Copy the code into a Python file, e.g., `word_count.py`.
2. Run the script in the terminal:
    ```bash
    python word_count.py
    ```
3. Enter your string when prompted.
4. The program will output the number of words in the string.

## Conclusion 🚀

This simple program is efficient for counting words in a string, ensuring that multiple spaces or empty inputs are handled correctly.
