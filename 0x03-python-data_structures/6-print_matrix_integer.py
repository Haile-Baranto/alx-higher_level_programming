#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        new_list = i
        for j in range(len(new_list) - 1):
            print("{:d}, ".format(new_list[j]), end='')
            print(new_list[len(new_list) - 1])
