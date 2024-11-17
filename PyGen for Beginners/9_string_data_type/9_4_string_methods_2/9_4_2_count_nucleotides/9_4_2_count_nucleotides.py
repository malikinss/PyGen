'''
TODO:
    The input to the program is a string of genetic code consisting
    of the letters A (adenine), G (guanine), C (cytosine), T (thymine).

    Write a program that counts how many adenine, guanine, cytosine
    and thymine are included in a given line of the genetic code.
'''


def count_nucleotides(genetic_code: str) -> None:
    """
    Counts the number of occurrences of adenine (A), guanine (G), cytosine (C),
    and thymine (T) in the given genetic code string.

    Args:
        genetic_code (str): The string representing the genetic code.

    Returns:
        None: Prints the count of each nucleotide (A, G, C, T).
    """
    # Convert the genetic code to lowercase for case-insensitive counting
    genetic_code = genetic_code.lower()

    # Count occurrences of each nucleotide
    adenine = genetic_code.count('a')
    guanine = genetic_code.count('g')
    cytosine = genetic_code.count('c')
    thymine = genetic_code.count('t')

    # Print the counts
    print('Adenine:', adenine)
    print('Guanine:', guanine)
    print('Cytosine:', cytosine)
    print('Thymine:', thymine)


# User input
genetic_code = input("Enter the genetic code: ")

# Call the function to count nucleotides
count_nucleotides(genetic_code)
