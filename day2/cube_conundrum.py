import re

if __name__ == "__main__":
    data_path = r'../data/day2/example_2.txt'

    with open(data_path, "r") as f:
        doc = f.readlines()
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

    for clue in doc:
        mo = game_regex.search(clue)
        print(mo.group('Game_ID'))
        print(mo.group('Game1'))
        print(mo.group('Game2'))
        print(mo.group('Game3'))
        print(mo.group('Game4'))

