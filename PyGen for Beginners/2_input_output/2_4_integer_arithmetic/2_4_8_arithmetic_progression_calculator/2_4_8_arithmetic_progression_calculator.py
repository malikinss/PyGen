'''
TODO:
    An arithmetic progression is a sequence of numbers a1, a2, ..., an, each
    of which, starting with a2, is obtained from the previous one by adding to
    it the same constant number d (the difference of the progression).

    If the first term of the progression (a1) and its difference (d) are known,
    then the n-th term of the arithmetic progression is found by the formula:
        an = a1 + d (n - 1)

    The program is fed three integers: a1, d and n, each on a separate line.

    The program must output the n-th term of the arithmetic progression.

NOTE:
    For example, the following sequence is an arithmetic progression:
        -6, -3, 0, 3, 6, 9, 12
'''
# Input the first term of the arithmetic progression
first_term = int(input())
# Input the common difference of the arithmetic progression
common_difference = int(input())
# Input the position of the term to find
term_index = int(input())

# Calculate the n-th term of the arithmetic progression
nth_term = first_term + common_difference * (term_index - 1)

# Output the n-th term
print(nth_term)
