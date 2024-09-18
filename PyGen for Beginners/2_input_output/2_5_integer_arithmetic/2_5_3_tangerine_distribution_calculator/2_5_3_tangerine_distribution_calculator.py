'''
TODO:
    n schoolchildren divide k tangerines equally, the undivided remainder
    remains in the basket.

    How many whole tangerines will each schoolchild get?

    How many whole tangerines will remain in the basket?

    The program is given two integers as input: the number of schoolchildren
    and the number of tangerines, each on a separate line.

    The program must output two numbers: the number of tangerines that each
    schoolchild will get and the number of tangerines that will remain in
    the basket, each on a separate line.
'''
num_schoolchildren = int(input())
num_tangerines = int(input())

tangerines_per_child = num_tangerines // num_schoolchildren
tangerines_remaining = num_tangerines % num_schoolchildren

print(tangerines_per_child, tangerines_remaining, sep='\n')
