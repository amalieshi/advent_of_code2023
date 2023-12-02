def color_parser(string):
    '''
    parsing a subgame into a list of rgb value
    :param string: a string describing the sub-game
    :return: a list of the rgb value
    '''
    red = 0
    green = 0
    blue = 0
    cube_catalog = string.split(", ")
    for cube in cube_catalog:
        if not cube.find("red") == -1:  # if the cube is about the blue kind
            red += int(cube.split(" ")[0])
        if not cube.find("green") == -1:  # if the cube is about the blue kind
            green += int(cube.split(" ")[0])
        if not cube.find("blue") == -1:  # if the cube is about the blue kind
            blue += int(cube.split(" ")[0])
    return [red, green, blue]


def color_police(game_rgb_value, limit_rgb_value):
    """
    a color police that will alarm (return true) if a cube of any color is out of the limit
    :param game_rgb_value: the list of the quantities of the cube in the sub-game
    :param limit_rgb_value: the given limit of the rgb value from the question prompt
    :return:
    """
    if game_rgb_value is None:
        return False
    else:
        red_alarm = game_rgb_value[0] > limit_rgb_value[0]
        green_alarm = game_rgb_value[1] > limit_rgb_value[1]
        blue_alarm = game_rgb_value[2] > limit_rgb_value[2]
        if any([red_alarm, green_alarm, blue_alarm]):
            return True
        else:
            return False

def max_rgb_for_a_game(rgb_results):
    """
    getting the rbg value for a game and produce a list of the maximum number of cube from each color category
    :param rgb_results: the list of all the sub-game results
    :return:
    """
    red_max = rgb_results[0][0]
    green_max = rgb_results[0][1]
    blue_max = rgb_results[0][2]
    for rgb in rgb_results:
        red_max = max([red_max, rgb[0]])
        green_max = max([green_max, rgb[1]])
        blue_max = max([blue_max, rgb[2]])
    return [red_max, green_max, blue_max]