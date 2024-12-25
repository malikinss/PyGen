'''
TODO:
    A natural number is being processed.

    You need to write a program that displays the product of the digits
    of the entered number.

    The programmer was in a hurry and wrote the program incorrectly.

    Find all the errors in this program (there are exactly 3 of them).

    It is known that each error affects only one line and can be fixed without
    changing other lines.
'''

# original code:
n = input()

product = n % 10
while n >= 10:  # type: ignore
    digit = n % 10
    product = product * digit  # type: ignore
    n //= 10  # type: ignore
print(product)

# fixed code:
n = int(input())  # type: ignore

product = 1  # type: ignore

while n > 0:  # type: ignore
    digit = n % 10
    product *= digit  # type: ignore
    n //= 10  # type: ignore

print(product)
