'''
TODO:
    Write a program that calculates the sum and product of the digits of
    a positive three-digit number and outputs text in the following format:
        Sum of digits = <sum of digits>
        Product of digits = <product of digits>

    The program is given a positive three-digit number as input.

    The program should output text in accordance with the problem statement.

NOTE:
    Pay attention to extra spaces or their absence.
'''
number: int = int(input("Enter a three-digit number: "))

hundreds_digit: int = number // 100
tens_digit: int = number // 10 % 10
units_digit: int = number % 10

digit_sum: int = hundreds_digit + tens_digit + units_digit
digit_product: int = hundreds_digit * tens_digit * units_digit

print('Sum of digits =', digit_sum)
print('Product of digits =', digit_product)
