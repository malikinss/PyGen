# Adding Points to Class Scores

## Description 📝

This Python program reads a file `class_scores.txt` containing surnames and test scores, adds 5 points to each score, and writes the updated results (surnames and new scores) to a file `new_scores.txt`. The score cannot exceed 100.

## Purpose 🎯

The purpose of this program is to demonstrate file handling, string manipulation, and simple mathematical operations on test scores. It shows how to read data from a file, modify the data, and save it back to a new file.

## How It Works 🔍

1. **Reading Data**:
    - The `read_data_from_file()` function reads the contents of the `class_scores.txt` file and returns the lines as a list of strings.
2. **Adding Points**:
    - The `get_new_score()` function calculates the new score by adding 5 points, ensuring it doesn't exceed 100.
    - The `add_scores()` function processes each line, splits it into the surname and score, and updates the score.
3. **Writing Data**:
    - The `write_data_to_file()` function writes the updated data to the `new_scores.txt` file.

## Output 📜

The program creates (or overwrites) the `new_scores.txt` file, where each line contains a surname and the updated score, for example:

```
Smith 80
Johnson 90
Williams 85
```

## Usage 📦

1. Save the code in a file, e.g., `add_points.py`.
2. Ensure the `class_scores.txt` file is in the same directory and contains surnames and test scores like:
    ```
    Smith 75
    Johnson 85
    Williams 80
    ```
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is located.
5. Run the script using the command:
   `python add_points.py`
6. The program will create or overwrite the `new_scores.txt` file with the updated scores.

## Conclusion 🚀

This program demonstrates how to process and manipulate data in files, add points to test scores, and write the modified data back to a new file. It is an example of basic file handling and data processing in Python.
