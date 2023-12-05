# TODO 1: Break down the list into a dictionary.
# TODO 2: Create an panda dataframe of source and the corresponding destination.
# TODO 3: Find the location of the see.d
# TODO 4: Get the minimum seed number.

import re


def break_down_almanac(almanac):
    '''
    Use regex to break down the almanac (a list) into a dictionary.
    :param almanac: a list describing the almanac.
    :return: a dictionary where the key is the source to dictionary name and the values are the information about the replacement.
    '''
    dictionary_key = []
    dictionary_value = []
    almanac_in_str = ''.join(almanac)
    almanac_by_category = re.split(r'\n\n', almanac_in_str)
    for category in almanac_by_category:
        key, values = re.split(r'\:', category)
        values = re.split(r'\n', values)
        values = [i for i in values if i != '']
        values = [re.split('\s', i) for i in values]
        for loop, value in enumerate(values):
            value = [int(i) for i in value if i != '' ]
            values[loop] = value
        if key.find(' map') != -1:
            dictionary_key.append(key.replace(' map', ''))
        dictionary_value.append(values)
    almanac_in_dictionary = {dictionary_key[i]: dictionary_value[i] for i in range(len(dictionary_key))}
    return almanac_in_dictionary
