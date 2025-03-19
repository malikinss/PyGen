'''
TODO:
    Complete the code below so that the regex variable contains a regular
    expression that matches dates in the following formats:
        DD.MM.YYYY
        DD/MM/YYYY
        YYYY.MM.DD
        YYYY/MM/DD

NOTE:
    No additional validation of the date is required.
'''
regex = r'(?:\d{2}\.\d{2}\.\d{4}|' \
        r'\d{2}/\d{2}/\d{4}|' \
        r'\d{4}/\d{2}/\d{2}|' \
        r'\d{4}\.\d{2}\.\d{2})'
