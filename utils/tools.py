"""
Generic helper functions

Created on 09/11/2019
@author: nidragedd
"""
import datetime


def get_human_readable_time(start_time, end_time):
    """
    Returns a string in the form [D day[s], ][H]H:MM:SS[.UUUUUU], where D is negative for negative t.
    :param start_time: (float) the beginning of the task
    :param end_time: (float) the end of the task
    :return: (string) human readable string with hours, minutes and seconds
    """
    return str(datetime.timedelta(seconds=(end_time - start_time)))


def count_duplicates(arr):
    """
    Count how many times the same value is found in a given array
    :param arr: the array to evaluate
    :return: number of duplicated elements
    """
    # Size of the given array minus the size of unique elements found in this array = nb of duplicates
    return len(arr) - len(set(arr))