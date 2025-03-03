# Email Sending with Partial Functions 📝

## Description 📝

This task demonstrates how to use Python's `partial` function from the `functools` module to create reusable email-sending functionalities with fixed parameters.
The goal is to implement two partial functions that send emails to specific recipients with customizable messages.

## Purpose 🎯

The purpose of these partial functions is to streamline the process of sending emails.
By fixing certain parameters, such as recipient name and email address, we minimize redundancy in the code.
The flexibility of these partial functions allows for easy customization of other parameters, like the email text.

## How It Works 🔍

1. **`to_Timur` Function**:

    - A partial function pre-configured with the recipient's name (`Timur`) and email address (`timyrik20@beegeek.ru`).
    - Only the `text` (content of the email) is customizable when the function is called.

2. **`send_an_invitation` Function**:
    - A partial function pre-configured with a default invitation message.
    - The recipient's `name` and `email_address` are flexible and specified when calling the function.

## Output 📜

The output for both functions should be a confirmation message showing the recipient's name, email address, and the content of the email.

## Usage 📦

1. **`to_timur`**: This function sends an email specifically to "Timur" at `timyrik20@beegeek.ru`. The content (`text`) can be customized on each call.

    Example usage:

    ```python
    to_timur(text="Добро пожаловать в наш курс!")
    ```

2. **`send_an_invitation`**: This function sends a predefined invitation email. The recipient's `name` and `email_address` are specified when calling the function.

    Example usage:

    ```python
    send_an_invitation(name="Анна", email_address="anna@example.com")
    ```

## Conclusion 🚀

By using the `partial` function, you can create flexible and reusable email-sending functions with fixed parameters.
This approach reduces code repetition and enhances modularity, making the email-sending process easier to manage.
