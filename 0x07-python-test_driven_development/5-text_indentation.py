#!/usr/bin/python3
# 5-text_indentation.py
""" File name : 5-text_indentation.py
    Text indentation :  function that prints a text with 2
    new lines after each of these characters: ., ? and :
    Prototype: def text_indentation(text)
    You are not allowed to import any module
"""


def text_indentation(text):
    """

    Args:
        text (_type_): _description_

    Raises:
        TypeError: _description_
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    string = ""
    i = 0
    while i < len(text):
        if text[i] != "." and text[i] != "?" and text[i] != ":":
            string += text[i]
        else:
            string += text[i]
            print(string)
            print()
            string = ""
            while i < (len(text) - 1) and text[i+1] == " ":
                i += 1
        i += 1
    print(string, end="")
