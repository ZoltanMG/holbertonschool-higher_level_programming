#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def append_write(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    and returns the number of characters written
    """

    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
