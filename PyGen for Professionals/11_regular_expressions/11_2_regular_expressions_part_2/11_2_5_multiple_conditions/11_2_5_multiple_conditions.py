'''
TODO:
    Complete the code below so that the variable regex contains a regular
    expression that matches character sequences of length 6 that satisfy all
    of the following conditions simultaneously:
        - the first character is any digit
        - the second character is a lowercase Latin vowel (a, e, i, o, u, y)
        - the third character is any character except b, c, D, F
        - the fourth character is any non-whitespace character
        - the fifth character is any character except an uppercase Latin vowel
          (A, E, I, O, U, Y)
        - the sixth character is any character except a period or comma
'''
regex = r'\d[aeiouy][^bcDF]\S[^AEIOUY][^.,]'
