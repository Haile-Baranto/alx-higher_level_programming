#!/usr/bin/python3


class Square(object):
    """ Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module
    """
    def __init__(self, size):
        """ Inirialize size"""
        self.__size = size
