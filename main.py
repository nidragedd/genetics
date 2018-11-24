"""
Created on 10/11/2018
@author: nidragedd
"""

from sudoku import sudoku_genetics

if __name__ == '__main__':
    population_size = 1000
    selection_rate = 0.25
    random_selection_rate = 0.25
    nb_children = 4
    mutation_rate = 0.05

    max_nb_generations = 1000
    model_to_solve = '3x3-easy-01'

    sudoku_genetics.start(population_size, selection_rate, random_selection_rate, nb_children, max_nb_generations,
                          mutation_rate, model_to_solve, False)
