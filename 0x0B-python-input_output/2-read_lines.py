#!/usr/bin/python3
"""
function that reads n lines of a text file (UTF8)
and prints it to stdout
"""


def read_lines(filename="", nb_lines=0):
    """
    function that reads n lines of a text file (UTF8)
    and prints it to stdout
    """

    number_lines = 1
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            if nb_lines <= 0:
                print(line, end='')
            elif number_lines <= nb_lines:
                print(line, end='')
            else:
                break
            number_lines += 1
