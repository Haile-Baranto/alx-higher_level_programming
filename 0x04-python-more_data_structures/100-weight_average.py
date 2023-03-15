#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    multiplication = 0
    weigth_sum = 0
    for item in my_list:
        multiplication += item[0] * item[1]
    for item in my_list:
        weigth_sum += item[1]
    return multiplication/weigth_sum
