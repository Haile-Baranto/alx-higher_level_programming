#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """ prints all integers in reverse order
    Format: one integer per line. See example
    You are not allowed to import any module
    You can assume that the list only contains integers
    You are not allowed to cast integers into strings
    You have to use str.format() to print integers

    Args:
        my_list (list, optional): _description_. Defaults to [].
    """
    for i in range(1, len(my_list) + 1):
        print("{}".format(my_list[-i]))
