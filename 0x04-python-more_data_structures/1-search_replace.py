#!/usr/bin/pyhon3
def search_replace(my_list, search, replace):
    new_list = []

    if my_list:
        for i in my_list:
            if i != search:
                new_list.append(i)
            else:
                new_list.append(replace)
    return new_list
