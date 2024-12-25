'''
TODO:
    Sort the list in ascending order by implementing the selection
    sort algorithm.
'''
from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list in ascending order using the selection sort algorithm.

    Args:
        arr (List[int]): List of integers to be sorted.

    Returns:
        List[int]: Sorted list in ascending order.
    """
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Example usage
a: List[int] = [
    78, -32, 5, 39, 58,
    -5, -63, 57, 72, 9,
    53, -1, 63, -97, -21,
    -94, -47, 57, -8, 60,
    -23, -72, -22, -79, 90,
    96, -41, -71, -48, 84,
    89, -96, 41, -16, 94,
    -60, -64, -39, 60, -14,
    -62, -19, -3, 32, 98,
    14, 43, 3, -56, 71,
    -71, -67, 80, 27, 92,
    92, -64, 0, -77, 2,
    -26, 41, 3, -31, 48,
    39, 20, -30, 35, 32,
    -58, 2, 63, 64, 66,
    62, 82, -62, 9, -52,
    35, -61, 87, 78, 93,
    -42, 87, -72, -10, -36,
    61, -16, 59, 59, 22,
    -24, -67, 76, -94, 59
]

print(selection_sort(a))
