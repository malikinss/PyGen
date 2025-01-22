'''
TODO:
    The emails dictionary contains information about user email addresses,
    grouped by domain.

    Expand the code to display all email addresses in alphabetical order,
    each on a separate line, in the format username@domain.

NOTE:
    To sort alphabetically, use the built-in sorted() function or the sort()
    list method.

    You don't need to group email addresses by domain.
'''


def print_sorted_emails(emails: dict) -> None:
    """
    Prints all email addresses in alphabetical order, each on a new line,
    in the format username@domain.

    Args:
        emails (dict): A dictionary where keys are domains (str) and values
                       are lists of usernames (str).
    """
    # Generate the full email addresses and sort them
    emails_list = [
        f"{username}@{domain}"
        for domain, usernames in emails.items()
        for username in usernames
    ]

    for email in sorted(emails_list):
        print(email)


# Input dictionary
emails = {
    'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
    'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
    'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
    'yandex.ru': ['surface', 'google'],
    'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
    'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']
}

# Print the sorted emails
print_sorted_emails(emails)
