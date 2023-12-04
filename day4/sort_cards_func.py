import re
def find_matching_cards(game):
    result = re.split(r"[\:\|]", game)
    winning_cards = set([i for i in result[1].split(" ") if i != ""])
    observation_cards = set([i for i in result[2].split(" ") if i != ""])
    common_set = winning_cards.intersection(observation_cards)
    return common_set