'''
TODO:
    Write a program to convert a time interval value given in minutes into a
    value expressed in hours and minutes in the following format:
        <original number of minutes> min is <total number of hours> hour
        <remaining number of minutes> minutes.

    The input to the program is an integer - the number of minutes.

    The program should output text in accordance with the problem statement.

NOTE:
    Don't forget the period at the end. 😊
'''
all_minutes = int(input("Enter number of minutes: "))

hours = all_minutes // 60
minutes = all_minutes % 60

print(all_minutes, 'min is', hours, 'hour ', minutes, 'minutes.')
