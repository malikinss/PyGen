'''
TODO:
    Write a program that determines if a year with a given number ends
    in two zeros.
    If the year ends, then print "YES", otherwise print "NO".
'''
year = int(input())

if year % 100 == 0:
    print("YES")
else:
    print("NO")
