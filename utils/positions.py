"""
Created on 15/11/2018
@author: nidragedd
"""
from random import shuffle


def retrieve_row_id_from_position_and_size(position, size):
    """
    Given a position in the sudoku values, determine the id of the row (starting at 0)
    :param position: (int) position in the sudoku values (starting at 0)
    :param size: (int) the size of the sudoku (i.e number of elements per row/column/grid)
    :return: (int) id of the row (starting at 0)
    """
    return position // size


def retrieve_column_id_from_position_and_size(position, size):
    """
    Given a position in the sudoku values, determine the id of the row (starting at 0)
    :param position: (int) position in the sudoku values (starting at 0)
    :param size: (int) the size of the sudoku (i.e number of elements per row/column/grid)
    :return: (int) id of the column (starting at 0)
    """
    return position % size


def retrieve_grid_id_from_row_and_col(row_id, col_id, grid_size):
    """
    Given a position by it row and column id (starting at 0), determine the id of the grid (also starting at 0)
    :param row_id: (int) self-explained, the row id (starting at 0)
    :param col_id: (int) self-explained, the column id (starting at 0)
    :param grid_size: (int) self-explained, the size of one sudoku grid (which equals to the square root of the
    sudoku size, which is the number of elements per row/column/grid)
    :return: (int) id of the grid (starting at 0)
    """
    return int(col_id // grid_size + ((row_id // grid_size) * grid_size))


def retrieve_range_rows_from_grid_id(grid_id, grid_size):
    """
    Retrieve range of rows (indexes) linked to the given grid id (starting at 0) for a given grid size
    /!\ Be careful, this method returns the upper row index included because it is a 'range' in the Python sense and
    the range (start, end) does not include the 'end' element while looping with 'for' or 'enumerate'. For example,
    for a grid size=3 and grid_id=0 (the first one), the range returned will be (0, 3) so that the loop will take row 0,
    1 and 2
    :param grid_id: (int) the grid id (starting at 0) for which we want to get the range of rows
    :param grid_size: (int) size of one grid (not the sudoku size, its square root)
    :return: a range of rows indexes
    """
    start = int(grid_id / grid_size) * grid_size
    return range(start, start + grid_size)


def retrieve_range_columns_from_grid_id(grid_id, grid_size):
    """
    Retrieve range of columns (indexes) linked to the given grid id (starting at 0) for a given grid size.
    /!\ Be careful, this method returns the upper column index included because it is a 'range' in the Python sense and
    the range (start, end) does not include the 'end' element while looping with 'for' or 'enumerate'. For example,
    for a grid size=3 and grid_id=0 (the first one), the range returned will be (0, 3) so that the loop will take column
    0, 1 and 2
    :param grid_id: (int) the grid id (starting at 0) for which we want to get the range of columns
    :param grid_size: (int) size of one grid (not the sudoku size, its square root)
    :return: a range of columns indexes
    """
    start = int(grid_id % grid_size) * grid_size
    return range(start, start + grid_size)


def retrieve_row_id_from_grid_id_and_position(grid_id, grid_position, grid_size):
    """
    Given a position by it grid id and position in the grid (both starting at 0), determine the id of row (also
    starting at 0)
    :param grid_id: (int) self-explained, the grid id (starting at 0)
    :param grid_position: (int) the position of the element in this grid (starting at 0)
    :param grid_size: (int) self-explained, the size of one sudoku grid (which equals to the square root of the
    sudoku size, which is the number of elements per row/column/grid)
    :return: (int) id of the row (starting at 0)
    """
    row_in_grid = retrieve_row_id_from_position_and_size(grid_position, grid_size)
    delta_row = grid_size * (retrieve_row_id_from_position_and_size(grid_id, grid_size))
    return delta_row + row_in_grid


def retrieve_column_id_from_grid_id_and_position(grid_id, grid_position, grid_size):
    """
    Given a position by it grid id and position in the grid (both starting at 0), determine the id of column (also
    starting at 0)
    :param grid_id: (int) self-explained, the grid id (starting at 0)
    :param grid_position: (int) the position of the element in this grid (starting at 0)
    :param grid_size: (int) self-explained, the size of one sudoku grid (which equals to the square root of the
    sudoku size, which is the number of elements per row/column/grid)
    :return: (int) id of the column (starting at 0)
    """
    col_in_grid = retrieve_column_id_from_position_and_size(grid_position, grid_size)
    delta_col = grid_size * (retrieve_column_id_from_position_and_size(grid_id, grid_size))
    return delta_col + col_in_grid


def fill_with_some_valid_values(array_to_fill, length):
    """
    Based on a given array containing '0' and non-zero values, return a new array filled with distinct and authorized
    values randomly placed where there were '0'.
    :param array_to_fill: (array) represents a grid, column or row and contains non-zero values if they are known or
    zero otherwise
    :param length: (int) size of the sudoku
    :return: (array) new array filled with distinct and authorized values randomly placed where there were '0'.
    """
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
