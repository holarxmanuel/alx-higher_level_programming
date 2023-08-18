#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.

    :param my_list: The initial list
    :param search: The element to replace in the list
    :param replace: The new element
    :return: A new list with replacements
    """
    new_list = [replace if item == search else item for item in my_list]
    return new_list

if __name__ == "__main__":
    # Example usage
    original_list = [1, 2, 3, 2, 4, 5, 2]
    new_element = 9
    replacement_list = search_replace(original_list, 2, new_element)
    print(replacement_list)
