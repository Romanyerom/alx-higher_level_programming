#!/usr/bin/python3
"""
    This function takes an object as input and returns a list containing the names of all attributes and methods
    associated with that object.

    Args:
        obj: The object for which to retrieve attributes and methods.

    Returns:
        A list of attribute and method names.
    """
def lookup(obj):
    return dir(obj)
