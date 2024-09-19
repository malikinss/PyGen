'''
TODO:
    Two cells of a chessboard are given.

    Write a program that determines whether the specified cells have the same
    color or not.

    If they are painted in the same color, then print the word "YES",
    and if they are in different colors, then print "NO".
'''
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())

if (a1 + a2 + b1 + b2) % 2 == 0:
    print('YES')
else:
    print('NO')
