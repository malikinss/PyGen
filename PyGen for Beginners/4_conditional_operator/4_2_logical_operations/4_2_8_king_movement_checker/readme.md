# King Movement Checker

## Description 📝
This Python program determines whether a king can move from one square to another on a chessboard in a single move.

## Purpose 🎯
The purpose of this program is to validate king movements according to chess rules, where a king can move one square in any direction.

## How It Works 🔍
1. **User Input**:
   - The program prompts the user to input four integers:
     - The first two integers represent the column and row of the first square.
     - The last two integers represent the column and row of the second square.
2. **Movement Check**:
   - The program checks if the king can move from the first square to the second by verifying:
     - The difference in the column is between -1 and 1 (`-1 <= a - c <= 1`).
     - The difference in the row is also between -1 and 1 (`-1 <= b - d <= 1`).
3. **Output**:
   - The program prints "YES" if the king can move to the second square.
   - It prints "NO" otherwise.

## Output 📜
The program outputs whether a king can move from the first square to the second.

### Example:
For input: `4 4 5 5` The output will be: `YES`

## Usage 📦
1. Save the code in a file named `4_2_8_king_movement_checker.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python 4_2_8_king_movement_checker.py`
5. Enter the square coordinates when prompted, and the program will display whether the king can move to the second square.

## Conclusion 🚀
This program effectively checks king movements on a chessboard, showcasing the implementation of conditional statements in Python.
