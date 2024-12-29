# Russian Alphabet String Processor Program 🔤

## Description 📝

This program processes a string by iterating through the Russian alphabet in alphabetical order.
For each letter in the alphabet, the program checks if the letter exists in the string.
If the letter is found, it displays the string with the letter removed and prints the letter.
This process continues until all letters in the Russian alphabet have been checked.

## Purpose 🎯

The goal of this program is to implement an algorithm that removes each letter of the Russian alphabet (in order) from the input string, printing the updated string at each step.

## How It Works 🔍

1. **Input Format**:
    - The program takes a string of text as input, containing lowercase Russian letters and possibly other characters.
2. **Processing**:
    - The program iterates through each letter of the Russian alphabet (from 'а' to 'я').
    - If the letter is found in the string, it prints the string and the letter, then removes all occurrences of the letter.
3. **Example**:

    - **Input**:
        ```
        абвгде
        ```
    - **Output**:
        ```
        абвгде а
        бвгде б
        вгде в
        где г
        де д
        е е
        ```

4. **Edge Cases**:
    - If no letters from the Russian alphabet are found in the string, nothing is printed.
    - The program stops removing letters once all the letters of the Russian alphabet are processed.

## Usage 📦

1. Copy the code into a Python file, e.g., `russian_alphabet_processor.py`.
2. Run the script in the terminal:
    ```bash
    python russian_alphabet_processor.py
    ```
3. Enter the string when prompted.
4. The program will print the string after each letter removal.

## Conclusion 🚀

This program is a simple yet effective demonstration of how to process and modify a string by sequentially removing letters in a specific order.
It provides a clear output showing the state of the string after each modification.
