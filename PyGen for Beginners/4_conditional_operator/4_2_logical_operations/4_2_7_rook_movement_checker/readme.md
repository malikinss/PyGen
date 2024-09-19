# Rook Movement Checker

## Description 📝
This Python program determines whether a rook can move from one square to another on a chessboard in a single move.

## Purpose 🎯
The purpose of this program is to validate rook movements according to chess rules, where a rook can move any number of squares along a row or column.

## How It Works 🔍
1. **User Input**:
   - The program prompts the user to input four integers:
     - The first two integers represent the column and row of the first square.
     - The last two integers represent the column and row of the second square.
2. **Movement Check**:
   - The program checks if the rook can move from the first square to the second by verifying:
     - If the columns of both squares are the same (`x1 == x2`), or
     - If the rows of both squares are the same (`y1 == y2`).
3. **Output**:
   - The program prints "YES" if the rook can move to the second square.
   - It prints "NO" otherwise.

## Output 📜
The program outputs whether a rook can move from the first square to the second.

### Example:
For input: `1 1 1 5` The output will be: `YES`

## Usage 📦
1. Save the code in a file named `4_2_7_rook_movement_checker.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python 4_2_7_rook_movement_checker.py`
5. Enter the square coordinates when prompted, and the program will display whether the rook can move to the second square.

## Conclusion 🚀
This program effectively checks rook movements on a chessboard, showcasing the implementation of conditional statements in Python.
😊
