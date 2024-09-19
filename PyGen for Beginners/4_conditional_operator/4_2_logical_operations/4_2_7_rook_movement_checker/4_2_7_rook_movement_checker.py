'''
TODO:
    Two different squares of a chessboard are given.

    Write a program that determines whether a rook can move from the first
    square to the second square in one move.

    The program receives four numbers from 1 to 8 as input, each specifying
    the column number and row number first for the first square, then for the
    second square.

    The program should output "YES" if a rook can move from the first square
    to the second square, or "NO" otherwise.
'''
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 == x2) or (y1 == y2):
    print('YES')
else:
    print('NO')
