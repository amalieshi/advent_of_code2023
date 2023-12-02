import re
from cube_conumdrum_func import (color_parser, color_police)

if __name__ == "__main__":
    data_path = r'../data/day2/example_1.txt'
    with open(data_path, "r") as f:
        doc = f.readlines()
    red_limit = 12
    green_limit = 13
    blue_limit = 14
    rgb_limit = [red_limit, green_limit, blue_limit]
    doc = [i.rstrip('\n') for i in doc]
    game_regex = re.compile(r'''(
    (Game\s) # 'Game '
    (?P<Game_ID>\d+) # numerical value of the Game ID
    (:\s) # ":" symbol and a space 
    (?P<Game1>[a-z0-9,\s]+) # the result of the first game
    (;\s)? # (optional) ';' symbol and a space   
    (?P<Game2>[a-z0-9,\s]*) # (optional) the result of the second game
    (;\s)? # (optional) ';' symbol and a space 
    (?P<Game3>[a-z0-9,\s]*) # (optional) the result of the third game
    (;\s)? # (optional) ';' symbol and a space 
    (?P<Game4>[a-z0-9,\s]*) # (optional) the result of the forth game
                                 )''', re.VERBOSE)
    black_list = [] # a list storing all the Game IDs that out of range of the given limit
    for clue in doc:
        mo = game_regex.search(clue)
        game_id = mo.group('Game_ID')
        game_1 = mo.group('Game1')
        game_2 = mo.group('Game2')
        game_3= mo.group('Game3')
        game_4 = mo.group('Game4')
        actual_rgb_value = color_parser(game_1)
        game_1_status = color_police(actual_rgb_value, rgb_limit)

    a=1
