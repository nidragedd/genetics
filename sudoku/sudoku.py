"""
Created on 10/11/2018
@author: nidragedd
"""
from math import sqrt
from random import randint

from utils import commons, positions


class Sudoku(object):
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
        Method used to populate the sudoku with values
        :param values: (string) No spaces, no new lines, only all numbers needed to fill the sudoku. If one value is
        unknown, put a '0' character, otherwise provide the fixed-numbered-value.
        Then, rows, columns and grids are computed based on those values and a dict of fixed values is created
        """
        self._init_values = values
        expected_len = pow(self._size, 2)
        if len(values) != expected_len:
            raise Exception("You must provide a number of values matching the size of the sudoku. Got {} whereas {} "
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
                self._fixed_values[commons.build_fixed_val_key(row_id, col_id)] = val

    def display(self):
        """
        Iterate over rows to print values and display the sudoku. We need to take care about new lines and subgrids
        separations (horizontal and vertical)
        """
        for i in range(self._size):
            if i > 1 and i % self._grid_size == 0:
                print(commons.build_separator_line(self._grid_size))

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
        return commons.build_fixed_val_key(row_id, col_id) in self._fixed_values

    def grids(self):
        """
        :return: (dict) grids of sudoku as dict where key is the 'grid id' and value an array of values
        """
        return self._grids

    def rows(self):
        """
        :return: (dict) rows of sudoku as dict where key is the 'row id' and value an array of values
        """
        return self._rows

    def columns(self):
        """
        :return: (dict) columns of sudoku as dict where key is the 'column id' and value an array of values
        """
        return self._columns

    def size(self):
        """
        :return: (int) size of the sudoku, i.e number of elements per row/column/grid
        """
        return self._size

    def grid_size(self):
        """
        :return: (int) size of a grid of the sudoku (i.e the square root of the size). For a 9x9 size, this method
        returns 3
        """
        return self._grid_size

    def initial_values(self):
        """
        :return: (string) the values used to build the sudoku at first time
        """
        return self._init_values


def build_random(values_to_set):
    """
    Build a random (but valid in terms of grids) sudoku based on a given string representing known values and unknown
    ones
    :param values_to_set: (string) No spaces, no new lines, only all numbers needed to fill the sudoku. If one value is
    unknown, put a '0' character, otherwise provide the fixed-numbered-value.
    :return: a sudoku with grids all filled with available values and no duplicates. But there might (for sure there will)
    be some duplicates in rows/columns.
    """
    sudoku_size = commons.get_sudoku_size(values_to_set)
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
    Init a sudoku object by giving initial values + grids
    :param values_to_set: (string) No spaces, no new lines, only all numbers needed to fill the sudoku. If one value is
    unknown, put a '0' character, otherwise provide the fixed-numbered-value.
    :param grids: (object) one of the 2 elements used to build/generate a new one
    :return: (object) a sudoku which is built from given grids
    """
    sudoku_size = commons.get_sudoku_size(values_to_set)
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
    Within the given sudoku, pick randomly 2 elements to swap if they are not fixed values
    Once this is done, change the value in the sudoku arrays (rows, columns and grids)
    :param individual: (object) sudoku to mutate
    :param grid_id: (int) chosen grid id where we will swap values
    :return: (object) changed sudoku
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
