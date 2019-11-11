"""
Created on 09/11/2019
@author: nidragedd
"""
import numpy as np
import random

from objects.sudoku import Sudoku


def create_generation(population_size, values_to_set):
    """
    Create the first generation knowing its size
    :param population_size: (int) size of the population we need to generate
    :param values_to_set: the values we have to set to init the objects
    :return: (array) of individuals randomly generated. Array has strictly <population_size> individuals
    """
    population = []
    for i in range(population_size):
        population.append(Sudoku(values_to_set).fill_random())
    return population


def rank_population(population):
    """
    Evaluate each individual of the population and give a ranking note whether it solves a lot or a little the problem
    (based on fitness method)
    :param population: (array) array of individuals to rank
    :return: (list) a sorted (asc) population. Individuals are sorted based on their fitness score
    """
    individuals_and_score = {}
    for individual in population:
        individuals_and_score[individual] = individual.fitness()
    return sorted(individuals_and_score, key=individuals_and_score.get)


def pick_from_population(ranked_population, selection_rate, random_selection_rate):
    """
    Select in a sorted population the best elements according to the given selection rate + add randomly some other
    elements
    :param ranked_population: (list) list of individuals sorted (asc) by the score, meaning that the best element is
    placed at the beginning and the worst at the end
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
        next_breeders.append(ranked_population[i])
    for i in range(nb_random_to_select):
        next_breeders.append(random.choice(ranked_population))

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
                                                    next_breeders[i].get_initial_values()))
    return next_population


def create_children_random_parents(next_breeders, nb_children):
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
    for i in range(int(len(next_breeders) / 2)):
        for j in range(nb_children):
            # Randomly pick 1 father and 1 mother
            father = random.choice(next_breeders)
            mother = random.choice(next_breeders)
            next_population.append(create_one_child(father, mother, father.get_initial_values()))
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
    sudoku_size = father.size()
    crossover_point = np.random.randint(1, sudoku_size - 1)

    child_grids = []
    for i in range(sudoku_size):
        if i < crossover_point:
            child_grids.append(father.grids()[i])
        else:
            child_grids.append(mother.grids()[i])
    return Sudoku(values_to_set).fill_with_grids(child_grids)


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
            individual = individual.swap_2_values()
        population_with_mutation.append(individual)
    return population_with_mutation
