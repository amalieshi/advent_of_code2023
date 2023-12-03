from engine_gear_func import (
    is_digit,
    gather_all_symbols,
    is_symbol,
    find_positions_of_all_true_cell,
    is_neighbor_symbol,
    extract_value_from_part_number_index,
    remove_neighbors,
    find_position_of_the_star,
remove_neighbors_and_association
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
    part_number_indices , _ = is_neighbor_symbol(is_digit_indices, is_symbol_indices)
    single_part_number_indices = remove_neighbors(part_number_indices)
    all_part_numbers = []
    for part_number_index in single_part_number_indices:
        part_number = extract_value_from_part_number_index(part_number_index, doc)
        all_part_numbers.append(int(part_number))
    print(f"The sum of all parts numbers is {sum(all_part_numbers)}.")  # answer of part 1

    stars_positions = find_position_of_the_star(doc)
    part_numbers_indices_near_gear, association = is_neighbor_symbol(part_number_indices, stars_positions)
    single_part_numbers_indices_near_gear, association = remove_neighbors_and_association(part_numbers_indices_near_gear, association)
    part_numbers_near_gear = []
    for index in single_part_numbers_indices_near_gear:
        pn = extract_value_from_part_number_index(index, doc)
        part_numbers_near_gear.append(pn)
    pn_repository = [int(i) for i in part_numbers_near_gear]
    gear_ratio = 0
    is_gear_pn = []
    for loop, i in enumerate(association):
        if association.count(i)<2:
            is_gear_pn.append(False)
        else:
            is_gear_pn.append(True)
    gear_pn_repository = [value for i, value in enumerate(pn_repository) if is_gear_pn[i]]

    odd_digit_pn = gear_pn_repository[::2]
    even_digit_pn = gear_pn_repository[1::2]
    for loop, value in enumerate(odd_digit_pn):
        gear_ratio += value * even_digit_pn[loop]
    print(odd_digit_pn)
    print(even_digit_pn)
    print(pn_repository)
    print(gear_ratio)


