'''
TODO:
    Given three different integers, write a program that finds the midpoint
    of these numbers.
NOTE:
    The midpoint of a set of numbers is the number that is in the middle
    of the set when sorted in ascending order.
'''
a = int(input())
b = int(input())
c = int(input())

if a > b > c or c > b > a:
    print(b)
elif b > a > c or c > a > b:
    print(a)
else:
    print(c)
