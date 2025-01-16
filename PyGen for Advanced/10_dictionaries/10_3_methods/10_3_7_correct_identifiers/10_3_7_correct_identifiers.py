"""
TODO:
    The program is given a string containing identifier strings as input.

    Write a program that corrects them so that the resulting string
    doesn't contain duplicates.

    To do this, you need to add the postfix _n to the repeating identifiers,
    where n is the number of times such an identifier has already
    been encountered.
"""


def correct_identifiers(input_string: str) -> str:
    """
    Corrects a string of identifiers by ensuring no duplicates exist.
    Appends a postfix `_n` to repeating identifiers, where `n` is the
    occurrence count minus one.

    Args:
        input_string (str): A space-separated string of identifiers.

    Returns:
        str: A space-separated string of corrected identifiers.
    """
    # Convert to lowercase and split identifiers
    identifiers = input_string.lower().split()
    count: dict = {}
    corrected_ids = []

    for identifier in identifiers:
        # Update the count of the identifier
        count[identifier] = count.get(identifier, 0) + 1

        # Append the identifier with a suffix if it's a duplicate
        if count[identifier] > 1:
            corrected_ids.append(f"{identifier}_{count[identifier] - 1}")
        else:
            corrected_ids.append(identifier)

    # Return the corrected identifiers as a single string
    return " ".join(corrected_ids)


# Example usage
input_ids = input("Enter identifier strings: ")
result = correct_identifiers(input_ids)
print(result)
