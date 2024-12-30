'''
TODO:
    Using the list's append() method, complete the code below so that list1
    looks like this:
        list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
'''
from typing import List


list1: List = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)

print(list1)
