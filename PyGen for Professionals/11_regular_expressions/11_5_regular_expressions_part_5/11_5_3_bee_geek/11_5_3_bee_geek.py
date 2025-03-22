'''
TODO:
    Complete the code below so that the variable regex contains a regular
    expression that matches character sequences that satisfy all of the
    following conditions simultaneously:
        - the sequence must consist only of bee and geek
        - the sequence must contain at least one geek
        - bee cannot be next to itself (there can be no beebee)
        - geek can only appear after a bee
        - every bee must eventually be followed by a geek
'''
regex = r'(bee(geek)+)+'
