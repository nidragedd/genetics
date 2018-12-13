"""
Created on 13/12/2018
@author: nidragedd
"""
import matplotlib.pyplot as plt


def draw_best_worst_fitness_scores(best_data, worst_data):
    """
    Using matplotlib module to draw a simple graphic with 2 lines: one for the best solutions evaluations among
    generations and another one for the worst
    :param best_data: (array) the best fitness result for each generation
    :param worst_data: (array) the worst fitness result for each generation
    """
    # Create a new figure of size 8x6 points, using 100 dots per inch
    plt.figure(figsize=(8, 6), dpi=80)
    plt.plot(best_data, label="Best solution score", color="blue", linewidth=1.0, linestyle="-")
    plt.plot(worst_data, label="Worst solution score", color="red", linewidth=1.0, linestyle="-")
    plt.ylabel('Fitness function value evaluation')
    plt.xlabel('Number of generations')
    plt.ylim(0, worst_data[0])
    plt.xlim(0, len(best_data))
    plt.legend()
    plt.show()
