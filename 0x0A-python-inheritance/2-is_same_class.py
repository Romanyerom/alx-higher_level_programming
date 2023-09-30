#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare with.

    Returns:
        bool: True if the object is an instance
        of the specified class, False otherwise.
    """
    return type(obj) is a_class


if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
        if is_same_class(a, float):
            print("{} is an instance of the class {}".format(a, float.__name__))
            if is_same_class(a, object):
                print("{} is an instance of the class {}".format(a, object.__name__))
