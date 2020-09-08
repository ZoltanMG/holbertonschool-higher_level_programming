#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)

    for i in range(2):
        if len(a) < 2:
            a.append(0)
        if len(b) < 2:
            b.append(0)

    tuple_add = []
    tuple_add.append(a[0] + b[0])
    tuple_add.append(a[1] + b[1])
    tuple_add = tuple(tuple_add)
    return tuple_add
