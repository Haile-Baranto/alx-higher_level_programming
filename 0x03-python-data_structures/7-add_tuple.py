#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """_summary_Adds the first two elements of each tuple
    with equal index and returns tuple with two integers.
    You are not allowed to import any module
    You can assume that the two tuples will only contain integers
    If a tuple is smaller than 2, use the value 0 for each missing integer
    If a tuple is bigger than 2, use only the first 2 integers

    Args:
        tuple_a (tuple, optional): _description_. Defaults to ().
        tuple_b (tuple, optional): _description_. Defaults to ().
    """
    two_element_tuple = ()
    zero_tuple = (0, 0)
    tuple_1 = tuple_a + zero_tuple
    tuple_2 = tuple_b + zero_tuple
    two_element_tuple = (tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1])
    return two_element_tuple
