# Roulette Pocket Color Detector

## Description 📝
This Python program determines the color of a pocket on a roulette wheel based on the pocket number.
The pockets are numbered from 0 to 36, with specific colors assigned to each pocket according to standard roulette rules.

## Purpose 🎯
The purpose of this program is to provide an easy way to identify the color of a roulette pocket by entering its number.
It also includes error handling for invalid input.

## How It Works 🔍
1. **User Input**:
   - The user is prompted to enter a pocket number (0-36).
2. **Color Determination**:
   - The program checks the range of the entered number and assigns colors based on the following rules:
     - Pocket **0**: Green
     - Pockets **1-10**:
       - Odd: Red
       - Even: Black
     - Pockets **11-18**:
       - Odd: Black
       - Even: Red
     - Pockets **19-28**:
       - Odd: Red
       - Even: Black
     - Pockets **29-36**:
       - Odd: Black
       - Even: Red
3. **Error Handling**:
   - If the input number is outside the range 0 to 36, the program outputs `"input error"`.

## Output 📜
The program outputs the color of the pocket or an error message if the input is invalid.
Below are some examples:
- **Input**: `0` ➜ **Output**: `green`
- **Input**: `1` ➜ **Output**: `red`
- **Input**: `10` ➜ **Output**: `black`
- **Input**: `15` ➜ **Output**: `black`
- **Input**: `36` ➜ **Output**: `red`
- **Input**: `37` ➜ **Output**: `input error`

### Example:
For input: `7`
The output will be: `red`

## Usage 📦
1. Save the code in a file named `4_3_8_roulette_color_detector.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python 4_3_8_roulette_color_detector.py`
5. Enter a pocket number when prompted, and the program will display the color or an error message.

## Conclusion 🚀
This program provides a simple way to determine the color of a pocket on a roulette wheel.
It incorporates basic input validation, making it suitable for beginners looking to practice their programming skills in Python.
🎲🟢🔴⚫