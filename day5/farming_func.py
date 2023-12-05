import re
import pandas as pd

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
        values = [re.split(r'\s', i) for i in values]
        for loop, value in enumerate(values):
            value = [int(i) for i in value if i != '' ]
            values[loop] = value
        if key.find(' map') != -1:
            dictionary_key.append(key.replace(' map', ''))
        dictionary_value.append(values)
    almanac_in_dictionary = {dictionary_key[i]: dictionary_value[i] for i in range(len(dictionary_key))}
    return almanac_in_dictionary

def find_swapping_location_and_value(lst):
    destination_start = lst[0]
    source_start = lst[1]
    range_length = lst[2]
    destination_end = destination_start + range_length
    source_end = source_start + range_length
    swap_value = list(range(destination_start, destination_end))
    swap_location = list(range(source_start, source_end))
    return swap_location, swap_value


def find_max_end_value(lst):
    destination_start = lst[0]
    source_start = lst[1]
    range_length = lst[2]
    destination_end = destination_start + range_length
    source_end = source_start + range_length
    max_end_value = max([destination_end, source_end])
    return max_end_value

def produce_destination_list(almanac_2D_list):
    max_value = 0
    for i in almanac_2D_list:
        max_in_one_item = find_max_end_value(i)
        if max_in_one_item > max_value:
            max_value = max_in_one_item
    destination_lst = range(0, max_value)
    index_lst = [str(i) for i in destination_lst]
    desination_series =pd.Series(destination_lst, index=index_lst)
    for i in almanac_2D_list:
        swap_location, swap_value = find_swapping_location_and_value(i)
        desination_series.iloc[swap_location] = swap_value
    return desination_series.to_list()