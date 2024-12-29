# Consecutive Heads Counter Program 🧠💥

## Description 📝

This program analyzes a string of text consisting of the letters "H" and "T".
The letter "H" represents the appearance of Heads, and the letter "T" represents the appearance of Tails.
The program counts the greatest number of consecutive Heads ("H") in the given string.
If there are no Tails ("T") in the string, the program will return 0.

## Purpose 🎯

The goal is to find the longest sequence of consecutive "H"s in a string, which can help in scenarios like analyzing coin toss results or streaks in games.
The program will output the maximum length of consecutive Heads, and it handles edge cases where no Tails appear.

## How It Works 🔍

1. **Input Format**:
    - A string `s` consisting of the characters 'H' and 'T' (e.g., "HHTHTH").
2. **Output**:
    - The program will output an integer representing the longest sequence of consecutive "H"s in the input string.
3. **Example**:

    - **Input**:
        ```
        HHTHTHHH
        ```
    - **Output**:
        ```
        3
        ```
    - **Explanation**:
        - The longest streak of consecutive "H"s is 3 (in the sequence "HHH").

4. **Edge Cases**:
    - If there are no "H"s (e.g., "TTTT"), the result is 0.
    - If there are no "T"s, the result will be the total number of "H"s in the string.

## Usage 📦

1. Copy the code into a Python file, e.g., `max_heads.py`.
2. Run the script in the terminal:
    ```bash
    python max_heads.py
    ```
3. Input a string of 'H' and 'T' when prompted.
4. The program will output the longest sequence of consecutive 'H's.

## Conclusion 🚀

This program efficiently counts the longest sequence of consecutive Heads in a string of coin tosses, offering valuable insights into patterns or streaks.
It handles edge cases where there are no Heads or no Tails, providing accurate results every time.
