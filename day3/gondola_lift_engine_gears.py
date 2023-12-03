from engine_gear_func import (is_digit, is_symbol, find_positions_of_all_true_cell)

if __name__ == '__main__':
    data_path = r'../data/day3/example_engine_schema1.txt'

    with open(data_path, 'r') as f:
        doc = f.readlines()

    is_digit_map = []
    is_symbol_map = []
    for row in doc:
        is_digit_for_row = is_digit(row)
        is_symbol_for_row = is_symbol(row)
        is_digit_map.append(is_digit_for_row)
        is_symbol_map.append(is_symbol_for_row)
        a = find_positions_of_all_true_cell(is_digit_map)
    a=1