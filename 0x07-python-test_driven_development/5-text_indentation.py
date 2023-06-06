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
    Prints the given text with two new lines after each occurrence of '.', '?', and ':'.
    Removes indentation at the start or end of each line.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If `text` is not a string.
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
            line = string.strip()  # Remove leading and trailing whitespace
            print(line)
            print()
            string = ""
            while i < len(text) - 1 and text[i + 1] == " ":
                i += 1
        i += 1
    line = string.strip()  # Remove leading and trailing whitespace
    print(line, end="")