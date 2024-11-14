'''
TODO:
    The program receives two integers a and b (a≤b) as input.

    Write a program that counts the number of numbers between a and b 
    inclusive whose cube ends in 4 or 9.
'''


def count_numbers_with_special_cubes(a: int, b: int) -> int:
    """
    Counts how many numbers between a and b (inclusive) have a cube
    that ends in 4 or 9.

    Args:
        a (int): The starting number.
        b (int): The ending number.

    Returns:
        int: The count of numbers whose cube ends in 4 or 9.
    """
    counter = 0
    for i in range(a, b + 1):
        cube = i ** 3
        # Check if the cube ends in 4 or 9
        if cube % 10 == 4 or cube % 10 == 9:
            counter += 1
    return counter


# Input data
a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

# Call the function and print the result
result = count_numbers_with_special_cubes(a, b)
print(result)
