# Three-Digit Number Digit Sum and Product

## Description 📝
This Python script calculates the sum and product of the digits of a positive three-digit number.
The result is displayed in a specified format showing both the sum and the product of the digits.

## Purpose 🎯
The goal of this program is to demonstrate how to extract and process individual digits from a number to compute their sum and product.
This exercise helps in understanding integer division and modulus operations for digit extraction.

## How It Works 🔍
1. **`input()` Function**: Reads a three-digit number from the user.
2. **Digit Extraction**:
   - **Hundreds Digit**: Extracted using integer division (`//`) by 100.
   - **Tens Digit**: Extracted by first dividing the number by 10 and then taking the modulus (`%`) by 10.
   - **Units Digit**: Extracted using modulus (`%`) by 10.
3. **Calculations**:
   - **Sum of Digits**: Computed by adding the hundreds, tens, and units digits.
   - **Product of Digits**: Computed by multiplying the hundreds, tens, and units digits.
4. **`print()` Function**: Outputs the sum and product of the digits in the specified format.

## Output 📜
When the script is executed and the user inputs a three-digit number, the output will display:
    `Sum of digits = <sum of digits>`
    `Product of digits = <product of digits>`

For example, if the user inputs:
    `234`

The output will be:
    `Sum of digits = 9`
    `Product of digits = 24`

## Usage 📦
1. Save the code to a file named `three_digit_number_digit_sum_product.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
   `python 2_5_7_three_digit_number_digit_sum_product.py`
5. Enter a positive three-digit number when prompted and press Enter.
6. The program will display the sum and product of the digits of the entered number.

## Conclusion 🚀
This exercise demonstrates how to work with individual digits of a number and perform basic arithmetic operations. 
It reinforces understanding of digit extraction and arithmetic operations in Python.
Happy coding! 😊