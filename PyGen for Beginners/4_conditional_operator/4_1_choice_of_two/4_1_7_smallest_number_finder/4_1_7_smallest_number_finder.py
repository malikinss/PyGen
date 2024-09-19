'''
TODO:
    Write a program that determines the smallest of four numbers.
'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

smallest1 = 0
smallest2 = 0


if num1 > num2:
    smallest1 = num2
else:
    smallest1 = num1

if num3 > num4:
    smallest2 = num4
else:
    smallest2 = num3

if smallest1 > smallest2:
    print(smallest2)
else:
    print(smallest1)
