'''
TODO:
    You have access to the data dictionary.
    Complete the code below to print this dictionary in reverse order.

NOTE:
    For example, if the data dictionary were:
        data = OrderedDict(key1='value1', key2='value2', key3='value3')
    then the program would print (prior to Python 3.12):
        OrderedDict(
            [('key3', 'value3'), ('key2', 'value2'), ('key1', 'value1')]
        )
    in Python 3.12:
        OrderedDict(
            {('key3', 'value3'), ('key2', 'value2'), ('key1', 'value1')}
        )
'''
from collections import OrderedDict


def reverse_dict_order(
    ordered_dict: OrderedDict[str, str]
) -> OrderedDict[str, str]:
    """
    Reverses the order of an OrderedDict.

    Args:
        ordered_dict (OrderedDict[str, str]): The OrderedDict to reverse.

    Returns:
        OrderedDict[str, str]: The reversed OrderedDict with items in
        reverse order.
    """
    return OrderedDict(reversed(list(ordered_dict.items())))


data = OrderedDict({
    'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника',
    'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ',
    'District': 'район Арбат',
    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2',
    'SeatsCount': '10'
})
print(reverse_dict_order(data))
