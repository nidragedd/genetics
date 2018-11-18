"""
Created on 10/11/2018
@author: nidragedd
"""
from math import sqrt
from sudoku.sudoku import Sudoku
from utils import fileloader, positions


def start(population_size, selection_rate, random_selection_rate, nb_children, max_nb_generations,
          mutation_rate, model_to_solve):
    if selection_rate * nb_children != 1:
        raise Exception("Either the selection rate or the number of children is not well adapted to fit the population")

    global sudoku_size
    global grid_size
    values_to_set = fileloader.load_file_as_values(model_to_solve)
    sudoku_size = int(sqrt(len(values_to_set)))
    grid_size = int(sqrt(sudoku_size))

    s = Sudoku(sudoku_size)
    s.init_with_values(values_to_set)
    s.display()

    # Create the 1st generation
    new_population = create_first_generation(population_size, values_to_set)
    generate_random_individual(values_to_set)


def create_first_generation(population_size, values_to_set):
    """
    Create the first generation knowing its size
    :param values_to_set: the values we have to set to init the sudoku
    :param (int) population_size: size of population to generate
    :return: (array) of individuals randomly generated. Array has strictly <population_size> individuals
    """
    population = []
    for i in range(population_size):
        population.append(generate_random_individual(values_to_set))
    return population


def generate_random_individual(values_to_set):
    """
    Generate one individual (that will be placed in the population)
    One individual that might solve the problem is a sudoku with the known values and other randomly filled
    :param values_to_set: the values we have to set to init the sudoku
    """
    individual = Sudoku(sudoku_size)
    individual.init_with_values(values_to_set)

    # We want to ensure that at least grids are 'correct' so we fill each one with available values to avoid duplicates
    for grid_id, grid_values in individual.grids().items():
        available_values = positions.fill_with_some_valid_values(grid_values, sudoku_size)

        # Get row and col from grid_id and position in grid and substitute the value
        for position, new_value in enumerate(available_values):
            row_id = positions.retrieve_row_id_from_grid_id_and_position(grid_id, position, grid_size)
            col_id = positions.retrieve_column_id_from_grid_id_and_position(grid_id, position, grid_size)
            individual.columns()[col_id][row_id] = new_value
            individual.rows()[row_id][col_id] = new_value

        # Substitute value with new one in grids arrays
        individual.grids()[grid_id] = available_values
    
    return individual
