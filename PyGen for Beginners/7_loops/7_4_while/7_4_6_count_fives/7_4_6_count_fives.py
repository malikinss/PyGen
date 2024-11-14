'''
TODO:
    The input to the program is a sequence of integers from 1 to 5,
    characterizing the student's grade, each number on a separate line.

    The end of the sequence is any negative number, or a number greater than 5.

    Write a program that prints the number of fives.
'''


def count_fives() -> int:
    """
    Reads a sequence of student grades from 1 to 5 and counts how many
    of them are fives.

    The sequence ends when a negative number or a number greater
    than 5 is entered, which does not count as part of the sequence.

    Returns:
        int: The count of fives in the sequence.
    """
    count_of_fives = 0
    num = int(input("Enter a grade: "))

    while num in range(6):  # Loop continues only if num is in the range 0 to 5
        if num == 5:
            count_of_fives += 1
        num = int(input("Enter a grade: "))

    return count_of_fives


# Call the function and print the result
result = count_fives()
print("Number of fives:", result)
