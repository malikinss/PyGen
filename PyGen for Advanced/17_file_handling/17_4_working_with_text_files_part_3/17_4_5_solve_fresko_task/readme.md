# Jacques Fresco Goat Riddle Solver

## Description 📝

This Python program reads a file `goats.txt`, which contains a list of goat colors and their occurrences. It processes the data to find which goat colors make up more than 7% of the total number of goats. The program then writes the list of these goat colors to an output file `answer.txt`.

## Purpose 🎯

The purpose of this program is to demonstrate file handling, string manipulation, counting occurrences, calculating percentages, and filtering data based on conditions. It solves a riddle by identifying goat colors that represent a significant portion of the total population.

## How It Works 🔍

1. **Reading Data**:
    - The `read_data_from_file()` function reads the content of `goats.txt` into a list of strings, each representing a line in the file.
2. **Extracting Available Colors**:
    - The `get_available_colors()` function extracts the list of available goat colors from the section of the file marked with the word "COLOURS".
3. **Counting Goat Colors**:
    - The `count_goat_colors()` function counts how many goats of each color are present in the file using the `Counter` class from the `collections` module.
4. **Calculating Percentages**:
    - The `calculate_color_percentages()` function calculates the percentage of goats for each color relative to the total number of goats.
5. **Filtering by Threshold**:
    - The `filter_colors_by_percentage()` function filters the goat colors that exceed the 7% threshold and returns a sorted list of these colors.
6. **Writing the Result**:
    - The `write_data_to_file()` function writes the sorted list of goat colors that make up more than 7% of the total goats to the file `answer.txt`.

## Output 📜

The program creates (or overwrites) the `answer.txt` file, where each line contains a goat color that represents more than 7% of the total goats, sorted alphabetically.

For example, the `answer.txt` file may contain:

```
Brown
Black
White
```

## Usage 📦

1. Save the code in a file, e.g., `solve_riddle.py`.
2. Ensure the `goats.txt` file is in the same directory and follows the format:
    ```
    COLOURS
    Brown
    Black
    White
    GOATS
    Brown
    White
    Black
    Brown
    Brown
    White
    ```
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is located.
5. Run the script using the command:
   `python solve_riddle.py`
6. The program will create or overwrite the `answer.txt` file with the goat colors exceeding the 7% threshold.

## Conclusion 🚀

This program efficiently solves the riddle by processing goat data, calculating percentages, and filtering based on a threshold. It showcases the use of basic file manipulation, data processing, and sorting in Python.
