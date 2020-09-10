#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    name = ''

    if a_dictionary is None:
        return None

    for i, j in a_dictionary.items():
        if j > score:
            name = i
            score = j
    return name
