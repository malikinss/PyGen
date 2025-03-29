'''
TODO:
        Given a sequence of numbers 𝑎1, 𝑎2, ..., 𝑎𝑛.
        We call a pair (𝑎𝑖, 𝑎𝑗) an inversion if:
            (𝑖 < 𝑗) and (𝑎𝑖 > 𝑎𝑗).

        For example, the sequence 3,1,4,2 has three inversions:
            (3,1)
            (3,2)
            (4,2)

        Each inversion is a pair of elements that violate the order.

        Implement the inversions() function that takes one argument:
            sequence — a sequence whose elements are numbers

        The function must return a single number — the number of
        inversions in the sequence.

NOTE:
        A sequence is an object that has a length and supports indexing.
        For example, objects of type list or range are sequences.
'''


def merge_and_count(
    arr: list[int],
    temp_arr: list[int],
    left: int,
    mid: int,
    right: int
) -> int:
    """
    Merges two halves of an array and counts the number of inversions.

    Args:
        arr (list[int]): The input array.
        temp_arr (list[int]): A temporary array for merging.
        left (int): Left index.
        mid (int): Middle index.
        right (int): Right index.

    Returns:
        int: The number of inversions.
    """
    i, j, k = left, mid + 1, left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


def merge_sort_and_count(
    arr: list[int], temp_arr: list[int], left: int, right: int
) -> int:
    """
    Implements merge sort with inversion counting.

    Args:
        arr (list[int]): The input array.
        temp_arr (list[int]): A temporary array for merging.
        left (int): Left index.
        right (int): Right index.

    Returns:
        int: The number of inversions.
    """
    if left >= right:
        return 0

    mid = (left + right) // 2
    inv_count = merge_sort_and_count(arr, temp_arr, left, mid)
    inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
    inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count


def inversions(sequence: list[int]) -> int:
    """
    Counts the number of inversions in a sequence.

    Args:
        sequence (list[int]): The input sequence.

    Returns:
        int: The number of inversions.
    """
    if not sequence:
        return 0

    return merge_sort_and_count(
        arr=sequence[:],
        temp_arr=[0] * len(sequence),
        left=0,
        right=len(sequence) - 1
    )
