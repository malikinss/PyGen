# Email Greeting Validator

## Description 📝

This program checks if an email starts with one of Timur's preferred greetings.
If the email starts with a greeting such as "Hello", "Good morning", "Good afternoon", or "Good evening" (case-insensitive), it is considered worthy of attention.

## Purpose 🎯

The purpose of this program is to determine if an email is worthy of Timur’s attention based on whether it begins with one of his favorite greetings.

## How It Works 🔍

1. **Input**:

    - The program accepts a single string as input, which represents the subject of an email or a letter.

2. **Regex Matching**:

    - The program uses a regular expression to check if the input string starts with one of the following greetings:
        - "Hello"
        - "Good morning"
        - "Good afternoon"
        - "Good evening"

    The matching is case-insensitive to allow any capitalization of the greetings.

3. **Output**:
    - The program will output `True` if the email starts with one of the above greetings and `False` otherwise.

## Output 📜

### Example Input:

```text
Good evening, I hope you're well.
```

### Example Output:

```text
True
```

### Example Input:

```text
Hey there, I wanted to discuss something important.
```

### Example Output:

```text
False
```

## Usage 📦

1. Save the program in a Python file (e.g., `email_greeting_validator.py`).
2. Run the script.
3. Enter the email greeting string when prompted.
4. The program will output `True` if the greeting matches Timur’s criteria, or `False` otherwise.

## Conclusion 🚀

This program is a simple and efficient way to determine whether an email starts with a greeting Timur values.
It's helpful in filtering out unwanted emails and ensuring only the emails that follow his preferred greetings are worthy of his attention.
