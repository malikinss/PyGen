'''
TODO:
    When hiring new employees at the BEEGEEK online school, its director tests
    not only the candidate's professional qualities, but also his memory.

    The candidate is shown several different numbers for a short time,
    and then the candidate must name them.

    It does not matter in what order he remembers them, and whether he repeats
    himself or not, the main thing is that he must name all the numbers
    without adding extra ones.

    Write a program that determines whether the candidate has successfully
    passed the memory test.
'''


def check_memory_test(given_numbers: frozenset, candidate_numbers: set) -> str:
    """
    Checks if the candidate has successfully passed the memory test
    by comparing the set of given numbers and the set of numbers provided
    by the candidate.

    Args:
        given_numbers (frozenset): A set of numbers shown to the candidate.
        candidate_numbers (set): A set of numbers the candidate remembers.

    Returns:
        str: "YES" if the candidate remembers the correct numbers,
             "NO" otherwise.
    """
    return "YES" if candidate_numbers == given_numbers else "NO"


def main() -> None:
    """
    Main function to read the input and determine if the candidate has passed
    the memory test.
    """
    # Reading the given numbers and candidate numbers
    given_numbers = frozenset(input().split())
    candidate_numbers = set(input().split())

    # Checking the result and printing the outcome
    result = check_memory_test(given_numbers, candidate_numbers)
    print(result)


if __name__ == "__main__":
    main()
