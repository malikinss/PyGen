'''
TODO:
    You have access to the already implemented send_email() function, which
    takes three arguments in the following order:
        name — name
        email_address — email address
        text — content of the letter

    The function sends a letter to the user named name to the address
    email_address with the content text.

    Implement the to_Timur() function using the partial() function, which
    takes one argument:
        text — content of the letter

    The function should send a letter to the user named Timur to the address
    timyrik20@beegeek.ru with the content text.

    Implement the send_an_invitation() function using the partial() function,
    which takes two arguments in the following order:
        name — name
        email_address — email address

    The function should send a letter to the name name and to the address
    email_address with the following content:
        BEEGEEK School invites you to a new course on programming in Python.
        here...

NOTE:
    The functions to_Timur() and send_an_invitation() must be partial objects.
'''
from functools import partial


def send_email(name: str, email_address: str, text: str) -> str:
    """
    Sends an email to the given name and email address with the provided text.

    Args:
        name (str): The recipient's name
        email_address (str): The recipient's email address
        text (str): The content of the email

    Returns:
        str: Confirmation of the email being sent
    """
    try:
        # Simulate email sending logic
        return (
            f'В письме для {name} на адрес {email_address}'
            f' сказано следующее: {text}'
        )
    except Exception as e:
        return f"Ошибка при отправке письма: {e}"


# Partial function to send an email to Timur
to_timur = partial(
    send_email,
    'Тимур',  # Fixed name
    'timyrik20@beegeek.ru'  # Fixed email address
)

# Partial function to send an invitation with a default message
send_an_invitation = partial(
    send_email,
    text='Школа BEEGEEK приглашает Вас на новый курс по программированию \
        на языке Python. Здесь...'
)

print(to_timur(text="Добро пожаловать в наш курс!"))
print(send_an_invitation(name="Анна", email_address="anna@example.com"))
