
def color_parser(string):
    red = 0
    green = 0
    blue =0
    cube_catalog = string.split(', ')
    for cube in cube_catalog:
        if not cube.find('red')==-1: # if the cube is about the blue kind
            red += int(cube.lstrip(' ')[0])
        if not cube.find('green')==-1: # if the cube is about the blue kind
            green += int(cube.lstrip(' ')[0])
        if not cube.find('blue')==-1: # if the cube is about the blue kind
            blue += int(cube.lstrip(' ')[0])
    return [red, green, blue]

def color_police(game_rgb_value, limit_rgb_value):
    '''
    a color police that will alarm (return true) if a cube of any color is out of the limit
    :param game_rgb_value:
    :param limit_rgb_value:
    :return:
    '''
    red_alarm = game_rgb_value[0] > limit_rgb_value[0]
    green_alarm = game_rgb_value[1] > limit_rgb_value[1]
    blue_alarm = game_rgb_value[2] > limit_rgb_value[2]
    if any([red_alarm, green_alarm, blue_alarm]):
        return True
    else:
        return False
