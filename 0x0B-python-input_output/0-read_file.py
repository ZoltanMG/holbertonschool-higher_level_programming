#!/usr/bin/python3
""" open file """


def read_file(filename=""):
    """ open file"""

    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
