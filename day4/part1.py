from sort_cards_func import find_matching_cards

if __name__ == "__main__":
    data_path = "../data/day4/card_pattern1.txt"
    game_points = 0
    with open(data_path, "r") as f:
        games = f.readlines()
    games = [i.split("\n")[0] for i in games]
    for game in games:
        common_set = find_matching_cards(game)
        power_value = len(common_set) - 1
        if power_value >= 0:
            game_points += pow(2, power_value)
    print(f"The answer to part 1 is {game_points}")
