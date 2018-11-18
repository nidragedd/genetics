'''
Created on 10/11/2018
@author: nidragedd
'''
import os
import re


def load_file_as_values(file_name):
    file_to_load = os.path.join(os.path.abspath(os.getcwd()), 'samples', file_name + '.txt')
    content = ''
    if os.path.exists(file_to_load):
        with open(file_to_load, 'rt') as f:
            content = f.read()
    return re.sub('(\n|\||-|\s)', '', content)