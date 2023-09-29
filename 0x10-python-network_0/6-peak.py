#!/usr/bin/python3
"""This script finds the peak in a list"""


def find_peak(list_of_integers):
    """This function finds the peak in a list"""
    # Check if the list is empty
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        # Compare the middle element with its neighbors
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    # The peak will be at the 'left' index
    return list_of_integers[left]
