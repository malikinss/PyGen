'''
TODO:
    Given a month number (1,2,…, 12).

    Write a program that displays the number of days in this month, given that
    the year is not a leap year.
NOTE:
    Try to write a program so that it has no more than three conditions.
'''
x = int(input())

if x == 2:
    print('28')
elif x == 4 or x == 6 or x == 9 or x == 11:
    print('30')
else:
    print('31')
