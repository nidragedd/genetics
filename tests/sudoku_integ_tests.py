"""
Created on 23/11/2018
@author: nidragedd
"""
from math import sqrt
from random import randint

from objects import sudoku, sudoku_genetics
from objects.sudoku import Sudoku
from utils import fileloader

if __name__ == '__main__':
    model_to_solve = '3x3-easy-01'
    values_to_set = fileloader.load_file_as_values(model_to_solve)
    sudoku_size = int(sqrt(len(values_to_set)))
    grid_size = int(sqrt(sudoku_size))

    print("TEST N°1: displaying the objects with '0' values:")
    s = Sudoku(sudoku_size)
    s.init_with_values(values_to_set)
    s.display()
    print("Fitness evaluation for this objects is {}".format(sudoku_genetics.fitness(s)))

    print("\nTEST N°2: generating 2 random individuals")
    father = sudoku.build_random(values_to_set)
    father.display()
    mother = sudoku.build_random(values_to_set)
    mother.display()
    print("Fitness evaluation for father is {}".format(sudoku_genetics.fitness(father)))
    print("Fitness evaluation for mother is {}".format(sudoku_genetics.fitness(mother)))

    print("\nTEST N°3: generating child from father and mother")
    child = sudoku_genetics.create_one_child(father, mother, values_to_set)
    child.display()
    print("Fitness evaluation for child is {}".format(sudoku_genetics.fitness(child)))

    print("\nTEST N°4: randomly choose 2 values to swap in grid n° 3")
    print("Note: in grid 3, fixed positions are 0, 5 and 6")
    grid_id = 3
    rand_pos_1, row_id_1, col_id_1 = sudoku.get_random_not_fixed(child, grid_id, -1)
    rand_pos_2, row_id_2, col_id_2 = sudoku.get_random_not_fixed(child, grid_id, rand_pos_1)
    val_1 = child.grids()[grid_id][rand_pos_1]
    val_2 = child.grids()[grid_id][rand_pos_2]
    print("Values to swap are pos={} [row {}/col {}] (value={}) and pos={} [row {}/col {}] (value={})".
          format(rand_pos_1, row_id_1, col_id_1, val_1, rand_pos_2, row_id_2, col_id_2, val_2))

    print("\nTEST N°5: mutate the child")
    print("Note: values that will swap are not the same one as in TEST N°4")
    random_grid_id = randint(0, child.size() - 1)
    print("Chosen grid id for mutation is {}".format(random_grid_id))
    swapped_child = sudoku.swap_2_values_in_grid(child, random_grid_id)
    swapped_child.display()
    print("Fitness evaluation for mutated child is {}".format(sudoku_genetics.fitness(swapped_child)))
    print("DEBUG: check that swapped child is not the same as original child")
    print("Child rows: {}".format(child.rows()))
    print("Child columns: {}".format(child.columns()))
    print("Child grids: {}".format(child.grids()))
    print("Swapped child rows: {}".format(swapped_child.rows()))
    print("Swapped child columns: {}".format(swapped_child.columns()))
    print("Swapped child grids: {}".format(swapped_child.grids()))
