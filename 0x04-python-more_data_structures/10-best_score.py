#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0

    if a_dictionary is not None:
        for i, j in a_dictionary.items():
            if j > score:
                score = j
    else:
        return None
    return score
