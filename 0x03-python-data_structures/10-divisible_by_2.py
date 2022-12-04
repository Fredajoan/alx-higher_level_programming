#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    A_list = []
    for i in my_list:
        if (i % 2 == 0):
            A_list.append(True)
        else:
            A_list.append(False)
    return (A_list)

