'''
TODO:
    As we know from biology, DNA and RNA are sequences of nucleotides.

    Four nucleotides in DNA:
        - adenine (A);
        - cytosine (C);
        - guanine (G);
        - thymine (T).

    Four nucleotides in RNA:
        - adenine (A);
        - cytosine (C);
        - guanine (G);
        - uracil (U).

    The RNA chain is built on the basis of the DNA chain by the sequential
    addition of complementary nucleotides:
        G → C;
        C → G;
        T → A;
        A → U.

    Write a program that converts the DNA chain into the RNA chain.
'''


def dna_to_rna(dna_seq: str) -> str:
    """
    Converts a given DNA sequence to its complementary RNA sequence.

    Args:
        dna_seq (str): A string representing the DNA sequence.

    Returns:
        str: The corresponding RNA sequence.
    """
    dna_to_rna_mapping = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }

    # Assigning the generator expression to a variable
    mapped_rna = (dna_to_rna_mapping[nucleotide] for nucleotide in dna_seq)

    # Joining the mapped RNA sequence into a string
    return ''.join(mapped_rna)


# Get user input for the DNA sequence
given_dna = input("Enter the DNA sequence: ").strip()

# Convert DNA to RNA
rna_sequence = dna_to_rna(given_dna)

# Print the RNA sequence
print(rna_sequence)
