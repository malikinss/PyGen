'''
TODO:
    Implement the DomainException exception class.

    Also implement the Domain class to handle domains.

    The Domain class must support three ways to create its instance:
        directly through a class call, and also using two class methods
        from_url() and from_email():
            domain1 = Domain('pygen.ru') # directly based on the domain
            domain2 = Domain.from_url('https://pygen.ru') # based on the url
            domain3 = Domain.from_email('support@pygen.ru')
            # based on the email

    When attempting to create an instance of the Domain class based on
    an invalid domain, url, or email, a DomainException exception must be
    raised with the text:
        Invalid domain, url, or email

    As an informal string representation, an instance of the Domain class must
    have its own domain:
        print(str(domain1)) # pygen.ru
        print(str(domain2)) # pygen.ru
        print(str(domain3)) # pygen.ru

NOTE:
    We will consider the domain to be valid if it is a sequence of one or more
    Latin letters, followed by a period, and then one or more Latin letters
    again.

    We will consider a URL to be correct if it is a string http:// or https://,
    followed by a correct domain.

    We will consider an email address to be correct if it is a sequence of one
    or more Latin letters, followed by an at sign (@), and then a correct
    domain.
'''
