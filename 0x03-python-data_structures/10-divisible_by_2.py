#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """_summary_ finds multiple of two in a list. the function return
    a list of true if divisible by two else false at the same index where
    the test of divisibility by 2 takes paces.
    The new list should have the same size as the original list
    You are not allowed to import any module

    Args:
        my_list (list, optional): _description_. Defaults to [].
    """
    boolean_lsit = []
    for i in my_list:
        if i % 2 == 0:
            boolean_lsit.append(True)
        else:
            boolean_lsit.append(False)
    return boolean_lsit
