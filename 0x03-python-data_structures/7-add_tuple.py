#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        a1 = tuple_a[0] if len(tuple_a) > 0 else 0
        a2 = 0
    else:
        a1, a2 = tuple_a[:2]

    if len(tuple_b) < 2:
        b1 = tuple_b[0] if len(tuple_b) > 0 else 0
        b2 = 0
    else:
        b1, b2 = tuple_b[:2]

    return (a1 + b1, a2 + b2)
