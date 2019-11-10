"""
Created on 10/11/2018
@author: nidragedd
"""
import os
import re


def load_file_as_values(file_name):
    """
    Load values from a file that has the given file_name and should be placed under samples directory.
    The loading functions removes new lines and whitespaces so that all values are gathered into a simple string which
    is a suite of numbers.
    :param file_name: (string) name of the file containing values
    :return: (string) all values for the sudoku (values to guess are '0's)
    """
    file_to_load = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), 'samples',
                                file_name + '.txt')
    if os.path.exists(file_to_load):
        with open(file_to_load, 'rt') as f:
            content = f.read()
        return re.sub('(\||-)', '', content).replace('\n', ' ').replace('  ', ' ').split(' ')
    else:
        raise Exception("The file '{}' does not exist in 'samples' directory, please check your folder".
                        format(file_name))
