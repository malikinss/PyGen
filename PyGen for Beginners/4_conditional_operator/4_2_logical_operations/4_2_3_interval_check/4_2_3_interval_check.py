'''
TODO:
    Write a program that takes an integer x and determines whether the number
    belongs to the specified intervals. [-30, -2] [7, 25]
'''
x = int(input())

if (-30) < x <= (-2) or (7) < x <= (25):
    print('Belongs to')
else:
    print('Does not belongs to')
