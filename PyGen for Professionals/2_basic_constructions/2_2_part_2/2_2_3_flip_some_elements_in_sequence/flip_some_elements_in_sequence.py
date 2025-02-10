'''
TODO:
    A sequence of natural numbers from 1 to n inclusive is given.

    Write a program that first arranges in reverse order part of the elements
    of this sequence from element number X to element number Y, and then from
    element number A to element number B.

NOTE:
    Numbering of sequence members starts from one
'''
from typing import List


def generate_sequence(n: int) -> List[str]:
    """
    Generates a sequence of natural numbers from 1 to n.

    Args:
        n (int): The number up to which the sequence will be generated.

    Returns:
        List[str]: A list of numbers in string format from 1 to n.
    """
    return [str(i) for i in range(1, n + 1)]


def flip_sequence(sequence: List[str]) -> List[str]:
    """
    Reverses the order of elements in the sequence.

    Args:
        sequence (List[str]): The list to be reversed.

    Returns:
        List[str]: The reversed list.
    """
    return sequence[::-1]


def flip_segment_in_sequence(
    sequence: List[str], start_id: int, finish_id: int
) -> List[str]:
    """
    Flips a segment of the sequence from start_id to finish_id.

    Args:
        sequence (List[str]): The sequence of elements.
        start_id (int): The starting index of the segment to flip
                        (0-based index).
        finish_id (int): The ending index of the segment to flip
                        (0-based index).

    Returns:
        List[str]: The sequence with the specified segment flipped.
    """
    result_sequence = []

    # Extract the parts of the sequence
    before_segment = sequence[:start_id]
    segment = sequence[start_id:finish_id+1]
    flipped_segment = flip_sequence(segment)
    after_segment = sequence[finish_id+1:]

    # Construct the result sequence
    result_sequence.extend(before_segment)
    result_sequence.extend(flipped_segment)
    result_sequence.extend(after_segment)

    return result_sequence


def flip_some_elements_in_sequence(input_data: str) -> List[str]:
    """
    Flips specified segments in the sequence based on the input data.

    Args:
        input_data (str): The space-separated input data containing:
                            n, x, y, a, b.

    Returns:
        List[str]: The sequence with the specified segments flipped.
    """
    n, x, y, a, b = map(int, input_data.split())

    sequence = generate_sequence(n)

    # Flip the specified segments in the sequence
    sequence = flip_segment_in_sequence(sequence, x-1, y-1)
    sequence = flip_segment_in_sequence(sequence, a-1, b-1)

    return sequence


# Take user input and print the result
user_input = input("Enter values for n, X, Y, A, B: ")
result_sequence = flip_some_elements_in_sequence(user_input)
print(" ".join(result_sequence))
