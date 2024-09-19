'''
TODO:
    Write a program that determines whether a user is allowed to
    access an Internet resource or not.

    The program should display the text "Access Granted" if the user
    is at least 18 years old, or "Access Denied" otherwise.
'''
user_age = int(input())

if user_age >= 18:
    print('Access Granted')
else:
    print('Access Denied')
