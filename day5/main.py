from farming_func import break_down_almanac, produce_destination_list
import re
import pandas as pd
# TODO 3: Find the location of the see.d
# TODO 4: Get the minimum seed number.

if __name__ == '__main__':
    data_path = '../data/day5/almanac1.txt'
    with open(data_path,'r') as f:
        doc = f.readlines()
    # Step 1: Break down the list into a dictionary.
    seeds = doc[0].replace('\n','')
    _ , seeds_value = seeds.split(r': ')
    seeds_value = re.split(r'\s', seeds_value)
    seeds_value = [int(i) for i in seeds_value]
    almanac_maps = doc[2:]
    almanac_maps = break_down_almanac(almanac_maps)
    # Create an panda dataframe of source and the corresponding destination.
    full_list = []
    for key in almanac_maps.keys():
        list = produce_destination_list(almanac_maps[key])
        full_list.append(list)
    df = pd.DataFrame(full_list)
    df = df.T
    column_names = [i for i in almanac_maps.keys()]
    df.columns = column_names
    a=1
