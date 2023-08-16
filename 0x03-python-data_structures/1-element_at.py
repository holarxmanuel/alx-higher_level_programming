#!/usr/bin/python3
def element_at(my_list, idx):
    list_length = 0
    for _ in my_list:
        list_length += 1

    if idx < 0 or idx >= list_length:
        return None
    return my_list[idx]
