#!/usr/bin/python3
def best_score(a_dictionary):
    score = -1000

    if a_dictionary:
        for i, j in a_dictionary.items():
            if j > score:
                score = j
    else:
        return None
    return score
