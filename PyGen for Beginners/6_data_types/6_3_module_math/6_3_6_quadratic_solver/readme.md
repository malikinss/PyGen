# Quadratic Equation Solver

## Description 📝
This Python program finds the real roots of a quadratic equation of the form:
\[ ax^2 + bx + c = 0 \]
where \( a \), \( b \), and \( c \) are real numbers provided by the user.

## Purpose 🎯
The program calculates the roots of a quadratic equation, if they exist, using the discriminant method.
It helps users understand how quadratic equations work and how to find their solutions.

## How It Works 🔍
1. **User Input**:
   - The program prompts the user to enter three real numbers \( a \), \( b \), and \( c \).
2. **Discriminant Calculation**:
   - It calculates the discriminant \( D = b^2 - 4ac \).
3. **Root Calculation**:
   - If \( D > 0 \): The equation has two distinct real roots, which are calculated and printed in ascending order.
   - If \( D = 0 \): The equation has exactly one real root, which is calculated and printed.
   - If \( D < 0 \): The equation has no real roots, and the program prints "No roots".
4. **Output**:
   - The program displays the roots or a message indicating no roots exist.

## Output 📜
The program prints the real roots of the quadratic equation or "No roots" if none exist.

## Usage 📦
1. Save the code in a file named `6_3_6_quadratic_solver.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python 6_3_6_quadratic_solver.py`
5. Enter the values of \( a \), \( b \), and \( c \) when prompted.

## Conclusion 🚀
This program efficiently solves quadratic equations and provides insights into the nature of their roots based on the discriminant. 📊
