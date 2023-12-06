import re
import numpy as np

def find_all_winning_instance_holding_time(time, winning_distance):
    '''
    Create a list of all the instance of holding time if it wins the game.
    :param time: an integer
    :return:
    '''
    winning_holding_time = []
    for i in range(time):
        speed = i
        time_travelled = time - i
        total_distance = speed * time_travelled
        if total_distance > winning_distance:
            winning_holding_time.append(i)
    return winning_holding_time



if __name__ == '__main__':
    with open('../data/day6/data2.txt') as f:
        doc = f.readlines()
    # Part 1
    time_info = re.split(r'\s+', doc[0])
    time_info = [i for i in time_info if i != '']
    distance_info = re.split(r'\s+', doc[1])
    total_winning_instances = []
    for i in range(1, len(time_info)):
        winning_holding_time = find_all_winning_instance_holding_time(int(time_info[i]), int(distance_info[i]))
        total_winning_instances.append(len(winning_holding_time))
    result = np.prod(total_winning_instances)
    print(f'The result of part one is {result}')

    # PART 2
    _, time_info = re.split(r'\:\s+', doc[0])
    time_info = time_info.replace('\n', '').replace(' ', '')
    _, distance_info = re.split(r'\:\s+', doc[1])
    distance_info = distance_info.replace('\n', '').replace(' ', '')
    ans2 = len(find_all_winning_instance_holding_time(int(time_info), int(distance_info)))
    print(f'The answer to part 2 is {ans2}')
