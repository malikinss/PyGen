'''
TODO:
    Each citizen of the country of Utopia is given an identification number,
    which has the following format:
        - the number starts with 0-3 lowercase Latin letters inclusive
        - then follows a sequence of digits, the length of which must be from
        2 to 8 inclusive
        - after the digits there are 3 or more uppercase Latin letters

    Complete the code below so that the variable regex contains a regular
    expression that corresponds to the identification numbers of Utopian
    citizens.
'''
regex = r'[a-z]{0,3}\d{2,8}[A-Z]{3,}'
