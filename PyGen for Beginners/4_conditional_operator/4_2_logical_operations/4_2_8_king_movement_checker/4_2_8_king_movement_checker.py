'''
TODO:
    Two different squares of a chessboard are given.

    Write a program that determines whether the king can move from the first
    square to the second square in one move.

    The program receives four numbers from 1 to 8 as input, each specifying
    the column number and row number first for the first square, then for
    the second square.

    The program should output "YES" if the king can move from the first square
    to the second square, or "NO" otherwise.
'''
a, b, c, d = int(input()), int(input()), int(input()), int(input())

if (-1 <= a - c <= 1) and (-1 <= b - d <= 1):
    print('YES')
else:
    print('NO')
