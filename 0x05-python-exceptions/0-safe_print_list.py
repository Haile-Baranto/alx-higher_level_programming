#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len = 0
    count = 0
    for i in my_list:
        len += 1
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
        except Exception:
            print("")
            return len
        count += 1
    print("")
    return count
