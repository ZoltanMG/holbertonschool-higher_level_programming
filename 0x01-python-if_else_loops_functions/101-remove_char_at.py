#!/usr/bin/python3
def remove_char_at(str, n):
    string = ''
    count = 0
    for letter in str:
        if count != n:
            string += letter
        count += 1
    return string
