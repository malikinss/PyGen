'''
TODO:
    Let's call a number beautiful if it is four-digit and divisible by 7 or 17.

    Write a program that determines whether the entered number is beautiful.

    The program should output "YES" (without quotes) if the number
    is beautiful, or "NO" (without quotes) otherwise.
'''
num = int(input())

condition1 = 999 < num < 10000
condition2 = num % 7 == 0
condition3 = num % 17 == 0

if condition1 and (condition2 or condition3):
    print('YES')
else:
    print('NO')
