#!/usr/bin/python3
"""
Module 6-peak
A module that contains a function to find a peak in an
unsorted list of integers.
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): The list of integers.

    Returns:
        int: A peak value from the list.
    """
    if not list_of_integers:
        return None
    low = 0
    high = len(list_of_integers) - 1
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return list_of_integers[low]
