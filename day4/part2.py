from sort_cards_func import find_matching_cards

if __name__ == "__main__":
    data_path = "../data/day4/card_pattern2.txt"
    with open(data_path, "r") as f:
        games = f.readlines()
    games = [i.split("\n")[0] for i in games]

    total_games = len(games)
    card_account = {str(i): 1 for i in range(1, total_games+1)}
    for game_index, game in enumerate(games[:-1], 1):
        common_set = find_matching_cards(game)
        power_value = len(common_set)
        if power_value >= 0:
            current_number_of_cards = card_account[str(game_index)]
            for i in range(game_index+1, game_index+power_value+1):
                card_account[str(i)] = current_number_of_cards + card_account[str(i)]
    total_scratch_cards = sum(card_account.values())

    print(f'There are {total_scratch_cards} scratchcards in the end')
