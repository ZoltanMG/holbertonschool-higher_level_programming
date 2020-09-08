#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_str = [0, None]

    if len(sentence) > 0:
        tuple_str[0] = len(sentence)
        tuple_str[1] = sentence[0]

    tuple(tuple_str)
    return tuple_str
