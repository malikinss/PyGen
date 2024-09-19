# Summing Repeated Digits

## Description 📝
This Python program reads a positive integer `n` (where \( n \in [1, 9] \)) and computes the value of the expression \(n + nn + nnn\).
This calculation involves forming multi-digit numbers by repeating `n`.

## Purpose 🎯
The program demonstrates how a single-digit number can be expanded into multi-digit forms and then summed, providing insight into number manipulation using arithmetic and concatenation.

## How It Works 🔍
1. **User Input**:
   - The user enters a single-digit integer `n` (between 1 and 9).
2. **Calculation**:
   - The program computes:
     - \(nn = n \times 10 + n\)
     - \(nnn = n \times 100 + nn\)
   - It then sums the values \(n + nn + nnn\).
3. **Output**:
   - The result of the expression is printed to the console.

## Output 📜
The program outputs the value of \(n + nn + nnn\) for the given `n`.

### Example:
For input:
    `n = 5`

The output will be:
    `615`

Explanation:
- \(n = 5\)
- \(nn = 55\)
- \(nnn = 555\)
- Sum = \(5 + 55 + 555 = 615\)

## Usage 📦
1. Save the code in a file named `3_2_4_summation_of_repeated_digits.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using the command:
   `python 3_2_4_summation_of_repeated_digits.py`
5. Enter a positive integer (between 1 and 9) when prompted, and the program will display the calculated result.

## Conclusion 🚀
This program allows you to explore how numbers can be manipulated and summed in creative ways by repeating digits.
It provides a clear example of how Python handles basic arithmetic and string manipulation in numeric contexts.
Enjoy experimenting! 😊