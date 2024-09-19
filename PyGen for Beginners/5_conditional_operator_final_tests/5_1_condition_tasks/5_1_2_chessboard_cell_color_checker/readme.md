# Chessboard Cell Color Checker

## Description 📝
This Python program checks if two given cells on a chessboard have the same color.
The chessboard is represented by a coordinate system where the rows and columns are numbered from 1 to 8.

## Purpose 🎯
The purpose of this program is to quickly determine if two specified cells on a chessboard are the same color, which can be useful in various chess-related applications and games.

## How It Works 🔍
1. **User Input**:
   - The program takes four integers as input, representing the coordinates of the two cells: (a1, a2) for the first cell and (b1, b2) for the second cell.
2. **Color Check Logic**:
   - The program uses the sum of the coordinates of both cells. If the sum of the coordinates for both cells has the same parity (both even or both odd), they are of the same color.
3. **Output**:
   - The program prints "YES" if the cells are of the same color, otherwise it prints "NO".

## Output 📜
The output of the program can be one of the following:
- `"YES"` if the two cells are of the same color.
- `"NO"` if the two cells are of different colors.

### Example:
For input: `1` `1` `2` `2`
The output will be: `YES`

## Usage 📦
1. Save the code in a file named `5_1_2_chessboard_cell_color_checker.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python 5_1_2_chessboard_cell_color_checker.py`
5. Enter the coordinates of the two cells when prompted.

## Conclusion 🚀
This program provides a simple method to determine if two cells on a chessboard share the same color, which is an essential aspect of many chess strategies and rules.
♟️