#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    return ({x: a_dictionary[x] for x in sorted(a_dictionary)})
