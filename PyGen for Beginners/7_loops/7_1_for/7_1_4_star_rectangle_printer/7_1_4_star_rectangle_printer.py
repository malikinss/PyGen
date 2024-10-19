'''
TODO:
    The input to the program is a natural number n.
    Write a program that prints an n*19 star rectangle.
'''

n = int(input())
star = '*'

for _ in range(n):
    print(star * 19)
