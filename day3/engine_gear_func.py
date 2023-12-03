from itertools import chain

def is_digit(str):
    return [i.isdigit() for i in str]

def is_symbol(str):
    symbols = '*, #, +, $'
    symbols = symbols.split(', ')
    return [i in symbols for i in str]


def find_positions_of_all_true_cell(boolean_2d_list):
    indices_in_2D = [[]]
    for row_index, row_value in enumerate(boolean_2d_list):
        indices =[[row_index, column_index] for column_index, x in enumerate(row_value) if x]
    return indices