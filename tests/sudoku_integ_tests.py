"""
Created on 23/11/2018
@author: nidragedd
"""
from math import sqrt
from sudoku import ga_utils
from objects.sudoku import Sudoku
from utils import fileloader

if __name__ == '__main__':
    model_to_solve = '3x3-easy-02'
    values_to_set = fileloader.load_file_as_values(model_to_solve)
    sudoku_size = int(sqrt(len(values_to_set)))
    grid_size = int(sqrt(sudoku_size))

    print("TEST N°1: displaying the objects with '0' values:")
    s = Sudoku(values_to_set)
    s.display()
    print("Fitness evaluation for this objects is {}".format(s.fitness()))

    print("\nTEST N°2: generating 2 random individuals")
    father = Sudoku(values_to_set).fill_random()
    father.display()
    mother = Sudoku(values_to_set).fill_random()
    mother.display()
    print("Fitness evaluation for father is {}".format(father.fitness()))
    print("Fitness evaluation for mother is {}".format(mother.fitness()))

    print("\nTEST N°3: generating child from father and mother")
    child = ga_utils.create_one_child(father, mother, values_to_set)
    child.display()
    print("Fitness evaluation for child is {}".format(child.fitness()))

    print("\nTEST N°4: mutate the child")
    swapped_child = child.swap_2_values()
    swapped_child.display()
    print("Fitness evaluation for mutated child is {}".format(swapped_child.fitness()))
    print("DEBUG: check that swapped child is not the same as original child")
    print("Child rows: {}".format(child.rows()))
    print("Child columns: {}".format(child.columns()))
    print("Child grids: {}".format(child.grids()))
    print("Swapped child rows: {}".format(swapped_child.rows()))
    print("Swapped child columns: {}".format(swapped_child.columns()))
    print("Swapped child grids: {}".format(swapped_child.grids()))
