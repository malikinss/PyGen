'''
TODO:
    Write a program that takes three positive numbers and determines whether
    a non-degenerate triangle with those sides exists.

    The program should output "YES" or "NO" according to the problem statement.

NOTE:
    A triangle exists if the triangle inequality holds:
        a+b>c
        a+c>b
        b+c>a
'''
a = int(input())
b = int(input())
c = int(input())

if a < b + c and b < a + c and c < a + b:
    print('YES')
else:
    print('NO')
