"""
Created on 10/11/2018
@author: nidragedd
"""
from math import sqrt

from sudoku import positions, s_utils


class Sudoku(object):
    """
    A sudoku grid has a size and contains some fixed values (either given at the beginning, either guessed after runs of
    computation). This class handles also some dicts for rows, columns and grids
    """
    _grid_size = 0
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
        self._grid_size = int(sqrt(nb_rows))
        self._rows = {}
        self._columns = {}
        self._grids = {}
        self._fixed_values = {}
        self._init_values = ''
        if nb_rows/self._grid_size != self._grid_size:
            raise Exception("You must provide a power number value")

    def init_with_values(self, values):
        """
        Method used to populate the objects with values
        :param values: (string) No spaces, no new lines, only all numbers needed to fill the objects. If one value is
        unknown, put a '0' character, otherwise provide the fixed-numbered-value.
        Then, rows, columns and grids are computed based on those values and a dict of fixed values is created
        """
        self._init_values = values
        expected_len = pow(self._size, 2)
        if len(values) != expected_len:
            raise Exception("You must provide a number of values matching the size of the objects. Got {} whereas {} "
                            "was expected".format(len(values), expected_len))

        # Init the dicts
        for i in range(self._size):
            self._rows[i] = []
            self._columns[i] = []
            self._grids[i] = []

        # In the above section we determine, according to the position in the given values, in which
        # column, row and grid the value belongs to
        position = 0
        for character in values:
            val = int(character)
            row_id = positions.retrieve_row_id_from_position_and_size(position, self._size)
            col_id = positions.retrieve_column_id_from_position_and_size(position, self._size)
            grid_id = positions.retrieve_grid_id_from_row_and_col(row_id, col_id, self._grid_size)

            position += 1

            # Add this value to all dicts we maintain
            self._rows[row_id].append(val)
            self._columns[col_id].append(val)
            self._grids[grid_id].append(val)

            # Keep knowledge of fixed values where key is their position (key= row_id|col_id)
            if val != 0:
                self._fixed_values[s_utils.build_fixed_val_key(row_id, col_id)] = val

    def display(self):
        """
        Iterate over rows to print values and display the objects. We need to take care about new lines and subgrids
        separations (horizontal and vertical)
        """
        for i in range(self._size):
            if i > 1 and i % self._grid_size == 0:
                print(s_utils.build_separator_line(self._grid_size))

            line = self._rows[i]
            for j in range(self._size):
                if j > 0 and j % self._grid_size == 0:
                    print(' | {}'.format(line[j]), end='')
                elif j == (self._size - 1):
                    print(' {}'.format(line[j]))
                else:
                    print(' {}'.format(line[j]), end='')
        print("")

    def is_fixed(self, row_id, col_id):
        """
        Given a row id and a column id, returns True if the value is fixed at the beginning
        :param row_id: (int) the row id
        :param col_id: (int) the column id
        :return: (boolean) True if value is fixed (i.e it is a given value), False otherwise
        """
        return s_utils.build_fixed_val_key(row_id, col_id) in self._fixed_values

    def grids(self):
        """
        :return: (dict) grids of objects as dict where key is the 'grid id' and value an array of values
        """
        return self._grids

    def rows(self):
        """
        :return: (dict) rows of objects as dict where key is the 'row id' and value an array of values
        """
        return self._rows

    def columns(self):
        """
        :return: (dict) columns of objects as dict where key is the 'column id' and value an array of values
        """
        return self._columns

    def size(self):
        """
        :return: (int) size of the objects, i.e number of elements per row/column/grid
        """
        return self._size

    def grid_size(self):
        """
        :return: (int) size of a grid of the objects (i.e the square root of the size). For a 9x9 size, this method
        returns 3
        """
        return self._grid_size

    def initial_values(self):
        """
        :return: (string) the values used to build the objects at first time
        """
        return self._init_values
