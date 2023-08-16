#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_length = 0
    for _ in my_list:
        list_length += 1

    idx = list_length - 1
    while idx >= 0:
        number = my_list[idx]
        
        # Convert and print the number without using str.format() or casting to string
        digit_list = []
        while number > 0:
            digit = number % 10
            digit_list.insert(0, chr(ord('0') + digit))
            number //= 10
        
        integer_str = ''.join(digit_list)
        print(integer_str)

        idx -= 1
