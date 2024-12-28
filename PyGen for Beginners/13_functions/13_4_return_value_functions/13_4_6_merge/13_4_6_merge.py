'''
TODO:
    Write a function merge(list1, list2) that takes two ascending-sorted
    integer lists as arguments and merges them into one sorted list.

NOTE:
    You can use the sort() list method, or you can do without it 😎.
'''


def merge(list1, list2):
    """
    Merges two sorted lists into one sorted list.

    Args:
    list1 (list[int]): First sorted list.
    list2 (list[int]): Second sorted list.

    Returns:
    list[int]: A new list that contains all elements from list1 and list2,
               sorted.
    """
    merged = []
    i, j = 0, 0

    # Merge the lists by comparing elements
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Append the remaining elements from list1 or list2, if any
    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged


# Example usage
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]
print(merge(numbers1, numbers2))
