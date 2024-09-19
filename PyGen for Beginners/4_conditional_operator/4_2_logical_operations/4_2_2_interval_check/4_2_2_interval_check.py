'''
TODO:
    Write a program that takes an integer x and determines whether the number
    belongs to the specified intervals. [-∞, -3] [7, +∞]
'''
x = int(input())

if (-3) >= x or x >= 7:
    print('Belongs to')
else:
    print('Does not belongs to')
