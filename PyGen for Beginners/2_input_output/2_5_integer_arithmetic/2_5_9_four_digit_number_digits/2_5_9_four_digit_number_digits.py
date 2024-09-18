'''
TODO:
    Write a program to find the digits of a four-digit number.
'''
four_digit_number = int(input("Please enter a four-digit number: "))

thousands = four_digit_number // 1000
hundreds = four_digit_number // 100 % 10
tens = four_digit_number // 10 % 10
units = four_digit_number % 10

print('The digit in the thousands position is', thousands)
print('The digit in the hundreds position is', hundreds)
print('The digit in the tens position is', tens)
print('The digit in the units position is', units)
