import unittest

from sudoku import positions
from math import sqrt

from utils import tools


class PositionsTestCase(unittest.TestCase):
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

    def test_count_duplicates(self):
        self.assertEqual(0, tools.count_duplicates([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertEqual(1, tools.count_duplicates([0, 1, 2, 1, 4, 5, 6, 7, 8, 9]))
        self.assertEqual(2, tools.count_duplicates([0, 1, 2, 3, 4, 2, 6, 7, 2, 9]))
        self.assertEqual(3, tools.count_duplicates([0, 1, 2, 9, 4, 9, 6, 9, 8, 9]))
        self.assertEqual(6, tools.count_duplicates([0, 4, 0, 9, 4, 9, 4, 9, 9]))

    def test_get_rows(self):
        self.assertEqual(range(0, 3), positions.retrieve_range_rows_from_grid_id(0, 3))
        self.assertEqual(range(0, 3), positions.retrieve_range_rows_from_grid_id(1, 3))
        self.assertEqual(range(0, 3), positions.retrieve_range_rows_from_grid_id(2, 3))
        self.assertEqual(range(3, 6), positions.retrieve_range_rows_from_grid_id(3, 3))
        self.assertEqual(range(3, 6), positions.retrieve_range_rows_from_grid_id(4, 3))
        self.assertEqual(range(3, 6), positions.retrieve_range_rows_from_grid_id(5, 3))
        self.assertEqual(range(6, 9), positions.retrieve_range_rows_from_grid_id(6, 3))
        self.assertEqual(range(6, 9), positions.retrieve_range_rows_from_grid_id(7, 3))
        self.assertEqual(range(6, 9), positions.retrieve_range_rows_from_grid_id(8, 3))
        self.assertEqual(range(0, 4), positions.retrieve_range_rows_from_grid_id(0, 4))
        self.assertEqual(range(0, 4), positions.retrieve_range_rows_from_grid_id(2, 4))
        self.assertEqual(range(0, 4), positions.retrieve_range_rows_from_grid_id(3, 4))
        self.assertEqual(range(4, 8), positions.retrieve_range_rows_from_grid_id(4, 4))
        self.assertEqual(range(4, 8), positions.retrieve_range_rows_from_grid_id(7, 4))
        self.assertEqual(range(8, 12), positions.retrieve_range_rows_from_grid_id(8, 4))

    def test_get_cols(self):
        self.assertEqual(range(0, 3), positions.retrieve_range_columns_from_grid_id(0, 3))
        self.assertEqual(range(3, 6), positions.retrieve_range_columns_from_grid_id(1, 3))
        self.assertEqual(range(6, 9), positions.retrieve_range_columns_from_grid_id(2, 3))
        self.assertEqual(range(0, 3), positions.retrieve_range_columns_from_grid_id(3, 3))
        self.assertEqual(range(3, 6), positions.retrieve_range_columns_from_grid_id(4, 3))
        self.assertEqual(range(6, 9), positions.retrieve_range_columns_from_grid_id(5, 3))
        self.assertEqual(range(0, 3), positions.retrieve_range_columns_from_grid_id(6, 3))
        self.assertEqual(range(3, 6), positions.retrieve_range_columns_from_grid_id(7, 3))
        self.assertEqual(range(6, 9), positions.retrieve_range_columns_from_grid_id(8, 3))
        self.assertEqual(range(0, 4), positions.retrieve_range_columns_from_grid_id(0, 4))
        self.assertEqual(range(8, 12), positions.retrieve_range_columns_from_grid_id(2, 4))
        self.assertEqual(range(12, 16), positions.retrieve_range_columns_from_grid_id(3, 4))
        self.assertEqual(range(0, 4), positions.retrieve_range_columns_from_grid_id(4, 4))
        self.assertEqual(range(12, 16), positions.retrieve_range_columns_from_grid_id(7, 4))


if __name__ == '__main__':
    unittest.main()
