from farming_func import break_down_almanac

if __name__ == '__main__':
    data_path = '../data/day5/almanac1.txt'
    with open(data_path,'r') as f:
        doc = f.readlines()
        break_down_almanac(doc)