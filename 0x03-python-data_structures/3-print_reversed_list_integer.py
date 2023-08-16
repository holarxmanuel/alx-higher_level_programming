#!/usr/bin/pytho
def print_reversed_list_integer(my_list=[]):
    for idx in range(len(my_list)):
        digit_list = []
        number = my_list[-(idx + 1)]

        if number == 0:
            digit_list.append(chr(ord('0')))
        else:
            while number > 0:
                digit = number % 10
                digit_list.insert(0, chr(ord('0') + digit))
                number //= 10

        integer_str = ''.join(digit_list)
        print("{}".format(integer_str))

# Example usage:
my_list = [5, 10, 15, 20, 25]
print_reversed_list_integer(my_list)n
