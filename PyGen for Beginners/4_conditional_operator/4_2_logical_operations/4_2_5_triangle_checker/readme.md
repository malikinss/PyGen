# Triangle Existence Checker

## Description 📝
This Python program determines whether a non-degenerate triangle can be formed using three positive numbers as its sides.

## Purpose 🎯
The purpose of this program is to validate the possibility of forming a triangle based on the triangle inequality theorem.

## How It Works 🔍
1. **User Input**:
   - The program prompts the user to enter three positive integers representing the lengths of the sides of a triangle.
2. **Triangle Inequality Check**:
   - It checks if the following conditions hold:
     - \( a + b > c \)
     - \( a + c > b \)
     - \( b + c > a \)
3. **Output**:
   - The program prints "YES" if a non-degenerate triangle can be formed.
   - It prints "NO" if a triangle cannot be formed.

## Output 📜
The program outputs whether a non-degenerate triangle can exist with the provided sides.

### Example:
For input: `3 4 5` The output will be: `YES`


## Usage 📦
1. Save the code in a file named `4_2_5_triangle_checker.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python 4_2_5_triangle_checker.py`
5. Enter three positive numbers when prompted, and the program will display whether a non-degenerate triangle can be formed.

## Conclusion 🚀
This program effectively checks the conditions for forming a non-degenerate triangle, demonstrating the application of the triangle inequality theorem in Python.
😊