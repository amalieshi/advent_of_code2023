import re
from itertools import permutations

def is_digit(str):
    return [i.isdigit() for i in str]


def gather_all_symbols(doc):
    symbols_regex = re.compile(r"([^a-zA-Z0-9\.])")
    symbols = []
    for line in doc:
        symbol = symbols_regex.findall(line)
        symbols += symbol
    return set(symbols)


def is_symbol(str, symbols):
    return [i in symbols for i in str]


def find_positions_of_all_true_cell(boolean_2d_list):
    indices = []
    for row_index, row_value in enumerate(boolean_2d_list):
        for column_index, x in enumerate(row_value):
            if x:
                indices.append([row_index, column_index])
    return indices


def is_neighbor_symbol(is_digit_indices, is_symbol_indices):
    association_with_symbol = []
    neighbor_indices = []
    for is_digit_index in is_digit_indices:
        r = is_digit_index[0]
        c = is_digit_index[1]
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                cell_index = [i, j]
                if cell_index in is_symbol_indices:
                    neighbor_indices.append(is_digit_index)
                    association_with_symbol.append(cell_index)
    return neighbor_indices, association_with_symbol



def remove_neighbors(part_number_indices):
    single_part_number_indices = []
    for part_number_index in part_number_indices:
        if [part_number_index[0], part_number_index[1] + 1] not in part_number_indices:
            single_part_number_indices.append(part_number_index)
    return single_part_number_indices

def remove_neighbors_and_association(part_number_indices, association):
    single_part_number_indices = []
    association_without_neighbor = []
    for loop, part_number_index in enumerate(part_number_indices):
        if [part_number_index[0], part_number_index[1] + 1] not in part_number_indices:
            single_part_number_indices.append(part_number_index)
            association_without_neighbor.append(association[loop])
    return single_part_number_indices, association_without_neighbor

def extract_value_from_part_number_index(index, doc):
    r = index[0]
    c = index[1]
    row_schema = list(doc[r])
    reversed_value = []
    for i in reversed(row_schema[:c]):
        if i.isdigit():
            reversed_value.append(i)
        else:
            break
    start_value = "".join(reversed(reversed_value))
    end_value = []
    for i in row_schema[c:]:
        if i.isdigit():
            end_value.append(i)
        else:
            break
    start_value = "".join(reversed(reversed_value))
    end_value = "".join(end_value)
    final_value = start_value + end_value
    return final_value


def find_position_of_the_star(doc):
    all_positions_gears= []
    for r, line in enumerate(doc):
        c = line.find('*')
        if c != -1:
            all_positions_gears.append([r, c])
    return all_positions_gears




