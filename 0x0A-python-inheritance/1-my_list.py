#!/usr/bin/python3
"""
MyList class inherits from the built-in list class and provides a custom method.
"""

class MyList(list):
    """
    Methods:
        print_sorted(self): Prints the list in ascending sorted order.

    Attributes:
        Inherits all attributes from the list class.
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
