import re
from cube_conumdrum_func import color_parser, color_police, max_rgb_for_a_game

if __name__ == "__main__":
    data_path = r"../data/day2/example_2.txt"
    with open(data_path, "r") as f:
        doc = f.readlines()
    red_limit = 12
    green_limit = 13
    blue_limit = 14
    rgb_limit = [red_limit, green_limit, blue_limit]
    doc = [i.rstrip("\n") for i in doc]
    game_regex = re.compile(
        r"""(
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
    (;\s)? # (optional) ';' symbol and a space 
    (?P<Game5>[a-z0-9,\s]*) # (optional) the result of the fifth game
    (;\s)? # (optional) ';' symbol and a space 
    (?P<Game6>[a-z0-9,\s]*) # (optional) the result of the sixth game
                                 )""",
        re.VERBOSE,
    )
    white_list = (
        []
    )
    power_rgb_sum = 0# a list storing all the Game IDs that out of range of the given limit
    for loop, clue in enumerate(doc):
        mo = game_regex.search(clue)
        game_id = mo.group("Game_ID")
        game_1 = mo.group("Game1")
        game_2 = mo.group("Game2")
        game_3 = mo.group("Game3")
        game_4 = mo.group("Game4")
        game_5 = mo.group("Game5")
        game_6 = mo.group("Game6")
        actual_rgb_value_game1 = color_parser(game_1)
        game_1_status = color_police(actual_rgb_value_game1, rgb_limit)
        actual_rgb_value_game2 = color_parser(game_2)
        game_2_status = color_police(actual_rgb_value_game2, rgb_limit)
        actual_rgb_value_game3 = color_parser(game_3)
        game_3_status = color_police(actual_rgb_value_game3, rgb_limit)
        actual_rgb_value_game4 = color_parser(game_4)
        game_4_status = color_police(actual_rgb_value_game4, rgb_limit)
        actual_rgb_value_game5 = color_parser(game_5)
        game_5_status = color_police(actual_rgb_value_game5, rgb_limit)
        actual_rgb_value_game6 = color_parser(game_6)
        game_6_status = color_police(actual_rgb_value_game6, rgb_limit)
        rgb_results = [actual_rgb_value_game1, actual_rgb_value_game2, actual_rgb_value_game3, actual_rgb_value_game4, actual_rgb_value_game5, actual_rgb_value_game6]
        max_rgb = max_rgb_for_a_game(rgb_results)
        power_rgb = max_rgb[0]*max_rgb[1]*max_rgb[2]
        power_rgb_sum += power_rgb
        if not any([game_1_status, game_2_status, game_3_status, game_4_status,game_5_status,game_6_status]):
            white_list.append(int(game_id))
    print(sum(white_list))
    print(power_rgb_sum)
