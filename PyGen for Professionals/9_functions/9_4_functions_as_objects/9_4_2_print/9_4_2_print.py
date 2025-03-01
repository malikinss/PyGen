# TODO:
#         Write a program that overrides the built-in print() function so that
#         it prints all passed string arguments in uppercase.
#
# NOTE:
#         The sep and end values must also be converted to uppercase.

original_print = print


def print(*args: tuple, **kwargs: dict) -> None:
    """
    Custom print function that prints all string arguments in uppercase.

    Args:
        *args (Any): Positional arguments to be printed.
        **kwargs (Any): Keyword arguments, including 'sep' and 'end'.

    Returns:
        None
    """
    def _is_str(obj):
        return isinstance(obj, str)

    def _update_print_kwargs(kwargs_dict: dict[str, str]) -> dict[str, str]:
        """
        Update keyword arguments for print function.

        Args:
            kwargs_dict (dict[str, str]): Dictionary of keyword arguments.

        Returns:
            updated_kwargs (dict[str, str]): Updated dictionary with modified
            values.
        """

        updated_kwargs = {'sep': ' ', 'end': '\n'}

        for key in updated_kwargs:
            # If the key is in the original dictionary, update the value.
            if key in kwargs_dict:
                old_kwarg = kwargs_dict[key]

                if _is_str(old_kwarg):
                    old_kwarg = old_kwarg.upper()

                updated_kwargs[key] = old_kwarg

        return updated_kwargs

    def _convert_args_to_uppercase(args: tuple) -> tuple:
        """
        Convert all string arguments to uppercase.

        Args:
            args (tuple): Tuple of arguments to be converted.

        Returns:
            tuple: Tuple with string arguments converted to uppercase.
        """
        return tuple(arg.upper() if _is_str(arg) else arg for arg in args)

    uppercased_args = _convert_args_to_uppercase(args)

    kwargs = _update_print_kwargs(kwargs)

    original_print(*uppercased_args, sep=kwargs['sep'], end=kwargs['end'])
