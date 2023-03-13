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
    maximum = 0
    for i in my_list:
        if len(my_list) == 0:
            return None
        elif len(my_list) == 1:
            return my_list[0]
        else:
            for i in range(len(my_list) - 1):
                if my_list[i] >= my_list[i + 1]:
                    maximum = my_list[i]
                else:
                    maximum = my_list[i + 1]
    return maximum
