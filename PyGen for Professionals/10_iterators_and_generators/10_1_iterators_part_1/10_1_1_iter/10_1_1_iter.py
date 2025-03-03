'''
TODO:
    You have a list numbers that contains integers.

    Complete the code below using the iter() and next() functions so that it
    prints the fourth element of the list.
'''
numbers = [100, 70, 34, 45, 30,
           83, 12, 83, -28, 49,
           -8, -2, 6, 62, 64,
           -22, -19, 61, 13, 5,
           80, -17, 7, 3, 21,
           73, 88, -11, 16, -22]

num_iter = iter(numbers)

for _ in range(4):
    result = next(num_iter)

print(result)
