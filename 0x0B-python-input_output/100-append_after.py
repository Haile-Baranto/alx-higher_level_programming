#!/usr/bin/python3
"""Prototype: def append_after(filename="", search_string="", new_string=""):
    You must use the with statement
    You don’t need to manage file permission or file doesn't exist exceptions.
    You are not allowed to import any module

    """


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line
            containing a specific string.

    Args:
        filename (str): name of the file to insert into.
        search_string (str): string to search for.
        new_string (str): string to insert after each line containing
            the search_string.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')
