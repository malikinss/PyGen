'''
TODO:
    Very often, students of the "Python Generation" confuse the concepts
    of "sum of cubes" and "cube of sum".

    In order to clarify this eternal mathematical question, we suggest you
    solve the following problem.

    The program is given two integers a and b as input.
    Your program must calculate the sum of their cubes and
    the cube of their sum for these numbers and output the result of
    the calculations in the following format:

    For numbers <number a> and <number b>:
    Sum of cubes: <number a> **3 + <number b> **3 = <sum of cubes of a and b>
    Cube of sum: (<number a> + <number b>) **3 = <cube of the sum of a and b>

NOTE:
    Do not confuse the sum of cubes and the cube of the sum. 😉
'''


def calculate_cubes_and_sum(a, b):
    # Calculate the sum of cubes and the cube of the sum
    cube_of_sum = (a + b) ** 3
    sum_of_cubes = (a ** 3) + (b ** 3)

    # Output the results
    print(f'For numbers {a} and {b}:')
    print(f'Sum of cubes: {a}**3 + {b}**3 = {sum_of_cubes}')
    print(f'Cube of sum: ({a} + {b})**3 = {cube_of_sum}')


# Input numbers
a = int(input())
b = int(input())

# Call the function with the provided inputs
calculate_cubes_and_sum(a, b)
