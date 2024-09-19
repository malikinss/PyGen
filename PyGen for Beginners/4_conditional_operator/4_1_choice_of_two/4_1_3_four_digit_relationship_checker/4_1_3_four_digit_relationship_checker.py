'''
TODO:
    Write a program that checks whether the following relationship holds
    for a given four-digit number:
        the sum of the first and last digits is equal to the difference
        between the second and third digits.
'''
num = int(input())

first_digit = num // 1000
second_digit = num // 100 % 10
third_digit = num // 10 % 10
fourth_digit = num % 10

operand_1 = first_digit + fourth_digit
operand_2 = second_digit - third_digit

if operand_1 == operand_2:
    print('YES')
else:
    print('NO')
