#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).

    :param my_list: The input list
    :return: The sum of unique integers
    """
    unique_set = set()
    sum_unique = 0
    
    for num in my_list:
        if num not in unique_set:
            unique_set.add(num)
            sum_unique += num
    
    return sum_unique
