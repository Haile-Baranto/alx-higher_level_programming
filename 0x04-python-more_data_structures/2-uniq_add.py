#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniq_list = set(my_list)
    for item in uniq_list:
        sum += item
        return sum
