# Three-Digit Number Permutations

## Description 📝
This Python script takes a three-digit number with distinct digits as input and generates all six possible permutations of its digits.
The original number and its permutations are printed as output.

## Purpose 🎯
The goal of this program is to demonstrate how to generate and display all permutations of the digits of a given three-digit number.
This exercise helps in understanding digit extraction and permutation generation.

## How It Works 🔍
1. **`input()` Function**: Reads a three-digit number with distinct digits from the user.
2. **Digit Extraction**:
   - **Digit 1**: Extracted using integer division (`//`) by 100.
   - **Digit 2**: Extracted by first dividing the number by 10 and then taking the modulus (`%`) by 10.
   - **Digit 3**: Extracted using modulus (`%`) by 10.
3. **Permutations**: Generates all possible permutations of the three digits and prints them in the following format:
   - Original number
   - Permutations: digit1-digit3-digit2, digit2-digit1-digit3, digit2-digit3-digit1, digit3-digit1-digit2, digit3-digit2-digit1

## Output 📜
When the script is executed and the user inputs a three-digit number with distinct digits, the output will display:
    ```
    <original number>
    <permutation 1>
    <permutation 2>
    <permutation 3>
    <permutation 4>
    <permutation 5>
    ``` 

For example, if the user inputs: 
    ``` 123 ```
The output will be: 
```
    123
    132
    213
    231
    312
    321
```

## Usage 📦
1. Save the code to a file named `2_5_8_three_digit_number_permutations.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Execute the script using the command:
`python 2_5_8_three_digit_number_permutations.py`
5. Enter a three-digit number with distinct digits when prompted and press Enter.
6. The program will display the original number and all possible permutations of its digits.

## Conclusion 🚀
This exercise demonstrates how to handle digit extraction and generate permutations of a three-digit number.
It reinforces the understanding of basic operations and permutations in Python.
Happy coding! 😊