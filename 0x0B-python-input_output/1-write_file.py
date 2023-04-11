#!/usr/bin/python3
""" The module contains write_file function
    Prototype: def write_file(filename="", text=""):
    You must use the with statement
    You don’t need to manage file permission exceptions.
    Your function should create the file if doesn’t exist.
    Your function should overwrite the content of the file
        if it already exists.
    You are not allowed to import any module
    """


def write_file(filename="", text=""):
    """write_file writes a string to a text file (UTF8) and returns
        the number of characters written

    Args:
        filename (str, optional): path to the file we will write.
            Defaults to "".
        text (str, optional): the string to be written. Defaults to "".

    Returns:
        int: The number of charachters written to the file
    """
    with open(filename, 'w', encoding="utf-8") as writer:
        byte_number = writer.write(text)
    return byte_number
