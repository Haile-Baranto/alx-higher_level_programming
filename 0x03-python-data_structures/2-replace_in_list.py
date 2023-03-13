#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """appdates my_list list with value element at index idx.
    if idx is -ve or out of range it returns the orgional list.
    No use of any module or try/except

    Args:
        my_list (list): list whose element will be replaced
        idx (int): inedex at which the value will be replaced
        element (any valid pyhton type): value to replace value at my_list[idx]
    """
    if (idx < 0) or (idx >= len(my_list)):
        return my_list
    else:
        my_list[idx] = element
        return my_list
