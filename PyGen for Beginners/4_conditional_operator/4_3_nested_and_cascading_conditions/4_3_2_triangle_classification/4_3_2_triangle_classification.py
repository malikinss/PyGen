'''
TODO:
    Write a program that classifies a triangle based on the lengths
    of its sides.

    The program should take three numbers, each representing the length of one
    of its sides.

    As a result, the program should determine whether the triangle
    is equilateral, isosceles, or scalene.
'''
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('Equilateral')
elif a == b or a == c or b == c:
    print('Isosceles')
else:
    print('Scalene')
