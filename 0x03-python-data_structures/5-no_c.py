#!/usr/bin/python3


def no_c(my_string):
    char_list = []
    for charachter in my_string:
        char_list.append(charachter)

    for item in char_list:
        if item == 'c' or item == 'C':
            char_list.remove(item)
    my_new_string = ''
    for item in char_list:
        my_new_string += item
    return my_new_string
