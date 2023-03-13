#!/usr/bin/python3
def max_integer(my_list=[]):
    """_summary_ Returns the largest element of a list.
    If the list is empty, return None
    You can assume that the list only contains integers
    You are not allowed to import any module
    You are not allowed to use the builtin max()

    Args:
        my_list (list, optional): _description_. Defaults to [].
    """
    if len(my_list) == 0:
        return None
    else:
        maximum = my_list[0]
        for item in my_list:
            if item > maximum:
                maximum = item
        return maximum
