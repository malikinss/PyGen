'''
TODO:
    A three-digit number abc is given, in which all the digits are different.

    Write a program that outputs the six numbers formed by rearranging the
    digits of the given number.
'''
# Input a three-digit number
number = int(input("Enter a three-digit number with distinct digits: "))

# Extract digits
digit1 = number // 100
digit2 = number // 10 % 10
digit3 = number % 10

# Print the original number
print(number)

# Print all permutations of the digits
print(digit1 * 100 + digit3 * 10 + digit2)
print(digit2 * 100 + digit1 * 10 + digit3)
print(digit2 * 100 + digit3 * 10 + digit1)
print(digit3 * 100 + digit1 * 10 + digit2)
print(digit3 * 100 + digit2 * 10 + digit1)
