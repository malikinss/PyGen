# Knight Move Checker

## Description 📝
This Python program determines whether a knight can move from one cell to another on a chessboard in a single move.
The input consists of two different cells represented by their column and row numbers.

## Purpose 🎯
The purpose of this program is to evaluate the possible movement of a knight based on the rules of chess, specifically its unique L-shaped movement.

## How It Works 🔍
1. **User Input**:
   - The program prompts the user to enter the column and row numbers for two different cells on the chessboard.
2. **Movement Evaluation**:
   - The program checks the differences between the column and row numbers. The knight can move in an L-shape, meaning it moves two squares in one direction and one square perpendicular to that direction (or vice versa).
3. **Output**:
   - The program prints "YES" if the knight can move to the second cell in one move, or "NO" otherwise.

## Output 📜
The output can be one of the following:
- "YES" if the knight can move from the first cell to the second.
- "NO" if the knight cannot make the move.

### Example:
For input: `2` `3` `3` `5`
The output will be: `YES`

## Usage 📦
1. Save the code in a file named `5_1_7_knight_move_checker.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python 5_1_7_knight_move_checker.py`
5. Enter the column and row numbers for both cells when prompted.

## Conclusion 🚀
This program provides a simple and efficient way to determine the possible movement of a knight on a chessboard, reinforcing the understanding of conditional statements and chess rules. ♞