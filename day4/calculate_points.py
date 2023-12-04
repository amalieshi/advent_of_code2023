import re

if __name__ == '__main__':
    data_path = '../data/day4/card_pattern2.txt'
    game_point = 0
    with open(data_path, 'r') as f:
        games = f.readlines()
    games = [i.split('\n')[0] for i in games]
    for game in games:
        result = re.split(r'[\:\|]',game)
        winning_cards = set([i for i in result[1].split(' ') if i !=''])
        observation_cards = set([i for i in result[2].split(' ') if i !=''])
        common_set = winning_cards.intersection(observation_cards)
        power_value = len(common_set) - 1
        if power_value >=0:
            game_point += pow(2, power_value)
    print(game_point)