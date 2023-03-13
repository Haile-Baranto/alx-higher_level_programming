#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """_summary_deletes the item at a specific position in a list.
    If idx is negative or out of range, nothing change (returns the same list)
    You are not allowed to use pop()
    You are not allowed to import any module

Args:
        my_list (list, optional): a list whose element to be deleted
        idx (int, optional): index at which we will delete element io my_list
    """
    if idx >= len(my_list) or idx < 0:
        return my_list
    else:
        del my_list[idx]
        return my_list
