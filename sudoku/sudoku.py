"""
Created on 10/11/2018
@author: nidragedd
"""
from math import sqrt

from utils import commons, positions


class Sudoku(object):
    _sqrt = 0
    _size = 0
    _fixed_values = None
    _rows = None
    _columns = None
    _grids = None

    def __init__(self, nb_rows):
        """
        Constructor
        """
        self._size = nb_rows
        self._sqrt = int(sqrt(nb_rows))
        self._rows = {}
        self._columns = {}
        self._grids = {}
        self._fixed_values = {}
        if nb_rows/self._sqrt != self._sqrt:
            raise Exception("You must provide a power number value")

    def init_with_values(self, values):
        """
        Method used to populate the sudoku with values
        :param values: (string) No spaces, no new lines, only all numbers needed to fill the sudoku. If one value is
        unknown, put a '0' character, otherwise provide the fixed-numbered-value.
        Then, rows, columns and grids are computed based on those values and a dict of fixed values is created
        """
        expected_len = pow(self._size, 2)
        if len(values) != expected_len:
            raise Exception("You must provide a number of values matching the size of the sudoku. Got {} whereas {} "
                            "was expected".format(len(values), expected_len))

        # Init the dicts
        for i in range(1, self._size + 1):
            self._rows[i] = []
            self._columns[i] = []
            self._grids[i] = []

        # In the above section we determine, according to the position in the given values, in which
        # column, row and grid the value belongs to
        position = 1
        for character in values:
            val = int(character)
            row_id = positions.retrieve_row_id_from_global_position(position, self._size)
            col_id = positions.retrieve_column_id_from_global_position(position, self._size)
            grid_id = positions.retrieve_grid_id_from_row_and_col(row_id, col_id, self._sqrt)

            position += 1

            # Add this value to all dicts we maintain
            self._rows[row_id].append(val)
            self._columns[col_id].append(val)
            self._grids[grid_id].append(val)

            # Keep knowledge of fixed values where key is their position (key= row_id|col_id)
            if val != 0:
                self._fixed_values[commons.build_fixed_val_key(row_id, col_id)] = val

    def display(self):
        """
        iterate over rows to print values and display the sudoku. We need to take care about new lines and subgrids
        separations (horizontal and vertical)
        """
        for i in range(1, self._size + 1):
            if i > 1 and i % self._sqrt == 1:
                print(commons.build_separator_line(self._sqrt))

            line = self._rows[i]
            for j in range(len(line)):
                if j > 0 and j % self._sqrt == 0:
                    print(' | {}'.format(line[j]), end='')
                elif j == (self._size - 1):
                    print(' {}'.format(line[j]))
                else:
                    print(' {}'.format(line[j]), end='')

    def grids(self):
        """
        Access to all grids of this sudoku
        :return: grids of sudoku as dict where key is the 'grid id' and value an array of values
        """
        return self._grids

    def rows(self):
        """
        Access to all rows of this sudoku
        :return: rows of sudoku as dict where key is the 'row id' and value an array of values
        """
        return self._rows

    def columns(self):
        """
        Access to all columns of this sudoku
        :return: columns of sudoku as dict where key is the 'column id' and value an array of values
        """
        return self._columns
