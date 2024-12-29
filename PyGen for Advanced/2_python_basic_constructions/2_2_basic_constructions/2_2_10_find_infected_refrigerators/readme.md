# Infected Refrigerators Finder Program 🧊💻

## Description 📝

This program helps the owner of a company find all infected refrigerators by analyzing a series of data strings.
Each data line represents a refrigerator's status.
The program looks for the sequence "anton" in each data line (not necessarily adjacent), and if the sequence is found, the refrigerator is considered infected.
The program will output the refrigerator numbers that are infected, numbered starting from one.

## Purpose 🎯

The goal is to detect which refrigerators are infected by searching for the sequence "anton" in each string.
The program prints the numbers of all infected refrigerators.

## How It Works 🔍

1. **Input Format**:
    - The first input is an integer `n` representing the number of refrigerators.
    - The next `n` lines contain strings representing each refrigerator's data, consisting of lowercase letters and numbers.
2. **Output**:

    - The program will output the numbers of the refrigerators that contain the sequence "anton".
      If no refrigerators are infected, it will output `0`.

3. **Example**:

    - **Input**:
        ```
        3
        anton123
        abcantonxyz
        randomword
        ```
    - **Output**:
        ```
        1 2
        ```
    - **Explanation**:
        - The sequence "anton" is found in the first and second refrigerators' data lines.
        - The third refrigerator does not contain "anton".

4. **Edge Cases**:
    - If no refrigerators are infected (no sequence "anton"), the program outputs `0`.
    - If the sequence "anton" appears in multiple refrigerators, all of their numbers are printed.

## Usage 📦

1. Copy the code into a Python file, e.g., `infected_refrigerators.py`.
2. Run the script in the terminal:
    ```bash
    python infected_refrigerators.py
    ```
3. Enter the number of refrigerators and their respective data strings when prompted.
4. The program will output the refrigerator numbers that are infected.

## Conclusion 🚀

This program is designed to efficiently find infected refrigerators based on the presence of the sequence "anton".
It works well with different input sizes and handles edge cases gracefully.
