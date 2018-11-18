import unittest

from utils import positions
from math import sqrt


class MyTestCase(unittest.TestCase):
    sudoku_size = 9
    grid_size = sqrt(sudoku_size)

    def test_row_id(self):
        self.assertEqual(0, positions.retrieve_row_id_from_position_and_size(0, self.sudoku_size))
        self.assertEqual(0, positions.retrieve_row_id_from_position_and_size(self.sudoku_size - 1, self.sudoku_size))
        self.assertEqual(1, positions.retrieve_row_id_from_position_and_size(self.sudoku_size, self.sudoku_size))
        self.assertEqual(1, positions.retrieve_row_id_from_position_and_size(self.sudoku_size + 1, self.sudoku_size))
        self.assertEqual(2, positions.retrieve_row_id_from_position_and_size(self.sudoku_size * 2, self.sudoku_size))
        self.assertEqual(self.sudoku_size - 1, positions.retrieve_row_id_from_position_and_size((self.sudoku_size * self.sudoku_size) - 1, self.sudoku_size))

    def test_col_id(self):
        self.assertEqual(0, positions.retrieve_column_id_from_position_and_size(0, self.sudoku_size))
        self.assertEqual(0, positions.retrieve_column_id_from_position_and_size(self.sudoku_size, self.sudoku_size))
        self.assertEqual(1, positions.retrieve_column_id_from_position_and_size(1, self.sudoku_size))
        self.assertEqual(1, positions.retrieve_column_id_from_position_and_size(self.sudoku_size + 1, self.sudoku_size))
        self.assertEqual(self.sudoku_size - 1, positions.retrieve_column_id_from_position_and_size(self.sudoku_size - 1, self.sudoku_size))

    def test_grid_id(self):
        self.assertEqual(0, positions.retrieve_grid_id_from_row_and_col(0, 0, self.grid_size))
        self.assertEqual(0, positions.retrieve_grid_id_from_row_and_col(1, 2, self.grid_size))
        self.assertEqual(1, positions.retrieve_grid_id_from_row_and_col(1, self.grid_size, self.grid_size))
        self.assertEqual(1, positions.retrieve_grid_id_from_row_and_col(1, self.grid_size + 1, self.grid_size))
        self.assertEqual(self.grid_size - 1, positions.retrieve_grid_id_from_row_and_col(1, self.sudoku_size - 1, self.grid_size))

    def test_row_from_grid_id_and_pos(self):
        self.assertEqual(0, positions.retrieve_row_id_from_grid_id_and_position(0, 0, self.grid_size))
        self.assertEqual(0, positions.retrieve_row_id_from_grid_id_and_position(0, 1, self.grid_size))
        self.assertEqual(0, positions.retrieve_row_id_from_grid_id_and_position(0, 2, self.grid_size))
        self.assertEqual(1, positions.retrieve_row_id_from_grid_id_and_position(0, 3, self.grid_size))
        self.assertEqual(1, positions.retrieve_row_id_from_grid_id_and_position(0, 4, self.grid_size))
        self.assertEqual(1, positions.retrieve_row_id_from_grid_id_and_position(2, 5, self.grid_size))
        self.assertEqual(4, positions.retrieve_row_id_from_grid_id_and_position(5, 5, 3))
        self.assertEqual(6, positions.retrieve_row_id_from_grid_id_and_position(6, 0, 3))
        self.assertEqual(8, positions.retrieve_row_id_from_grid_id_and_position(8, 6, 3))

    def test_col_from_grid_id_and_pos(self):
        self.assertEqual(0, positions.retrieve_column_id_from_grid_id_and_position(0, 0, self.grid_size))
        self.assertEqual(1, positions.retrieve_column_id_from_grid_id_and_position(0, 1, self.grid_size))
        self.assertEqual(2, positions.retrieve_column_id_from_grid_id_and_position(0, 2, self.grid_size))
        self.assertEqual(0, positions.retrieve_column_id_from_grid_id_and_position(0, 3, self.grid_size))
        self.assertEqual(1, positions.retrieve_column_id_from_grid_id_and_position(0, 4, self.grid_size))
        self.assertEqual(8, positions.retrieve_column_id_from_grid_id_and_position(2, 5, 3))
        self.assertEqual(8, positions.retrieve_column_id_from_grid_id_and_position(5, 5, 3))
        self.assertEqual(3, positions.retrieve_column_id_from_grid_id_and_position(7, 6, 3))


if __name__ == '__main__':
    unittest.main()
