from farming_func import break_down_almanac, produce_destination_list
import re
import numpy as np
import pandas as pd
# TODO 4: Get the minimum seed number.

if __name__ == '__main__':
    data_path = '../data/day5/almanac2.txt'
    with open(data_path,'r') as f:
        doc = f.readlines()
    # Step 1: Break down the list into a dictionary.
    seeds = doc[0].replace('\n','')
    _ , seeds_value = seeds.split(r': ')
    seeds_value = re.split(r'\s', seeds_value)
    seeds_value = [int(i) for i in seeds_value]
    almanac_maps = doc[2:]
    almanac_maps = break_down_almanac(almanac_maps)
    # Create a panda dataframe of source and the corresponding destination.
    full_list = []
    for key in almanac_maps.keys():
        lst = produce_destination_list(almanac_maps[key])
        full_list.append(lst)
    df = pd.DataFrame(full_list)
    df = df.T
    column_names = [i for i in almanac_maps.keys()]
    df.columns = column_names
    # Find the location of the seed
    total_steps = len(df.columns)
    all_locations = []
    for tracker in seeds_value:
        for i in range(total_steps):
            series = df.iloc[:, i]
            result = series.iloc[tracker]
            if np.isnan(result):
                result = int(tracker)
            else:
                tracker = int(result)
        all_locations.append(tracker)
    answer_to_part_one = min(all_locations)
    print(f"The answer to part one is {answer_to_part_one}.")