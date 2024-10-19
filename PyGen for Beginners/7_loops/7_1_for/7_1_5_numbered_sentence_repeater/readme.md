# Numbered Sentence Repeater

## Description 📝
This Python program reads a sentence from the user and prints it 10 times, each line numbered from 0 to 9.
The program also includes error handling to ensure that the input is not empty.

## Purpose 🎯
The program showcases how to repeat a user input multiple times with numbered output and provides a practical example of basic input validation and loop handling in Python.

## How It Works 🔍
1. **User Input**:
   - The program prompts the user to input a sentence.
2. **Validation**:
   - If the input is empty or consists only of whitespace, the program raises a `ValueError` and stops execution.
3. **Output**:
   - Using a `for` loop, the program prints the given sentence 10 times, each line numbered from 0 to 9.

## Output 📜
For an input like `Python is fun`, the program will output:
    0 Python is fun 1 Python is fun 2 Python is fun 3 Python is fun 4 Python is fun 5 Python is fun 6 Python is fun 7 Python is fun 8 Python is fun 9 Python is fun

If the user provides an empty input, the program will raise the following error:
    Error: The input sentence cannot be empty.


## Usage 📦
1. Save the code in a file named `7_1_5_numbered_sentence_repeater.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python 7_1_5_numbered_sentence_repeater.py`
5. Enter a sentence when prompted, and the program will print it 10 times, numbered from 0 to 9.

## Conclusion 🚀
This program demonstrates how to handle basic user input validation and loop logic in Python, helping users understand how to repeat input and manage error cases efficiently.