#!/usr/bin/python3
"""2-is_same_class module
"""


def is_same_class(obj, a_class):
    """ checks if obj is instance of a_class
    Args: obj (_object_): _description
          a_class(_class_):_description
    Returns:
        True: if obj is instance of a_class
        False: if not
    """
    return True if type(obj) is a_class else False
