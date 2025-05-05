# DomainException and Domain Class Implementation

## Description 📝

The provided code implements the `DomainException` exception class and the `Domain` class to handle and validate domains.
The `Domain` class supports three creation methods: direct initialization with a domain, `from_url()` for extracting a domain from a URL, and `from_email()` for extracting a domain from an email address.
It validates inputs using regular expressions, raising `DomainException` with the message "Invalid domain, url, or email" for invalid inputs.
The informal string representation of a `Domain` instance is the domain itself.

## Purpose 🎯

Intended for applications requiring domain validation and extraction, such as web scraping, email processing, or educational examples of Python classes, regular expressions, and exception handling.

## How It Works 🔍

-   **DomainException Class**:
    -   Inherits from `Exception`.
    -   Initializes with a default message: "Invalid domain, url, or email".
    -   Used to signal invalid domain, URL, or email inputs.
-   **Domain Class**:
    -   Defines a class constant `DOMAIN_REGEX = r'[a-zA-Z]+\.[a-zA-Z]+'` for validating domains (one or more Latin letters, a dot, one or more Latin letters).
    -   **Initialization (`__init__`)**:
        -   Takes a `domain` string.
        -   Validates using `_is_correct_domain`.
        -   Raises `DomainException` if invalid.
        -   Stores the domain in `self._domain`.
    -   **from_url (Class Method)**:
        -   Takes a `url` string (e.g., `https://pygen.ru`).
        -   Validates using `_is_correct_url`.
        -   Raises `DomainException` if invalid.
        -   Extracts the domain by splitting on `//` and taking the second part.
        -   Returns a new `Domain` instance.
    -   **from_email (Class Method)**:
        -   Takes an `email` string (e.g., `support@pygen.ru`).
        -   Validates using `_is_correct_email`.
        -   Raises `DomainException` if invalid.
        -   Extracts the domain by splitting on `@` and taking the second part.
        -   Returns a new `Domain` instance.
    -   **Validation Methods (Static)**:
        -   `_is_correct_domain(domain)`: Checks if `domain` matches `DOMAIN_REGEX`.
        -   `_is_correct_url(url)`: Checks if `url` matches `r'https?://' + DOMAIN_REGEX`.
        -   `_is_correct_email(email)`: Checks if `email` matches `r'[a-zA-Z]+@' + DOMAIN_REGEX`.
        -   All use `re.fullmatch` to ensure exact matches.
    -   **String Representation (`__str__`)**:
        -   Returns `self._domain` as the informal string representation.
-   **Behavior**:
    -   Validates domains (e.g., `pygen.ru`), URLs (e.g., `http://pygen.ru`, `https://pygen.ru`), and emails (e.g., `support@pygen.ru`).
    -   Raises `DomainException` for invalid inputs (e.g., `pygen`, `http://pygen`, `user@pygen`).
    -   Extracts domains correctly from valid URLs and emails.
    -   Returns the domain as its string representation.

## Verification ✅

Implementation satisfies requirements:

-   **DomainException**:
    -   Correctly defined with message "Invalid domain, url, or email".
    -   Example: Raised when `Domain('pygen')` is called.
-   **Domain Initialization**:
    -   Direct: `Domain('pygen.ru')` creates instance with domain `pygen.ru`.
    -   From URL: `Domain.from_url('https://pygen.ru')` extracts `pygen.ru`.
    -   From Email: `Domain.from_email('support@pygen.ru')` extracts `pygen.ru`.
-   **Validation**:
    -   Domain: Valid if matches `[a-zA-Z]+\.[a-zA-Z]+` (e.g., `pygen.ru`, `a.b`).
    -   URL: Valid if `http://<domain>` or `https://<domain>` (e.g., `https://pygen.ru`).
    -   Email: Valid if `[a-zA-Z]+@<domain>` (e.g., `support@pygen.ru`).
    -   Invalid cases (e.g., `pygen`, `http://pygen`, `user@pygen`) raise `DomainException`.
