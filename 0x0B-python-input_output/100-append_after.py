#!/usr/bin/python3
"""
Function that inserts a line of text to a file, after each
line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert.

    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        i = 0
        for line in lines:
            if search_string in line:
                lines.insert(i + 1, new_string)
            i += 1
        file.seek(0)
        file.writelines(lines)
