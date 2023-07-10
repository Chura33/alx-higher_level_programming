#!/usr/bin/python3
""" 4-inherits_from module
Checks whether an object is an instance
of a class that inherits from a_class either directly
or indirectly and the object is not a direct
instance of a_class
"""


def inherits_from(obj, a_class):
    """
    Determines if obj is an instance of a class
    and not a direct descendant
    Args:
        obj: object to look at
        a_class: the class that we inspect
    Returns: returns True of False
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
