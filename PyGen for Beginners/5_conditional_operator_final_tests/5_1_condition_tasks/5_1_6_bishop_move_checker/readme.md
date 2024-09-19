# Bishop Move Checker

## Description 📝
This Python program determines whether a bishop can move from one cell to another on a chessboard in a single move.
The input consists of two different cells represented by their column and row numbers.

## Purpose 🎯
The purpose of this program is to evaluate the possible movement of a bishop based on the rules of chess, specifically its diagonal movement.

## How It Works 🔍
1. **User Input**:
   - The program prompts the user to enter the column and row numbers for two different cells on the chessboard.
2. **Movement Evaluation**:
   - The program checks if the absolute difference between the column numbers is equal to the absolute difference between the row numbers. This condition ensures that the bishop can move diagonally.
3. **Output**:
   - The program prints "YES" if the bishop can move to the second cell in one move, or "NO" otherwise.

## Output 📜
The output can be one of the following:
- "YES" if the bishop can move from the first cell to the second.
- "NO" if the bishop cannot make the move.

### Example:
For input: `2` `3` `4` `5`
The output will be: `YES`

## Usage 📦
1. Save the code in a file named `5_1_6_bishop_move_checker.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python 5_1_6_bishop_move_checker.py`
5. Enter the column and row numbers for both cells when prompted.

## Conclusion 🚀
This program provides a simple and efficient way to determine the possible movement of a bishop on a chessboard, reinforcing the understanding of conditional statements and chess rules. ♟️