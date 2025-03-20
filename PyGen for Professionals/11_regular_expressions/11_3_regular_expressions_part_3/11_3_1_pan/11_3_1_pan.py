'''
TODO:
    PAN (Permanent Account Number) is a unique number assigned to all
    taxpayers in India.

    It has the following format:
        <letter><letter><letter><letter><letter><digit><digit><digit><letter>

    PAN always consists of 10 characters, where letter is a capital Latin
    letter and digit is a digit.

    Complete the code below so that the regex variable contains the regular
    expression that PAN numbers match.
'''
regex = r'[A-Z]{5}\d{4}[A-Z]'
