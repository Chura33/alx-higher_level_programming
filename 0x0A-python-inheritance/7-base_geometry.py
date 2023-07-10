#!/usr/in/python3
""" 7-base_geometry module"""


class BaseGemoetry:
    def area(self):
        """This method simply raises an exception"""

        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):

    """ This validates the value """
    if type(value) != int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
