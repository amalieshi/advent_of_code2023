from farming_func import break_down_almanac

if __name__ == '__main__':
    data_path = '../data/day5/almanac1.txt'
    with open(data_path,'r') as f:
        doc = f.readlines()
        seed = doc[0]
        almanac_maps = doc[2:]
        break_down_almanac(almanac_maps)