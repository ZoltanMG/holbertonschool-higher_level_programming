#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma = 0
    new_list = sorted(my_list[:])

    for i in range(len(new_list)):
        if i == 0:
            suma += new_list[i]
        elif new_list[i] != new_list[i - 1]:
            suma += new_list[i]

    return suma
