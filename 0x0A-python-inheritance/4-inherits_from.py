#!/usr/bin/python3
# 4-inherits_from.py

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare with.

    Returns:
        bool: True if the object is an instance of a class that inherited from the specified class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
