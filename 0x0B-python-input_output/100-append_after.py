#!/usr/bin/python3
"""
File Append After

This module provides a function to insert a line of text
after each line containing a specific string in a file.

Example:
    # Insert "New line" after each line containing
    # "old line" in the file "example.txt"
    append_after("example.txt", "old line", "New line")

"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing
    a specific string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after each matching line.

    """
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string + '\n')

    with open(filename, 'w') as file:
        file.writelines(lines)
