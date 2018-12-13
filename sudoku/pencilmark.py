"""
Created on 29/11/2018
@author: nidragedd
"""

from utils import commons, positions


def use_pencil(values_to_set):
    """
    Start the pencil mark algorithm by giving it the initial values (unknown values are represented by a '0' digit).
    The strategy is to loop until we cannot deduce new values to place in the given sudoku. For very basic puzzles,
    this algorithm might fill it up.
    :param values_to_set: (string) the initial values (unknown values are represented by a '0' digit)
    :return: (string)  new values to init the puzzle
    """
    found_new = True
    given_fixed_values = values_to_set
    sudoku_size = commons.get_sudoku_size(given_fixed_values)
    grid_size = commons.get_grid_size(given_fixed_values)

    while found_new:
        pencil_mark = get_pencil_mark(given_fixed_values, sudoku_size, grid_size)
        new_values = generate_values_from_pencil(pencil_mark)
        found_new = new_values != given_fixed_values
        given_fixed_values = new_values
    return given_fixed_values


def get_pencil_mark(given_fixed_values, sudoku_size, grid_size):
    """
    Pencil mark method: each cell has a bool array (all init to True). Each of the boolean represents the digit (from 1
    to N = sudoku size). For each given fixed value we put other boolean (so representing other digits) to False in same
    row, column, grid
    :param given_fixed_values: (string) the initial values (unknown values are represented by a '0' digit)
    :param sudoku_size: (int) the sudoku size, for a 9x9 sudoku puzzle, it will be 9
    :param grid_size: (int) the sudoku size, for a 9x9 sudoku puzzle, it will be 3
    :return: (dict) a pencil mark object. Key is the row/column position and value is a boolean array where True means
    that the value is fixed
    """
    # 1- Init a pencil mark with all set to True
    pencil_mark = {}
    for i in range(sudoku_size):
        for j in range(sudoku_size):
            pencil_mark[commons.build_fixed_val_key(i, j)] = [True] * sudoku_size

    position = 0
    for character in given_fixed_values:
        digit = int(character)
        if digit != 0:
            r = positions.retrieve_row_id_from_position_and_size(position, sudoku_size)
            c = positions.retrieve_column_id_from_position_and_size(position, sudoku_size)
            g = positions.retrieve_grid_id_from_row_and_col(r, c, grid_size)

            # For each cell (at row r, column c, grid g):
            #   set to False the digit d for each cell in row r
            #   set to False the digit d for each cell in column c
            for i in range(sudoku_size):
                key_row = commons.build_fixed_val_key(r, i)
                key_column = commons.build_fixed_val_key(i, c)
                pencil_mark[key_row][digit - 1] = False
                pencil_mark[key_column][digit - 1] = False

            # Set to False the digit d for each cell in grid g
            range_rows = positions.retrieve_range_rows_from_grid_id(g, grid_size)
            range_columns = positions.retrieve_range_columns_from_grid_id(g, grid_size)
            for i in range_rows:
                for j in range_columns:
                    key_grid = commons.build_fixed_val_key(i, j)
                    pencil_mark[key_grid][digit - 1] = False

            # Set all others to False at this fixed place and replace the original fixed/predetermined to True
            key_fixed = commons.build_fixed_val_key(r, c)
            pencil_mark[key_fixed] = [False] * sudoku_size
            pencil_mark[key_fixed][digit - 1] = True

        position += 1
    return pencil_mark


def generate_values_from_pencil(pencil_mark):
    """
    Given a pencil mark object, iterate over it and if at some position there is a single value found it means either it
    is a fixed one (i.e known at the beginning) or a predetermined one (i.e there is no option that this value). In this
    case we can add this new found value, otherwise we keep it as unknown with a '0' digit character.
    :param pencil_mark: (dict) a pencil mark object. Key is the row/column position and value is a boolean array where
    True means that the value is fixed
    :return: (string) of new values determined with such a pencil mark
    """
    new_values = ''
    for key, bool_arr in pencil_mark.items():
        indices = [i for i, x in enumerate(bool_arr) if x]
        if len(indices) == 1:
            new_values += str(int(indices[0]) + 1)
        else:
            new_values += '0'
    return new_values
