#!/usr/bin/python3
"""MyList inhertes from list built in object
    You can assume that all the elements of the list will be of type int
    You are not allowed to import any module
    """


class MyList(list):
    """ class MyList inherits from list:

    Args:
        list (list): list of integers to be sorted
    """
    def print_sorted(self):
        print(sorted(self))
