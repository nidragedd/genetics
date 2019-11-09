"""
Created on 09/11/2019
@author: nidragedd
"""
import numpy as np
import random

from sudoku import s_utils


def create_generation(population_size, values_to_set):
    """
    Create the first generation knowing its size
    :param population_size: (int) size of the population we need to generate
    :param values_to_set: the values we have to set to init the objects
    :return: (array) of individuals randomly generated. Array has strictly <population_size> individuals
    """
    population = []
    for i in range(population_size):
        population.append(s_utils.build_random(values_to_set))
    return population


def rank_population(population):
    """
    Evaluate each individual of the population and give a ranking note whether it solves a lot or a little the problem
    (based on fitness method)
    :param population: (array) array of individuals to rank
    :return: (list) a sorted list of tuples where first element is the individual and second is the
    score. The list is sorted (asc) by the score, meaning that the best element is placed at the beginning and the worst
    at the end
    """
    individuals_and_score = {}
    for individual in population:
        individuals_and_score[individual] = fitness(individual)
    return [(k, individuals_and_score[k]) for k in sorted(individuals_and_score, key=individuals_and_score.get)]


def fitness(candidate):
    """
    The most important function of the program. Here we give a note to the candidate according to the values
    Basically it is: how many figures are at the right place among the number of figures to find
    'Right place' = the number of duplicate symbols in rows or columns. Fewer duplicates presumably means a better
    solution
    :param candidate: (object) the candidate to evaluate/score
    :return: (int) a score for this candidate, lower it is, better is the candidate
    """
    duplicates_counter = 0
    for i in range(candidate.size()):
        duplicates_counter += s_utils.count_duplicates(candidate.rows()[i]) + \
                              s_utils.count_duplicates(candidate.columns()[i])
    return duplicates_counter


def pick_from_population(ranked_population, selection_rate, random_selection_rate):
    """
    Select in a sorted population the best elements according to the given selection rate + add randomly some other
    elements
    :param ranked_population: (list) a sorted list of tuples where first element is the individual and second is the
    score. The list is sorted (asc) by the score, meaning that the best element is placed at the beginning and the worst
    at the end
    :param selection_rate: (float) given selection rate, it is a parameter that can be changed to act on the program
    :param random_selection_rate: (float) a random selection rate, it is a parameter that can also be changed to act
    on the program
    :return: (array) elements that have been selected in the given population. Not only the best are taken to avoid
    being stuck with a local minima
    """
    next_breeders = []

    nb_best_to_select = int(len(ranked_population) * selection_rate)
    nb_random_to_select = int(len(ranked_population) * random_selection_rate)

    # Keep n best elements in the population + randomly n other elements (note: might be the same)
    for i in range(nb_best_to_select):
        next_breeders.append(ranked_population[i][0])
    for i in range(nb_random_to_select):
        next_breeders.append(random.choice(ranked_population)[0])

    # Shuffle everything to avoid having only the best (copyright Tina Turner) at the beginning
    np.random.shuffle(next_breeders)
    return next_breeders


def create_children(next_breeders, nb_children):
    """
    Create the children from the given breeders generation
    :param next_breeders: (array) the population that will be used to create the next one
    :param nb_children: (int) number of children to create per couple father/mother, it is a parameter that can be
    changed to act on the program
    :return: (array) children generated with this population. They represent the next generation to evaluate
    (after mutation)
    """
    next_population = []
    # Divided by 2: one 'father' and one 'mother'
    for i in range(int(len(next_breeders)/2)):
        for j in range(nb_children):
            # We take father at the beginning of the list, mother at the end (remember that elements have been shuffled)
            next_population.append(create_one_child(next_breeders[i], next_breeders[len(next_breeders) - 1 - i],
                                                    next_breeders[i].initial_values()))
    return next_population


def create_one_child(father, mother, values_to_set):
    """
    Concretely create a child from both parents. In our case we take a group of grids from father and another one from
    mother with a randomly selected crossover point
    :param father: (object) one of the 2 elements used to build/generate a new one
    :param mother: (object) one of the 2 elements used to build/generate a new one
    :param values_to_set: the values we have to set to init the objects
    :return: (object) a child which is the combination of both parents
    """
    # Avoid having only the whole father or the whole mother
    sudoku_size = s_utils.get_sudoku_size(values_to_set)
    crossover_point = np.random.randint(1, sudoku_size - 1)

    child_grids = []
    for i in range(sudoku_size):
        if i < crossover_point:
            child_grids.append(father.grids()[i])
        else:
            child_grids.append(mother.grids()[i])
    return s_utils.init_from_grids(values_to_set, child_grids)


def mutate_population(population, mutation_rate):
    """
    Randomly mutate some elements in the given population based on a given mutation rate
    :param population: (array) the whole population, few elements chosen randomly will mutate
    :param mutation_rate: (float) given mutation rate, it is a parameter that can be changed to act on the program
    :return: (array) new population with some elements that went through mutation. It is the next generation to evaluate
    """
    population_with_mutation = []
    for individual in population:
        if np.random.random() < mutation_rate:
            random_grid_id = np.random.randint(0, individual.size() - 1)
            individual = s_utils.swap_2_values_in_grid(individual, random_grid_id)
        population_with_mutation.append(individual)
    return population_with_mutation
