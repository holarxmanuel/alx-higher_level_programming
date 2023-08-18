#!/usr/bin/python3

"""
Returns the weighted average of integers in the list of tuples.

:param my_list: List of tuples containing integer score and weight
:return: Weighted average, or 0 if the list is empty
"""

def weight_average(my_list=[]):
    return sum(score * weight for score, weight in my_list) / sum(weight for _, weight in my_list) if my_list else 0
