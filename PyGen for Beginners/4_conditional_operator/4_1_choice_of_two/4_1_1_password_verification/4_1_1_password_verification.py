'''
TODO:
    When registering on websites, you are required to enter your
    password twice.

    This is done for security purposes, as this approach reduces
    the possibility of entering the password incorrectly.


    Write a program that compares the password and its confirmation.

    If they match, the program outputs:
        "Password accepted"
    ,otherwise:
        "Password not accepted".
'''
password_1 = input()
password_2 = input()

if password_1 == password_2:
    print('Password accepted')
else:
    print('Password not accepted')
