"""
Created on 10/11/2018
@author: nidragedd
"""

from sudoku import sudoku_genetics
from utils import positions

if __name__ == '__main__':
    population_size = 1000
    selection_rate = 0.2
    random_selection_rate = 0.2
    nb_children = 5
    mutation_rate = 0.25

    max_nb_generations = 1000
    model_to_solve = '3x3-easy-01'

    sudoku_genetics.start(population_size, selection_rate, random_selection_rate, nb_children, max_nb_generations,
                          mutation_rate, model_to_solve)
