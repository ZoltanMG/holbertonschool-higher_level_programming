#!/usr/bin/python3
def best_score(a_dictionary):
    name = ''

    if a_dictionary is None:
        return None

    for i, j in sorted(a_dictionary.items()):
        name = i
    return name
