'''
TODO:
    Given a positive real number.

    Print its first digit after the decimal point.
'''
num = float(input())

print(int((num * 10) % 10))
