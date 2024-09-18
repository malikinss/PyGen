'''
TODO:
    A geometric progression is a sequence of numbers b1, b2, ..., bn, each of
    which, starting with b2, is obtained from the previous one by multiplying
    by the same constant number q (the denominator of the progression).

    If the first term of the progression and its denominator are known, then
    the n-th term of the geometric progression is found by the formula:
    bn = b1 * q^(n - 1)

    The program is given three integers b1, q and n, each on a separate line.

    The program must output the n-th term of the geometric progression.
'''
first_term = int(input("Enter the first term (b1): "))
denominator = int(input("Enter the common ratio (q): "))
term_index = int(input("Enter the term index (n): "))

nth_term = first_term * denominator**(term_index - 1)

print(nth_term)
