'''
TODO:
    The ignore_command() function takes a single string argument
    command - the command to check, and returns True if the command contains
    a substring from the ignore list, or False if it does not.

    def ignore_command(command):
        ignore = [
            'alias', 'configuration', 'ip',
            'sql', 'select', 'update',
            'exec', 'del', 'truncate'
        ]

        for word in ignore:
            if word in command:
                return True

        return False

    Rewrite the ignore_command() function to use the built-in all()/any()
    functions, while preserving its functionality.
'''


def ignore_command(command: str) -> bool:
    """
    Checks if the given command contains any forbidden substrings.

    Args:
        command (str): The command to check.

    Returns:
        bool: True if the command contains a forbidden substring,
              otherwise False.
    """
    ignore = [
        'alias', 'configuration', 'ip',
        'sql', 'select', 'update',
        'exec', 'del', 'truncate'
    ]

    return any(word in command for word in ignore)
