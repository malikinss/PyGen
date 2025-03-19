'''
TODO:
    Complete the code below so that the variable regex contains a regular
    expression that matches character sequences of length 6 that
    simultaneously satisfy all of the following conditions:
        - the first character is the digit 1, 2, or 3
        - the second character is the digit 0, 1, or 2
        - the third character is the digit 1, 2, or lowercase Latin letter x
        - the fourth character is the digit 0, 3, or the Latin letter a
          in any case
        - the fifth character is the lowercase Latin letter x, s, or u
        - the sixth character is a period or comma
'''
regex = r'[1-3][0-2][12x][03aA][xsu][.,]'
