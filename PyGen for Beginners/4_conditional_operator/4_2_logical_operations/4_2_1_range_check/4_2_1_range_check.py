'''
TODO:
    Write a program that takes an integer x and determines whether the number
    is in the specified range. [-1 : 17].

NOTE:
    If the dot is punctured, the boundary is not included.
    If the dot is filled, the boundary is included.
'''
x = int(input())

if (-1) < x < 17:
    print('Belongs to')
else:
    print('Does not belong')
