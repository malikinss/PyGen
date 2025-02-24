'''
TODO:
    It was required to write a program that takes two integers a and b as
    input, each on a separate line, and outputs a list of all integers from a
    to b inclusive that are divisible by 7 without a remainder.

    The programmer was in a hurry and wrote the program incorrectly.

    Find and correct all the errors made in this program (there are exactly 5
    of them).
NOTE:
    It is known that each error affects only one string and can be corrected
    without changing other strings.
'''
# original code
a = input()
b = input()
numbers = []

for i in range(a, b):
    if i // 7 == 0:
        numbers = numbers.append(i)

print(numbers)


# fixed code
a = int(input())
b = int(input())
print([i for i in range(a, b+1) if i % 7 == 0])
