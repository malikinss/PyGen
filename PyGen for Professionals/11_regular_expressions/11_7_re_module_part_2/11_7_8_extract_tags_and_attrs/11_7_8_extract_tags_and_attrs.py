'''
TODO:
    HTML elements are the basis of the HTML language.

    Each HTML element is designated by a start (opening) and end (closing) tag.

    The opening and closing tags contain the name of the element.

    The opening tag can contain additional information - attributes and
    attribute values:
        <b>BeeGeek</b>
        <a href="https://stepik.org">Stepik</a>

    In the example above, the <b> tag does not contain any attributes, and
    the <a> tag contains the href attribute with the value https://stepik.org.

    Write a program that finds all the attributes of each tag in an HTML page
    fragment.

    The program is given an arbitrary number of lines that form an HTML page
    fragment.

    The program must find all the tags in the entered HTML page fragment and
    output them, specifying the corresponding attributes for each.

    Tags together with all attributes must be placed each on a separate line,
    in the following format:
        <tag>: <attribute>, <attribute>, ...

    Tags, as well as tag attributes, must be placed in lexicographic order.
'''
import re
import sys
from typing import List, Dict, Set
from collections import defaultdict


def read_lines_from_input() -> List[str]:
    """
    Reads input lines from stdin and returns them as a list of stripped
    strings.

    Returns:
        List[str]: A list of strings representing lines of an HTML fragment.
    """
    return [line.strip() for line in sys.stdin.readlines()]


def extract_tags(html_code: List[str]) -> str:
    """
    Combines a list of HTML lines into a single string.

    Args:
        html_code (List[str]): List of HTML fragment lines.

    Returns:
        str: The combined HTML text as a single string.
    """
    return ''.join(html_code)


def find_all_tags(html_text: str) -> List[re.Match]:
    """
    Identifies all HTML tags and their attributes in the given HTML text.

    Args:
        html_text (str): The HTML fragment as a single string.

    Returns:
        List[re.Match]: A list of regex match objects representing HTML tags.
    """
    tag_regex = r'<(\w+)([^>]*)>'
    return list(re.finditer(tag_regex, html_text))


def find_attributes(attributes_str: str) -> List[str]:
    """
    Extracts attribute names from a string containing tag attributes.

    The regex correctly captures attributes, including those containing
    hyphens.

    Args:
        attributes_str (str): A string containing tag attributes.

    Returns:
        List[str]: A list of extracted attribute names.
    """
    attrs_regex = r'([a-zA-Z0-9_-]+)\s*(?:=\s*["\'][^"\']*["\'])?'
    return re.findall(attrs_regex, attributes_str)


def process_tags_and_attrs(html_text: str) -> Dict[str, Set[str]]:
    """
    Parses an HTML fragment and organizes tags with their attributes.

    Args:
        html_text (str): The HTML fragment as a single string.

    Returns:
        Dict[str, Set[str]]: A dictionary where keys are tag names and values
                             are sets of attributes.
    """
    tags_dict = defaultdict(set)
    for match in find_all_tags(html_text):
        tag = match.group(1)
        attributes_str = match.group(2)
        attributes = find_attributes(attributes_str)
        tags_dict[tag].update(attributes)
    return tags_dict


def sort_and_print_tags(tags_dict: Dict[str, Set[str]]) -> None:
    """
    Sorts and prints HTML tags along with their attributes in lexicographical
    order.

    Args:
        tags_dict (Dict[str, Set[str]]): A dictionary mapping tags to their
                                         attribute sets.

    Output Format:
        <tag>: <attribute1>, <attribute2>, ...
    """
    for tag in sorted(tags_dict.keys()):
        sorted_attrs = sorted(tags_dict[tag])
        print(
            f"{tag}: {', '.join(sorted_attrs)}" if sorted_attrs else f"{tag}:"
        )


def extract_tags_and_attrs(html_code: List[str]) -> None:
    """
    Extracts and displays HTML tags along with their attributes.

    Args:
        html_code (List[str]): List of HTML fragment lines.

    Output Format:
        The function prints each tag along with its attributes in
        lexicographical order.
    """
    html_text = extract_tags(html_code)
    tags_dict = process_tags_and_attrs(html_text)
    sort_and_print_tags(tags_dict)


extract_tags_and_attrs(read_lines_from_input())
