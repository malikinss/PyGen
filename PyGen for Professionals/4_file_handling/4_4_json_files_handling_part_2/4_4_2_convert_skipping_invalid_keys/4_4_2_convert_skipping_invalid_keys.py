'''
TODO:
    Complete the code below so that it converts the words dictionary to a
    JSON string, skipping pairs that have invalid keys, and assigns the
    result to the data_json variable.
'''
import json
from typing import Dict


def convert_words_to_json(words: Dict) -> str:
    """
    Converts the words dictionary to a JSON string, skipping pairs with
    invalid keys.

    Args:
        words (Dict): A dictionary containing words as keys and their
        corresponding phonetic representations as values.

    Returns:
        str: The JSON string representation of the dictionary, with invalid
        keys skipped.
    """
    return json.dumps(words, skipkeys=True)


# Example usage
words: Dict = {
    frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
    "travel": "trævl",
    ("hello", "world"): ("həˈləʊ", "wɜːld"),
    "moonlight": "muːn.laɪt",
    "sunshine": "ˈsʌn.ʃaɪn",
    ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
    "adventure": "ədˈventʃər",
    "beautiful": "ˈbjuːtɪfl",
    frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
    "bicycle": "baisikl",
    ("pilot", "fly"): ("pailət", "flai")
}
print(convert_words_to_json(words))
