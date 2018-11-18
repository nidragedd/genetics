"""
Created on 15/11/2018
@author: nidragedd
"""
from random import shuffle


def retrieve_row_id_from_global_position(global_position, sudoku_size):
    """
    Given a position in the sudoku values, determine the id of the row (starting at 1)
    :param global_position: (int) position in the sudoku values (starting at 1)
    :param sudoku_size: (int) the size of the sudoku (i.e number of elements per row/column/grid)
    :return: (int) id of the row (starting at 1)
    """
    return int(global_position / sudoku_size) if global_position % sudoku_size == 0 \
        else (global_position // sudoku_size) + 1


def retrieve_column_id_from_global_position(global_position, sudoku_size):
    """
    Given a position in the sudoku values, determine the id of the row (starting at 1)
    :param global_position: (int) position in the sudoku values (starting at 1)
    :param sudoku_size: (int) the size of the sudoku (i.e number of elements per row/column/grid)
    :return: (int) id of the column (starting at 1)
    """
    return sudoku_size if global_position % sudoku_size == 0 else global_position % sudoku_size


def retrieve_grid_id_from_row_and_col(row_id, col_id, grid_size):
    """
    Given a position by it row and column id (starting at 1), determine the id of the grid (also starting at 1)
    :param row_id: (int) self-explained, the row id (starting at 1)
    :param col_id: (int) self-explained, the column id (starting at 1)
    :param grid_size: (int) self-explained, the size of one sudoku grid (which equals to the square root of the
    sudoku size, which is the number of elements per row/column/grid)
    :return: (int) id of the grid (starting at 1)
    """
    if col_id % grid_size == 0:
        grid_id = col_id // grid_size
    else:
        grid_id = int(col_id / grid_size) + 1

    if row_id > grid_size:
        if row_id % grid_size == 0:
            row_id -= 1
        grid_id += (row_id // grid_size) * grid_size
    return grid_id


def retrieve_row_id_from_grid_id_and_position(grid_id, grid_position, grid_size):
    """
    Given a position by it grid id and position in the grid (both starting at 1), determine the id of row (also
    starting at 1)
    :param grid_id: (int) self-explained, the grid id (starting at 1)
    :param grid_position: (int) the position of the element in this grid (starting at 1)
    :param grid_size: (int) self-explained, the size of one sudoku grid (which equals to the square root of the
    sudoku size, which is the number of elements per row/column/grid)
    :return: (int) id of the row (starting at 1)
    """
    row_in_grid = retrieve_row_id_from_global_position(grid_position, grid_size)
    delta_row = grid_size * (retrieve_row_id_from_global_position(grid_id, grid_size) - 1)
    return delta_row + row_in_grid


def retrieve_column_id_from_grid_id_and_position(grid_id, grid_position, grid_size):
    """
    Given a position by it grid id and position in the grid (both starting at 1), determine the id of column (also
    starting at 1)
    :param grid_id: (int) self-explained, the grid id (starting at 1)
    :param grid_position: (int) the position of the element in this grid (starting at 1)
    :param grid_size: (int) self-explained, the size of one sudoku grid (which equals to the square root of the
    sudoku size, which is the number of elements per row/column/grid)
    :return: (int) id of the column (starting at 1)
    """
    col_in_grid = retrieve_column_id_from_global_position(grid_position, grid_size)
    delta_col = grid_size * (retrieve_column_id_from_global_position(grid_id, grid_size) - 1)
    return delta_col + col_in_grid


def fill_with_some_valid_values(array_to_fill, length):
    # Get fixed values
    fixed_values = [value for value in array_to_fill if value > 0]
    # Get fixed values and their index
    fixed_index_values = [(pos, value) for pos, value in enumerate(array_to_fill) if value > 0]
    # Determine what are the available values based on fixed values
    available_values = [x for x in range(1, length + 1) if x not in fixed_values]
    shuffle(available_values)
    # Add fixed values in the shuffled array
    for index, val in fixed_index_values:
        available_values.insert(index, val)
    return available_values
