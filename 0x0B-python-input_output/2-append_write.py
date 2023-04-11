#!/usr/bin/python3
""" The module contanis append_write function that appends to
    the end of file.
    Prototype: def append_write(filename="", text=""):
    If the file doesn’t exist, it should be created
    You must use the with statement
    You don’t need to manage file permission or
        file doesn't exist exceptions.
    You are not allowed to import any module
    """


def append_write(filename="", text=""):
    """append_write appends a string at the end of a text
    file (UTF8) and returns the number of characters added:

    Args:
        filename (str, optional): file where to append. Defaults to "".
        text (str, optional): string to be appended. Defaults to "".

    Returns:
        int: number of bytes appended
    """
    with open(filename, 'a', encoding="utf-8") as append_write:
        nb_bytes = append_write.write(text)
    return nb_bytes
