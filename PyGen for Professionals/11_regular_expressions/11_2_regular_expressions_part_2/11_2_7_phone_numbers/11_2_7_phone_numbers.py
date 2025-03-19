'''
TODO:
    Complete the code below so that the regex variable contains a regular
    expression that matches phone numbers in the following formats:
        +7xxxxxxxxxx
        +7(xxx)xxxxxxx
        +7(xxx)-xxx-xx-xx
        +7 xxx xxx xx xx
    where x is an arbitrary digit.

NOTE:
    No additional validation of the phone number is required.

    The +, (, and ) symbols are metacharacters.

    If you want to match the +, (, and ) symbols themselves, they must be
    preceded by the backslash character "\\+", "\\(", and "\\)" in
    the regular expression.
'''
regex = r'\+7(?:' \
        r'\d{10}|' \
        r'\(\d{3}\)\d{7}|' \
        r'\(\d{3}\)-\d{3}-\d{2}-\d{2}|' \
        r'\s\d{3}\s\d{3}\s\d{2}\s\d{2}' \
        r')'
