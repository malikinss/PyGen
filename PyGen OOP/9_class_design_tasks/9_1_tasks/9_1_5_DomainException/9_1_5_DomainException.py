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
import re


class DomainException(Exception):
    """
    Exception for invalid domain, URL, or email.
    """
    def __init__(
        self, message: str = "Invalid domain, url, or email"
    ) -> None:
        super().__init__(message)


class Domain:
    """
    Class to handle and validate domains.
    """
    # One or more letters, dot, one or more letters
    DOMAIN_REGEX = r'[a-zA-Z]+\.[a-zA-Z]+'

    def __init__(self, domain: str) -> None:
        """
        Initialize with a domain.

        Args:
            domain: Domain string (e.g., 'pygen.ru').

        Raises:
            DomainException: If domain is invalid.
        """
        if not Domain._is_correct_domain(domain):
            raise DomainException
        self._domain = domain

    @classmethod
    def from_url(cls, url: str) -> 'Domain':
        """
        Create Domain from a URL.

        Args:
            url: URL string (e.g., 'https://pygen.ru').

        Returns:
            Domain instance.

        Raises:
            DomainException: If URL is invalid.
        """
        if not Domain._is_correct_url(url):
            raise DomainException
        domain = url.split('//')[1]
        return cls(domain)

    @classmethod
    def from_email(cls, email: str) -> 'Domain':
        """
        Create Domain from an email.

        Args:
            email: Email string (e.g., 'support@pygen.ru').

        Returns:
            Domain instance.

        Raises:
            DomainException: If email is invalid.
        """
        if not Domain._is_correct_email(email):
            raise DomainException
        domain = email.split('@')[1]
        return cls(domain)

    @staticmethod
    def _is_correct_domain(domain: str) -> bool:
        """
        Check if domain is valid.

        Args:
            domain: Domain string.

        Returns:
            True if domain matches regex, False otherwise.
        """
        return bool(re.fullmatch(Domain.DOMAIN_REGEX, domain))

    @staticmethod
    def _is_correct_url(url: str) -> bool:
        """
        Check if URL is valid.

        Args:
            url: URL string.

        Returns:
            True if URL matches regex, False otherwise.
        """
        regex = r'https?://' + Domain.DOMAIN_REGEX
        return bool(re.fullmatch(regex, url))

    @staticmethod
    def _is_correct_email(email: str) -> bool:
        """
        Check if email is valid.

        Args:
            email: Email string.

        Returns:
            True if email matches regex, False otherwise.
        """
        regex = r'[a-zA-Z]+@' + Domain.DOMAIN_REGEX
        return bool(re.fullmatch(regex, email))

    def __str__(self) -> str:
        """
        Return domain as string.
        """
        return self._domain
