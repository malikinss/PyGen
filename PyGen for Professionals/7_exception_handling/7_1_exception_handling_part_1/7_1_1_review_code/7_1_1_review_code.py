'''
TODO:
    The file data.txt is given.
    It was necessary to write a program that determines how many lines are
    contained in this file and displays the result.

    The programmer was in a hurry and wrote the program incorrectly.

    Find and correct all the errors made in this program (there are exactly 3).

NOTE:
    It is known that each error affects only one line and can be corrected
    without changing other lines.
'''
# original code
total = 0

with open(data.txt, encoding='utf-8') as file:
    for _ in file.readlines:
        total == total + 1

print(total)


# fixed code
total = 0

with open('data.txt', encoding='utf-8') as file:
    for _ in file.readlines():
        total += 1

print(total)
