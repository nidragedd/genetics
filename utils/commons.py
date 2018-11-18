"""
Created on 15/11/2018
@author: nidragedd
"""


def build_fixed_val_key(row_id, col_id):
    """
    Util method used to build a key for the 'fixed_values' dict
    :param row_id: (int) self-explained, the row number in the sudoku (starting at 1)
    :param col_id: (int) self-explained, the column number in the sudoku (starting at 1)
    :return: (string) a string that will be the key used in the 'fixed_values' dict
    """
    return "[{}|{}]".format(str(row_id), str(col_id))


def build_separator_line(grid_size):
    """
    Build a separator line that will be used when printing the sudoku on screen
    :param grid_size: (int) self-explained, the size of one sudoku grid (which equals to the square root of the
    sudoku size, which is the number of elements per row/column/grid)
    :return: (string) a string to display after each group of grids to horizontally separate them
    """
    separator_line = '{}-|'.format('--' * grid_size) * grid_size
    return separator_line[:len(separator_line) - 1]
