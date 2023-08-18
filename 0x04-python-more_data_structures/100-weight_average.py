#!/usr/bin/python3

"""
Calculates the weighted average of integers in the list of tuples.

:param my_list: List of tuples containing integer score and weight
:return: Weighted average, or 0 if the list is empty
"""

def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    return total_score / total_weight
