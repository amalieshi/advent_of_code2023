import re
if __name__ == '__main__':
    with open('../data/day6/data1.txt') as f:
        doc = f.readlines()
    time_info = re.split(r'\s', doc[0])
    distance_info = re.split(r'\s', doc[1])
    a=1