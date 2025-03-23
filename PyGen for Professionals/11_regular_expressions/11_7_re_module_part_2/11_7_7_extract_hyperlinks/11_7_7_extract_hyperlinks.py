'''
TODO:
    HTML elements are the basis of the HTML language.

    Each HTML element is designated by a start (opening) and end (closing) tag.

    The opening and closing tags contain the name of the element.

    The opening tag can contain additional information - attributes and
    attribute values.

    Hyperlinks in HTML are created using the <a></a> tag.

    The text that will be displayed on the web page is placed inside.

    A mandatory component of the <a></a> tag is the href attribute, which
    specifies the URL of the web page:
        <a href="https://stepik.org">Stepik</a>

    A hyperlink consists of two parts - a pointer (Stepik) and an address part
    (https://stepik.org).

    A link pointer is a fragment of text or an image visible to the user.

    The address part of the link is not visible to the user, it is the address
    of the resource to which you need to go.

    Sometimes the pointer can be surrounded by various tags
    (<b></b>, <h1></h1>):
        <a href="https://stepik.org"><b><h1>Stepik</h1></b></a>

    Write a program that finds all hyperlinks in an HTML page fragment and
    outputs their components — address parts and pointers.

    The program is fed an arbitrary number of lines that form an HTML page
    fragment.

    The program must find all hyperlinks in the entered HTML page fragment and
    output their components — address parts and pointers, in the following
    format:
        <address part>, <pointer>
        <address part>, <pointer>
        ...

NOTE:
    The order of the data about the next hyperlink must match the order of
    their sequence in the entered HTML page fragment.
'''
import re
import sys
from typing import List


def read_lines_from_input() -> List[str]:
    """
    Reads input lines from stdin.

    This function reads all input lines, strips trailing
    whitespace, and returns them as a list of strings.

    Returns:
        List[str]: A list of strings representing the input lines.
    """
    return [line.strip() for line in sys.stdin.readlines()]


def extract_hyperlinks(html_code: List[str]):
    """
    Extracts hyperlinks (address parts and pointers) from the given HTML code.

    This function uses a regular expression to find all <a> tags with an href
    attribute in the input HTML code and prints the corresponding address and
    pointer (text inside the <a> tag).

    Args:
        html_code (List[str]): A list of strings representing the HTML code
        to process.
    """
    regex = r'<a\s+href="([^"]+)">(.+?)</a>'
    html_text = ''.join(html_code)
    links = re.findall(regex, html_text)
    for address, pointer in links:
        print(f"{address}, {pointer}")


extract_hyperlinks(read_lines_from_input())
