#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    [print('{}: {}'.format(i, j)) for i, j in sorted(a_dictionary.items())]
