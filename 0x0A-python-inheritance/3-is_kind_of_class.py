#!/usr/bin/python3
""" 3-is_kind_of_class module
This checks if an object is either a descendant of a class
"""


def is_kind_of_class(obj, a_class):
    """Finds if an obj is an instance of a_class
    or an instance of a child class
    Args:
        obj: object
        a_class: The class to evaluate
    Returns: True if object is instance of class or False if not
    """
    return (isinstance(obj, a_class))
