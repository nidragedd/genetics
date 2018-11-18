import unittest

from utils import positions
from math import sqrt


class MyTestCase(unittest.TestCase):
    sudoku_size = 9
    grid_size = sqrt(sudoku_size)

    def test_row_id(self):
        self.assertEqual(positions.retrieve_row_id_from_global_position(self.sudoku_size - 1, self.sudoku_size), 1)
        self.assertEqual(positions.retrieve_row_id_from_global_position(self.sudoku_size, self.sudoku_size), 1)
        self.assertEqual(positions.retrieve_row_id_from_global_position(self.sudoku_size + 1, self.sudoku_size), 2)
        self.assertEqual(positions.retrieve_row_id_from_global_position(self.sudoku_size * self.sudoku_size, self.sudoku_size), self.sudoku_size)

    def test_col_id(self):
        self.assertEqual(positions.retrieve_column_id_from_global_position(1, self.sudoku_size), 1)
        self.assertEqual(positions.retrieve_column_id_from_global_position(self.sudoku_size - 1, self.sudoku_size), self.sudoku_size - 1)
        self.assertEqual(positions.retrieve_column_id_from_global_position(self.sudoku_size, self.sudoku_size), self.sudoku_size)
        self.assertEqual(positions.retrieve_column_id_from_global_position(self.sudoku_size + 1, self.sudoku_size), 1)

    def test_grid_id(self):
        self.assertEqual(positions.retrieve_grid_id_from_row_and_col(1, 1, self.grid_size), 1)
        self.assertEqual(positions.retrieve_grid_id_from_row_and_col(1, 2, self.grid_size), 1)
        self.assertEqual(positions.retrieve_grid_id_from_row_and_col(1, self.grid_size, self.grid_size), 1)
        self.assertEqual(positions.retrieve_grid_id_from_row_and_col(1, self.grid_size + 1, self.grid_size), 2)
        self.assertEqual(positions.retrieve_grid_id_from_row_and_col(1, self.sudoku_size, self.grid_size), self.grid_size)

    def test_row_from_grid_id_and_pos(self):
        self.assertEqual(1, positions.retrieve_row_id_from_grid_id_and_position(1, 1, self.grid_size))
        self.assertEqual(1, positions.retrieve_row_id_from_grid_id_and_position(1, 2, self.grid_size))
        self.assertEqual(1, positions.retrieve_row_id_from_grid_id_and_position(1, 3, self.grid_size))
        self.assertEqual(2, positions.retrieve_row_id_from_grid_id_and_position(1, 4, self.grid_size))
        self.assertEqual(2, positions.retrieve_row_id_from_grid_id_and_position(1, 5, self.grid_size))
        self.assertEqual(2, positions.retrieve_row_id_from_grid_id_and_position(3, 6, self.grid_size))
        self.assertEqual(5, positions.retrieve_row_id_from_grid_id_and_position(6, 6, 3))
        self.assertEqual(7, positions.retrieve_row_id_from_grid_id_and_position(7, 1, 3))
        self.assertEqual(9, positions.retrieve_row_id_from_grid_id_and_position(8, 7, 3))

    def test_col_from_grid_id_and_pos(self):
        self.assertEqual(1, positions.retrieve_column_id_from_grid_id_and_position(1, 1, self.grid_size))
        self.assertEqual(2, positions.retrieve_column_id_from_grid_id_and_position(1, 2, self.grid_size))
        self.assertEqual(3, positions.retrieve_column_id_from_grid_id_and_position(1, 3, self.grid_size))
        self.assertEqual(1, positions.retrieve_column_id_from_grid_id_and_position(1, 4, self.grid_size))
        self.assertEqual(2, positions.retrieve_column_id_from_grid_id_and_position(1, 5, self.grid_size))
        self.assertEqual(9, positions.retrieve_column_id_from_grid_id_and_position(3, 6, 3))
        self.assertEqual(9, positions.retrieve_column_id_from_grid_id_and_position(6, 6, 3))
        self.assertEqual(4, positions.retrieve_column_id_from_grid_id_and_position(8, 7, 3))


if __name__ == '__main__':
    unittest.main()
