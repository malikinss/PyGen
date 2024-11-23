'''
TODO:
    The input to the program is a text string containing natural numbers.

    A list of numbers is formed from this string.

    Write a program that counts how many pairs of elements in the resulting
    list are equal to each other.

    It is believed that any two elements that are equal to each other form one
    pair, which must be calculated.
'''


def count_equal_pairs(numbers: str) -> int:
    """
    This function counts how many pairs of elements in the given list
    are equal to each other. A pair is formed by any two elements
    that are equal.

    Args:
        numbers (str): A string containing space-separated natural numbers.

    Returns:
        int: The number of pairs of equal elements in the list.
    """
    num_list = numbers.split()
    num_list_len = len(num_list)
    count = 0

    # Compare each pair of elements in the list
    for i in range(num_list_len):
        for j in range(i + 1, num_list_len):
            if num_list[i] == num_list[j]:
                count += 1

    return count


# Input: String of numbers
input_string = input()

# Calling the function and printing the result
result = count_equal_pairs(input_string)
print(result)
