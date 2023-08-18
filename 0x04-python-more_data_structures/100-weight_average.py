#!/usr/bin/python3

def weighted_average_calculator(tuples_list=[]):
    if not tuples_list:
        return 0

    numerator = 0
    denominator = 0

    for score_weight_tuple in tuples_list:
        numerator += score_weight_tuple[0] * score_weight_tuple[1]
        denominator += score_weight_tuple[1]

    return (numerator / denominator)
