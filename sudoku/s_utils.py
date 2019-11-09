"""
Created on 09/11/2019
@author: nidragedd
"""
from random import randint
import datetime
from math import sqrt

from objects.sudoku import Sudoku
from sudoku import positions


def build_fixed_val_key(row_id, col_id):
    """
    Util method used to build a key for the 'fixed_values' dict
    :param row_id: (int) self-explained, the row number in the objects (starting at 1)
    :param col_id: (int) self-explained, the column number in the objects (starting at 1)
    :return: (string) a string that will be the key used in the 'fixed_values' dict
    """
    return "[{}|{}]".format(str(row_id), str(col_id))


def build_separator_line(grid_size):
    """
    Build a separator line that will be used when printing the objects on screen
    :param grid_size: (int) self-explained, the size of one objects grid (which equals to the square root of the
    objects size, which is the number of elements per row/column/grid)
    :return: (string) a string to display after each group of grids to horizontally separate them
    """
    separator_line = '{}-|'.format('--' * grid_size) * grid_size
    return separator_line[:len(separator_line) - 1]


def count_duplicates(arr):
    """
    Count how many times the same value is found in a given array
    :param arr: the array to evaluate
    :return: number of duplicated elements
    """
    # Size of the given array minus the size of unique elements found in this array = nb of duplicates
    return len(arr) - len(set(arr))


def get_sudoku_size(values_to_set):
    """
    Compute the objects size, meaning how many elements per row/column/grid
    :param values_to_set: (string) the values we have to set to init the objects
    :return: (int) objects size, meaning how many elements per row/column/grid
    """
    return int(sqrt(len(values_to_set)))


def get_grid_size(values_to_set):
    """
    Compute the grid size of the objects. For example, for a 9x9 objects, the grid size is 3
    :param values_to_set: (string) the values we have to set to init the objects
    :return: (int) grid size
    """
    return int(sqrt(get_sudoku_size(values_to_set)))


def get_human_readable_time(start_time, end_time):
    """
    Returns a string in the form [D day[s], ][H]H:MM:SS[.UUUUUU], where D is negative for negative t.
    :param start_time: (float) the beginning of the task
    :param end_time: (float) the end of the task
    :return: (string) human readable string with hours, minutes and seconds
    """
    delay = datetime.timedelta(seconds=(end_time - start_time))
    return str(delay)


def build_random(values_to_set):
    """
    Build a random (but valid in terms of grids) objects based on a given string representing known values and unknown
    ones
    :param values_to_set: (string) No spaces, no new lines, only all numbers needed to fill the objects. If one value is
    unknown, put a '0' character, otherwise provide the fixed-numbered-value.
    :return: a objects with grids all filled with available values and no duplicates. But there might (for sure there will)
    be some duplicates in rows/columns.
    """
    sudoku_size = get_sudoku_size(values_to_set)
    s = Sudoku(sudoku_size)
    s.init_with_values(values_to_set)

    # We want to ensure that at least grids are 'correct' so we fill each one with available values to avoid duplicates
    for grid_id, grid_values in s.grids().items():
        available_values = positions.fill_with_some_valid_values(grid_values, sudoku_size)

        # Get row and col from grid_id and position in grid and substitute the value
        for position, new_value in enumerate(available_values):
            row_id = positions.retrieve_row_id_from_grid_id_and_position(grid_id, position, s.grid_size())
            col_id = positions.retrieve_column_id_from_grid_id_and_position(grid_id, position, s.grid_size())
            s.columns()[col_id][row_id] = new_value
            s.rows()[row_id][col_id] = new_value

        # Substitute value with new one in grids arrays
        s.grids()[grid_id] = available_values
    return s


def init_from_grids(values_to_set, grids):
    """
    Init a objects object by giving initial values + grids
    :param values_to_set: (string) No spaces, no new lines, only all numbers needed to fill the objects. If one value is
    unknown, put a '0' character, otherwise provide the fixed-numbered-value.
    :param grids: (object) one of the 2 elements used to build/generate a new one
    :return: (object) a objects which is built from given grids
    """
    sudoku_size = get_sudoku_size(values_to_set)
    s = Sudoku(sudoku_size)
    s.init_with_values(values_to_set)

    for grid_id, grid_values in enumerate(grids):
        # Get row and col from grid_id and position in grid and substitute the value
        for position, value in enumerate(grid_values):
            row_id = positions.retrieve_row_id_from_grid_id_and_position(grid_id, position, s.grid_size())
            col_id = positions.retrieve_column_id_from_grid_id_and_position(grid_id, position, s.grid_size())
            s.columns()[col_id][row_id] = value
            s.rows()[row_id][col_id] = value
            '''
            Copy/paste value per value to avoid references issue (i.e 's.grids()[grid_id] = grid_values' will work but
            it will generate further issues with mutation (as parent will also mutate and there are more than 1 child
            per couple)
            '''
            s.grids()[grid_id][position] = value
    return s


def get_random_not_fixed(individual, grid_id, forbidden_pos):
    """
    Randomly pick one value in the given grid id for the individual. The picked value cannot be a fixed one or a
    forbidden one
    :param individual: (object) the original individual to pick one value from
    :param grid_id: (int) id of the grid
    :param forbidden_pos: (int) in addition to the fixed value, specify a position that cannot be picked neither, even
    if not a fixed one
    :return: (tuple of 3 int) the picked position in the grid, the row id and the column id
    """
    rand_pos = -1
    row_id = -1
    col_id = -1
    is_fixed = True
    while is_fixed or rand_pos == forbidden_pos:
        rand_pos = randint(0, individual.size() - 1)
        # We need to find their position (row and column) in the whole table to check whether it is fixed or not
        row_id = positions.retrieve_row_id_from_grid_id_and_position(grid_id, rand_pos, individual.grid_size())
        col_id = positions.retrieve_column_id_from_grid_id_and_position(grid_id, rand_pos, individual.grid_size())
        is_fixed = individual.is_fixed(row_id, col_id)
    return rand_pos, row_id, col_id


def swap_2_values_in_grid(individual, grid_id):
    """
    Within the given objects, pick randomly 2 elements to swap if they are not fixed values
    Once this is done, change the value in the objects arrays (rows, columns and grids)
    :param individual: (object) objects to mutate
    :param grid_id: (int) chosen grid id where we will swap values
    :return: (object) changed objects
    """
    s = init_from_grids(individual.initial_values(), individual.grids().values())

    rand_pos_1, row_id_1, col_id_1 = get_random_not_fixed(individual, grid_id, -1)
    rand_pos_2, row_id_2, col_id_2 = get_random_not_fixed(individual, grid_id, rand_pos_1)

    grid_values = s.grids()[grid_id]
    val_1 = grid_values[rand_pos_1]
    val_2 = grid_values[rand_pos_2]

    grid_values[rand_pos_1] = val_2
    grid_values[rand_pos_2] = val_1
    s.rows()[row_id_1][col_id_1] = val_2
    s.rows()[row_id_2][col_id_2] = val_1
    s.columns()[col_id_1][row_id_1] = val_2
    s.columns()[col_id_2][row_id_2] = val_1

    return s
