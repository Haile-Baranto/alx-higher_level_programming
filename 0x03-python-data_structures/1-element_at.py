#!/usr/bin/python3


def element_at(my_list, idx):
    """retrieves an element from a list like in C. return None if idx
    negative or index is out of range. Not allowed to use try/except or
    any module

    Args:
        my_list (list): is a list whose element is to be retrieved
        idx (int): index of the value to be returned
    """
    if (idx > (len(my_list) - 1)) or (idx < 0):
        return None
    else:
        return my_list[idx]
