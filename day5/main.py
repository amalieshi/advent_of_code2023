from farming_func import break_down_almanac, produce_destination_series
import re
import pandas as pd
# TODO 2: Create an panda dataframe of source and the corresponding destination.
# TODO 3: Find the location of the see.d
# TODO 4: Get the minimum seed number.

if __name__ == '__main__':
    data_path = '../data/day5/almanac1.txt'
    with open(data_path,'r') as f:
        doc = f.readlines()
    # Step 1: Break down the list into a dictionary.
    seeds = doc[0].replace('\n','')
    _ , seeds_value = seeds.split(': ')
    seeds_value = re.split('\s', seeds_value)
    seeds_value = [int(i) for i in seeds_value]
    almanac_maps = doc[2:]
    almanac_maps = break_down_almanac(almanac_maps)
    produce_destination_series(almanac_maps['seed-to-soil'])
    a=1