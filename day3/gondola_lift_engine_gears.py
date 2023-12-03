from engine_gear_func import (
    is_digit,
    gather_all_symbols,
    is_symbol,
    find_positions_of_all_true_cell,
    is_neighbor_symbol,
    extract_value_from_part_number_index,
    remove_neighbors,
)

if __name__ == "__main__":
    data_path = r"../data/day3/schema_example2.txt"
    with open(data_path, "r") as f:
        doc = f.readlines()
    doc = [i.strip() for i in doc]
    is_digit_map = []
    is_symbol_map = []
    for row in doc:
        is_digit_for_row = is_digit(row)
        symbols = gather_all_symbols(doc)
        is_symbol_for_row = is_symbol(row, symbols)
        is_digit_map.append(is_digit_for_row)
        is_symbol_map.append(is_symbol_for_row)
    is_digit_indices = find_positions_of_all_true_cell(is_digit_map)
    is_symbol_indices = find_positions_of_all_true_cell(is_symbol_map)
    part_number_indices = is_neighbor_symbol(is_digit_indices, is_symbol_indices)
    part_number_indices = remove_neighbors(part_number_indices)
    all_part_numbers = []
    for part_number_index in part_number_indices:
        part_number = extract_value_from_part_number_index(part_number_index, doc)
        all_part_numbers.append(int(part_number))
    print(sum(all_part_numbers))  # answer of part 1
