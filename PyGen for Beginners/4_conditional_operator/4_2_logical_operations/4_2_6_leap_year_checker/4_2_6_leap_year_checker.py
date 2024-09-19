'''
TODO:
    Write a program that determines whether a year with a given number is
    a leap year.

    If the year is a leap year, then print "YES", otherwise print "NO".

    A year is a leap year if its number is a multiple of 4 but not a multiple
    of 100, or if it is a multiple of 400.
'''
year = int(input())

condition1 = year % 4 == 0
condition2 = year % 100 != 0
condition3 = year % 400 == 0

if (condition1 and condition2) or condition3:
    print('YES')
else:
    print('NO')
