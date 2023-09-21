#!/usr/bin/python3

class LockedClass:
    def __setattr__(self, name, value):
        if name == "first_name":
            # Allow setting the 'first_name' attribute
            super().__setattr__(name, value)
        else:
            # Raise an AttributeError for any other attribute
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
