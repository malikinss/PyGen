'''
TODO:
    Write a program that reads a positive integer n, n∈[1;9], and prints
    the value of the number n + nn + nnn.
'''
n = int(input())

nn = (n * 10) + n
nnn = (n * 100) + nn

print(n + nn + nnn)
