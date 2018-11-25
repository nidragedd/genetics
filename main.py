"""
Created on 10/11/2018
@author: nidragedd
"""

from sudoku import sudoku_genetics

if __name__ == '__main__':
    population_size = 2000
    selection_rate = 0.5
    random_selection_rate = 0.5
    nb_children = 2
    mutation_rate = 0.25

    max_nb_generations = 500
    restart_after_n_generations_without_improvement = 300
    model_to_solve = '3x3-easy-01'

    presolving = False

    sudoku_genetics.start(population_size, selection_rate, random_selection_rate, nb_children, max_nb_generations,
                          mutation_rate, model_to_solve, presolving, restart_after_n_generations_without_improvement)
