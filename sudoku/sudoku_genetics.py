"""
Created on 10/11/2018
@author: nidragedd
"""
from random import choice, shuffle, randint, random

from sudoku import sudoku
from sudoku.sudoku import Sudoku
from utils import fileloader, commons


def start(population_size, selection_rate, random_selection_rate, nb_children, max_nb_generations,
          mutation_rate, model_to_solve, presolving, restart_after_n_generations_without_improvement):
    """
    Start the GA to solve the sudoku
    :param population_size: (int) the whole population size to generate for each generation
    :param selection_rate: (float) elitism parameter: rate of the best elements to keep from one generation to be part
    of the next breeders
    :param random_selection_rate: (float) part of the population which is randomly selected to be part of the next
    breeders
    :param nb_children: (int) how many children do we generate from 2 individuals
    :param max_nb_generations: (int) maximum number of generations to generate. If a solution is found before, it is
    displayed, otherwise the best solution (but not THE solution) is displayed
    :param mutation_rate: (float) part of the population that will go through mutation (avoid eugenics)
    :param model_to_solve: (string) name of the .txt file which should be under 'samples' directory and contains the
    sudoku problem to solve
    :param presolving: (boolean) (not used for the moment) if True, we can help by pre-solving the puzzle with easy
    values to find using a pencil mark approach
    :param restart_after_n_generations_without_improvement: (int) if > 0, the program will automatically restart if
    there is no improvement on fitness value for best element after this number of generations
    """
    if ((selection_rate + random_selection_rate) / 2) * nb_children != 1:
        raise Exception("Either the selection rate, random selection rate or the number of children is not "
                        "well adapted to fit the population")

    values_to_set = fileloader.load_file_as_values(model_to_solve)

    print("The solution we have to solve is:")
    s = Sudoku(commons.get_sudoku_size(values_to_set))
    s.init_with_values(values_to_set)
    s.display()

    best_data = []
    worst_data = []
    found = False
    nb_generations_done = 0
    overall_nb_generations_done = 0
    restart_counter = 0

    while not found:
        new_population = create_first_generation(population_size, values_to_set)

        overall_nb_generations_done += nb_generations_done
        nb_generations_done = 0
        remember_the_best = 0
        nb_generations_without_improvement = 0

        # Loop until max allowed generations is reached or a solution is found
        while nb_generations_done < max_nb_generations and not found:
            # Rank the solutions
            ranked_population = rank_population(new_population)
            best_solution = ranked_population[0][0]
            best_score = ranked_population[0][1]
            worst_score = ranked_population[population_size - 1][1]
            best_data.append(best_score)
            worst_data.append(worst_score)

            # Manage best value and improvements among new generations over time
            if remember_the_best == best_score:
                nb_generations_without_improvement += 1
            else:
                remember_the_best = best_score
            if 0 < restart_after_n_generations_without_improvement < nb_generations_without_improvement:
                print("No improvement since {} generations, restarting the program".
                      format(restart_after_n_generations_without_improvement))
                restart_counter += 1
                break

            # Check if problem is solved and print best and worst results
            if best_score > 0:
                print("Problem not solved on generation {} (restarted {} times). Best solution score is {} and worst is {}".
                      format(nb_generations_done, restart_counter, best_score, worst_score))
                # Not solved => select a new generation among this ranked population
                # Retain only the percentage specified by selection rate
                next_breeders = select_some_individuals_from_population(ranked_population, selection_rate,
                                                                        random_selection_rate)

                children = create_children(next_breeders, nb_children)
                new_population = mutate_population(children, mutation_rate)

                nb_generations_done += 1
            else:
                print("Problem solved after {} generations !!! Solution found is:".format(nb_generations_done))
                best_solution.display()
                found = True

    if not found:
        print("Problem not solved after {} generations. Printing best and worst results below".
              format(overall_nb_generations_done))
        ranked_population = rank_population(new_population)
        best_solution = ranked_population[0][0]
        worst_solution = ranked_population[population_size - 1][0]
        print("Best is:")
        best_solution.display()
        print("Worst is:")
        worst_solution.display()

    #TODO: use matplotlib to display graph of best and worst over time


def create_first_generation(population_size, values_to_set):
    """
    Create the first generation knowing its size
    :param values_to_set: the values we have to set to init the sudoku
    :param (int) population_size: size of population to generate
    :return: (array) of individuals randomly generated. Array has strictly <population_size> individuals
    """
    population = []
    for i in range(population_size):
        population.append(sudoku.build_random(values_to_set))
    return population


def fitness(candidate):
    """
    The most important function of the program. Here we give a note to the candidate according to the values
    Basically it is: how many figures are at the right place among the number of figures to find
    'Right place' = the number of duplicate symbols in rows or columns. Fewer duplicates presumably means a better solution
    :param candidate: (object) the candidate to evaluate/score
    :return: (int) a score for this candidate, lower it is, better is the candidate
    """
    duplicates_counter = 0
    for i in range(candidate.size()):
        duplicates_counter += commons.count_duplicates(candidate.rows()[i]) + \
                              commons.count_duplicates(candidate.columns()[i])
    return duplicates_counter


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


def select_some_individuals_from_population(ranked_population, selection_rate, random_selection_rate):
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
        next_breeders.append(choice(ranked_population)[0])

    # Shuffle everything to avoid having only the best (copyright Tina Turner) at the beginning
    shuffle(next_breeders)
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
    :param values_to_set: the values we have to set to init the sudoku
    :return: (object) a child which is the combination of both parents
    """
    # Avoid having only the whole father or the whole mother
    sudoku_size = commons.get_sudoku_size(values_to_set)
    crossover_point = randint(1, sudoku_size - 1)

    child_grids = []
    for i in range(sudoku_size):
        if i < crossover_point:
            child_grids.append(father.grids()[i])
        else:
            child_grids.append(mother.grids()[i])
    return sudoku.init_from_grids(values_to_set, child_grids)


def mutate_population(population, mutation_rate):
    """
    Randomly mutate some elements in the given population based on a given mutation rate
    :param population: (array) the whole population, few elements chosen randomly will mutate
    :param mutation_rate: (float) given mutation rate, it is a parameter that can be changed to act on the program
    :return: (array) new population with some elements that went through mutation. It is the next generation to evaluate
    """
    population_with_mutation = []
    for individual in population:
        if random() < mutation_rate:
            random_grid_id = randint(0, individual.size() - 1)
            individual = sudoku.swap_2_values_in_grid(individual, random_grid_id)
        population_with_mutation.append(individual)
    return population_with_mutation
