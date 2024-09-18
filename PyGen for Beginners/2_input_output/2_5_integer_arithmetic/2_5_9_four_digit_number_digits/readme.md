# Four-Digit Number Digits Extraction

## Description 📝
This Python script takes a four-digit number as input and extracts each digit in the thousands, hundreds, tens, and units positions.
It then prints each extracted digit along with its positional label.

## Purpose 🎯
The purpose of this program is to demonstrate how to extract and display individual digits from a four-digit number.
It helps in understanding basic integer operations and digit manipulation.

## How It Works 🔍
1. **`input()` Function**: Reads a four-digit number from the user.
2. **Digit Extraction**:
   - **Thousands Digit**: Extracted using integer division (`//`) by 1000.
   - **Hundreds Digit**: Extracted by dividing the number by 100 and taking the modulus (`%`) by 10.
   - **Tens Digit**: Extracted by first dividing the number by 10 and then taking the modulus (`%`) by 10.
   - **Units Digit**: Extracted using modulus (`%`) by 10.
3. **Printing**: Each digit is printed with its corresponding positional label.

## Output 📜
When the script is executed and the user inputs a four-digit number, the output will display:
```
The digit in the thousands position is <thousands_digit> The digit in the hundreds position is <hundreds_digit>
The digit in the tens position is <tens_digit>
The digit in the units position is <units_digit>
```
For example, if the user inputs:
    `4721`

The output will be:
```
The digit in the thousands position is 4
The digit in the hundreds position is 7
The digit in the tens position is 2
The digit in the units position is 1
```

## Usage 📦
1. Save the code to a file named `2_5_9_four_digit_number_digits.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
   `python 2_5_9_four_digit_number_digits.py`
5. Enter a four-digit number when prompted and press Enter.
6. The program will display each digit in its corresponding positional label.

## Conclusion 🚀
This exercise demonstrates how to extract individual digits from a four-digit number using integer operations.
It reinforces basic programming concepts and helps in understanding digit manipulation in Python.
Happy coding! 😊