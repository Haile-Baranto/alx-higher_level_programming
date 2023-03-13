#!/usr/bin/python3


def multiple_returns(sentence):
    """_summary_ returns tuple containing length of string and
    its first charachter.
    If the sentence is empty, the first character should be equal to None
    You are not allowed to import any module

    Args:
        sentence (string): string of charachters whose first char and length
        to be returned
    """
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
