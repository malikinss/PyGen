'''
TODO:
    You have a program that adds the remainder of 36 to each number in the
    numbers list to the remainders list.

    If the number is zero, it is ignored.

    Add a try-except construct to the code below to ensure that it runs
    without errors.
'''
numbers = [
    6, 0, 36, 8, 2,
    36, 0, 12, 60,
    0, 45, 0, 3, 23
]

remainders = []

for number in numbers:
    try:
        remainders.append(36 % number)
    except ZeroDivisionError:
        continue

print(remainders)