-   **String Representation**:
    -   Informal: Returns the domain string.
    -   Example: `str(Domain('pygen.ru'))` → `pygen.ru`.
-   **Correctness**:
    -   `re.fullmatch` ensures exact regex matches for validation.
    -   Splitting (`//` for URLs, `@` for emails) correctly extracts domains.
    -   Static methods `_is_correct_*` encapsulate validation logic.
    -   No additional validation needed, as inputs are guaranteed to be strings.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `DOMAIN_REGEX` (`[a-zA-Z]+\.[a-zA-Z]+`) matches valid domains like `pygen.ru`, `a.b`, but excludes invalid ones like `pygen`, `123.ru`, `pygen..ru`.
    -   URL regex (`https?://` + domain) matches `http://` or `https://` followed by a valid domain.
    -   Email regex (`[a-zA-Z]+@` + domain) matches one or more letters, `@`, and a valid domain.
    -   Splitting logic (`url.split('//')[1]`, `email.split('@')[1]`) assumes valid formats after regex validation.
    -   `DomainException` is raised consistently for all invalid cases.
-   **Performance**:
    -   Initialization: O(n) for regex matching (n is string length).
    -   `from_url`, `from_email`: O(n) for regex and splitting.
    -   `__str__`: O(1) for returning stored domain.
    -   Efficient for typical domain/URL/email lengths.
-   **Design**:
    -   Class methods `from_url` and `from_email` provide clear alternative constructors.
    -   Static validation methods improve modularity and reusability.
    -   Type hints (`str`, `'Domain'`) clarify signatures.
    -   Single regex for domain validation ensures consistency across methods.
-   **Alternatives**:
    -   Manual string parsing: Error-prone and verbose compared to regex.
    -   Third-party libraries (e.g., `urllib.parse`): Overkill for simple validation.
    -   Separate regex for each method: Less DRY, as domain validation is shared.
-   **Extensibility**:
    -   Easily extended to support more complex domains (e.g., subdomains, other TLDs).
    -   Could add validation for specific cases (e.g., max length) if needed.
-   **Edge Cases**:
    -   Minimal domain: `a.b` is valid.
    -   Invalid domains: `pygen`, `pygen..ru`, `123.ru` raise `DomainException`.
    -   Invalid URLs: `http://pygen`, `ftp://pygen.ru` raise `DomainException`.
    -   Invalid emails: `user@pygen`, `123@pygen.ru` raise `DomainException`.
    -   Case sensitivity: Handled correctly, as regex uses `[a-zA-Z]`.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Test valid domain creation
domain1 = Domain('pygen.ru')
print(str(domain1))  # pygen.ru

domain2 = Domain.from_url('https://pygen.ru')
print(str(domain2))  # pygen.ru

domain3 = Domain.from_email('support@pygen.ru')
print(str(domain3))  # pygen.ru

# Test alternative valid cases
print(str(Domain('a.b')))  # a.b
print(str(Domain.from_url('http://test.com')))  # test.com
print(str(Domain.from_email('a@test.org')))  # test.org

# Test invalid cases
try:
    Domain('pygen')  # Invalid domain
except DomainException as e:
    print(e)  # Invalid domain, url, or email

try:
    Domain.from_url('http://pygen')  # Invalid URL
except DomainException as e:
    print(e)  # Invalid domain, url, or email

try:
    Domain.from_email('user@pygen')  # Invalid email
except DomainException as e:
    print(e)  # Invalid domain, url, or email
```

## Conclusion 🚀

The `DomainException` and `Domain` class implementations are precise, correctly handling domain creation, validation, and extraction from domains, URLs, and emails.
The regex-based validation ensures robust checking, and the class methods provide clear interfaces for alternative instantiation.
The implementation is efficient, extensible, and ideal for domain-related tasks or teaching regex and exception handling, fully compliant with the task’s requirements.
