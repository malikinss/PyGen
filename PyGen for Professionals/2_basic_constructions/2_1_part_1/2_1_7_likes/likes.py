'''
TODO:
    There are systems of likes in various social networks, which, depending on
    the number of people who rated the post, show relevant information.

    Implement the likes() function, which takes a single argument:
        names — list of names

    The function should return a string according to the examples below,
    the content of which depends on the number of names in the names list.

NOTE:
    The names in the string generated and returned by the function must be in
    their original order.

    Note that if there are more than three names in the list passed to the
    function, then only the first two of them are explicitly specified.
'''
from typing import List


def likes(names: List[str]) -> str:
    """
    Returns a message based on the number of names in the 'names' list.

    Args:
        names (List[str]): A list of names who liked the post.

    Returns:
        str: A message indicating who liked the post, or if no one did.

    - If the list is empty, it returns:
        "Никто не оценил данную запись"
    - If one name, it returns:
        "<name> оценил(а) данную запись"
    - If two names, it returns:
        "<name1> и <name2> оценили данную запись"
    - If three names, it returns:
        "<name1>, <name2> и <name3> оценили данную запись"
    - If more than three names, it returns:
        "<name1>, <name2> и <n других> оценили данную запись"
    """
    number_of_likes = len(names)

    if number_of_likes == 0:
        return "Никто не оценил данную запись"
    elif number_of_likes == 1:
        return f"{names[0]} оценил(а) данную запись"
    elif number_of_likes == 2:
        return f"{names[0]} и {names[1]} оценили данную запись"
    elif number_of_likes == 3:
        return f"{names[0]}, {names[1]} и {names[2]} оценили данную запись"
    else:
        return f"{names[0]}, {names[1]} и {number_of_likes - 2} других " \
               "оценили данную запись"
