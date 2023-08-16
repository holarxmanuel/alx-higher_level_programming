#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    list_length = 0
    for _ in my_list:
        list_length += 1

    if idx < 0 or idx >= list_length:
        return my_list
    
    my_list[idx] = element
    return my_list
