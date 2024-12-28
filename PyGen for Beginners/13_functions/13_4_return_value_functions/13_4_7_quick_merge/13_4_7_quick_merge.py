'''
TODO:
    The input to the program is the number n, and then n lines containing
    integers in ascending order.

    Lists of numbers are formed from these lines.

    Write a program that merges the given lists into one sorted list using
    the quick_merge() function and then outputs it.
'''
from typing import List


def quick_merge(list1: List[int], list2: List[int]) -> List[int]:
    """
    Merges two sorted lists into one sorted list.

    Args:
        list1 (List[int]): The first sorted list of integers.
        list2 (List[int]): The second sorted list of integers.

    Returns:
        List[int]: A new list containing all the elements from list1 and list2,
                   sorted in ascending order.

    Example:
        quick_merge([1, 3, 5], [2, 4, 6])
        # Returns: [1, 2, 3, 4, 5, 6]
    """
    result = []  # This will hold the merged result

    p1 = 0  # Pointer to list1
    p2 = 0  # Pointer to list2

    # Merge the two lists until one of them is exhausted
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])  # Add the smaller element from list1
            p1 += 1
        else:
            result.append(list2[p2])  # Add the smaller element from list2
            p2 += 1

    # If there are remaining elements in list1, append them to result
    if p1 < len(list1):
        result += list1[p1:]

    # If there are remaining elements in list2, append them to result
    if p2 < len(list2):
        result += list2[p2:]

    return result  # Return the merged list


# Main code to read input and merge all lists
total_list: List[int] = []  # This will hold the merged list

# Read the number of lists to merge
for i in range(int(input("Enter number of lists: "))):  # Read number of lists
    num = [int(q) for q in input().split()]  # Read each list

    # Merge it with the current total_list
    total_list = quick_merge(total_list, num)

# Output the final merged list
print(*total_list)
